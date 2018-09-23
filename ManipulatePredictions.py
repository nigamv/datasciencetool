'''
Created on Dec 30, 2015

@author: vibhor
'''
import pandas as pd
import csv

class ManipulatePredictions:
     
    def pick_modes(self,predictions,test_id):
        new_features = pd.DataFrame(pd.Series(pred) for pred in predictions)
        new_features = new_features.transpose()

        # Taking mode of all predictions 
        pred_df= [max(row) for row in new_features.as_matrix()]
        print len(pred_df)

        with open('modes_results.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Id','Response'])

            for ids,label in zip(test_id,pred_df):
                spamwriter.writerow([ids,label])

        print "file written modes_results.csv" 