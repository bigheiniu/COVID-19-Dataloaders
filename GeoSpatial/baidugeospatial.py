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
        return "Learn about COVID‑19 mobility trends in countries/regions and \
        cities from Baidu Mobility Data"


    def column_info(self, **kwargs):
        return self.data.columns.values

if __name__ == '__main__':
    geospatial = GeoSpatial()
    # credit for data set https://doi.org/10.7910/DVN/FAEZIO
    geospatial.download("../stored_data/dataverse_files/baidu_out_20200425.csv")
    print(geospatial.data)
    print(geospatial.column_info())
    print(len(geospatial))
    print(geospatial[0])
