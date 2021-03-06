from django.shortcuts import render
import json
from models import ArtPiece
from art_map.forms import UserForm, UserProfileForm, PictureForm
# import os
# from django.conf import settings
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # file_name = os.path.join(settings.BASE_DIR, 'static/public_art.json')
    # json_file = open(file_name)
    # json_data = json_file.read()
    # art = json.dumps(json_data)
    # json_file.close()
    art = json.dumps(serializers.serialize('json', ArtPiece.objects.all()))
    context_dict = {'key': ""}
    context_dict['art'] = art
    return render(request, 'art_map/index.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'art_map/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/art_map/profile/')
            else:
                return HttpResponse("your account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'art_map/login.html', {'login_error': "Invalid login details supplied."})
    else:
        return render(request, 'art_map/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/art_map/')


@login_required
def add_favourite(request):
    if request.method == 'POST':
        if request.user.is_active:
            art_id = request.POST.get('art_id')
            art_piece = ArtPiece.objects.get(pk=art_id)
            request.user.userprofile.favourites.add(art_piece)
            request.user.userprofile.save()
            return HttpResponseRedirect('/art_map/')
        else:
            return HttpResponse("your account is disabled")


@login_required
def profile(request):
    picture = ""
    if request.user.userprofile.picture:
        picture = request.user.userprofile.picture.url
    if request.method == 'POST' and picture == "":
        picture_form = PictureForm(request.POST, instance=request.user.userprofile)
        if picture_form.is_valid():
            picture_form.save(commit=False)
            if 'picture' in request.FILES:
                request.user.userprofile.picture = request.FILES['picture']
            picture_form.save()
            return HttpResponseRedirect('/art_map/profile/')
        else:
            print(picture_form.errors)
    else:
        picture_form = PictureForm()
    favourites_list = request.user.userprofile.favourites.all()
    return render(request, 'art_map/profile.html',
                  {'favourites': favourites_list, 'picture': picture, 'picture_form': picture_form})
