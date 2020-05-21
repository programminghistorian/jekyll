window.onload = function () {

    // EDIT HERE: get an access token, it will look something like "pk.eyJ1Ijoia2ltcGhhbTU0IiwiYSI6IkdJX0tvM2cifQ.fVsdGC_QJrFYZ3SxZCsvhQ"
    L.mapbox.accessToken = 'pk.eyJ1Ijoia2ltcGhhbTU0IiwiYSI6IkdJX0tvM2cifQ.fVsdGC_QJrFYZ3SxZCsvhQ';

    // EDIT HERE: add the new baselayer style, replace 'YOURLINKHERE' with something like "kimpham54.au2i6bt9"
    var basemap = L.tileLayer('https://api.mapbox.com/v4/kimpham54.au2i6bt9/{z}/{x}/{y}.png?access_token=' + L.mapbox.accessToken, {
        attribution: '<a href="https://www.mapbox.com/tos/">Mapbox</a>'
      });

    $.getJSON("stations.geojson", function(data) {

    var geojson = L.geoJson(data, {

//EDIT HERE
      pointToLayer: function (feature, latlng) {
       var smallIcon = L.icon({
                          iconSize: [27, 27],
                          iconAnchor: [13, 27],
                          popupAnchor:  [1, -24],
                          iconUrl: 'leaf.png'
                  });

         return L.marker(latlng, {icon: smallIcon});
        },

      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name + '<p><b> Line: ' + feature.properties.line + '</b></p>');
      }

    });


    var map = L.map('my-map')
    .fitBounds(geojson.getBounds());
    //.setView([51.505,-0.09], 9);

    basemap.addTo(map);
    geojson.addTo(map);
  });

};
