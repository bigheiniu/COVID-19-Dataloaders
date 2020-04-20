# COVID-19-Dataloaders
The repository affords researchers an easy tool and uniform tool to load the COVID-19 related dataset listed in [here](https://github.com/bigheiniu/awesome-coronavirus19-dataset).


This dataloader is still under construction for automatically downloading from the Internet. 


## About

### Goal
- This tool is easy to use. All the datasets are in [pandas.Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) format which is easy for further data analysis. Researchers can run one python command to automatically load the dataset 

    
        data = TweetIDCorpus.download(url_or_path)
        pandas_df = data.data

- This dataloader can load datasets from different perspectives, i.e Academic, Social Media, News, Case Report, Geo-Spatial, etc. 
Researchers can find some connections among different kinds of datasets. And we believe this will boost the development in defending COVID-19.


### Contributing
- Although this project is still under construction, you can still take part in the data load construction. 
I have only implemented two topics: Social media and Academics, and auto-downloading is still on the way. 
If you like, you can work on other topics except for these two topics. It is better to check the base dataloader [class](https://github.com/bigheiniu/COVID-19-Dataloaders/blob/master/DataLoader.py). 

- Please feel free to send me [pull requests](https://github.com/bigheiniu/COVID-19-Dataloaders/pulls) or email ([yichuan1@asu.edu](mailto:yichuan1@asu.edu)) to add resources.


  


