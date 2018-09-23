'''
Created on Jan 8, 2016

@author: vibhor
'''
#!/usr/bin/env python
import wx
import os
import pandas as pd
# import wx.lib.agw.buttonpanel as BP

from Constants import Constants, MenuConstants
from ManipulateMenubar import ManipulateMenubar
from ManipulateMenubar import Menu
from Tree import MyTree
from TextCtrl import MyTextCtrl
from ProcessingScripts import ProcessingScripts
from ExploratoryCharts import Exploratory

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.FULLSCREEN_ALL, title=title)
        panel1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel3 = wx.Panel(self, -1, style=wx.RAISED_BORDER)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.createMenu()
        self.createPanel1(panel1)
        self.createPanel2(panel2)
        self.createPanel3(panel3)
        # # Setting up a TextCntrl in panel3

        sizer.Add(panel1, 1, wx.EXPAND | wx.ALL, 3)
        sizer.Add(panel2, 1, wx.EXPAND | wx.ALL, 3)
        sizer.Add(panel3, 1, wx.EXPAND | wx.ALL, 3)

        self.SetSizer(sizer)
        self.selectedAlgorithm = ""

    def createMenu(self):
        item_list = [MenuConstants.loadTrainDataFile, MenuConstants.loadTestDataFile]
        filemenu = Menu(MenuConstants.file)
        filemenu.setItemList(item_list)

        item_list = [MenuConstants.dropColumns, MenuConstants.fillNA, MenuConstants.identifyLabelColumns,
        MenuConstants.identifyTestIdColumn]

        tempmenu = Menu(MenuConstants.processData)
        tempmenu.setItemList(item_list)

        menu_list = [filemenu, tempmenu]
        menuBar = ManipulateMenubar().createMenuBar(menu_list)
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.SetTitle("Still to decide")

    def createPanel1(self, panel):
        # # Seeting up a tree in panel 1
        self.tree = MyTree(panel)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.onTreeLeftClick, id=wx.ID_ANY)
        treeTitle = wx.StaticText(panel, label="Choose an Algorithm")
        treeSizer = wx.BoxSizer(wx.VERTICAL)
        treeSizer.Add(treeTitle)
        treeSizer.Add(self.tree, 1, wx.EXPAND)
        panel.SetSizer(treeSizer)

    def createPanel2(self, panel):

        boxPanel = wx.Panel(panel, -1)
        boxPanelSizer = wx.BoxSizer(wx.HORIZONTAL)

        trainBoxPanel = wx.Panel(boxPanel, -1)
        trainBoxPanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.listBox1 = self.createListbox(Constants.trainDataFileDir, trainBoxPanel)
        listBox1Title = wx.StaticText(trainBoxPanel, label="Select Training Data Set")
        self.listBox2 = self.createListbox(Constants.trainLabelFileDir, trainBoxPanel)
        listBox2Title = wx.StaticText(trainBoxPanel, label="Select Training Label File")
        trainBoxPanelSizer.Add(listBox1Title)
        trainBoxPanelSizer.Add(self.listBox1, 1, wx.EXPAND | wx.ALL, 2)
        trainBoxPanelSizer.Add(listBox2Title)
        trainBoxPanelSizer.Add(self.listBox2, 1, wx.EXPAND | wx.ALL, 2)
        trainBoxPanel.SetSizer(trainBoxPanelSizer)

        testBoxPanel = wx.Panel(boxPanel, -1)
        testBoxPanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.listBox3 = self.createListbox(Constants.testDataFiileDir, testBoxPanel)
        listBox3Title = wx.StaticText(testBoxPanel, label="Select Test Data Set")
        self.listBox4 = self.createListbox(Constants.testDataIdDir, testBoxPanel)
        listBox4Title = wx.StaticText(testBoxPanel, label="Select Test Id")
        testBoxPanelSizer.Add(listBox3Title)
        testBoxPanelSizer.Add(self.listBox3, 1, wx.EXPAND | wx.ALL, 2)
        testBoxPanelSizer.Add(listBox4Title)
        testBoxPanelSizer.Add(self.listBox4, 1, wx.EXPAND | wx.ALL, 2)
        testBoxPanel.SetSizer(testBoxPanelSizer)

        boxPanelSizer.Add(trainBoxPanel, 1, wx.EXPAND | wx.ALL, 2)
        boxPanelSizer.Add(testBoxPanel, 1, wx.EXPAND | wx.ALL, 2)
        boxPanel.SetSizer(boxPanelSizer)

        buttonPanel = wx.Panel(panel, -1)
        buttonPanelSizer = wx.BoxSizer(wx.HORIZONTAL)
        runButton = wx.Button(buttonPanel, 1 , 'Run', size=(90, 30))
        self.Bind(wx.EVT_BUTTON, self.OnRunButton, id=1)
        refreshButton = wx.Button(buttonPanel, 2 , 'Refresh', size=(90, 30))
        self.Bind(wx.EVT_BUTTON, self.OnRefreshButton, id=2)
        buttonPanelSizer.Add(refreshButton, 1, wx.EXPAND | wx.ALL, 2)
        buttonPanelSizer.Add(runButton, 1, wx.EXPAND | wx.ALL, 2)
        buttonPanel.SetSizer(buttonPanelSizer)

        self.text_ctrl2 = MyTextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        panel2Sizer = wx.BoxSizer(wx.VERTICAL)
        panel2Sizer.Add(boxPanel, 10, wx.EXPAND | wx.ALL, 3)
        panel2Sizer.Add(buttonPanel, 1, wx.EXPAND | wx.ALL, 3)
        panel2Sizer.Add(self.text_ctrl2, 3, wx.EXPAND | wx.ALL, 3)
        panel.SetSizer(panel2Sizer)

    def createPanel3(self, panel):
        self.text_ctrl3 = MyTextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        text_ctrl3Label = wx.StaticText(panel, label="Algorithm Description")
        textCtrlSizer3 = wx.BoxSizer(wx.VERTICAL)
        textCtrlSizer3.Add(text_ctrl3Label)
        textCtrlSizer3.Add(self.text_ctrl3, 1, wx.EXPAND)
        panel.SetSizer(textCtrlSizer3)

    # # static function for creating ListBox
    def createListbox(self, dirName, panel):
        choiceList = [fileName for fileName in os.listdir(dirName)]
        return wx.ListBox(panel, -1, choices=choiceList, style=wx.LB_SINGLE | wx.LB_HSCROLL)

    def onTreeLeftClick(self, event):
        self.selectedAlgorithm = self.tree.GetItemText(event.GetItem())
        print "reached", self.selectedAlgorithm
        keys = Constants.algo_const_mapping.keys()
        if self.selectedAlgorithm in keys:
            print Constants.algo_const_mapping[self.selectedAlgorithm]
        self.text_ctrl3.SetValue(Constants.algo_description['Algorithm'])


    def onMenuClick(self, event):
        menuItems = event.GetMenuItems()
        print menuItems[0].GetItemLabelText()



    def OnRunButton(self, event):

        if self.selectedAlgorithm == "":
            wx.MessageBox("Please select an Algorithm")
            return

        elif self.listBox1.GetSelection() == -1:
            wx.MessageBox("Please select a training set")
            return

        elif self.listBox2.GetSelection() == -1:
            wx.MessageBox("Please select a testing set")
            return

        elif self.listBox3.GetSelection() == -1:
            wx.MessageBox("Please select a training label")
            return

        elif self.listBox4.GetSelection() == -1:
            wx.MessageBox("Please select a training label")
            return

        print "Primary conditions checked"

        if self.selectedAlgorithm in Constants.chartList:
            print " Reached charts condition"
            self.createCharts()
        else:
            trainingFileName = self.listBox1.GetStrings() [self.listBox1.GetSelection()]
            print "training data set is ", trainingFileName
            labelFileName = self.listBox2.GetStrings()[self.listBox2.GetSelection()]
            print "training label set is ", labelFileName
            testingFileName = self.listBox3.GetStrings()[self.listBox3.GetSelection()]
            print "testing data set is ", testingFileName
            testIdFileName = self.listBox4.GetStrings()[self.listBox4.GetSelection()]
            print "testing label set is ", testIdFileName



            train_df = pd.read_csv(Constants.trainDataFileDir + trainingFileName)
            print "length of training data frame is ", len(train_df)
            train_df = train_df.fillna(-1)
            train_label = pd.read_csv(Constants.trainLabelFileDir + labelFileName)
            print "legth of label is", len(train_label)
            test_df = pd.read_csv(Constants.testDataFiileDir + testingFileName)
            print "length of test data frame is ", len(test_df)
            test_df = test_df.fillna(-1)
            test_id = pd.read_csv(Constants.testDataIdDir + testIdFileName)
            print "length of test id's are", len(test_id)
            model_sequence = [Constants.algo_const_mapping[self.selectedAlgorithm]]

            scripts = ProcessingScripts(trainingFileName)
            scripts.primary_evaluation_script(train_df, train_label, test_df, model_sequence, test_id)

    def createCharts(self):
        print "Reached create charts function"
        trainingFileName = self.listBox1.GetStrings() [self.listBox1.GetSelection()]
        train_df = pd.read_csv(Constants.trainDataFileDir + trainingFileName)
        print "length of training data frame is ", len(train_df)
        train_df = train_df.fillna(-1)

        base_dir = "ExploratoryCharts/"
        charts = Exploratory()
        print Constants.charts_const_mapping[self.selectedAlgorithm]
        charts.generatePlot(train_df, base_dir, Constants.charts_const_mapping[self.selectedAlgorithm])
        print "Chart Generated"


    def OnRefreshButton(self, event):
        self.trainingList = [fileName for fileName in os.listdir(Constants.trainDataFileDir)]
        self.listBox1.Set(self.trainingList)

        self.trainLabelList = [fileName for fileName in os.listdir(Constants.trainLabelFileDir)]
        self.listBox2.Set(self.trainLabelList)

        self.testingList = [fileName for fileName in os.listdir(Constants.testDataFiileDir)]
        self.listBox3.Set(self.testingList)

        self.testIdList = [fileName for fileName in os.listdir(Constants.testDataIdDir)]
        self.listBox4.Set(self.testIdList)

        pass

#         print "testing data set is ". self.listBox2.GetSelection()

app = wx.App(False)
frame = MainWindow(None, "")
frame.Show()
frame.Maximize(True)
app.MainLoop()
