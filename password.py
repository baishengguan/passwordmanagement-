# User and Password management software

import xlrd
import wx
import wx.grid
import re
import os

# auto read file path
path = os.getcwd()
list = os.listdir()

if 'password.xlsx' in list:
    path = path + '\\password.xlsx'
    data = xlrd.open_workbook(path)

# data = xlrd.open_workbook('E:\\password.xlsx')

table = data.sheets()[0]
list = table.col_values(0)
rows = table.nrows  # calculate rows

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "password")
        self.panel = wx.Panel(self)
        # add icon
        self.icon = wx.Icon("favicon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # create the controls
        time = wx.StaticText(self.panel, -1, "2018.1.24 [guanbaisheng]", (100, 10), (160, -1), wx.ALIGN_CENTER)

        title = wx.StaticText(self.panel, -1, "密码管理")
        title.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD))

        # self.inputText = wx.TextCtrl(panel, -1, "input search", size=(150, -1), style= wx.TE_PROCESS_ENTER)
        self.inputText = wx.TextCtrl(self.panel, -1, "input search", size=(150, -1))
        searchBtn = wx.Button(self.panel, -1, "search all")

        # self.show = wx.TextCtrl(panel, -1, "show text", size=(600, 400), style= wx.TE_MULTILINE)
        # self.show = wx.TextCtrl(panel, -1, size=(600, 400), style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.grid = wx.grid.Grid(self.panel)
        self.grid.CreateGrid(15, 4)
        self.grid.SetColLabelValue(0, "website")
        self.grid.SetColLabelValue(1, "user")
        self.grid.SetColLabelValue(2, "password")
        self.grid.SetColLabelValue(3, "else")
        self.grid.SetColSize(0, 130)
        self.grid.SetColSize(1, 210)
        self.grid.SetColSize(2, 135)
        self.grid.SetColSize(3, 150)

    # do the layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title, 0, wx.ALL|wx.ALIGN_CENTER, 5)
        mainSizer.Add(wx.StaticLine(self.panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 0)

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer.Add(time, 0, wx.LEFT, 50)
        boxSizer.Add(self.inputText, 0, wx.LEFT|wx.RIGHT, 100)
        boxSizer.Add(searchBtn, 0, wx.RIGHT, 50)
        addrSizer.Add(boxSizer, 0, wx.ALIGN_CENTER)

        addrSizer.Add((10, 10))  # some empty space
        # addrSizer.Add(self.show, 0, wx.EXPAND)
        addrSizer.Add(self.grid, 0, wx.EXPAND)

        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)

        self.panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

    # event process
        self.Bind(wx.EVT_BUTTON, self.OnButton, searchBtn)  # searchBtn event
        # self.Bind(wx.EVT_TEXT_ENTER, self.onText, self.inputText)   # text event
        self.Bind(wx.EVT_TEXT, self.onText, self.inputText)  # text event

    def OnButton(self, event): # searchBtn event
        self.readEXCELAll()

    def onText(self, event): # text event
        text = self.inputText.GetValue()
        # print(text)
        self.choose(text)

    # read all
    def readEXCELAll(self):
        # self.show.Clear()
        self.grid.ClearGrid()
        self.grid.AppendRows(rows-15, 4)
        for i in range(rows):
            text = table.row_values(i)
            # # print(text)
            # self.show.write(text[0] + "    " + text[1] + "    " + text[2] + "    " + text[3] + "\n")
            self.grid.SetCellValue(i, 0, text[0])
            self.grid.SetCellValue(i, 1, text[1])
            self.grid.SetCellValue(i, 2, text[2])
            self.grid.SetCellValue(i, 3, text[3])

    # read one line for your choose
    def readEXCELOne(self, index, j):
        if (index in list):
            number = list.index(index)
            text = table.row_values(number)
            # print(text)
            # print(text[0] + " " + text[1] + " " + text[2] + " " + text[3])
            # self.show.write(text[0] + "    " + text[1] + "    " + text[2] + "    " + text[3]+ "\n")
            self.grid.SetCellValue(j, 0, text[0])
            self.grid.SetCellValue(j, 1, text[1])
            self.grid.SetCellValue(j, 2, text[2])
            self.grid.SetCellValue(j, 3, text[3])


    # choose filter
    def choose(self, text):
        # self.show.Clear()
        self.grid.ClearGrid()
        j = 0
        if(text != '' and text != ' '):
            for i in range(len(list)):
                searchObj = re.search(text, list[i], re.M | re.I)
                # print(searchObj)
                if searchObj:
                    # print("searchObj.group() : ", searchObj.group())
                    self.readEXCELOne(list[i], j)
                    j = j+1
                    if(j >= 10):
                        self.grid.AppendRows(10, 4)
                # else:
                #     print("Nothing found!!")


if __name__ == '__main__':
    app = wx.App()
    frame = TestFrame()
    frame.Show(True)
    app.MainLoop()