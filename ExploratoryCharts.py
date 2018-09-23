from Constants import Constants
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt 
import matplotlib as matplotlib 
import pandas as pd 
import numpy as np 

class Exploratory:

    def createPlot(self,data, cols, plotType, msg, pdf):
        fig = plt.figure()
        if plotType in ['hist']:
            fig = data[cols].hist()
        elif plotType in ['pie']:
            fig = data[cols].value_counts().plot.pie()
        elif plotType in ['kde']:
            fig = data[cols].plot.kde()
        elif plotType in ['lag']:
            from pandas.tools.plotting import lag_plot
            fig = lag_plot(data[cols])
        elif plotType in ['autocorrelation']:
            from pandas.tools.plotting import autocorrelation_plot
            fig = autocorrelation_plot(data[cols])
        elif plotType in ['plots']:
            fig = data[cols].plot(x_compat=True)
        else:
            fig = data[cols].value_counts().plot(kind = plotType)
        if plotType in ['bar','hist','kde','lag','autocorrelation','plots']:
            fig.set_ylabel(cols)
        fig.set_title(msg)
        pdf.savefig(fig.get_figure())

    ## The function is used to create scatter plots for each columns in the data set
    def createScatterPlots(self,data,base_dir, fileName):
        pdf = PdfPages(''.join([base_dir,fileName]))
        columns = data._get_numeric_data().columns
        for i in range(1, len(columns)):
            for j in range(i+1, len(columns)):
                fig = plt.figure()
                fig = data.plot.scatter(columns[i], columns[j])
                fig.set_ylabel(columns[j])
                fig.set_xlabel(columns[i])
                fig.set_title(''.join(["plot of ", columns[j]," vs ", columns[i]]))
                pdf.savefig(fig.get_figure())
        pdf.close()

    def createRadViz(self,data,base_dir,fileName):
        from pandas.tools.plotting import radviz
        pdf = PdfPages(''.join([base_dir,fileName]))
        for cols in data.columns.values:
            if len(data[cols].value_counts()) <= 20 and len(data[cols].value_counts()) > 1:
                req_data = data._get_numeric_data()
                req_data[cols]= data[cols]
                fig = plt.figure()
                fig = radviz(req_data, cols)
                fig.set_title(''.join(["plot of radviz vis ", cols]))
                pdf.savefig(fig.get_figure())
        pdf.close()

    def createParallelCoordinates(self,data,base_dir,fileName):
        from pandas.tools.plotting import parallel_coordinates
        pdf = PdfPages(''.join([base_dir,fileName]))
        for cols in data.columns.values:
            if len(data[cols].value_counts()) <= 20 and len(data[cols].value_counts()) > 1:
                req_data = data._get_numeric_data()
                req_data[cols]= data[cols]
                fig = plt.figure()
                fig = parallel_coordinates(req_data, cols)
                fig.set_title(''.join(["plot of radviz vis ", cols]))
                pdf.savefig(fig.get_figure())
        pdf.close()

    def createCategoricalPlots(self,data,base_dir,fileName,plotType):
	pdf = PdfPages(''.join([base_dir,fileName]))
	for cols in data.columns.values:
		if len(data[cols].value_counts()) >= 10:
			self.createPlot(data, cols, plotType, ''.join(["plot of", cols]), pdf)
	pdf.close()

    def generatePlot(self,vcpe_data,base_dir,plotType):
	print "Reached Generate Plots"
        if plotType==Constants.keywordBar:
            filenameBar = "BarPlots.pdf"
            self.createCategoricalPlots(vcpe_data, base_dir, filenameBar,plotType)
        elif plotType == Constants.keywordBox:
            filenameBox = "BoxPlots.pdf"
            self.createNumericPlots(vcpe_data, base_dir, filenameBox,plotType)
        elif plotType == Constants.keywordScatter:
            filenameScatter = "ScatterPlots.pdf"
            self.createScatterPlots(vcpe_data,base_dir, filenameScatter)
        elif plotType == Constants.keywordHistogram:
            filenameHistogram = "Histograms.pdf"
            self.createNumericPlots(vcpe_data,base_dir, filenameHistogram,plotType)
        elif plotType == Constants.keywordPie:
            filenamePiePlots = "PiePlots.pdf"
            self.createCategoricalPlots(vcpe_data,base_dir, filenamePiePlots,plotType)
        elif plotType == Constants.keywordDensity:
            filenameDensityPlots = "DensityPlots.pdf"
            self.createNumericPlots(vcpe_data,base_dir, filenameDensityPlots,plotType)
        elif plotType == Constants.keywordLag:
            filenameLagPlots = "LagPlots.pdf"
            self.createNumericPlots(vcpe_data,base_dir, filenameLagPlots,plotType)
        elif plotType == Constants.keywordAutoCorrelation:
            filenameAutoCorrelationPlots = "AutoCorrelationPlots.pdf"
            self.createNumericPlots(vcpe_data,base_dir, filenameAutoCorrelationPlots,plotType)
        elif plotType == Constants.keywordBootStrap:
            filenameBootStrapPlots = "BootStrapPlots.pdf"
            self.createBootStrapPlots(vcpe_data,base_dir, filenameBootStrapPlots)
        elif plotType == Constants.keywordPlots:
            filenamePlots = "Plots.pdf"
            self.createNumericPlots(vcpe_data,base_dir, filenamePlots,plotType)
        elif plotType == Constants.keywordradviz:
            fileNameRadViz = "RadvizPlots.pdf"
            self.createRadViz(vcpe_data,base_dir,fileNameRadViz)
