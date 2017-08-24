import geopy, sys
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# versions used: geopy 1.10.0, pandas 0.16.2, python 2.7.8

inputfile=str(sys.argv[1])
# namecolumn=str(sys.argv[2])
# your command will look something like 'python geocoder-singlecolumn_withhelper.py census-historic-population-borough.csv'. column names are specified in the code.

def main():
  io = pandas.read_csv(inputfile, index_col=None, header=0, sep=",")

  def get_latitude(x):
    return x.latitude

  def get_longitude(x):
    return x.longitude

  # geolocator = Nominatim(timeout=5)
  geolocator = GoogleV3(timeout=5)
  # uncomment the geolocator you want to use
  # change the timeout value if you get a timeout error, for instance, geolocator = Nominatim(timeout=60)
  io['helper'] = io['Area_Name'].map(str) + " " + io['Country'].map(str)
  geolocate_column = io['helper'].apply(geolocator.geocode)
  io['latitude'] = geolocate_column.apply(get_latitude)
  io['longitude'] = geolocate_column.apply(get_longitude)
  io.to_csv('geocoding-output-helper.csv')

if __name__ == '__main__':
  main()
