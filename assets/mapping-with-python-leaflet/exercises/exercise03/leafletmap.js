window.onload = function () {
    var basemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  });

    $.getJSON("stations.geojson", function(data) {

    var geojson = L.geoJson(data, {
      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name + '<p><b> Line: ' + feature.properties.line + '</b></p>');
        //EDIT HERE
      }
    });


    var map = L.map('my-map')
    .fitBounds(geojson.getBounds());
    // .setView([51.505,-0.09], 9);

    basemap.addTo(map);
    geojson.addTo(map);
  });

};
