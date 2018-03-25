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




    def exonsCount (self,text):
        global decfirst
        global decsecond
        global decthird
        global decthird2
        global endings
        app.entry2.delete('1.0', 'end-1c')
        ARRS = text
        exoncount = []
        prexon=''
        if ARRS.find(',') != -1:
            ARRS=ARRS.split(",")
            n=len(ARRS)
            a = ARRS
            m=n-1
            while m>0:
                for i in range(m):
                    fir = a[i].split('-')
                    fir2 =a[i+1].split('-')
                    if int(fir[0]) > int(fir2[0]):
                        x=a[i]
                        a[i]=a[i+1]
                        a[i+1]=x
                m=m-1
            sta=a
        else:
            sta=[]
            sta.append(ARRS)
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
