
# install twarc
try:
    from twarc import Twarc
except:
    raise ModuleNotFoundError(" Please use pip3 install twarc")

from DataLoader import Data
import pandas as pd

class HydrateTwitterID(object):
    def __init__(self, configure_key_secret):
        super(HydrateTwitterID, self).__init__()
        self.configure(configure_key_secret)
        
    def configure(self, configure_key_secret):
        self.t = Twarc(**configure_key_secret)
    
    
    def hydrate(self, tweetIDs):
        data = []
        for tweet in self.t.hydrate(tweetIDs):
            data.append(tweet)
        
        self.data = pd.DataFrame(data)

    
        
    
