'''
Created on Dec 30, 2015

@author: vibhor
'''
import xgboost as xgb
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from ProcessData import ProcessData

class XGBoost:

    def __init__(self):
        self.process_data = ProcessData()

    def xgboost_train_multiclass(self,features_train,labels_train,features_test,
                                 labels_test, num_class,eta_list = [0.1, 0.2, 0.3, 0.4],
                                 depths_list = [6,9,12,15]):
        print "Number of classes are", num_class
        params = {}
#         eta_list = [0.1, 0.2, 0.3, 0.4]
#         depths_list = [6,9,12,15]
        params["objective"] = "multi:softprob"
#         params["eta"] =  0.1
        params["subsample"] = 0.8
        params["colsample_bytree"] = 0.8
        params["num_class"]=num_class+1
#     params["scale_pos_weight"] = 1
        params["silent"] = 1
#         params["max_depth"] = 12
        params["eval_metric"] = 'mlogloss'


        offset = 10000
        num_rounds = 200
        best_accuracy = 0
        best_f1score=0
        best_model = None
        best_pred = None

        for eta in eta_list:
            params["eta"] = eta
            for depth in depths_list:

                params["max_depth"]= depth
                plst = list(params.items())

                ftrs_train, lbls_train, ftrs_vld, lbls_vld = self.process_data.break_training_data_set(features_train, labels_train)
                print " shape of ftrs_train", ftrs_train.shape
                print "shape of lbls_train", lbls_train.shape
                print "shape of ftrs_vld", ftrs_vld.shape
                print "shape of lbls_vld", lbls_vld.shape

                # ftrs_train = ftrs_train.astype(float)
                # lbls_train = lbls_train.astype(float)
                # print "data types of train", ftrs_train.dtypes
                # print "data type of label", lbls_train.dtypes
                print lbls_train.dtypes
                xgtrain = xgb.DMatrix(ftrs_train, lbls_train.as_matrix())
                xgval = xgb.DMatrix(ftrs_vld, lbls_vld.as_matrix())
                watchlist = [(xgtrain, 'train'),(xgval, 'val')]
                model = xgb.train(plst, xgtrain, num_rounds, watchlist, early_stopping_rounds=50,verbose_eval=True)

                xgtest = xgb.DMatrix(features_test, labels_test.as_matrix())
                pred = model.predict(xgtest,ntree_limit= model.best_iteration)
                pred_df = pd.DataFrame(pred)
                pred_xgb = pred_df.apply(self.process_data.get_cat,axis=1)

                accuracy = accuracy_score(labels_test, pred_xgb)
                print "accuracy with eta ", eta, "and depth ", depth,"is ",accuracy
                if accuracy > best_accuracy:
                    best_accuracy = accuracy

                f1score = f1_score(labels_test, pred_xgb, average = 'weighted')
                print "f1score with eta ", eta, "and depth ", depth, "is", f1score
                if f1score > best_f1score:
                    best_f1score = f1score
                    best_model = model
                    best_pred = pred_xgb

        return (best_model,best_accuracy,best_f1score,best_pred)

    def xgboost_train_regression(self,features_train,labels_train,features_test, labels_test, num_class):

        params = {}
        params["objective"] = "reg:linear"
#         params["eta"] =  0.1
        params["subsample"] = 0.8
        params["colsample_bytree"] = 0.8
#         params["num_class"]=num_class
#     params["scale_pos_weight"] = 1
        params["silent"] = 1
#         params["max_depth"] = 12
        params["eval_metric"] = 'rmse'

        plst = list(params.items())
#         offset = 10000
        num_rounds = 200

        ftrs_train, lbls_train, ftrs_vld, lbls_vld = self.process_data.break_training_data_set(features_train, labels_train)
        xgtrain = xgb.DMatrix(ftrs_train, lbls_train)
        xgval = xgb.DMatrix(ftrs_vld, lbls_vld)
        watchlist = [(xgtrain, 'train'),(xgval, 'val')]
        model = xgb.train(plst, xgtrain, num_rounds, watchlist, early_stopping_rounds=50,verbose_eval=True)

        xgtest = xgb.DMatrix(features_test, labels_test)
        pred_xgb = model.predict(xgtest)
#         pred_df = pd.DataFrame(pred)
#         pred_xgb = pred_df.apply(self.process_data.get_cat,axis=1)

        accuracy = accuracy_score(labels_test, pred_xgb)
        f1score = f1_score(labels_test, pred_xgb, average = 'weighted')

        return (model,accuracy,f1score,pred_xgb)
