'''
Created on Dec 30, 2015

@author: vibhor
'''
import csv
import collections
import matplotlib.pyplot as plt

class PlotGraphs:
    
    def plot_pie_chart(self,labels,fracs,fileName,title,initial_frac):
        explode= (0, 0, 0, 0, 0, 0, 0, 0.05)
        fig,(ax1,ax2) = plt.subplots(1,2)
        ax1.pie(fracs,explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax2.pie(initial_frac,explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.set_title(title, bbox={'facecolor':'0.8', 'pad':5})
        ax2.set_title('training labels', bbox={'facecolor':'0.8', 'pad':5})
#     fig.title(title, bbox={'facecolor':'0.8', 'pad':5})
        fig.savefig(fileName)
        plt.figure(figsize=(20,20))
        plt.close()
        
    
    def plot_results_pie_chart(self,fileName,imageName,title,initial_frac):
        with open(fileName, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            response = [row[1] for row in spamreader ]
        response= response[1:]
        counter = collections.Counter(response)
        labels = [x+1 for x in xrange(8)]
        fracs = [val for key,val in counter.iteritems()]
        self.plot_pie_chart(labels,fracs,'../images/'+imageName,title,initial_frac)
        
    
    def plot_hist(self,ylabels,label="",bins=50,xlabel="",ylabel="",title="",filePath='images/'):
        plt.hist(ylabels, bins, facecolor='b', alpha=0.7)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.savefig(filePath+title+'.jpeg')
        plt.close()
    
    def plot_multiple_hist(self,ylabels,facecolors = ['b','g','y','r','o']):
        for ylabel,color in zip(ylabels,facecolors):
            plt.hist(ylabel,facecolor=color, alpha=0.7)
#             plt.axis([1,8, 0, 1])
        return plt