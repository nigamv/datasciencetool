'''
Created on Dec 30, 2015

@author: vibhor
'''

import pandas as pd
from ProcessingScripts import ProcessingScripts
from sklearn.preprocessing import LabelEncoder
from ProcessData import PreProcessData
from ProcessData import ProcessData
from Constants import Constants
pd.options.mode.chained_assignment = None

# from ProcessData import ProcessData
# from PlotGraphs import PlotGraphs

if __name__ == '__main__':

    print "starting process"
      
    train_df = pd.read_csv('data/Prudential/train.csv')
    print "dimensions of training data", train_df.shape
  
    train_df = train_df.fillna(-1)
    features_train=train_df.drop(["Id","Response"],axis=1)
    le=LabelEncoder()
    features_train["Product_Info_2"]=le.fit_transform(features_train["Product_Info_2"])
      
    labels=train_df["Response"].astype("category")
    print "len of labels is", labels
    labels=labels.cat.rename_categories(range(8))
  
 
    test_df = pd.read_csv('data/Prudential/test.csv')
    print "dimension of test data", test_df.shape
  
    test_id = test_df['Id']
    test_df=test_df.fillna(-1)
    features_test=test_df.drop(["Id"],axis=1)
    features_test["Product_Info_2"]=le.transform(features_test["Product_Info_2"])
  
#    model_sequence = ['naivebayes','logistic','svm','gradient','decisiontree','randomforest','xgboost']
#     model_sequence = [Constants.gaussianNB,Constants.logisticRegression,Constants.linearSVM,
#                       Constants.gbmClassifier,Constants.randomForestClassifier]
    model_sequence = [Constants.decisionTreeClassifier,Constants.randomForestClassifier]
    scripts = ProcessingScripts('Prudential')
    predictions = scripts.primary_evaluation_script(features_train,labels,features_test,
                                                                        model_sequence,test_id)
    



#     print "starting process"
#
#     train_df = pd.read_csv('data/Prudential/train.csv')
#     print "dimensions of training data", train_df.shape
#
#     train_df = train_df.fillna(-1)
#     features_train=train_df.drop(["Id","Response"],axis=1)
#     le=LabelEncoder()
#     features_train["Product_Info_2"]=le.fit_transform(features_train["Product_Info_2"])
#
#     labels=train_df["Response"].astype("category")
#     print "len of labels is", labels
#     labels=labels.cat.rename_categories(range(8))
#
#
#     test_df = pd.read_csv('data/Prudential/test.csv')
#     print "dimension of test data", test_df.shape
#
#     test_id = test_df['Id']
#     test_df=test_df.fillna(-1)
#     features_test=test_df.drop(["Id"],axis=1)
#     features_test["Product_Info_2"]=le.transform(features_test["Product_Info_2"])
#
# #    model_sequence = ['naivebayes','logistic','svm','gradient','decisiontree','randomforest','xgboost']
# #     model_sequence = [Constants.gaussianNB,Constants.logisticRegression,Constants.linearSVM,
# #                       Constants.gbmClassifier,Constants.randomForestClassifier]
#     model_sequence = [Constants.decisionTreeClassifier]
#     scripts = ProcessingScripts('Prudential')
#     predictions = scripts.primary_evaluation_script(features_train,labels,features_test,
#                                                                         model_sequence,test_id)


