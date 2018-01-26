class curentarr():
    def __init__(self):
        self.count = {u"\xd71": "Делеция", u"\xd72": "Дупликация", u"\xd73": "Дупликация",
                      u"\xd71~2": 'Мозаичная делеция',
                      u"\xd72~3": "Мозаичная дупликация",
                      u"\xd70~1": "Мозаичная делеция", u"\xd74": "Трипликация",
                      u"\xd72hmz": "Частичная потеря гетерозиготности"}
        self.SmallCount = {u"\xd71": "делеция", u"\xd72": "дупликация", u"\xd73": "дупликация",
                           u"\xd71~2": 'мозаичная делеция',
                           u"\xd72~3": "мозаичная дупликация",
                           u"\xd70~1": "мозаичная делеция", u"\xd74": "трипликация",
                           u"\xd72hmz": "частичная потеря гетерозиготности"}
        self.kegg = ''
        self.size = ''
        self.chrom = ''
        self.genes = ''
        self.deas = ''
        self.rares = ''
        self.ansarr = ''

    def initarr(self):
        self.ansarr = "{} {} {} {}".format(str(self.count[arr.counts]), str(arr.chromos), BO.ranSize,
                                           self.SmallCount[arr.counts])
