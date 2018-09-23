'''
Created on Feb 11, 2016

@author: vibhor
'''
# import wx 
from wx.stc import StyledTextCtrl,STC_WRAP_WORD

class MyTextCtrl(StyledTextCtrl):
    
    def __init__(self,parent,style):
        
        StyledTextCtrl.__init__(self,parent,style)
        self.SetWrapMode(STC_WRAP_WORD)
    
    