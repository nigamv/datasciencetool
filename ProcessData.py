'''
Created on Dec 30, 2015

@author: vibhor
'''
from __future__ import division
import numpy as np
import pandas as pd
import collections
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


class ProcessData:

    def break_training_data_set(self,training_features, training_labels):

        msk = np.random.rand(len(training_features)) < 0.8
        ftrs_train = training_features[msk]
        lbls_train = training_labels[msk]

        ftrs_vld = training_features[~msk]
        lbls_vld = training_labels[~msk]

        return (ftrs_train, lbls_train, ftrs_vld, lbls_vld)

    def getTrainTestValData(self,data, label):
        # Generate a random index for 80 % of the data
        msk_cat = np.random.rand(len(data)) < 0.8

        # Prepare the training data and training label
        temp_cat = data[msk_cat]
        temp_label = label[msk_cat]

        msk_val = np.random.rand(len(temp_cat)) < 0.75

        train_data = temp_cat[msk_val]
        train_label = temp_label[msk_val]

        val_data = temp_cat[~msk_val]
        val_label = temp_label[~msk_val]

        # Prepare the test data and label
        test_data = data[~msk_cat]
        test_label = label[~msk_cat]

        print "Dimensions of training data: ", train_data.shape
        print "Dimensions of validation set: ", val_data.shape
        print "Dimensions of test set: ", test_data.shape

        return [(train_data,train_label), (val_data,val_label), (test_data, test_label)]

    def add_dummy_variable(self,dataset, variable_list):

        print "dimensions of dataset before processing", dataset.shape

        categorical_df = dataset[variable_list]
        print "dimensions of categorical dataset ", categorical_df.shape

        dataset = dataset.drop(variable_list,1)
        print "dimensions after dropping categorical variables", dataset.shape
        print "---------------------------------------------------------------------------------"

        dummy_df = pd.DataFrame()
        for name in variable_list:
            print "processing", name
            series = categorical_df[name].values
            dummy_df= dummy_df.add(pd.get_dummies(series))

#     dummy_df = pd.concat(new_df_list)
        dataset = dataset.add(dummy_df)
        print "final dimensions", dataset.shape
        print "---------------------------------------------------------------------------------"

        return dataset

    def get_cat(self,x):
        retval=x.idxmax()
        return retval

    def get_label_distribution(self,labels):
        counter = collections.Counter(labels)
        dist_list = counter.values()
        return dist_list


class Operations:

    def perform_operations(self,features_train, labels_train, features_test, labels_test,clf):

        clf.fit(features_train,labels_train)
        pred = clf.predict(features_test)
        accuracy = accuracy_score(labels_test, pred)
        f1score = f1_score(labels_test, pred, average = 'weighted')

        return (accuracy, f1score, pred)

class PreProcessData:

    ## This function is used to convert string columsn to categories with no NaN values.
    #   @param      data        dataset to operate upon
    #               colList     Columns which are to be converted from string to numeric categories
    #   @return     data        dataset with string categories converted to numeric
    def convStrToCat(self,data, colList):
        for col in colList:
            if data[col].isnull().sum() == 0:
                categories = data[col].value_counts().index
                cat_numeric = list(range(len(categories)))
                tupleList = {}
                for val, num in zip(categories, cat_numeric):
                    tupleList[val] = num
                data[col] = [tupleList[val] for val in data[col]]
        return data

    ## The function returns a subset of the dataset passed, with no NaN values
    #   @param      data            dataset to be processed
    #
    #   @return     final_data      The dataset with no NaN values
    #               perfectCols     List of column names with no NaN values
    def getPerfectColumns(self,data):
        # Get percentage NAN value for each column

        nanList = []
        for col in data.columns:
            per_NA = data[col].isnull().sum() / len(data)
            nanList.append((col, per_NA))

        # print nanList
        perfectCols = [elem[0] for elem in nanList if elem[1] == 0]
        final_data = data[perfectCols]

        return final_data, perfectCols

    ## The function fills categorical NaN values using any classification model
    #   @param      data            dataset to be processed
    #               final_data      dataset with no NaN value columns
    #               model           model to use for prediction
    #               perfectCols     List of cols with no NaN columns
    #   @return     final_data      dataset with NaN values completed using a prediction algorithm
    #               model           the model used for prediction
    def fillNanUsingModel(self,data, final_data, model, perfectCols):
        print "length of perfect cols is: ", len(perfectCols)
        nonPerfectCols = list(set(data._get_numeric_data().columns) - set(perfectCols))
        print "length of non perfect cols is: " , len(nonPerfectCols)
        for col in nonPerfectCols:
            print "current column being worked on ", col
            indexes = data[col].index[data[col].apply(np.isnan)]
            bad_df = data.index.isin(indexes)

            test_data = final_data[bad_df]
            train_data = final_data[~bad_df]
            train_label = data[col][~bad_df]

            model.fit(train_data, train_label)
            clf_pred = model.predict(test_data)

            final_data[col] = data[col]
            for index, val in zip(indexes, clf_pred):
                final_data.set_value(index, col, val)

        return final_data, model


    ## The function fills the NaN values in a categorical variable by filling the NaN values in same distribution
    ## as other labels are present in that column
    #
    #   @param      data            data set to be processed
    #               final_data      data set with no NaN columns
    #               perfectCols     list of column names with zero NaN values
    #   @return     final_data      processed data set
    def distributeCatonNan(self,data, final_data, perfectCols):
        nonPerfectCols = list(set(data._get_numeric_data().columns) - set(perfectCols))
        print "Total non perfect cols", len(nonPerfectCols)

        for col in nonPerfectCols:
            print col
            # Find the indexes of the particular columns with nan values
            indexes = data[col].index[data[col].apply(np.isnan)]
            bad_df = data.index.isin(indexes)

            # Get the distribution of remaining values in that column
            play_data = data[~bad_df]
            count_distribution = play_data[col].value_counts()/len(play_data)

            # Find the category with least distribution
            min_val = min(count_distribution.values)
            temp = pd.DataFrame([count_distribution.index, count_distribution.values]).transpose()
            temp.columns = ['category', 'values']
            min_cat = temp[temp['values'] == min_val]['category']

            # Create a list with a size of bad indexes with having the same distribution of categories as in previous
            repCount = count_distribution.values * ( len(req_data) - len(play_data) )
            repCountRounded= [math.floor(elem) for elem in repCount]
            nanList = np.repeat(count_distribution.index,repCountRounded)

            diffLength = (len(req_data) - len(play_data) ) - len(nanList)
            tempList = np.repeat(min_cat,diffLength)
            final_list = list(merge(nanList,tempList))

            # Add the column in final data with filled up NAN values
            final_data[col] = data[col]
            for index, val in zip(indexes, final_list):
                final_data.set_value(index, col, val)

        return final_data

    ## Drop columns with more than threshhold of the Data as NaN
    #   @param      data        data set to be processed
    #               threshhold  threshhold of acceptable NaN values
    #   @return     data        processed data set
    def dropAllNACols(self,data, threshhold):
        colsToDrop=[]

        for col in data.columns:
            sumNA = data[col].isnull().sum()
            if sumNA >= threshhold * data.shape[0]:
                colsToDrop.append(col)
        data.drop(colsToDrop, inplace=True, axis=1)
        return data

    ## The function finds categorical columns which are numeric. A categorical column is defined as one having less than 32 categories.
    #
    #   @param      data        data set to be processed
    #
    #   @return     data        data set with numeric categorical cols
    def findNumericCategoryColumns(self,data):
        categoricalCols = []
        for cols in data.columns:
            if len(data[cols].value_counts()) <= 32:
                categoricalCols.append(cols)
        return data[categoricalCols]
