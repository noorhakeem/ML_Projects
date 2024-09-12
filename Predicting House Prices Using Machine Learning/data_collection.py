import pandas as pd

class Data:
        
    def __init__(self):
        data = pd.read_csv('test.csv')
        
        print(data.shape)



        # print(data.head())
        # print(data.info())
        # print(data.describe())
    
if __name__ =='__main__':
    Data()



