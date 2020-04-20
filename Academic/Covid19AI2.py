import pandas as pd
from DataLoader import Data
import glob
import json
#############################################################################
# Copy from https://www.kaggle.com/maksimeren/covid-19-literature-clustering#
#############################################################################
class FileReader:
    def __init__(self, file_path):
        with open(file_path) as file:
            content = json.load(file)
            self.paper_id = content['paper_id']
            self.abstract = []
            self.body_text = []
            # Abstract
            for entry in content['abstract']:
                self.abstract.append(entry['text'])
            # Body text
            for entry in content['body_text']:
                self.body_text.append(entry['text'])
            self.abstract = '\n'.join(self.abstract)
            self.body_text = '\n'.join(self.body_text)
    def __repr__(self):
        return f'{self.paper_id}: {self.abstract[:200]}... {self.body_text[:200]}...'
        


class Covid19AI2MetaData(Data):
    def __init__(self):
        super(Covid19AI2MetaData, self).__init__()
        
    def __len__(self):
        return len(self.meta_df)
    
    def __getitem__(self, item):
        return self.meta_df.iloc[item, :].values.tolist()
    
    def collumn_info(self):
        return list(self.data.columns)
    
    def download(self, path_or_url, **kwargs):
        meta_data_path = f'{path_or_url}/metadata.csv'
        self.meta_df = pd.read_csv(meta_data_path, dtype={'pubmed_id': str,
        'Microsoft Academic Paper ID': str,
        'doi': str})
        self.data = self.meta_df
    
    


class Covid19AI2Paper(Data):
    def __init__(self):
        super(Covid19AI2Paper, self).__init__()
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
        return self.data.iloc[item, :].values.tolist()
    
    def download(self, path_or_url, **kwargs):
        meta_df = kwargs['meta_df']
        all_json = glob.glob(f'{path_or_url}/**/*.json', recursive=True)

        dict_ = {'paper_id': [], 'doi': [], 'abstract': [], 'body_text': [], 'authors': [], 'title': [], 'journal': [],
                 'abstract_summary': []}

        for idx, entry in enumerate(all_json):
            if idx % (len(all_json) // 10) == 0:
                print(f'Processing index: {idx} of {len(all_json)}')
            try:
                content = FileReader(entry)
            except Exception as e:
                continue

            meta_data = meta_df.loc[meta_df['sha'] == content.paper_id]
            # no metadata, skip this paper
            if len(meta_data) == 0:
                continue
            dict_['abstract'].append(content.abstract)
            dict_['paper_id'].append(content.paper_id)
            dict_['body_text'].append(content.body_text)
            dict_['title'].append(meta_data['title'].values[0])
            dict_['journal'].append(meta_data['journal'].values[0])
            dict_['authors'].append(meta_data['authors'].values[0])
            dict_['doi'].append(meta_data['doi'].values[0])
            
            if len(content.abstract) == 0:
                # no abstract provided
                dict_['abstract_summary'].append("Not provided.")
        self.data = pd.DataFrame(dict_,
                                columns=['paper_id', 'doi', 'abstract', 'body_text', 'authors', 'title', 'journal',
                                         'abstract_summary'])

    def column_info(self, **kwargs):
        return self.data.columns
    
            
