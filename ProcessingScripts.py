'''
Created on Jan 12, 2016

@author: vibhor
'''
from FileHandler import FileHandler
from ProcessData import ProcessData
from ProvideModels import ProvideModels
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from ImplementMethods import ImplementMethods


class ProcessingScripts:

    def __init__(self,folderName):
        self.algos = ImplementMethods()
        self.file_handler = FileHandler(folderName)
        self.process_data = ProcessData()
        self.model = ProvideModels()
    def primary_evaluation_script(self,train_df,labels, test_df,model_sequence,test_id):
        print "starting process"
        features_train, labels_train, features_test, labels_test = self.process_data.break_training_data_set(train_df, labels)
        print "size of training data is " ,features_train.shape
        print "size of training labels is ", labels_train.shape
        print "size of test set is ", features_test.shape
        print "size of test labels is ", labels_test.shape

        models, predictions = self.algos.apply_algorithms(features_train,labels_train,features_test,labels_test,model_sequence)

        # print "starting to process test data "
        #
        # predictions = []
        # for model,name in zip (models,model_sequence):
        #     pred = self.file_handler.write_file(model,test_df,name,test_id)
        #     predictions.append(pred)
        #
        #     print "process completed "
        return predictions

    def boost_with_pca(self,train_features,labels,test_features):
        print "starting process"

        features_train, labels_train, features_test, labels_test = self.process_data.break_training_data_set(
                                                                                        train_features, labels)
        n_components = [10,20,30,40,50,60,70,80,90,100,110,120]

        while(n_components):
            n_component = n_components[0]
            n_components.remove(n_component)

#         model = get_bernoulli_model(features_train, n_component)
            model = self.model.get_pca_model(features_train,n_component)
            accuracy, f1Score, pred = self.boost_with_model(features_train,labels_train,features_test,labels_test,
                                                                       model,n_component)
            print " accuracy with bernoulli RBM is ", accuracy
            print " calculated f1Score is ", f1Score
            print "-----------------------------------------------------------------------------------------------"

    def boost_with_model(self,features_train,labels_train,features_test,labels_test,model,n_component):

        train_data = model.transform(features_train)
        test_data = model.transform(features_test)


        clf = RandomForestClassifier(n_estimators = n_component)
        #     clf = svm.LinearSVC()
        clf=clf.fit(train_data,labels_train)
        pred = clf.predict(test_data)

        accuracy = accuracy_score(labels_test, pred)
        f1Score = f1_score(labels_test, pred, average = 'weighted')

        return (accuracy, f1Score, pred)

    def boost_with_gbm(self,features,feature_dict,labels):

        d_descending = sorted(feature_dict.items(), key=lambda x: (-x[1], x[0]))
        f1Score_old = 0
        ftrs_selected = 10
        while True:
            if ftrs_selected > len(features.columns):
                break
            top_10_descending = d_descending[1:ftrs_selected]
            col_nos = [int(col[0][1:]) for col in top_10_descending]

            new_train_data = features[col_nos]

            new_features_train, new_labels_train, new_features_test, new_labels_test = self.process_data.break_training_data_set(new_train_data, labels)

            clf, accuracy,f1Score,pred = self.algos.perform_gradient_boosting(new_features_train, new_labels_train,
                                                                           new_features_test, new_labels_test)

            print " accuracy in gradient boosting  is ", accuracy
            print " calculated f1Score is ", f1Score
            print "-----------------------------------------------------------------------------------------------"

            f1Score_old = f1Score
            ftrs_selected += 10

            if f1Score > f1Score_old:
                break

        return ftrs_selected,pred
