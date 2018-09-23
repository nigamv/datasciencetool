'''
Created on Feb 10, 2016

@author: vibhor
'''
import wx
from Constants import Constants

from TextCtrl import MyTextCtrl

## This tree class is used to generate a tree from the data stored in a tree data structure. For sample data structure please refer 
## to Constants.algo_Map
class MyTree(wx.TreeCtrl):
    
    def __init__(self, parent):
        
        wx.TreeCtrl.__init__(self, parent)
        self.TextCtrlValue = ""
        self.createTree()
    
    def createTree(self):
        root = self.AddRoot('Functions')
        algo_dict = Constants.algo_map
        self.addItemsFromDict(algo_dict, root)
#         self.Bind(wx.EVT_TREE_SEL_CHANGED, self.onLeftClick, id= wx.ID_ANY)
        
    ## The function adds data stored in dictionary type to the tree
    def addItemsFromDict(self,curr_dict,parent):
        for key,values in curr_dict.iteritems():
            child = self.AppendItem(parent,key)
            self.addItemsFromList(values, child)
    
    ## The function adds data stored in a list to the tree
    def addItemsFromList(self,child_list,parent):
        while (child_list):
            child = child_list[0]
            
            if type(child) is dict:
                self.addItemsFromDict(child, parent)
            else:    
                self.AppendItem(parent,child)
                
            child_list.remove(child)  

#     def onLeftClick(self,event):
#         print "reached", self.GetItemText(event.GetItem())
# #         MyTextCtrl.displayContent(self.GetItemText(event.GetItem()))
