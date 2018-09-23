'''
Created on Jan 3, 2016

@author: vibhor
'''
from AlgoDescription import AlgoDescription

class Constants:

    gaussianNB = 'naive_bayes:gaussian'
    multnomialNB = 'naive_bayes:multinomial'
    bernoulliNB = 'naive_bayes:bernoulli'

    logisticRegression = 'logisticRegression:normal'
    logisticRegressionSGD = 'logisticRegression:SGD'

    linearRegression = 'linearRegression:normal'

    decisionTreeClassifier = 'decisionTree:classifier'
    decisionTreeRegressor = 'decisionTree:regressor'

    linearSVM = 'linearSVM:normal'

    gbmClassifier = 'GBM:classifier'
    gbmRegressor = 'GBM:regressor'

    randomForestClassifier = 'randomForest:classifier'
    randomForestRegressor = 'randomForest:regressor'

    xgboostClassifier = 'xgboost:classifier'
    xgboostRegressor = ''

    naiveBayes = 'NaiveBayes'
    decisionTree = 'DecisionTree'
    randomForest = 'RandomForest'
    GBM='GradientBoosting'
    SVM='SVM'
    logistic = 'logisticRegression'
    linear = 'linearRegression'
    xgboost = 'XGBoost'

    keywordBar = 'bar'
    keywordBox = 'box'
    keywordScatter = 'Scatter'
    keywordHistogram = 'Histogram'
    keywordPie = 'pie'
    keywordDensity = 'density'
    keywordLag = 'lag'
    keywordAutoCorrelation = 'autocorrelation'
    keywordradviz = 'radviz'
    keywordBootStrap = 'bootstrap'
    keywordPlots = 'plots'

    dataFilePath = 'dataFilePath.txt'
    trainDataFileDir = 'ProcessedDataFiles/train/'
    trainLabelFileDir = 'ProcessedDataFiles/trainLabel/'
    testDataFiileDir = 'ProcessedDataFiles/test/'
    testDataIdDir = 'ProcessedDataFiles/testId/'

    trainLabel = 'trainLabel'
    testId = 'testId'

    fileSelectionMessage = " Please select a file before processing "

    algo_map = {'Algortihms':[{'Supervised': [{ 'NaiveBayes':[{'GaussianNB':['1','2']},'MultinomialNB','BernoulliNB'],
                'LogisticRegression':['logisticRegression','logisticRegressionSGD'],
                'DecisionTree':['DecisionTreeClassifier', 'DecisionTreeRegressor'],
                'GradientBoosting':['GradientBoostingClassifier', 'GradientBoostingRegressor'],
                'RandomForest':['RandomForestClassifier', 'RandomForestRegressor'],
                'LinearRegression':[],
                'SVM':[],
                'XGBoost':[] }]
		}],
		'Plots': [{'Histogram':[], 'BoxPlot':[], 'BarPlot':[], 'ScatterPlot':[],
			'PiePlot':[],'DesnityPlots':[], 'AutoCorrelationPlots':[],'RadvizPlots':[] }]
		}
    chartList = ['Histogram','BoxPlot','BarPlot','ScatterPlot','PiePlot','DesnityPlots','AutoCorrelationPlots',
		'RadvizPlots']

    algo_description = {'Algorithm':AlgoDescription.algorithms}

    algo_const_mapping = {'GaussianNB':gaussianNB,'MultinomialNB':multnomialNB,'BernoulliNB':bernoulliNB,
                          'logisticRegression':logisticRegression, 'logisticRegressionSGD':logisticRegressionSGD,
                          'DecisionTreeClassifier':decisionTreeClassifier,'DecisionTreeRegressor':decisionTreeRegressor,
                          'GradientBoostingClassifier':gbmClassifier,'GradientBoostingRegressor':gbmRegressor,
                          'RandomForestClassifier':randomForestClassifier,'RandomForestRegressor':randomForestRegressor,
                          'LinearRegression':linear,'SVM':SVM,'XGBoost':xgboost}

    charts_const_mapping = {'Histogram':keywordHistogram, 'BoxPlot': keywordBox, 'BarPlot':keywordBar,
				'ScatterPlot':keywordScatter, 'PiePlot':keywordPie, 'DensityPlots':keywordDensity,
				'AutoCorrelationPlots':keywordAutoCorrelation, 'RadvizPlots':keywordradviz}

class MenuConstants:

    file = 'File'
    loadTrainDataFile = 'Load Train Data File'
    loadTestDataFile = 'Load Test Data File'
    showProcessedDataFile = 'Show Processed Data File'

    processData = 'Process Data Files'
    dropColumns = 'Drop Columns'
    fillNA = 'Fill Null Values'
    identifyLabelColumns ='Identify Label Column'
    identifyTestIdColumn = 'Identify Test Id Column'
