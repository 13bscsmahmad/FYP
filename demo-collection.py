import pandas as pd
import numpy as np

TEST_DATA = "Dataset/id-based-features-and-numeric-test.csv"
PREDICTIONS = "xgboost/xgboost-default/submission-default-xgboost-pandas.csv"

# CHUNKSIZE = 50000
# NROWS = 150000

# nrows = 0

# for chunk_test, chunk_predictions in zip(pd.read_csv(TEST_DATA, chunksize=CHUNKSIZE), pd.read_csv(PREDICTIONS, chunksize=CHUNKSIZE, usecols=['Response'])):
# 	# get response for each id in chunk_predictions and corresponding features
# 	chunk_concat = pd.concat([chunk_test.set_index('Id'),chunk_predictions.set_index('Id')], axis=1, join='inner').reset_index()
# 	final = pd.concat(final,chunk_concat)
	
# 	nrows += CHUNKSIZE
# 	if nrows == 150000:
# 		break

# print final

##################################

test = pd.read_csv(TEST_DATA)
predictions = pd.read_csv(PREDICTIONS)
predictions.rename(columns={'# Id':'Id'}, inplace=True) # because submission file on server has Id column as '# Id'
concatenated = pd.concat([test.set_index('Id'),predictions.set_index('Id')], axis=1, join='inner').reset_index()

# get all 0s

allZeros = concatenated.loc[concatenated['Response'] == 0]
allOnes = concatenated.loc[concatenated['Response'] == 1]


# select only a few rows from allZeros

allZeros = allZeros.iloc[:40,:] # first 40 rows, + all columns

# select only a few rows from allOnes

allOnes = allOnes.iloc[:10,:] # first 10 rows, + all columns

# concat allOnes and allZeros randomly, but joined based on column "id"

finalConcat = pd.concat([allOnes.set_index('Id'),allZeros.set_index('Id')], axis=1, join='inner').reset_index()
finalConcat.to_csv("demo-data.csv")

# dfs = [allZeros, allOnes]
# n = len(dfs)
# nrows = dfs[0].shape[0]
# ncols = dfs[0].shape[1]
# A = pd.concat(dfs, axis=1).values.reshape(nrows,-1,ncols)
# sidx = np.random.rand(nrows,n).argsort(1)
# out_arr = A[np.arange(nrows)[:,None],sidx,:].reshape(nrows,-1)
# df = pd.DataFrame(out_arr)

# print df
# df.to_csv("demo-data.csv")

# save to file