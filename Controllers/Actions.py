class ButtonOptions():
    def __init__(self):
        self.NewWindow = object
        self.text = ''
        self.conclusion = ''
        self.ranSize = ''

    def SingleOptionExonsCount(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion = ctrl.exonsCount(self.text)
        app.entry2.insert(1.0, self.conclusion)

    def SingleOptionArrSize(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion = ctrl.arrSize(self.text)
        app.entry2.insert(1.0, self.conclusion)

    def SingleOptionKEGGgetter(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion = ctrl.KEGGgetter(self.text)
        app.entry2.insert(1.0, self.conclusion)

    def SingleOptionOMIMgetter(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion = ctrl.OMIMgetter(self.text)
        app.entry2.insert(1.0, self.conclusion)

    def GetNewWindow(self):
        arr.fullarr = ''
        self.NW = NewWindow()
        self.NW.mainloop()

    def GetFinalArrays(self):
        app.entry2.delete('1.0', 'end-1c')
        app.entry2.insert(1.0, arr.fullarr)

    def choose_array(self):
        app.entry.delete('1.0', 'end-1c')
        app.entry2.delete('1.0', 'end-1c')
        moment = self.NW.entry.get("1.0", "end-1c")
        arr.chromos = self.NW.entry2.get('1.0', "end-1c")
        self.ranSize = ctrl.arrSize(moment)
        app.entry.delete('1.0', 'end-1c')
        arr.counts = self.NW.var.get()
        qarr.initarr()
        arr.get_full()
        app.entry2.insert(1.0, qarr.ansarr)
