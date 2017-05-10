import pandas as pd
import numpy as np

TEST_DATA = "Dataset/id-based-features-and-numeric-test.csv"
PREDICTIONS = "xgboost/submission-default-xgboost-pandas.csv"

CHUNKSIZE = 50000
NROWS = 150000

nrows = 0

for chunk_test, chunk_predictions in zip(pd.read_csv(TEST_DATA, chunksize=CHUNKSIZE), pd.read_csv(PREDICTIONS, chunksize=CHUNKSIZE, usecols=['Response'])):
	# get response for each id in chunk_predictions and corresponding features
	chunk_concat = pd.concat([df1.set_index('Id'),df2.set_index('Id')], axis=1, join='inner').reset_index()
	final = pd.concat(final,chunk_concat)
	
	nrows += CHUNKSIZE
	if nrows == 150000:
		break

print final

