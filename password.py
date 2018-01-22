# User and Password Management software

import xlrd
import wx

data = xlrd.open_workbook('E:\\mima.xlsx')

table = data.sheets()[0]  # 通过索引顺序获取
list = table.col_values(0)

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "password")
        panel = wx.Panel(self)

    # create the controls
        title = wx.StaticText(panel, -1, "密码管理[baisheng]")
        title.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.inputText = wx.TextCtrl(panel, -1, "input search", size=(150, -1), style=wx.TE_PROCESS_ENTER)
        searchBtn = wx.Button(panel, -1, "search all")

        self.show = wx.TextCtrl(panel, -1, "show text", size=(600, 400), style= wx.TE_MULTILINE)

    # do the layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title, 0, wx.ALL|wx.ALIGN_CENTER, 5)
        mainSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 0)

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer.Add(self.inputText, 0, wx.RIGHT|wx.LEFT,50)
        boxSizer.Add(searchBtn, 0, wx.RIGHT|wx.LEFT, 50)
        addrSizer.Add(boxSizer, 0, wx.ALIGN_CENTER)

        addrSizer.Add((10, 10))  # some empty space
        addrSizer.Add(self.show, 0, wx.EXPAND)

        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)

        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    # event process
        self.Bind(wx.EVT_BUTTON, self.OnButton, searchBtn)  # searchBtn event
        self.Bind(wx.EVT_TEXT_ENTER, self.onText, self.inputText)   # text event

    def OnButton(self, event): # searchBtn event
        self.readEXCELAll()

    def onText(self, event): # text event
        text = self.inputText.GetValue()
        self.readEXCELOne(text)

    # read all
    def readEXCELAll(self):
        rows = table.nrows  # calculate rows
        self.show.Clear()
        for i in range(rows):
            text = table.row_values(i)
            # print(text)
            self.show.write(text[0] + "    " + text[1] + "    " + text[2] + "    " + text[3] + "\n")

    # read one line for your choose
    def readEXCELOne(self, index):
        if (index in list):
            number = list.index(index)
            text = table.row_values(number)
            # print(text)
            # print(text[0] + " " + text[1] + " " + text[2] + " " + text[3])
            self.show.Clear()
            self.show.write(text[0] + "    " + text[1] + "    " + text[2] + "    " + text[3])


if __name__ == '__main__':
    app = wx.App()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()


# class StaticTextFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None, -1, 'Password', size=(400, 300))
#         panel = wx.Panel(self, -1)
#
#     # 这是一个基本的静态文本、居中对齐，指定前景色和背景色
#         str = "密码管理软件"
#         text = wx.StaticText(panel, -1, str, (100, 10), (160, -1), wx.ALIGN_CENTER)
#         text.SetForegroundColour('white')
#         text.SetBackgroundColour('black')
#         font = wx.Font(16, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
#         text.SetFont(font)
#
#     # 输入查询文本
#         basicLabel = wx.StaticText(panel, -1,  "Input What")
#         inputText = wx.TextCtrl(panel, -1, "please your website!", size=(175, -1))
#         inputText.SetInsertionPoint(0)
#
#         sizer = wx.FlexGridSizer(cols=4, hgap=6, vgap=6)
#         sizer.AddMany([basicLabel, inputText])
#         panel.SetSizer(sizer)


# import xlrd
#
# data = xlrd.open_workbook('E:\\test.xlsx')
#
# table = data.sheets()[0]   # 通过索引顺序获取
# print(table.row_values(0))
# list = table.col_values(0)
# print(list)
#
# # read all
# rows = table.nrows  # 获取行数
# for i in range(rows):
#     print(table.row_values(i))
#
# # read one line for your choose
# index = '工行'
# if(index in list):
#     xuhao = list.index(index)
#     print(xuhao)
#     print(table.row_values(xuhao))