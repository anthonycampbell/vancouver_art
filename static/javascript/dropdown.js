function toggle(item, i, position){
    var interval = setInterval(helper, 2);
    var delta;
    position == "down" ?
    delta = 0 :
    delta = parseInt(item.style.top);
    function helper(){
        if ((delta == (100*i) && position == "down") || (delta == 0 && position == "up")){
            clearInterval(interval);
        } else {
            position == "down" ? delta++: delta--;
            item.style.top = delta + "%";
        }
    }
}

function toggleDropdown(){
    var dropdown = document.querySelectorAll('.header .dropdown');
    var dropdownItems = document.querySelectorAll('.header .dropdown-item');
    var top = parseInt(getComputedStyle(dropdownItems[dropdownItems.length-1]).top);
    var height = parseInt(getComputedStyle(dropdown[0]).height);
    for (var i = 1; i < dropdownItems.length; i++){
        if (top == 0){
            toggle(dropdownItems[i], i, "down");
        } else if (top == height*(dropdownItems.length-1)){
            toggle(dropdownItems[dropdownItems.length - i], i, "up");
        }
    }
}