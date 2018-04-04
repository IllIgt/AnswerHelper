class ExonRaw:
    def __init__(self, exons=""):
        self.exons = exons
        self.endings = {1: "ый", 2: "ь", 3: "ой", 4: "ого", 5: "ий", 6: "ьего", 7: "овой", 8: "о"}

    #return sorted array of splitted exons
    @staticmethod
    def sort_exons(exons):
        if exons.find(',') != -1:
            exons = exons.split(",")
            n = len(exons)
            m = n-1
            while m>0:
                for i in range(m):
                    fir = exons[i].split('-')
                    fir2 = exons[i+1].split('-')
                    if int(fir[0]) > int(fir2[0]):
                        x = exons[i]
                        exons[i] = exons[i+1]
                        exons[i+1] = x
                m = m-1
        return exons
