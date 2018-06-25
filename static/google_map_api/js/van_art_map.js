function initMap() {
  // The location of Uluru
  var vancouver = {lat: 49.2827, lng: -123.1207};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 11, center: vancouver});
  for (i = 0; i < art.length; i++){
    var lat = art[i].fields['lat'];
    var lon = art[i].fields['lon'];
    if (lat && lon){
      var point = {lat: lat, lng: lon};
      var marker = new google.maps.Marker({position: point, map: map});
    }
  }
}
