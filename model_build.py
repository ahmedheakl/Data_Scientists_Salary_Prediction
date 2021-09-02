import pandas as pd
import numpy as np
# choose the wanted columns
df = pd.read_csv('./csv_saved/data_eda.csv')
# print(df.columns)

df = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','per_hour','employer_provided',
             'job_state','same_state','age','python','spark','aws','excel','job_simp','seniority','desc_len']]

# get dummy data
df_dum = pd.get_dummies(df)

# train test split
from sklearn.model_selection import train_test_split
X = df_dum.drop('avg_salary', axis=1)
y = df_dum.avg_salary.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# statsmodel for inferencials
import statsmodels.api as sm

X_sm = sm.add_constant(X)
model = sm.OLS(y,X_sm)
# print(model.fit().summary())

# Linear Regression
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)
# print(np.mean(cross_val_score(linear_regression, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

# lasso regression
lasso = Lasso()
lasso.fit(X_train, y_train)
# print(np.mean(cross_val_score(lasso, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

# tuning lasso using smoothing with alpha parameter
alpha = []
error = []
for i in range(10, 100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))

import matplotlib.pyplot as plt
plt.plot(alpha,error)    
plt.show()

best_alpha = alpha[error.index(max(error))]
print(best_alpha, max(error))

lasso = Lasso(alpha=best_alpha)

# random forest
from sklearn.ensemble import RandomForestRegressor
random_forrest = RandomForestRegressor()
print(np.mean(cross_val_score(random_forrest, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

# tune best model
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(random_forrest,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)
gs.best_score_
gs.best_estimator_

# test phase 
pred_lm = linear_regression.predict(X_test)
pred_lml = lasso.predict(X_test)
pred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,pred_lm)
mean_absolute_error(y_test,pred_lml)
mean_absolute_error(y_test,pred_rf)

mean_absolute_error(y_test,(pred_lm+pred_rf)/2)

