window.onload = function () {
    var basemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  });

    $.getJSON("census.geojson", function(data) {

    var geojson = L.geoJson(data, {
      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.Area_Name);
      }
    });


    var map = L.map('my-map')
    //.fitBounds(geojson.getBounds());
    .setView([51.505,-0.09], 9);
    //EDIT HERE

    basemap.addTo(map);
    geojson.addTo(map);
  });

};
