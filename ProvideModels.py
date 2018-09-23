'''
Created on Dec 30, 2015

@author: vibhor
'''
from sklearn.decomposition import RandomizedPCA

from sklearn import naive_bayes
from sklearn import svm
from sklearn import linear_model
from sklearn import ensemble
from sklearn import tree

class ProvideModels:
    
    def get_GaussianNB(self):
        return naive_bayes.GaussianNB()
    
    def get_MultinomialNB(self):
        return naive_bayes.MultinomialNB()
    
    def get_BernoulliNB(self):
        return naive_bayes.BernoulliNB()
    
    def get_logisticRegression(self):
        return linear_model.LogisticRegression()
    
    def get_SGDClassifier(self):
        return linear_model.SGDClassifier
    
    def get_SGDRegressor(self):
        return linear_model.SGDRegressor
    
    def get_LinearSVM(self):
        return svm.LinearSVC()
    
    def get_DecisionTreeClassifier(self):
        return tree.DecisionTreeClassifier()
    
    def get_DecisionTreeRegressor(self):
        return tree.DecisionTreeRegressor()
    
    def get_RandomForestClassifier(self,estimators):
        return ensemble.RandomForestClassifier(n_estimators = estimators)
    
    def get_RandomForestRegressor(self,estimators):
        return ensemble.RandomForestRegressor(n_estimators = estimators)
    
    def get_GBMClassifier(self,estimators):
        return ensemble.GradientBoostingClassifier(n_estimators = estimators)
    
    def get_GBMRegressor(self,estimators):
        return ensemble.GradientBoostingRegressor(n_estimators = estimators)
    
    def get_LinearRegression(self):
        return linear_model.Lasso()
    
    def get_PCA(self,features_train,n_component):
        return RandomizedPCA(n_components=n_component, whiten=True).fit(features_train)
    
        