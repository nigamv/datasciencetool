'''
Created on Dec 30, 2015

@author: vibhor
'''
from XGBoost import XGBoost

class FeatureSelection:

    def __init__(self):
        self.xgboost = XGBoost()

    def feature_selection_withXGBoost(self,train_features,labels):
        print "starting process"

        features_train, labels_train, features_test, labels_test = self.break_training_data_set(train_features, labels)

        xgboost_model, accuracy,f1Score,pred = self.xgboost.xgboost_train(features_train.as_matrix(), labels_train.as_matrix(),
                                                     features_test.as_matrix(), labels_test.as_matrix(),
                                                         num_class= len(labels_train.unique()))

        xgboost_features = xgboost_model.get_fscore()

        return xgboost_features,train_features

    def varianceThreshold(threshhold=(0.8*(1-0.8))):
        from sklearn.feature_selection import VarianceThreshold
        # Set the threshold of variance at 80%
        sel = VarianceThreshold(threshold=threshhold)
        return pd.DataFrame(sel.fit_transform(dataToUse))
