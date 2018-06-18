function initMap() {
  // The location of Uluru
  var vancouver = {lat: 49.2827, lng: -123.1207};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 11, center: vancouver});
  // The marker, positioned at Uluru
  //var marker = new google.maps.Marker({position: vancouver, map: map});
}
