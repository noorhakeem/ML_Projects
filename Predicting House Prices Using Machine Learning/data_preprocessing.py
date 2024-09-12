
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Handling missing values
imputer = SimpleImputer(strategy='mean')
data['LotFrontage'] = imputer.fit_transform(data[['LotFrontage']])

# One-hot encoding for categorical features
data = pd.get_dummies(data)

# Scaling the features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)




