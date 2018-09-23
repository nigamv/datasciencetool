'''
Created on Feb 17, 2016

@author: vibhor
'''
import wx
import os
import csv
import pandas as pd
from Constants import MenuConstants
from CustomDialog import MyTextInpuDialog
from Constants import Constants

class FileMenuHandler(wx.Frame):
    
    def __init__(self, identifier, menuItemLabelText):
        wx.Frame.__init__(self, None)
        self.identifier = identifier
        self.menuItemLabelText = menuItemLabelText
    
    # # Create appropriate dialog for processing data or loading file 
    def createDialog(self):    
        if self.identifier == MenuConstants.file:
            self.createFileOpenDialog()
        elif self.identifier == MenuConstants.processData:
            self.createFileProcessDialog()
    
    # # Create appropriate file selection dialog        
    def createFileOpenDialog(self):

        fileDialog = wx.FileDialog(self, message="Choose a File", defaultDir=os.getcwd(), style=wx.OPEN)
        if fileDialog.ShowModal() == wx.ID_OK:
            fileName = fileDialog.GetPath()
            f = open(Constants.dataFilePath, 'w')
            f.write(fileName)
        fileDialog.Destroy()
        
    def createFileProcessDialog(self):
        if not os.path.exists(Constants.dataFilePath):
            self.createFileOpenDialog() 
        dataFrame = self.readFile()
        
        if self.menuItemLabelText == MenuConstants.dropColumns:
            processedDataFrame = self.createListBox(dataFrame, 'multi')
            self.readDataFrameToProcess(processedDataFrame)
            
        elif self.menuItemLabelText == MenuConstants.identifyLabelColumns:
            processedDataFrame = self.createListBox(dataFrame, 'single')
            self.writeLabelandId(processedDataFrame, Constants.trainLabel)
            
        elif self.menuItemLabelText == MenuConstants.identifyTestIdColumn:
            processedDataFrame = self.createListBox(dataFrame, 'single')
            self.writeLabelandId(processedDataFrame, Constants.testId)

       
        
    
    def writeLabelandId(self, dataFrame, dataLabel):
        fileName = self.getFileName()
        dlg = wx.TextEntryDialog(self, "Please give a fileName", fileName)
        dlg.ShowModal()
        textBoxValue = dlg.GetValue()
        if dataLabel == Constants.trainLabel:
            self.writeProcessedDataFrame(dataFrame, Constants.trainLabelFileDir, textBoxValue)
        elif dataLabel == Constants.testId:
            self.writeProcessedDataFrame(dataFrame, Constants.testDataIdDir, textBoxValue)
        
    def createFileNameInputDialog(self, fileName):
        
        dlg = MyTextInpuDialog(self, "Please give a fileName", fileName)
        if dlg.ShowModal() == wx.ID_OK:
            
            textBoxValue = dlg.textDlg.GetValue()
            if dlg.chkBox1.GetValue():
                result = textBoxValue 
            elif dlg.chkBox2.GetValue():
                result = textBoxValue 
            
        elif dlg.ShowModal() == wx.ID_CANCEL:
            result = "Cancelled"
        dlg.Destroy()
        return result
    
    def getFileName(self):
        with open(Constants.dataFilePath, 'r')as f:
            content = f.readline().split('/')
            fileName = content[len(content) - 1].split('.')[0]
        return fileName
    
    def readDataFrameToProcess(self, processedDataFrame):
        fileName = self.getFileName()
        result = self.createFileNameInputDialog(fileName)
        if result == "":
            wx.MessageBox("Please enter a file name to save file")
        elif not result == "Cancelled":
            content = result.split('_')
            if content[1] == 'train':
                self.writeProcessedDataFrame(processedDataFrame, Constants.trainDataFileDir, result)
            elif content[1] == 'test':
                self.writeProcessedDataFrame(processedDataFrame, Constants.testDataFiileDir, result)
                        
    # # Write the processed data frame 
    def writeProcessedDataFrame(self, dataFrame, dirName, fileName):
        print " filename to be written is ", fileName
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            
        if dirName == Constants.trainDataFileDir or dirName == Constants.testDataFiileDir:
            dataFrame.to_csv(dirName + fileName)
            print "fileWritten at", dirName + fileName
        
        else:
            filePath = dirName + fileName+'.csv'
            with open(filePath, 'wb') as csvfile:
            
                fileWriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fileWriter.writerow(['Id'])

                count = 0
                for label in dataFrame:
                    fileWriter.writerow([label])
                    count+=1
#             for ids, label in zip(test_id, pred_df):
#                 spamwriter.writerow([ids, label])

                print "fileWritten at", dirName + fileName
                print "rows written", count
    # # read File into dataFrame 

    def readFile(self):
        with open(Constants.dataFilePath, 'r')as f:
            fileName = f.readline()
            
        print " the fileName to be processed is ", fileName
        
        if fileName is None or fileName == "":
            self.showMessageDialog(Constants.fileSelectionMessage) 
            self.createFileOpenDialog()
            with open(Constants.dataFilePath, 'r')as f:
                fileName = f.readline() 
        
        content = fileName.split('.')
        
        if content[1] == 'csv':
            dataFrame = pd.read_csv(fileName)
        elif content[1] == 'xlsx':
            dataFrame = pd.read_excel(fileName)
        return dataFrame
        
    def showMessageDialog(self, displayMessage):
        dlg = wx.MessageDialog(self, message=displayMessage)
        dlg.ShowModal()
        dlg.Destroy()
    
    # # create List Box for dropping columns 
    def createListBox(self, dataFrame, kindofBox):
        print " total no of columns are", len(dataFrame.columns)
        columnList = dataFrame.columns.values
#         isLabel = False
        if kindofBox == 'multi':
            listBox = wx.MultiChoiceDialog(self, message='List of Columns', caption='Select Columns to Drop',
                                      choices=columnList)
            listBox.ShowModal()
            selectedIndexes = listBox.GetSelections()
            print " total columns selected are", len(selectedIndexes)
            selectedItems = [columnList[index] for index in selectedIndexes]
        
            print "selected items are", selectedItems
            dataFrame = dataFrame.drop(selectedItems, axis=1)
            
        elif kindofBox == 'single':
            listBox = wx.SingleChoiceDialog(self, message='List of Columns', caption='Select Label Column',
                                      choices=columnList)
            listBox.ShowModal()
            selectedItem = columnList[listBox.GetSelection()] 
        
            print "selected items are", selectedItem
            dataFrame = dataFrame[selectedItem]
            print len(dataFrame)
#             print "columns in label training dataFrame", len(dataFrame.columns)
        
            
        return dataFrame