import _Adding,os,sqlite3,time

print("""\n\n\n   <<<<<------    CNCBOT    ------>>>>>\n\n""")

print(""" ->>> 1| Run
 ->>> 2| Create New Project""")

chs = input("  Make your choise >>")
cntrl = 0
lstOfPrj = list()
global NmbrOfPrcss
a = 0
b = 0
c = 0
lstOfFunc = list()
lstOfCapDt = list()
lstOfTime = list()

def Split(text,par):
    text = str(text)
    nwTxt =""
    lstTxt = list()
    for i in text:
        if i == par:
            lstTxt.append(nwTxt)
            nwTxt = ""
        elif i == "'":
            continue
        else:
            nwTxt += i
        
    lstTxt.append(nwTxt)
    return lstTxt

def Sent_Write():
    text = input("Please enter a text for write your section area")
    _Adding.Write(Db_name,text)
    print("\nSUCCESS")            
#Sent_Write

def Sent_Compare():
    while True:
        value = input("""Enter your value what copare
                        with your selection area's number\n>>>""")
        equal = input("""Enter compare function like '=','>' or '<'
                        result will be; your value >,=,< getting value>>>""")
        if  not (value.isdigit()):
            print("wrong entry about value or equal.Lets retry!")
                    
        elif  not (equal == "=" or equal == ">" or equal == "<"):
            print("wrong entry about equal.Lets retry!")
        else:
            break 
                
    _Adding.Compare(Db_name,value,equal)
    print("\nSUCCESS")
#Sent_Compare

def Sent_Click():
    while True:
        button = input("""Select click type
1|left\n2|right\n3|middle\n4|Double Click\n>>>""")
        if button == "1":
            button = "left"
            break
        elif button == "2":
            button = "right"
            break
        elif button == "3":
            button = "middle"
            break
        elif button == "4":
            button = "Double_Click"
            break
        else:
            print("worng entry! Try again")
                
                 
    _Adding.Click(Db_name,button)
    print("\nSUCCESS")
#Sent_Click

def Order_Func():
    print("\nHere your sections")
    print("""\n1|Click\n2|Compare\n3|Write""")
    Func_chs = input("\nyour section>>>")

    if Func_chs == "1":#Click
        Sent_Click()
                  
    elif Func_chs == "2":#Compare
        Sent_Compare()     

    elif Func_chs == "3":#Write
        Sent_Write()
                                 
#Order_Func
    

if chs=="1": # Run
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\n\n   <<<<<------    CNCBOT    ------>>>>>\n\n""")
    path_doc=os.path.expanduser("~\\Documents\\CncBot\\")
    x = os.listdir(path_doc)
    
    for i in x:
        name = i.split(".")
        if name[1] == "sqlite":
            lstOfPrj.append(name[0])
            cntrl += 1
            print(" ->> {}| {}".format(str(cntrl),name[0]))
            

    if cntrl == 0:
        print("""There are not CncBot project.
                   Please "Create New Project" on Menu""")
        print("Use 'CTRL+C' combination for exit")
        input(">>>")

    else:
        chs = input("Select one of theme")
                  
#Connection to DataBase
        k = int(chs)- 1
    with  sqlite3.connect(path_doc + lstOfPrj[k] + ".sqlite") as con:
        print(lstOfPrj[k])
        crs = con.cursor()
        crs.execute("""SELECT * FROM Func_Order""")
        j  = crs.fetchall()
        for i in j:
            lstOfFunc.append(i)
        crs.execute("""SELECT * FROM Capture_Data""")
        j = crs.fetchall()
        for i in j:
            lstOfCapDt.append(i)
        crs.execute("""SELECT * FROM Time""")
        j = crs.fetchall()
        for i in j:
            lstOfTime.append(i)
    

        
    Cnt_RunTime = 1
    while True:
        while len(lstOfFunc) > a:
            commands = Split(lstOfFunc[a],',')
            if lstOfFunc[a][0][:3] == "Com":
                bl = _Adding._Compare(lstOfCapDt[b],commands[1],commands[2])
                if bl == 0:
                    a += 1
                    for i in lstOfFunc[a:]:
                        if i[0] !='Adverb':
                            a += 1
                            b += 1
                    
                    b -= 1
                else:
                    a += 1
                    b += 1       
            
            elif lstOfFunc[a][0][:3] == "Cli":
                _Adding._Click(lstOfCapDt[b],commands[1])
                a += 1
                b += 1
      
                  
            elif lstOfFunc[a][0][:3] == "Wri":
                _Adding._Write(lstOfCapDt[b],commands[1])
                a += 1
                b += 1    

            elif lstOfFunc[a][0][:3] == "Adv":
                for i in lstOfFunc[a+1:]:
                    if i !="Adverb":
                        a += 1
                        b += 1
                a += 1
                b -= 1 

            time.sleep(7)
        #End of  ---  While whl_bool  ---
        
        if int(lstOfTime[0][0]) == 1000:
            sec =""
            for i in lstOfTime[1]:
                i = str(i)
                if i.isdigit():
                    sec += i 
            time.sleep(int(sec))
            a = 0
            b = 0
        else:
            RunTime = Split(lstOfTime[Cnt_RunTime],'.')
            sec = (((int(RunTime[0][1:])-time.localtime().tm_hour) *3600) + ((int(RunTime[1][:2]) - time.localtime().tm_min) *60))
            
            if int(RunTime[1][:2]) < time.localtime().tm_min:
                sec += 3600
            if Cnt_RunTime == len(lstOfTime):
                break
            Cnt_RunTime += 1
            time.sleep(sec)
            a = 0
            b = 0
    #End of  ---  While True  ---              

                  
#End Of  ---   if chs =="1"  ---

#                                                             ^
#                                                            / \
#                                                            | |
#                                                            | |
#                                                       { Run Project }
#--------------------------------------------------------------------------------------------------------------------------------------
#                                                      { Create Project }
#                                                            | |
#                                                            | |
#                                                            \ /
#                                                             v

elif chs == "2": #Creat New Project
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\n\n   <<<<<------    CNCBOT    ------>>>>>\n\n""")
    prj_name = input("Give a name to your new CncBot project >>>")

    d = os.path.expanduser("~\\Documents")
    path_doc = os.listdir(d)
    a = 0
    for i in path_doc:
        if i == "CncBot":
            a += 1
    if a == 0:
        os.mkdir(d + "\\CncBot")
    Db_name = d + "\\CncBot\\" + prj_name 
    _Adding.Create_Project(Db_name)

    print("\n    Your project CREATED! \n\n")
    
    print("\nPlease select type of run time \n1|Repeat\n2|Define a few time")
    RunTime_Chs = input(">>>")
    cnt = 0
    while True:
        if RunTime_Chs == '1':
            RunTime = "1000"
            _Adding.Time(Db_name,RunTime)
            RunTime = input("Please enter time for waiting every between two run(second) >>")
            _Adding.Time(Db_name,RunTime)
            break
        elif RunTime_Chs == '2':
            RunTime = "2000"
            _Adding.Time(Db_name,RunTime)
            while  RunTime != '9' or cnt < 1:
                RunTime = input("Please enter a run time like '12.30' (if you finished entry; PRESS '9') >>")
                if RunTime != '9':
                    _Adding.Time(Db_name,RunTime)
                    cnt += 1
                else:
                    if cnt == 0:
                        print("\nYou must least enter a time!!!") 
            break
        else:
            print("Wrong entry!Let's try again")

    
    
    print(""" This program work with coordinates(pixels)!
\n  So before enter function your mause(cursor) must on it
what you want there\n\n""")
    print("For exit use 'CTRL+C' combination,it will save automaticly")
                  
    while True:
        print("\nHere your sections")
        print("""\n1|Click\n2|Compare\n3|Write""")
        Func_chs = input("\nyour section >>>")

        if Func_chs == "1":#Click
            Sent_Click()
                  
        elif Func_chs == "2":#Compare
            Sent_Compare()
            print("What do you want if result of compare is TRUE?")
            while True:#Adverb (Compare(TRUE))
                Func_chs = input("For continue in Compare(TRUE) press 1,for exit press 0>>>")
                if Func_chs == "1":
                    print("\nFor Compare(TRUE) select next function")
                    Order_Func()
                elif Func_chs == "0":
                    with sqlite3.connect(Db_name + ".sqlite") as Db: 
                        vt = Db.cursor()
                        vt.execute("""INSERT INTO Func_Order VALUES('Adverb')""")
                        Db.commit()
                    break
            print("\nSo what do you want if result of compare is FALSE?")

            while True:#Adverb (Compare(FALSE))
                Func_chs = input("For continue in Compare(FALSE) press 1,for exit press 0>>>")
                if Func_chs == "1":
                    print("\nFor Compare(FALSE) select next function")
                    Order_Func()
                elif Func_chs == "0":
                    with sqlite3.connect(Db_name + ".sqlite") as Db: 
                        vt = Db.cursor()
                        vt.execute("""INSERT INTO Func_Order VALUES('Adverb')""")
                        Db.commit() 
                    break
            print("You are exit of compare")        

        elif Func_chs == "3":#Write
            Sent_Write()
                                 
    #End of ---  while True  ---           
            
#End Of  ---   if chs =="2"  ---      
        
else:
    print("Wrong entry")
        
        

    
            
    

    
    


