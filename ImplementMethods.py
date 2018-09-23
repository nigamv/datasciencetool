'''
Created on Dec 29, 2015

@author: vibhor
'''

import csv
import pandas as pd
import numpy as np
from ProcessData import ProcessData
from Constants import Constants
from AlgorithmFactory import AlgorithmFactory

class ImplementMethods:
    "various machine learning algorithms"

    def __init__(self):

        self.process_data = ProcessData()

    def apply_algorithms(self,features_train,labels_train,features_test,labels_test,model_sequence):
    # applying logistic regression for classification purposes
        print "entered applied algorithms function"

        with open('results/Prudential/algorithms_results.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

            spamwriter.writerow(['Method','Accuracy','F1score'])
            predictions = []
            models = []

            print "File Created"
            for name in model_sequence:
                algo_name = name.split(':')
                print algo_name
                if 'naive_bayes' == algo_name[0]:
                    model = AlgorithmFactory(Constants.naiveBayes).get_object()
                    clf, accuracy,f1Score,pred = model.perform_naive_bayes(features_train, labels_train,
                                                                          features_test, labels_test,name)
                    predictions.append(pred)
                    models.append(clf)
                    print " accuracy in naive bayes is ", accuracy
                    print " calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['Naive Bayes',accuracy,f1Score])

                if 'logisticRegression' == algo_name[0]:
                    model = AlgorithmFactory(Constants.logistic).get_object()
                    clf, accuracy,f1Score,pred = model.perform_logistic_regression(features_train, labels_train,
                                                                                  features_test, labels_test, name)
                    predictions.append(pred)
                    models.append(clf)
                    print " accuracy in logistic regression is ", accuracy
                    print " calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['Logistic',accuracy,f1Score])

                if 'svm' == algo_name[0]:
                    model = AlgorithmFactory(Constants.SVM).get_object()
                    clf, accuracy,f1Score,pred = model.perform_svm_SVC(features_train, labels_train,
                                                                            features_test, labels_test)
                    predictions.append(pred)
                    models.append(clf)
                    print " accuracy in SVM regression is ", accuracy
                    print " calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['SVM',accuracy,f1Score])

                if 'GBM' == algo_name[0]:
                    model = AlgorithmFactory(Constants.GBM).get_object()
                    clf, accuracy,f1Score,pred = model.perform_gradient_boosting(features_train, labels_train,
                                                                                        features_test, labels_test,name)
                    predictions.append(pred)
                    models.append(clf)
                    print " accuracy in gradient boosting  is ", accuracy
                    print " calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['gradient',accuracy,f1Score])

                if 'decisionTree' == algo_name[0]:
                    model = AlgorithmFactory(Constants.decisionTree).get_object()
                    clf, accuracy,f1Score,pred = model.perform_decision_tree(features_train, labels_train,
                                                                                features_test, labels_test,name)
                    predictions.append(pred)
                    models.append(clf)
                    print "accuracy in decision tree", accuracy
                    print "calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['decision',accuracy,f1Score])

                if 'randomForest' == algo_name[0]:
                    model = AlgorithmFactory(Constants.randomForest).get_object()
                    clf, accuracy,f1Score,pred = model.perform_random_forest(features_train, labels_train,
                                                                            features_test, labels_test,name)
                    predictions.append(pred)
                    models.append(clf)
                    print "accuracy in random forest", accuracy
                    print "calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['random_forest',accuracy,f1Score])

                if 'XGBoost' == algo_name[0]:
                    print "Reached Xgboost condition"
                    model = AlgorithmFactory(Constants.xgboost).get_object()
                    print " number fo class", np.unique(labels_train)
                    clf, accuracy,f1Score,pred = model.xgboost_train_multiclass(features_train, labels_train, features_test, labels_test,
                                                                              num_class=len(np.unique(labels_train)),eta_list =[0.1,0.2],depths_list=[6,9])
                    predictions.append(pred)
                    models.append(clf)
                    print " accuracy in xgboost classification is ", accuracy
                    print " calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['xgboost_classification',accuracy,f1Score])

                if 'xgboost:linear' == algo_name[0]:
                    model = AlgorithmFactory(Constants.xgboost).get_object()
                    clf, accuracy,f1Score,pred = model.xgboost_train_regression(features_train, labels_train, features_test, labels_test,
                                                                              num_class=len(labels_train.unique()))
                    predictions.append(pred)
                    models.append(clf)
                    print " accuracy in xgboost regression is ", accuracy
                    print " calculated f1Score is ", f1Score
                    print "-----------------------------------------------------------------------------------------------"
                    spamwriter.writerow(['xgboost_regression',accuracy,f1Score])

        return (models,predictions)
