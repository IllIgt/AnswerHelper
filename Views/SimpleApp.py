import tkinter;


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = tk.Frame(self, width=600, height=50)
        self.entry = tk.Text(self, width=60, font="10")
        self.button6 = tk.Button(self.frame, text="Get Exons", command=BO.SingleOptionExonsCount)
        self.button5 = tk.Button(self.frame, text="Save File", command=Controller().save_file)
        self.button = tk.Button(self.frame, text="Get KEGG", command=BO.SingleOptionKEGGgetter)
        self.button7 = tk.Button(self.frame, text="Get OMIM", command=BO.SingleOptionOMIMgetter)
        self.button2 = tk.Button(self, text="Clear right field ", command=Controller().Clear_button_right)
        self.button3 = tk.Button(self, text="Clear left field ", command=Controller().Clear_button_left)
        self.button4 = tk.Button(self.frame, text="Get Size", command=BO.SingleOptionArrSize)
        self.entry2 = tk.Text(self, width=60, font="12")
        self.button10 = tk.Button(self, text="Get new arrangement", command=BO.GetNewWindow)

        self.button10.pack(side='top', fill='x')
        self.frame.pack(side='top')
        self.button.pack(side='left')
        self.button7.pack(side='left')
        self.button4.pack(side='left')
        self.button6.pack(side='left')
        self.button5.pack(side='left')
        self.button2.pack(side='right', fill='both')
        self.button3.pack(side='left', fill='both')
        self.entry.pack(side='left', fill='x')
        self.entry2.pack(side='right', fill='x')
