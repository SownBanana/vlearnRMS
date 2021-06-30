import os
import numpy as np
import pandas as pd 
from app.models.CF import CF
from sklearn.model_selection import train_test_split
basedir = os.path.abspath(os.path.dirname(__file__))

data_file = os.path.join(basedir, 'static/ratings.csv')

r_cols = ['book_id', 'user_id', 'rating']
ratings = pd.read_csv(data_file, usecols = r_cols, encoding='latin-1')

train, test = train_test_split(ratings, test_size=0.2)

rate_train = train.to_numpy()
rate_test = test.to_numpy()
print('Train: ',len(rate_train))
print('Test: ',len(rate_test))


rms = CF(rate_train, k = 2)
rms.fit()
# rms.print_recommendation()

n_tests = rate_test.shape[0]
SE = 0 # squared error
pred = 0
for n in range(n_tests):
    if n % 10000 == 0:
        print ('----------------------------------------------------------------')
        print ('n: ', n)
        print ('RMSE: ', np.sqrt(SE/n_tests))
    pred = rms.pred(rate_test[n, 0], rate_test[n, 1], normalized = 0)
    SE += (pred - rate_test[n, 2])**2 

RMSE = np.sqrt(SE/n_tests)
print ('============================================')
print ('Final results:')
print ('n_tests = ', n_tests)
print ('User-user CF, RMSE =', RMSE)