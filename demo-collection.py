import pandas as pd
import numpy as np

TEST_DATA = "Dataset/id-based-features-and-numeric-test.csv"
PREDICTIONS = "xgboost/xgboost-default/submission-default-xgboost-pandas.csv"

test = pd.read_csv(TEST_DATA)
predictions = pd.read_csv(PREDICTIONS)
predictions.rename(columns={'# Id':'Id'}, inplace=True) # because submission file on server has Id column as '# Id'
concatenated = pd.concat([test.set_index('Id'),predictions.set_index('Id')], axis=1, join='inner').reset_index()

# get all 0s
allZeros = concatenated.loc[concatenated['Response'] == 0]

# get all 1s
allOnes = concatenated.loc[concatenated['Response'] == 1]


# select only a few rows from allZeros
allZeros = allZeros.iloc[:40,:] # first 40 rows, + all columns

# select only a few rows from allOnes
allOnes = allOnes.iloc[:10,:] # first 10 rows, + all columns

# concat allOnes and allZeros randomly, but joined based on column "id"
dfs = [allOnes, allZeros]
finalConcat = pd.concat(dfs)
finalConcat.to_csv("demo-data.csv", index=False, index_label=False)
