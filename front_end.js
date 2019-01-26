var citymap = {
  Shreyal: {
    center: {lat: -6.7804, lng: 39.2053},
    acres: 0.00005
  },
  
    Tanzania: {
    center: {lat: -3.3869, lng: 38.6830},
    acres: 0.005
  },

};

function initMap() {
  // Create the map.
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: {lat: -6.3690, lng: 34.8888},
    mapTypeId: 'terrain'
  });

  for (var city in citymap) {
    var cityCircle = new google.maps.Circle({
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.35,
      map: map,
      center: citymap[city].center,
      radius: Math.sqrt(citymap[city].acres) * 50
    });
  }
}

function search(ele) {
    if(event.key === 'Enter') {
        alert(ele.value);        
    }
}
Chat Conversation End
Type a message...
