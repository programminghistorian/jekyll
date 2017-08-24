
window.onload = function () {
    var basemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});

    $.getJSON("census.geojson", function(data) {

    var geojson = L.geoJson(data, {
      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.Area_Name + '<p><b> 2001 Population: ' + feature.properties.Pop_2001 + '</b></p>' + '<p><b> 1801 Population ' + feature.properties.Pop_1801 + '</b></p>');
      }
    });


    var map = L.map('my-map')
    .fitBounds(geojson.getBounds());
//    .setView([0.0,-10.0], 2);

    basemap.addTo(map);
    geojson.addTo(map);
  });

};
