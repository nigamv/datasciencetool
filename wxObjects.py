'''
Created on Jan 11, 2016

@author: vibhor
'''
import wx

class wxObjects:
    
    def getMenu(self):
        return wx.Menu()
    
    def getMenuBar(self):
        return wx.MenuBar()
    
    ## On ubuntu menuItem can not be created without specifying menu.
    def getMenuItem(self):
        return wx.MenuItem()
        