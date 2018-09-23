'''
Created on Jan 6, 2016

@author: vibhor
'''
from Algorithms import LogisticRegression
from Algorithms import GradientBoosting
from Algorithms import LinearRegression
from Algorithms import NaiveBayes
from Constants import Constants
from Algorithms import DecisionTree
from Algorithms import RandomForest
from Algorithms import SVM
from XGBoost import XGBoost

class AlgorithmFactory:
    
    def __init__(self, name):
        self.model = None
        if name == Constants.logistic:
            self.model = LogisticRegression()
            
        elif name == Constants.linear:
            self.model = LinearRegression()
            
        elif name == Constants.GBM:
            self.model = GradientBoosting()
            
        elif name == Constants.naiveBayes:
            self.model = NaiveBayes()
            
        elif name == Constants.decisionTree:
            self.model = DecisionTree()
            
        elif name == Constants.randomForest:
            self.model = RandomForest()
        
        elif name == Constants.SVM:
            self.model = SVM()
        
        elif name == Constants.xgboost:
            self.model = XGBoost()
    
    def get_object(self):
        return self.model