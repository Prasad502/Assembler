import TableGenerator as TB

MacroFlag = 0       # Global Flag to Switch from Normal Instruction to Macro Instruction.
MacroNameFlag = 0   # Global Flag to check if Macro Name is on the same or next line.

def OutWrite(temp_list):
    Str1 = ' '.join(map(str,temp_list))
    f = open("output.txt", "a")
    f.write(Str1+"\n")
    f.close()
    

def Start_Index_of_MDT(MacroName):
    for i in range(0,len(TB.iMNT)):
        if (MacroName == TB.iMNT[i][0]):
            return TB.iMNT[i][2]
    return 0


def Check_in_MNT(Name): 
    for i in range(len(TB.iMNT)):
        if(Name == TB.iMNT[i][0]):
            return True
    return False


def Replace_Arguments(temp_list,Real_Arguments,Element,Index):
    for i in range(len(temp_list)):
        for j in range(len(Real_Arguments)):
            if(temp_list[i] == Element):
                temp_list[i] = Real_Arguments[Index - 1]
    return temp_list


def Instruction_Parser(temp_list):
    
    global MacroFlag,MacroNameFlag
    
    if (MacroFlag == 0):
        if (temp_list[0] == 'MACRO'):
            MacroFlag = 1
            Macro_Processor(temp_list)
        else:
            if (temp_list[0] == "START"):
                TB.Display_MDT()
                
            if(Check_in_MNT(temp_list[0])):

                Real_Arguments = TB.Replace_Arguments(temp_list)
                
                i = Start_Index_of_MDT(temp_list[0])
                
                while(i <= len(TB.iMDT)):
                    
                    if(TB.iMDT[i][0] == "MEND"):
                        break
                    
                    elif(Check_in_MNT(TB.iMDT[i][0])):
                        j = Start_Index_of_MDT(TB.iMDT[i][0])
                        while(j <= len(TB.iMDT)):
                            if(TB.iMDT[j][0] == "MEND"):
                                break
                            else:
                                OutWrite(TB.iMDT[j])
                            j += 1
                        
                    else:
                        temp = list()
                        for k in range(len(TB.iArgument_List)):
                            if(TB.iArgument_List[k][0] == temp_list[0]):
                                temp = TB.iArgument_List[k]   

                        temp1 = list()
                        for k in range(len(TB.iMDT[i])):
                            for l in range(len(temp)):
                                if(TB.iMDT[i][k] == temp[l]):
                                    temp1 = Replace_Arguments(TB.iMDT[i], Real_Arguments, TB.iMDT[i][k], l)
                            
                        OutWrite(temp1)

                    i += 1
            else:
                OutWrite(temp_list)
    else:
        Macro_Processor(temp_list)

    
def Macro_Processor(temp_list):
    
    global MacroFlag,MacroNameFlag
    
    if (temp_list[0] == "MACRO"):
        if(len(temp_list) > 1):
            Parameter = len(temp_list) - 2
            TB.MNT_Add(temp_list[1],Parameter)
            TB.Add_Argument(temp_list, MacroNameFlag, temp_list[1])
        else:
            MacroNameFlag = 1
    else:
        if (MacroNameFlag == 0):
            TB.MDT_Add(temp_list)
        else:
            Parameter = len(temp_list) - 1
            TB.MNT_Add(temp_list[0],Parameter)
            TB.Add_Argument(temp_list,MacroNameFlag, temp_list[0])
            MacroNameFlag = 0
        
    if (temp_list[0] == "MEND"):
        MacroFlag = 0