'''
Created on Feb 14, 2016

@author: vibhor
'''
import wx 

class MyTextInpuDialog(wx.Dialog):
    
    def __init__(self,parent,message,fileName):
        wx.Dialog.__init__(self,parent,-1,message, size = (200,200))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.textDlg= wx.TextCtrl(self)
        
        self.chkBox1 = wx.RadioButton(self,-1,"Train")
        self.chkBox2 = wx.RadioButton(self,-1,"Test")
#         self.chkbox3 = wx.RadioButton(self,-1,"TrainLabel")
        chkBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        chkBoxSizer.Add(self.chkBox1)
        chkBoxSizer.Add(self.chkBox2)
#         chkBoxSizer.Add(self.chkbox3)
        
        btns = self.CreateSeparatedButtonSizer(wx.OK | wx.CANCEL)
        
        sizer.Add(self.textDlg)
        sizer.Add(chkBoxSizer)
        sizer.Add(btns)
        self.SetSizer(sizer)
        