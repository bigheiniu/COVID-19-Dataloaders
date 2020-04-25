import sys
sys.path.append('../')
from DataLoader import Data
import pandas as pd
import re
class MaliciousURLs(Data):
    def __init__(self):
        super(MaliciousURLs, self).__init__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data.iloc[item, :]

    def download(self, path_or_url, **kwargs):
        data = open(path_or_url,'r').readlines()
        regex = r'(?=.*[\.])(?=.*[a-zA-Z0-9])([0-9a-zA-Z\.]+)'
        data = list(filter(lambda x: "." in x, data))
        data = [next(filter(lambda x: "." in x, re.findall(regex, url.strip()))) for url in data]
        self.data = pd.DataFrame(data, columns=['url'])
        # check whether the file is url or not

    def description(self):
        return "These URLs are malicious urls."

    def column_info(self, **kwargs):
        return self.data.columns.values


if __name__ == '__main__':
    malicious = MaliciousURLs()
    malicious.download("../stored_data/maliciousURLs.txt")
    print(malicious.data)
    print(malicious.column_info())
    print(len(malicious))
    print(malicious[0])