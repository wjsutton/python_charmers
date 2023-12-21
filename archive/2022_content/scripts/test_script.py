import math
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, cross_val_score, cross_val_predict 
from sklearn.linear_model import LogisticRegressionCV
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing, metrics, svm, ensemble
from sklearn.metrics import accuracy_score, classification_report
from tabpy.tabpy_tools.client import Client
#import tabpy

print('libraries loaded')

# Read the dataset (Note that the CSV provided for this demo has rows with the missing data removed)
df =  pd.read_csv('breastcancer.csv', header=0)

# Take a look at the structure of the file
df.head(n=10)

# Drop Id column not used in analysis
df.drop(['Id'], 1, inplace=True)

# Use LabelEncoder to convert textual classifications to numeric. 
# We will use the same encoder later to convert them back.
encoder = preprocessing.LabelEncoder()
df['Class'] = encoder.fit_transform(df['Class'])

# You could also do this manually in the following way:
# df['Class'] = df['Class'].map( {'benign': 0, 'malignant': 1} ).astype(int)

# Check the result of the transform
df.head(n=6)

# Split columns into independent/predictor variables vs dependent/response/outcome variable
X = np.array(df.drop(['Class'], 1))
y = np.array(df['Class'])

# Scale the data. We will use the same scaler later for scoring function
scaler = preprocessing.StandardScaler().fit(X)
X = scaler.transform(X)


# Define the parameter grid to use for tuning the Support Vector Machine
parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

# Pick the goal you're optimizing for e.g. precision if you prefer fewer false-positives
# recall if you prefer fewer false-negatives. For demonstration purposes let's pick several
# Note that the final model selection will be based on the last item in the list
scoringmethods = ['f1','accuracy','precision', 'recall','roc_auc']

# Iterate through different metrics looking for best parameter set
for score in scoringmethods:
    print("~~~ Hyper-parameter tuning for best %s ~~~" % score)
    
    # Setup for grid search with cross-validation for Support Vector Machine
    # n_jobs=-1 for parallel execution using all available cores
    svmclf = GridSearchCV(svm.SVC(C=1), parameters, cv=10, scoring=score,n_jobs=-1)
    svmclf.fit(X, y)
    
    # Show each result from grid search
    print("Scores for different parameter combinations in the grid:")
    print("  %0.3f  for %r"
              % (svmclf.best_score_, svmclf.best_params_)) 
    print("")
    
# Show classification report for the best model (set of parameters) run over the full dataset
print("Classification report:")
y_pred = svmclf.predict(X)
print(classification_report(y, y_pred))
    
# Show the definition of the best model
print("Best model:")
print(svmclf.best_estimator_)
    
# Show accuracy and area under ROC curve
print("Accuracy: %0.3f" % accuracy_score(y, y_pred, normalize=True))
print("Aucroc: %0.3f" % metrics.roc_auc_score(y, y_pred))
print("")

# Logistic regression with 10 fold stratified cross-validation using model specific cross-validation in scikit-learn
lgclf = LogisticRegressionCV(Cs=list(np.power(10.0, np.arange(-10, 10))),penalty='l2',scoring='roc_auc',cv=10)
lgclf.fit(X, y)
y_pred = lgclf.predict(X)

# Show classification report for the best model (set of parameters) run over the full dataset
print("Classification report:")
print(classification_report(y, y_pred))

# Show accuracy and area under ROC curve
print("Accuracy: %0.3f" % accuracy_score(y, y_pred, normalize=True))
print("Aucroc: %0.3f" % metrics.roc_auc_score(y, y_pred))

# Naive Bayes with 10 fold stratified cross-validation
nbclf = GaussianNB()
scores = cross_val_score(nbclf, X, y, cv=10, scoring='roc_auc')

# Show accuracy statistics for cross-validation
print("Accuracy: %0.3f" % (scores.mean()))
print("Aucroc: %0.3f" % metrics.roc_auc_score(y, cross_val_predict(nbclf, X, y, cv=10)))

# Define the parameter grid to use for tuning the Gradient Boosting Classifier
gridparams = dict(learning_rate=[0.01, 0.1],loss=['deviance','exponential'])

# Parameters we're not tuning for this classifier
params = {'n_estimators': 1500, 'max_depth': 4}

# Setup for grid search with cross-validation for Gradient Boosting Classifier
# n_jobs=-1 for parallel execution using all available cores
gbclf = GridSearchCV(ensemble.GradientBoostingClassifier(**params), gridparams, cv=10, scoring='roc_auc',n_jobs=-1)
gbclf.fit(X,y)

# Show the definition of the best model
print("Best model:")
print(gbclf.best_estimator_)
print("")

# Show classification report for the best model (set of parameters) run over the full dataset
print("Classification report:")    
y_pred = gbclf.predict(X)
print(classification_report(y, y_pred))

# Show accuracy and area under ROC curve
print("Accuracy: %0.3f" % accuracy_score(y, y_pred, normalize=True))
print("Aucroc: %0.3f" % metrics.roc_auc_score(y, y_pred))

# Connect to TabPy server using the client library
connection = Client('http://localhost:9004/')

# The scoring function that will use the Gradient Boosting Classifier to classify new data points
def SuggestDiagnosis(Cl_thickness, Cell_size, Cell_shape, Marg_adhesion, Epith_c_size, 
                     Bare_nuclei, Bl_cromatin, Normal_nucleoli, Mitoses):
    X = np.column_stack([Cl_thickness, Cell_size, Cell_shape, Marg_adhesion, Epith_c_size, 
                         Bare_nuclei, Bl_cromatin, Normal_nucleoli, Mitoses])
    X = scaler.transform(X)
    return encoder.inverse_transform(gbclf.predict(X)).tolist()


# Publish the SuggestDiagnosis function to TabPy server so it can be used from Tableau
# Using the name DiagnosticsDemo and a short description of what it does
connection.deploy('DiagnosticsDemo',
                  SuggestDiagnosis,
                  'Returns diagnosis suggestion based on ensemble model trained using Wisconsin Breast Cancer dataset', override = True)