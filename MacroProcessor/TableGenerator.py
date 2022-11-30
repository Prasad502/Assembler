iMNT = list()               # This is the definition for Macro Name Table.
iMDT = list()               # This is the definition for Macro Data Table.
iArgument_List = list()     # This is the defnition for Argument List Data.

def Display_MNT():
    for i in iMNT:
        print(i)
        
def Display_MDT():
    for i in iMDT:
        print(i)

def Display_Arguments():
    for i in iArgument_List:
        print(i)

def MDT_Add(temp_list):
    iMDT.append(temp_list)

def MNT_Add(Macro_Name,Parameter):
    temp = list()
    temp.append(Macro_Name)
    temp.append(Parameter)
    
    Start_Index = len(iMDT)
    
    temp.append(Start_Index)
    iMNT.append(temp)

def Add_Argument(temp_list,Flag,Name):
    temp = list()
    temp.append(Name)
    
    if(Flag == 0):
        for i in range(2,len(temp_list)):
            temp.append(temp_list[i])
        iArgument_List.append(temp)
        
    elif(Flag == 1):
        for i in range(1, len(temp_list)):
            temp.append(temp_list[i])
        iArgument_List.append(temp)