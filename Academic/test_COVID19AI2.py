import unittest
from Academic.Covid19AI2 import Covid19AI2MetaData, Covid19AI2Paper

class MyTestCase(unittest.TestCase):
    def test_meta(self, path):
        data = Covid19AI2MetaData().download(path_or_url="")
        print(len(data))
        print(data[10])
        print(data.column_info())
        print(data.data)
    def test_paper(self):
        meta =  Covid19AI2MetaData().download(path_or_url="")
        data = Covid19AI2Paper().download(meta, meta_df=meta)
        print(len(data))
        print(data[10])
        print(data.column_info())
        print(data.data)
        
if __name__ == '__main__':
    unittest.main()
