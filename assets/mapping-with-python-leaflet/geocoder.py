import geopy, sys
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# versions used: geopy 1.10.0, pandas 0.16.2, python 2.7.8

inputfile=str(sys.argv[1])
namecolumn=str(sys.argv[2])
# your command will look something like 'python geocoder-singlecolumn.py census-historic-population-borough.csv Area_Name'

def main():
  io = pandas.read_csv(inputfile, index_col=None, header=0, sep=",")

  def get_latitude(x):
    return x.latitude

  def get_longitude(x):
    return x.longitude

  geolocator = Nominatim()
  # geolocator = GoogleV3(timeout=5)
  # uncomment the geolocator you want to use
  # change the timeout value if you get a timeout error, for instance, geolocator = Nominatim(timeout=60)
  geolocate_column = io[namecolumn].apply(geolocator.geocode)
  io['latitude'] = geolocate_column.apply(get_latitude)
  io['longitude'] = geolocate_column.apply(get_longitude)

  io.to_csv('geocoding-output.csv')

if __name__ == '__main__':
  main()
