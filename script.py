def EDA():
    #import library
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.preprocessing import LabelEncoder  
    import warnings
    warnings.filterwarnings("ignore")  

    #load data 
    file_name = input('please enter the path of file')
    try:
        dataset = pd.read_csv(file_name+".csv")


    except:
        dataset = pd.read_excel(file_name+".xlsx")

    print(dataset.info()); print(dataset.describe())

    print()
    print('#---------------------------------------------------------------')
    print('Check for Mising Value or NaN Value in the Dataset')
    print('#---------------------------------------------------------------')
    # Method - 1
    # Count Number of Missing Value on Each Column    
    print('\nCount Number of Missing Value on Each Column: ')        
    print(dataset.isnull().sum(axis=0))
        
    # Count Number of Missing Value on Each Row    
    #print('\nCount Number of Missing Value on Each Row: ')        
    #print(dataset.isnull().sum(axis=0))

    # Method - 2
    # Check if there are any missing values in Dataset
    feature_count = dataset.columns[dataset.isnull().sum() != 0].size
    print()
    print("Total Features with missing Values = " + str(feature_count))

    # Method - 3
    # Drop all missing value.
    dataset = dataset.drop(dataset.columns[dataset.isnull().sum() != 0], axis = 1,inplace = False)
    print(dataset)

    columnsToEncode = list(dataset.select_dtypes(include=['category',
                                                     'object','bool']))
    le = LabelEncoder()
    for feature in columnsToEncode:
        try:
            dataset[feature] = le.fit_transform(dataset[feature])
        except:
            print('Error encoding '+feature)
    plt.figure(1, figsize=(15,5))
    sns.heatmap(dataset.corr(), annot=True)

    dataset.plot( subplots=True, figsize=(20,15))
    plt.show()

    sns.pairplot(dataset)
    plt.show()

    for col in dataset.columns:
        dataset[col].hist()
        plt.xlabel(col)
        plt.show()

        dataset[col].plot(kind = 'box')
        plt.show()

EDA()
