from DataLoader import Data
import os
import glob
import pandas as pd
import json
# Data is from  Chen Q, Allot A, Lu Z. Keep up with the latest coronavirus research. Nature. 2020;579(7798):193.

class LitCovidMeta(Data):
    def __init__(self):
        super(LitCovidMeta, self).__init__()

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
        return self.data.iloc[item,:].values.tolist()
    
    def download(self, path_or_url, **kwargs):
        assert "tsv" in path_or_url, "please use the TSV file from https://www.ncbi.nlm.nih.gov/research/coronavirus/#data-download"
        
        self.data = pd.read_csv(path_or_url,sep="\t", comment="#")
        
    def column_info(self, **kwargs):
        return self.data.columns
    

class LitCovidPaper(Data):
    def __init__(self):
        super(LitCovidPaper, self).__init__()
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
        return self.data.iloc[item, :].values.tolist()
    
    def download(self, path_or_url, **kwargs):
        # url = https://ftp.ncbi.nlm.nih.gov/pub/lu/LitCovid/litcovid2BioCJSON.gz
        assert "json" in path_or_url.lower(), "please download the json file in https://ftp.ncbi.nlm.nih.gov/pub/lu/LitCovid/"
        # TODO: use ellegant method to load the data
        # TODO Cannot use this method to directly load the data
        meta_df = kwargs['meta_df']
        data = []
        meta_id = set(meta_df['pmid'])
        with open(path_or_url,'r') as f1:
            for index, line in f1.readline():
                if index < 28:
                    continue
                try:
                    line = json.loads(line[1:])
                    if line['pmid'] in meta_id:
                        data.append(line)
                except:
                    continue
        self.data = pd.DataFrame(data)
        
        
                    
                
        # TODO: filter the paper that is not listed in the meta information
        
        
    
    def column_info(self, **kwargs):
        return self.data.columns