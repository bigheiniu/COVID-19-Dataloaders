import sys
sys.path.append('../')
from DataLoader import Data
import pandas as pd
import re

class GeoSpatial(Data):
    def __init__(self):
    	super(GeoSpatial, self).__init__()

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
    	return self.data.iloc[item, :]

    def download(self, path_or_url, **kwargs):
        self.data = pd.read_csv(path_or_url)

    
    # def to_pandas(self, **kwargs):
    #     raise NotImplementedError("Please implement to pandas function")

    def description(self):
        return "The downloadable data file is updated daily and contains the \
        latest available public data on COVID-19. Each row/entry contains the \
        number of new cases reported per day and per country. \
        You may use the data in line with ECDC’s copyright policy."


    def column_info(self, **kwargs):
        return self.data.columns.values

if __name__ == '__main__':
    geospatial = GeoSpatial()
    geospatial.download("../stored_data/geographic_distribution_worldwide.csv")
    print(geospatial.data)
    print(geospatial.column_info())
    print(len(geospatial))
    print(geospatial[0])
