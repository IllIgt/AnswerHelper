class arrangements():
    def __init__(self):
        self.allsize = ''
        self.chromos = ''
        self.counts = ''
        self.fullarr = ""

    def get_full(self):
        self.fullarr += "{}{}{},".format(str(self.chromos), ctrl.OutFinal, self.allsize + self.counts)
