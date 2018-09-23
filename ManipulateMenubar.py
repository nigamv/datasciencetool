'''
Created on Jan 11, 2016

@author: vibhor
'''

import wx
from wxObjects import wxObjects
from functools import partial
from FileMenuHandler import FileMenuHandler

class ManipulateMenubar:
    
    ## The method adds different menus to MenuBar        
    def addMenusToMenuBar(self,menu_list,menubar):
        for menu in menu_list:
            menu_obj = menu.getMenuObject()
            menubar.Append(menu_obj,menu_obj.GetTitle())
            
        return menubar
    
    ## This method creates a MenuBar for a given frame. 
    def createMenuBar(self,menu_list):
#         menubar = wxObjects().getMenuBar()
        menubar = wx.MenuBar()
        return self.addMenusToMenuBar(menu_list, menubar)


class Menu(wx.Menu):
    
    def __init__(self, title):
        self.wxObject = wxObjects()
        self.menu_ = self.wxObject.getMenu()
        self.menu_.SetTitle(title)
        
    def getMenuObject(self):
        return self.menu_
    
    def setItemList(self, item_list):
        count = 0
        for item in item_list:
            menuItem = wx.MenuItem(self.menu_,count+1,u"Test") 
            menuItem.SetItemLabel(item)
            self.menu_.AppendItem(menuItem)
            self.menu_.Bind(wx.EVT_MENU, partial (self.onClick, count), menuItem)
            count = count+1
#             self.menu_.Append(wx.ID_ANY, item)

    def onClick(self,number,event):
        menuItems = self.menu_.GetMenuItems()
        print menuItems[number].GetItemLabelText()
        handler = FileMenuHandler(self.menu_.GetTitle(),menuItems[number].GetItemLabelText())
        handler.createDialog()