import pandas as pd
class median:
    '''
    Calculates the median 
    '''
    def __init__(self,dataframe, date_column):
        '''
        dataframe : the dataframe that you wish to pass. Must be a pandas dataframe
        date_column : the name of the date column in the dataframe. Pass a string.
        '''
        self.dataframe = dataframe
        self.date_column = date_column
    
    def add_ind(self):
    
        self.dataframe['year'] = pd.DatetimeIndex(self.dataframe[self.date_column]).year
        self.dataframe['month'] = pd.DatetimeIndex(self.dataframe[self.date_column]).month
        self.dataframe['day'] = pd.DatetimeIndex(self.dataframe[self.date_column]).day
        return self.dataframe
    def calculate_median(self):
        
        
        self.dataframe[self.date_column]=pd.to_datetime(self.dataframe[self.date_column])
        test = self.add_ind()
        columns = test.columns.tolist()+['index']
        result = pd.DataFrame(columns=columns)
        year = test.year.unique().tolist()
        for y in year:
            year_set = test.loc[test['year'] == y]
            #result = pd.DataFrame(columns=columns)
            for i in range(1,13):
                test1 = year_set.loc[year_set.month ==i].copy()
                med = test1.loc[year_set.month == i].day.median()
                test1['index']=test1['day'].apply(lambda x: x-med)
                result = pd.concat([result,test1])
        return result