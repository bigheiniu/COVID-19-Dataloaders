import os
import pandas as pd
from DataLoader import Data
import glob
import re
from .HydrateHelper import  HydrateTwitterID


RegexDic = {
   "USC": r"coronavirus-tweet-id-(.*?)",
    "Harvard": r""
}
Keywords = {
    'USC': [],
    'GWU':["coronavirus" , "2019nCoV"]
}
class TweetIDCorpus(Data):
    def __init__(self):
        super(TweetIDCorpus, self).__init__()
        self.ID_name = ""
        self.data = pd.DataFrame()
        self.kw_list = []
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
        return self.data.iloc[item, :]
    
    def file_title_regex(self, file_name):
        return re.findall(RegexDic[self.ID_name], file_name)[0]
    
    def download(self, path_or_url, **kwargs):
        raise NotImplementedError
        
    def hydrate(self, configure_key_secret):
        # hydrate the data
        twarc = HydrateTwitterID(configure_key_secret)
        # TODO: Use two layers of index to handle Twitter IDs
        
    def column_info(self, **kwargs):
        return self.data.columns
    
    def load_keywords(self, **kwargs):
        raise NotImplementedError
    
    def get_keywords(self):
        return self.kw_list
    
class TweetIDCorpusUSC(TweetIDCorpus):
    def __init__(self):
        super(TweetIDCorpusUSC, self).__init__()
    
    def download(self, path_or_url, **kwargs):
        # https://github.com/echen102/COVID-19-TweetIDs - USC
        # https://zenodo.org/record/3723940#.Xpztr5ravaE - GWU
        all_txt = glob.glob(f'{path_or_url}/**/*.txt', recursive=True)
        data_dic = {
            'time': [],
            'tweet_id': []
        }
        for file_name in all_txt:
            name = re.findall(r"coronavirus-tweet-id-(.*?)", file_name)
            tweet_id = open(file_name, 'r').readlines()
            tweet_id = [i.strip() for i in tweet_id]
            # tweet_id_string = "_".join(tweet_id)
            data_dic['tweet_id'].extend(tweet_id)
            data_dic["time"].extend([name] * len(tweet_id))
        
        # reshape the data
        self.data = pd.DataFrame(data_dic, columns=['time', 'tweet_id'])
    
    def load_keywords(self, **kwargs):
        file_path = kwargs['kw_path']
        kw_list = open(file_path,'r').readlines()
        kw_list = [i.split()[0] for i in kw_list]
        self.kw_list = kw_list
    
class TweetIDGWU(TweetIDCorpus):
    def __init__(self):
        super(TweetIDGWU, self).__init__()
        
    def download(self, path_or_url, **kwargs):
        assert "tsv" in path_or_url, "You should pass a TSV file"
        self.data = pd.read_csv(path_or_url, sep="\t")
    
    def load_keywords(self, **kwargs):
        self.kw_list = ["coronavirus" , "2019nCoV"]
        
class TweetIDCROWDBREAKS(TweetIDCorpus):
    def __init__(self):
        super(TweetIDCROWDBREAKS, self).__init__()
    
    def download(self, path_or_url, **kwargs):
        #https://www.crowdbreaks.org/en/data_sharing
        tweet_ids = open(path_or_url,'r').readlines()
        tweet_ids = [i.strip() for i in tweet_ids]
        self.data = pd.DataFrame(tweet_ids, columns=['tweet_id'])
    
    def load_keywords(self, **kwargs):
        self.kw_list = 'wuhan, ncov, coronavirus, covid, sars-cov-2'.split(",")


    

        

        

        
        