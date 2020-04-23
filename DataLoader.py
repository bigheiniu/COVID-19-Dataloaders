import os
import glob

class Data(object):
    def __init__(self):
        self.init = True
    
    def __len__(self):
        raise NotImplementedError("Please implement length function")
    
    def __getitem__(self, item):
        raise NotImplementedError("Please implement getitem function")
    
    def download(self, path_or_url, **kwargs):
        # Currently only assume it is the path
        raise NotImplementedError("Please implement download function")
    
    # def to_pandas(self, **kwargs):
    #     raise NotImplementedError("Please implement to pandas function")

    def description(self):
        # Return the description about this dataset
        raise NotImplementedError
    def column_info(self, **kwargs):
        raise  NotImplementedError