'''
Created on Jan 12, 2016

@author: vibhor
'''
from sklearn.metrics import accuracy_score
import math
from Constants import Constants 
from ProcessData import Operations
from ProvideModels import ProvideModels

class DecisionTree:
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_decision_tree(self,features_train, labels_train, features_test, 
                                                labels_test,algo_name, depths = [6,8,10,12]):
    
        print "------------- performing decision tree -------------------------"
        if algo_name == Constants.decisionTreeClassifier:
            clf = self.model.get_DecisionTreeClassifier()
        elif algo_name == Constants.decisionTreeRegressor:
            clf = self.model.get_DecisionTreeRegressor()
        
        best_accuracy= None
        model = None
        best_f1Score = None
        
        for depth in depths:
            clf.set_params(max_depth = depth)    
            accuracy,f1score, pred = self.prfrm_oprtns.perform_operations(features_train, labels_train, 
                                                             features_test, labels_test,clf)
            print "accuracy with depth ", depth, " is", accuracy
            print "f1Score with depth ", depth, " is", f1score
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
            if f1score > best_f1Score:
                best_f1Score = f1score
                model = clf
        return (model,accuracy,f1score,pred)
    

class LinearRegression:
    
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_linear_regression(self,features_train,labels_train,features_test,labels_test):
    
        clf = self.model.get_LinearRegression()
        clf.fit(features_train,labels_train)
        pred = clf.predict(features_test)
        pred_floor = [int (math.floor(x)) for x in pred]
        print "accuracy on test set is ", accuracy_score(labels_test, pred_floor)
    
        return pred_floor
    
class LogisticRegression:
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_logistic_regression(self,features_train, labels_train, features_test, 
                                                                            labels_test,algo_name):
        print "------------ performing logistic regression ---------------------"
        penalties = ['l2','l1']
        best_accuracy = None
        best_f1Score = None
        model = None
        
        if algo_name == Constants.logisticRegression:
            clf = self.model.get_logisticRegression()
        elif algo_name == Constants.logisticRegressionSGD:
            clf = self.model.get_SGDClassifier()
        for curr_penalty in penalties:
            clf.set_params(penalty = curr_penalty)
            accuracy,f1score, pred = self.prfrm_oprtns.perform_operations(features_train, labels_train, 
                                                                          features_test, labels_test,clf)
            print "accuracy with penalty",curr_penalty,"is",accuracy
            print "f1score with penalty",curr_penalty,"is",f1score
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
            if f1score > best_f1Score:
                best_f1Score = f1score
                model = clf
                
        return (model,accuracy,f1score,pred)


class NaiveBayes:
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_naive_bayes(self,features_train, labels_train, features_test, labels_test,algo_name):
        
        print "-------------- performing naive bayes ---------------"
        if algo_name == Constants.gaussianNB:
            clf = self.model.get_GaussianNB()
        elif algo_name == Constants.multnomialNB:
            clf = self.model.get_MultinomialNB()
        elif algo_name == Constants.bernoulliNB:
            clf = self.model.get_BernoulliNB()
            
        accuracy,f1score, pred = self.prfrm_oprtns.perform_operations(features_train, labels_train, 
                                                                     features_test, labels_test,clf)
        return (clf,accuracy,f1score,pred)
    
class GradientBoosting:
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_gradient_boosting(self,features_train, labels_train, features_test, 
                                    labels_test, algo_name,learning_rates = [0.3]
                                    ,features = [0.7],depths = [9]):
    
        print "--------------- performing gradient boosting ----------------------"
        if algo_name == Constants.gbmClassifier:
            clf = self.model.get_GBMClassifier(len(features_train.columns))
        elif algo_name == Constants.gbmRegressor:
            clf = self.model.get_GBMRegressor(len(features_train.columns))
        
        best_accuracy = None
        model= None
        best_f1score= None
        
        for depth in depths:
            for feature in features:
                for curr_learning_rate in learning_rates:
                    clf.set_params(learning_rate = curr_learning_rate, max_depth = depth, 
                                        max_features = feature)
                    accuracy,f1score, pred = self.prfrm_oprtns.perform_operations(features_train, labels_train, 
                                                                     features_test, labels_test,clf)
                    print " accuracy with learning rate ",curr_learning_rate,"max_fatures ", feature, "and depth ", depth, "is ", accuracy
                    print " f1score with learning rate ",curr_learning_rate,"max_fatures ", feature, "and depth ", depth, "is ", f1score 
                    
                    if accuracy > best_accuracy:
                        best_accuracy = accuracy
                    if f1score > best_f1score:
                        best_f1score = f1score
                        model = clf
        return (model,accuracy,f1score,pred)
    
class SVM:
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_svm_SVC(self,features_train, labels_train, features_test, labels_test):
     
        print "------------ performing SVM --------------------"
        clf = self.model.get_LinearSVM()
        accuracy,f1score, pred = self.prfrm_oprtns.perform_operations(features_train, labels_train, features_test, labels_test,clf)
        return (clf,accuracy,f1score,pred)

class RandomForest:
    
    def __init__(self):
        self.prfrm_oprtns = Operations()
        self.model = ProvideModels()
        
    def perform_random_forest(self,features_train, labels_train, features_test, 
                              labels_test, algo_name, depths = [6,10,14,18,22,26]):
    
        print "-------------- performing random forest --------------------"
        if algo_name == Constants.randomForestClassifier:
            clf = self.model.get_RandomForestClassifier(len(features_train.columns))
        elif algo_name == Constants.randomForestRegressor:
            clf = self.model.get_RandomForestRegressor(len(features_train.columns))
        
        best_accuracy = None
        best_f1Score = None
        model = None
            
        for depth in depths:
            clf.set_params(max_depth  = depth)
            accuracy,f1score, pred = self.prfrm_oprtns.perform_operations(features_train, labels_train, 
                                                                          features_test, labels_test,clf)
            print "accuracy with depth ",depth,"is",accuracy
            print "f1score with depth",depth,"is",f1score
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
            if f1score > best_f1Score:
                best_f1Score = f1score
                model = clf
                
        return (model,accuracy,f1score,pred)
