import TableGenerator as TB

MacroFlag = 0       # Global Flag to Switch from Normal Instruction to Macro Instruction.
MacroNameFlag = 0   # Global Flag to check if Macro Name is on the same or next line.
index = 0

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

def Instruction_Parser(temp_list):
    
    global MacroFlag,MacroNameFlag,index
    
    if (MacroFlag == 0):
        if (temp_list[0] == 'MACRO'):
            MacroFlag = 1
            Macro_Processor(temp_list)
        else:
            if(Check_in_MNT(temp_list[0])):
                i = Start_Index_of_MDT(temp_list[0])
                while(i <= len(TB.iMDT)):
                    if(TB.iMDT[i][0] == "MEND"):
                        break
                    else:
                        OutWrite(TB.iMDT[i])
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