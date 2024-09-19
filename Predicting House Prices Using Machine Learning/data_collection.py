import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Data:
        
    def __init__(self):
        data = pd.read_csv('house_prices.csv')
        
        # print(f"Dataset Shape(Row, Column): {data.shape}")

        # print(data.head())
        # print(data.info())
        # print(data.describe())

        #### Statistic
        #print(f"Statistic: \n{data.describe()}")

        ### Missing value 
        # missing_values = data.isnull().sum()
        # print(missing_values[missing_values > 0])

        ### Catagorical features
        # print(data['Neighborhood'].unique())
        # print(data['Neighborhood'].value_counts())

        ###Indentify target variable
        
        #print(data['SalePrice'].describe())

        numeric_data = data.select_dtypes(include=[float, int])
    
        corr_matrix = numeric_data.corr()
        # corr_matrix = data.corr()

        # Visualize the correlation matrix with a heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.show()


    
if __name__ =='__main__':
    Data()



