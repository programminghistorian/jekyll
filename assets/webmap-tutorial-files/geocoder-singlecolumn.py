import geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# versions used: geopy 1.10.0, pandas 0.16.2, python 2.7.8
# this script is used to geocode one column in a csv file.  you need to modify the input file (census_borough.csv) and Area_Name column

def main():
	io = pandas.read_csv('census-historic-population-borough.csv', index_col=None, header=0, sep=",")
	geolocator = Nominatim()
	# geolocator = GoogleV3()
	# uncomment the geolocator you want to use
	io['latitude'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.latitude))
	io['longitude'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.longitude))
	io.to_csv('geocoding-output.csv')

if __name__ == '__main__':
  main()
