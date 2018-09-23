'''
Created on Dec 30, 2015

@author: vibhor
'''
from ProcessData import ProcessData
# from Constants import Constants, MenuConstants
# from CustomDialog import MyTextInpuDialog
import pandas as pd
import xgboost as xgb
import csv
import os
# import wx
# import os
class FileHandler:

    def __init__(self, folderName):
        self.process_data = ProcessData()
        self.write_path = 'results/' + folderName + '/'

    def write_file(self, clf, features_test, typeofSet, test_id):
        print "predicting for ---->", typeofSet
        if typeofSet == 'xgboost:classifier':
            xgtest = xgb.DMatrix(features_test)
            pred = clf.predict(xgtest, ntree_limit=clf.best_iteration)
            pred_df = pd.DataFrame(pred)
            pred_df = pred_df.apply(self.process_data.get_cat, axis=1)

        elif typeofSet == 'xgboost:regression':
            xgtest = xgb.DMatrix(features_test)
            pred = clf.predict(xgtest)
#             pred_df = pd.DataFrame(pred,columns=range(1,9))
#             pred_df = pred_df.apply(self.process_data.get_cat,axis=1)
        else:
            pred = clf.predict(features_test)
            pred_df = [x + 1 for x in pred]

        if not os.path.exists(self.write_path):
            os.mkdir(self.write_path)

        filePath = self.write_path + typeofSet + '_results.csv'
        with open(filePath, 'wb') as csvfile:

            spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Id', 'Response'])

            for ids, label in zip(test_id, pred_df):
                spamwriter.writerow([ids, label])

            print "file written", typeofSet

        return pred_df
