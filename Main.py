import tkinter as tk
import re
import tkinter.filedialog as filedialog
from docxtpl import DocxTemplate
from ExonRaw import ExonRaw as er


slovar_KEGG = {1:'одну геномную сеть',2:'две геномные сети',3:'три геномные сети',4:'четыре геномные сети',
               5:'пять геномных сетей',6:'шесть геномных сетей',7:'семь геномных сетей',8:'восемь геномных сетей',
               9:'девять геномных сетей',10:'десять геномных сетей',11:'одиннадцать геномных сетей',
               12:'двенадцать геномных сетей',13:'тринадцать геномных сетей',14:'четырнадцать геномных сетей',
               15:'пятнадцать геномных сетей',16:'шестнадцать геномных сетей',17:'семнадцать геномных сетей',
               18:'восемнадцать геномных сетей',19:'девятнадцать геномных сетей',20:'двадцать геномных сетей'}


decfirst = {0:'',1:"перв", 2:"втор", 3:"трет", 4:"четверт", 5:"пят", 6:"шест", 7:"седьм", 8:"восьм", 9:"девят"}
decsecond = {10:"десят", 11:"одиннадцат", 12:"двенадцат", 13:"тринадцат", 14:"четырнадцат", 15:"пятнадцат",
             16:"шестнадцат", 17:"семнадцат", 18:"восемнадцат", 19:"девятнадцат"}
decthird = {1:"десят",2:"двадцат", 3:"тридцат", 4:"сорок", 5:"пятьдесят", 6:"шестьдесят", 7:"семьдесят",
            8:"восемьдесят", 9:"девяност"}
decthird2 = {4:"сороков", 5:"пятидесят", 6:"шестидесят", 7:"семидесят", 8:"восьмидесят"}
endings = {1:"ый",2:"ь",3:"ой",4:"ого",5:"ий",6:"ьего",7:"овой",8:"о"}
#Vidget
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = tk.Frame(self, width = 600, height = 50)
        self.entry = tk.Text(self,width=60,font="10")
        self.button6 = tk.Button(self.frame, text="Get Exons", command=BO.SingleOptionExonsCount)
        self.button5 = tk.Button(self.frame, text="Save File", command=Controller().save_file)
        self.button8 = tk.Button(self.frame, text="Save As Answer", command=Controller().save_file_answer)
        self.button = tk.Button(self.frame, text="Get KEGG", command=BO.SingleOptionKEGGgetter)
        self.button7 = tk.Button(self.frame, text="Get OMIM", command=BO.SingleOptionOMIMgetter)
        self.button2 = tk.Button(self, text="Clear right field ", command=Controller().Clear_button_right)
        self.button3 = tk.Button(self, text="Clear left field ", command=Controller().Clear_button_left)
        self.button4 = tk.Button(self.frame, text="Get Size", command=BO.SingleOptionArrSize)
        self.entry2 = tk.Text(self,width=60,font="12")
        self.button10 = tk.Button(self, text="Get new arrangement", command= BO.GetNewWindow)

        self.button10.pack(side='top', fill = 'x')
        self.frame.pack(side ='top')
        self.button.pack(side='left')
        #self.button7.pack(side='left')
        self.button4.pack(side='left')
        self.button6.pack(side='left')
        self.button5.pack(side='left')
        self.button8.pack(side='left')
        self.button2.pack(side='right',fill = 'both')
        self.button3.pack(side='left',fill = 'both')
        self.entry.pack(side='left',fill = 'x')
        self.entry2.pack(side='right',fill = 'x')

class NewWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.var=tk.StringVar(self)
        self.var.set("CN")
        self.buttonComplete = tk.Button (self,text = "Complete", command = BO.GetFinalArrays)
        self.frame=tk.Frame(self,width=450,height=23)
        self.entry2 = tk.Text(self.frame,width = 10)
        self.entry = tk.Text(self.frame,width = 30)
        self.button2 = tk.Button(self.frame, text="Done", command=BO.choose_array)
        self.button = tk.Button(self.frame, text="add arrangement", command=self.add_arrangement)
        self.w = tk.OptionMenu(self.frame,self.var,"×1","×2",'×3','×1~2','×2~3','×0~1','×4','×2hmz')
        self.buttonComplete.pack(side='top',fill="x")
        self.frame.pack()
        self.frame.pack_propagate(False)
        self.button2.pack(side='right')
        self.button.pack(side='right')
        self.entry2.pack(side='left')
        self.w.pack(side="right")
        self.entry.pack()


    def add_arrangement(self):
        self.var=tk.StringVar(self)
        self.var.set("CN")
        self.frame=tk.Frame(self,width=450,height=23)
        self.entry2 = tk.Text(self.frame,width = 10)
        self.entry = tk.Text(self.frame,width = 30)
        self.button2 = tk.Button(self.frame, text="Done", command=BO.choose_array)
        self.button = tk.Button(self.frame, text="add arrangement", command=self.add_arrangement)
        self.w = tk.OptionMenu(self.frame,self.var,"×1","×2",'×3','×1~2','×2~3','×0~1','×4','×2hmz')
        self.frame.pack()
        self.frame.pack_propagate(False)
        self.button2.pack(side='right')
        self.button.pack(side='right')
        self.entry2.pack(side='left')
        self.w.pack(side="right")
        self.entry.pack()






#Model
class arrangements():
    def __init__(self):
        self.allsize = ''
        self.chromos = ''
        self.counts = ''
        self.fullarr = ""
    def get_full(self):
        self.fullarr += "{}{}{},".format(str(self.chromos), ctrl.OutFinal, self.allsize+self.counts)


class curentarr():
    def __init__(self):
        self.count={u"\xd71":"Делеция",u"\xd72":"Дупликация",u"\xd73":"Дупликация",u"\xd71~2":'Мозаичная делеция',
                    u"\xd72~3":"Мозаичная дупликация",
                    u"\xd70~1":"Мозаичная делеция",u"\xd74":"Трипликация",u"\xd72hmz":"Частичная потеря гетерозиготности"}
        self.SmallCount={u"\xd71":"делеция",u"\xd72":"дупликация",u"\xd73":"дупликация",u"\xd71~2":'мозаичная делеция',
                    u"\xd72~3":"мозаичная дупликация",
                    u"\xd70~1":"мозаичная делеция",u"\xd74":"трипликация",u"\xd72hmz":"частичная потеря гетерозиготности"}
        self.kegg=''
        self.size=''
        self.chrom = ''
        self.genes =''
        self.deas=''
        self.rares=''
        self.ansarr=''
    def initarr(self):
        self.ansarr = "{} {} {} {}".format (str(self.count[arr.counts]), str(arr.chromos), BO.ranSize,
                                             self.SmallCount[arr.counts])

class ButtonOptions():
    def __init__(self):
        self.NW=object
        self.text = ''
        self.conclusion = ''
        self.ranSize = ''
    def SingleOptionExonsCount(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion=ctrl.exonsCount(self.text)
        app.entry2.insert(1.0, self.conclusion)
    def SingleOptionArrSize(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion=ctrl.arrSize(self.text)
        app.entry2.insert(1.0, self.conclusion)
    def SingleOptionKEGGgetter(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion=ctrl.KEGGgetter(self.text)
        app.entry2.insert(1.0, self.conclusion)
    def SingleOptionOMIMgetter(self):
        app.entry2.delete('1.0', 'end-1c')
        self.text = app.entry.get("1.0", "end-1c")
        self.conclusion=ctrl.OMIMgetter(self.text)
        app.entry2.insert(1.0, self.conclusion)

    def GetNewWindow(self):
        arr.fullarr = ''
        self.NW = NewWindow()
        self.NW.mainloop()

    def GetFinalArrays(self):
        app.entry2.delete('1.0', 'end-1c')
        app.entry2.insert(1.0,arr.fullarr)
        self.NW.destroy()

    def choose_array(self):
        app.entry.delete('1.0', 'end-1c')
        app.entry2.delete('1.0', 'end-1c')
        moment = self.NW.entry.get("1.0", "end-1c")
        arr.chromos = self.NW.entry2.get('1.0',"end-1c")
        self.ranSize=ctrl.arrSize(moment)
        app.entry.delete('1.0', 'end-1c')
        arr.counts=self.NW.var.get()
        qarr.initarr()
        arr.get_full()
        app.entry2.insert(1.0,qarr.ansarr)







#Controller
class Controller():
    def __init__(self):
        self.OutFinal = ''



    def exonsCount (self,text):
        global decfirst
        global decsecond
        global decthird
        global decthird2
        global endings
        app.entry2.delete('1.0', 'end-1c')
        ARRS = text
        exoncount = []
        prexon = ''
        sta = er.sort_exons(text)
        for S in sta:
            if S.find('-') != -1:
                s = S.split("-")
                i2 = 0
                for dec in s:
                    inegr =[]
                    if int(dec) < 10:
                        if i2 == 0:
                            if int(dec) != 3:
                                inegr = decfirst[int(dec)]+endings[4]
                            else:
                                inegr = decfirst[int(dec)]+endings[6]
                        else:
                            if int(dec) == 1 or int(dec) == 4 or int(dec) ==5 or int(dec) ==9:
                                inegr = decfirst[int(dec)]+endings[1]
                            elif int(dec) == 2 or int(dec) ==6 or int(dec) ==7 or int(dec) ==8:
                                inegr = decfirst[int(dec)]+endings[3]
                            else:
                                inegr = decfirst[int(dec)]+endings[5]

                    elif int(dec) < 20 and int(dec) > 9:
                        if i2 == 0:
                            inegr = decsecond[int(dec)]+endings[4]
                        else:
                            inegr = decsecond[int(dec)]+endings[1]

                    elif int(dec) >= 20 and int(dec)<100:
                        if i2 == 0:#первый эллемент
                            if int(dec[1]) != 0:#единицы не равны нулю
                                if int(dec[0]) == 2 or int(dec[0]) == 3:#десятки равны 2 или3
                                    if int(dec[1]) != 3: #единица не равна 3
                                        inegr = decthird[int(dec[0])]+endings[2] +" "+decfirst[int(dec[1])]+endings[4]
                                    else:
                                        inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[6]
                                elif int(dec[0]) != 2 and int(dec[0]) != 3 and int(dec[0]) != 9:#десятки не равны 2 или 3 или 9
                                    if int(dec[1]) != 3:#единицы не равны 3
                                        inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[4]
                                    else:
                                        inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[6]
                                else:#методом исключения десятки равны 9
                                    if int(dec[1]) != 3:#единицы не равны 3
                                        inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[4]
                                    else:
                                        inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[6]
                            else:#единицы равны нулю
                                if int(dec[0]) ==4 or int(dec[0]) ==5 or int(dec[0]) ==6 or int(dec[0]) ==7 or int(dec[0]) ==8:#Десятки равны 4.5.6.7.8
                                    inegr = decthird2[int(dec[0])] + endings[4]
                                else:#десятки не равны 4,5,6,7,8
                                    inegr = decthird[int(dec[0])] + endings[4]

                        else:#второй эллимент
                            if int(dec[1]) != 0:#единицы не равны нудю
                                if int(dec[0]) == 2 or int(dec[0]) == 3:#десятки равны 2 или 3
                                    if int(dec[1]) == 1 or int(dec[1]) == 4 or int(dec[1]) ==5 or int(dec[1]) ==9:#единицы равны 4.5.9
                                        inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[1]
                                    elif int(dec[0]) == 2 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#единицы равны 2.6.7.8
                                        inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[3]
                                    else:#единица методом исключения равна 3
                                        inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[5]
                                elif int(dec[0]) != 2 and int(dec[0]) != 3 and int(dec[0]) != 9:#десятки не равны 2 или 3 или 9
                                    if int(dec[1]) == 1 or int(dec[1]) == 4 or int(dec[1]) ==5 or int(dec[1]) ==9:#единицы равны 1.4.5.9
                                        inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[1]
                                    elif int(dec[1]) == 2 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#единицы равны 2.6.7.8
                                        inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[3]
                                    else:#единицы равны 3
                                        inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[5]
                                else:#методом исключения десятки равны 9
                                    if int(dec[1]) == 1 or int(dec[1]) == 4 or int(dec[1]) ==5 or int(dec[1]) ==9:#единицы равны 1.4.5.9
                                        inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[1]
                                    elif int(dec[1]) == 2 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#единицы равны 2.6.7.8
                                        inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[3]
                                    else:#единицы равны 3
                                        inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[5]

                            else:#единицы равны нулю
                                if int(dec[0]) ==5 or int(dec[0]) ==6 or int(dec[0]) ==7 or int(dec[0]) ==8:#Десятки равны 5.6.7.8
                                    inegr = decthird2[int(dec[0])] + endings[1]
                                elif int(dec[0]) ==2 or int(dec[0]) ==3 or int(dec[0]) ==9:#Десятки равны 2.3.9
                                    inegr = decthird[int(dec[0])] + endings[1]
                                else:#Десятки равны 4
                                    inegr = decthird2[int(dec[0])] + endings[3]

                    elif int(dec) >= 100 and int(dec) <111 or int(dec) >= 120:
                        if i2 == 0:#первый эллемент
                            if int(dec[1]) != 0 and int(dec[2]) != 0:#единицы и десятки не равны нулю
                                if int(dec[1]) == 2 or int(dec[1]) == 3:#десятки равны 2 или3
                                    if int(dec[2]) != 3: #единица не равна 3
                                        inegr = "сто "+decthird[int(dec[1])]+endings[2] +" "+decfirst[int(dec[2])]+endings[4]
                                    else:
                                        inegr = "сто "+decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[6]
                                elif int(dec[1]) != 2 and int(dec[1]) != 3 and int(dec[1]) != 9:#десятки не равны 2 или 3 или 9
                                    if int(dec[2]) != 3:#единицы не равны 3
                                        inegr = "сто "+decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[4]
                                    else:
                                        inegr = "сто "+decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[6]
                                else:#методом исключения десятки равны 9
                                    if int(dec[2]) != 3:#единицы не равны 3
                                        inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[4]
                                    else:
                                        inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[6]

                            elif int(dec[1]) != 0 and int(dec[2]) == 0:#Десятки не равны нулю, единицы равны
                                if int(dec[1]) ==4 or int(dec[1]) ==5 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#Десятки равны 4.5.6.7.8
                                    inegr = "сто " +decthird2[int(dec[1])] + endings[4]
                                else:#десятки не равны 4,5,6,7,8
                                    inegr = "сто " + decthird[int(dec[1])] + endings[4]

                            elif int(dec[1]) == 0 and int(dec[2]) != 0:#десятки равны нулю, единицы не равны
                                    if int(dec[2]) != 3: #единица не равна 3
                                        inegr = "сто "+decfirst[int(dec[2])]+endings[4]
                                    else:
                                        inegr = "сто "+decfirst[int(dec[2])]+endings[6]
                            else: #десятки и единицы равны нулю
                                inegr = "сотого"

                        else:#второй эллимент
                            if int(dec[1]) != 0 and int(dec[2]) != 0:#единицы и десятки не равны нулю
                                if int(dec[1]) == 2 or int(dec[1]) == 3:#десятки равны 2 или 3
                                    if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 4.5.9
                                        inegr = "сто "+decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[1]
                                    elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                        inegr = "сто "+decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[3]
                                    else:#единица методом исключения равна 3
                                        inegr = "сто" +decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[5]
                                elif int(dec[1]) != 2 and int(dec[1]) != 3 and int(dec[1]) != 9:#десятки не равны 2 или 3 или 9
                                    if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 1.4.5.9
                                        inegr = "сто "+ decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[1]
                                    elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                        inegr = "сто "+decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[3]
                                    else:#единицы равны 3
                                        inegr = "сто "+decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[5]
                                else:#методом исключения десятки равны 9
                                    if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 1.4.5.9
                                        inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[1]
                                    elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                        inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[3]
                                    else:#единицы равны 3
                                        inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[5]

                            elif int(dec[1]) != 0 and int(dec[2]) == 0:#Десятки не равны нулю, единицы равны
                                if int(dec[1]) ==5 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#Десятки равны 5.6.7.8
                                    inegr = "сто "+decthird2[int(dec[1])] + endings[1]
                                elif int(dec[1]) ==2 or int(dec[1]) ==3 or int(dec[1]) ==9:#Десятки равны 2.3.9
                                    inegr = "сто "+decthird[int(dec[1])] + endings[1]
                                else:#Десятки равны 4
                                    inegr = "сто "+decthird2[int(dec[1])] + endings[3]

                            elif int(dec[1]) == 0 and int(dec[2]) != 0:#десятки равны нулю, единицы не равны
                                if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 4.5.9
                                    inegr = "сто "+decfirst[int(dec[2])]+endings[1]
                                elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                    inegr = "сто "+decfirst[int(dec[2])]+endings[3]
                                else:#единица методом исключения равна 3
                                    inegr = "сто" +decfirst[int(dec[2])]+endings[5]
                            else: #десятки и единицы равны нулю
                                inegr = "сотый"
                    elif int(dec) >= 111 and int(dec) < 120:
                        if i2 == 0:
                            inegr = "сто " + decsecond[int(dec[1]+dec[2])]+endings[4]
                        else:
                            inegr = "сто "+ decsecond[int(dec[1]+dec[2])]+endings[1]
                    else:
                        inegr = "НЕДОПУСТИМОЕ ЗНАЧЕНИЕ"
                    exoncount.insert(i2,inegr)
                    i2+=1
            else:
                dec=S
                if len(dec)<2:#Для единиц
                    if int(dec) == 1 or int(dec) == 4 or int(dec) ==5 or int(dec) ==9:
                        inegr = decfirst[int(dec)]+endings[1]
                    elif int(dec) == 2 or int(dec) ==6 or int(dec) ==7 or int(dec) ==8:
                        inegr = decfirst[int(dec)]+endings[3]
                    else:
                        inegr = decfirst[int(dec)]+endings[5]
                elif int(dec)>=10 and int(dec)<20:#c 10 до 19
                    inegr = decsecond[int(dec)]+endings[1]
                elif int(dec)>=20 and int(dec)<100:#десятки
                    if int(dec[1]) != 0:#единицы не равны нудю
                        if int(dec[0]) == 2 or int(dec[0]) == 3:#десятки равны 2 или 3
                            if int(dec[1]) == 1 or int(dec[1]) == 4 or int(dec[1]) ==5 or int(dec[1]) ==9:#единицы равны 4.5.9
                                inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[1]
                            elif int(dec[0]) == 2 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#единицы равны 2.6.7.8
                                inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[3]
                            else:#единица методом исключения равна 3
                                inegr = decthird[int(dec[0])]+endings[2]+" "+decfirst[int(dec[1])]+endings[5]
                        elif int(dec[0]) != 2 and int(dec[0]) != 3 and int(dec[0]) != 9:#десятки не равны 2 или 3 или 9
                            if int(dec[1]) == 1 or int(dec[1]) == 4 or int(dec[1]) ==5 or int(dec[1]) ==9:#единицы равны 1.4.5.9
                                inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[1]
                            elif int(dec[1]) == 2 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#единицы равны 2.6.7.8
                                inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[3]
                            else:#единицы равны 3
                                inegr = decthird[int(dec[0])]+" "+decfirst[int(dec[1])]+endings[5]
                        else:#методом исключения десятки равны 9
                            if int(dec[1]) == 1 or int(dec[1]) == 4 or int(dec[1]) ==5 or int(dec[1]) ==9:#единицы равны 1.4.5.9
                                inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[1]
                            elif int(dec[1]) == 2 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#единицы равны 2.6.7.8
                                inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[3]
                            else:#единицы равны 3
                                inegr = decthird[int(dec[0])]+endings[8]+" "+decfirst[int(dec[1])]+endings[5]

                    else:#единицы равны нулю
                        if int(dec[0]) ==5 or int(dec[0]) ==6 or int(dec[0]) ==7 or int(dec[0]) ==8:#Десятки равны 5.6.7.8
                            inegr = decthird2[int(dec[0])] + endings[1]
                        elif int(dec[0]) ==2 or int(dec[0]) ==3 or int(dec[0]) ==9:#Десятки равны 2.3.9
                            inegr = decthird[int(dec[0])] + endings[1]
                        else:#Десятки равны 4
                            inegr = decthird2[int(dec[0])] + endings[3]
                elif int(S) >= 100 and int(S) <111 or int(S) >= 120:
                    if int(dec[1]) != 0 and int(dec[2]) != 0:#единицы и десятки не равны нулю
                        if int(dec[1]) == 2 or int(dec[1]) == 3:#десятки равны 2 или 3
                            if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 4.5.9
                                inegr = "сто "+decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[1]
                            elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                inegr = "сто "+decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[3]
                            else:#единица методом исключения равна 3
                                inegr = "сто" +decthird[int(dec[1])]+endings[2]+" "+decfirst[int(dec[2])]+endings[5]
                        elif int(dec[1]) != 2 and int(dec[1]) != 3 and int(dec[1]) != 9:#десятки не равны 2 или 3 или 9
                            if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 1.4.5.9
                                inegr = "сто "+ decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[1]
                            elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                inegr = "сто "+decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[3]
                            else:#единицы равны 3
                                inegr = "сто "+decthird[int(dec[1])]+" "+decfirst[int(dec[2])]+endings[5]
                        else:#методом исключения десятки равны 9
                            if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 1.4.5.9
                                inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[1]
                            elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                                inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[3]
                            else:#единицы равны 3
                                inegr = "сто "+decthird[int(dec[1])]+endings[8]+" "+decfirst[int(dec[2])]+endings[5]

                    elif int(dec[1]) != 0 and int(dec[2]) == 0:#Десятки не равны нулю, единицы равны
                        if int(dec[1]) ==5 or int(dec[1]) ==6 or int(dec[1]) ==7 or int(dec[1]) ==8:#Десятки равны 5.6.7.8
                            inegr = "сто "+decthird2[int(dec[1])] + endings[1]
                        elif int(dec[1]) ==2 or int(dec[1]) ==3 or int(dec[1]) ==9:#Десятки равны 2.3.9
                            inegr = "сто "+decthird[int(dec[1])] + endings[1]
                        else:#Десятки равны 4
                            inegr = "сто "+decthird2[int(dec[1])] + endings[3]

                    elif int(dec[1]) == 0 and int(dec[2]) != 0:#десятки равны нулю, единицы не равны
                        if int(dec[2]) == 1 or int(dec[2]) == 4 or int(dec[2]) ==5 or int(dec[2]) ==9:#единицы равны 4.5.9
                            inegr = "сто "+decfirst[int(dec[2])]+endings[1]
                        elif int(dec[2]) == 2 or int(dec[2]) ==6 or int(dec[2]) ==7 or int(dec[2]) ==8:#единицы равны 2.6.7.8
                            inegr = "сто "+decfirst[int(dec[2])]+endings[3]
                        else:#единица методом исключения равна 3
                            inegr = "сто" +decfirst[int(dec[2])]+endings[5]
                    else: #десятки и единицы равны нулю
                        inegr = "сотый"
                elif int(dec) >= 111 and int(dec) < 120:
                    inegr = "сто "+ decsecond[int(dec[1]+dec[2])]+endings[1]
                else:
                    inegr = "НЕДОПУСТИМОЕ ЗНАЧЕНИЕ"


            if S == ARRS[0] and len(ARRS)>1 and S.find('-') != -1:
                z = "c {} по {} (либо".format (exoncount[0], exoncount[1])
            elif S != ARRS[-1] and  S != ARRS[0] and len(ARRS)>1 and S.find('-') != -1 and sta[0] != ARRS:
                z = "c {} по {}, либо ".format (exoncount[0], exoncount[1])
            elif S == ARRS[-1] and len(ARRS)>1 and S.find('-') != -1:
                z = "c {} по {}, в зависимости от изоформы) экзоны".format (exoncount[0], exoncount[1])
            elif S == ARRS[-1] and len(ARRS)<1 and S.find('-') != -1 or sta[0] == ARRS and S.find('-') != -1:
                z = "c {} по {} экзоны".format (exoncount[0], exoncount[1])
            elif  S.find('-') == -1 and S ==ARRS[0] and len(ARRS)>1:
                z = inegr + " (либо "
            elif  S.find('-') == -1 and S !=ARRS[0]and S != ARRS[-1] and len(ARRS)>1 and sta[0] != ARRS:
                z = inegr + ", либо "
            elif  S.find('-') == -1 and S == ARRS[-1] and len(ARRS)>1:
                z = inegr + ", в зависимости от изформы) экзон"
            elif  S.find('-') == -1 and S == ARRS[-1] and S == ARRS[0] or sta[0] == ARRS and S.find('-') == -1:
                z = inegr + ' экзон'
            else:
                z = "ЧТО-ТО ПОШЛО НЕ ПО ПЛАНУ В БЛОКЕ КОННОТАЦИИ"
            prexon += z
        return prexon

    def arrSize (self,text):
        r = text.split(" ")
        shortAn = []
        for digit in r:
            if len(digit) <= 6:
                dig = digit[:-3] + "," + digit[-3:]
                shortAn.append(dig)
            elif len(digit) > 6:
                dig = digit[:-6] + "," + digit[-6:-3]+ ',' + digit[-3:]
                shortAn.append(dig)
            elif len(digit) < 3:
                shortAn.append(dig)
        outSize = int(r[1])-int(r[0])
        OutRange = r[0] + "-" +r[1]
        self.OutFinal = '(' +shortAn[0] + "-" + shortAn[1] +')'
        ranSize = '(геномная локализация: ' + str(OutRange) + "; размер: " + str(outSize) + ' пн):'
        return ranSize


    def KEGGgetter(self,text):
        global slovar_KEGG
        u = text
        z=""
        u = u.replace(" - Homo sapiens (human)","")
        u = u.replace("\n","")
        r = u.split('hsa')
        for g in r:
            if g != "":
                geneInspection = g.split(" ")
                for word in geneInspection:
                    if word.isupper() == True:
                        h = g
                        break
                    else:
                        h = g.lower()
                h = h[0:6]+"("+h[6:]+")"
                if g == r[0]:
                    z += h
                elif g == r[-1]:
                    z += "hsa"+h
                else:
                    z += "hsa"+h + ", "
        if len(r) > 20:
            KEGGstring = "Больше двадцати геномных сетей" + " " + '[KEGG ID: '+ z + "]"
        else:
            KEGGstring = slovar_KEGG [int(len(r))-1] + " " + '[KEGG ID: '+ z + "]"
        return KEGGstring

    def OMIMgetter (self,text):
        StartOMIMString = text
        WithOMIMnums = ''
        SplitedOMIMString = re.split (r'\n', StartOMIMString)
        for SubUnit in SplitedOMIMString:
            SplitedSubUnit = SubUnit.split(" ")
            for word in SplitedSubUnit:
                if word.isdigit() == True and len(word)==6:
                    spliter = SubUnit.find(word)
                    Disease = SubUnit[:spliter]
                    WithOMIMnums += "{} [OMIM:{}], ".format(Disease, word)
        return WithOMIMnums



    def Clear_button_right(self):
        app.entry2.delete('1.0', 'end-1c')
    def Clear_button_left(self):
        app.entry.delete('1.0', 'end-1c')
    def save_file_answer(self):
        save_as = filedialog.asksaveasfilename(defaultextension='.docx',filetypes=[('Text File', '*.docx')])
        try:
            letter = (app.entry2.get('1.0', 'end-1c'))
            letter.encode('utf8')
            document = DocxTemplate("Blank.docx")
            context = {'results': letter}
            document.render(context)
            document.save(save_as)
        except:
            pass
    def save_file(self):
        save_as = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text File', '*.txt')])
        try:
            letter = (app.entry2.get('1.0', 'end-1c'))
            letter.encode('utf8')
            f = open(save_as, "w")
            f.write(letter)
            f.close()
        except:
            pass

BO=ButtonOptions()
qarr = curentarr()
ctrl = Controller()
arr = arrangements()
app = SampleApp()
app.mainloop()

