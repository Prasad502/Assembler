import TableGenerator as TB

MacroFlag = 0   # Global Flag to Switch from Normal Instruction to Macro Instruction.
MacroName = 0   # Global Flag to check if Macro Name is on the same or next line.

def OutWrite(temp_list):
    Str1 = ' '.join(map(str,temp_list))
    f = open("output.txt", "a")
    f.write(Str1+"\n")
    f.close()

def Check_in_MNT(Name): 
    for i in range(len(TB.iMNT)):
        if(Name == TB.iMNT[i][0]):
            return True
    return False

def Instruction_Parser(temp_list):
    
    global MacroFlag,MacroName
    
    if (MacroFlag == 0):
        if (temp_list[0] == 'MACRO'):
            MacroFlag = 1
            Macro_Processor(temp_list)
        else:
            if(Check_in_MNT(temp_list[0])):
                Str = ""
                for i in range(len(TB.iMDT)):
                    OutWrite(TB.iMDT[i])
            else:
                OutWrite(temp_list)
    else:
        Macro_Processor(temp_list)
        
            # print(temp_list)
            # for i in range(len(temp_list)):
            #     for j in range(len(temp_list[i])):
            #         if temp_list[i][j] == "=":
            #             temp = temp_list[i].split("=")
            #             print(temp)
    
def Macro_Processor(temp_list):
    
    global MacroFlag,MacroName
    
    if (temp_list[0] == "MACRO"):
        if(len(temp_list) > 1):
            Parameter = len(temp_list) - 2
            TB.MNT_Add(temp_list[1],Parameter)
            TB.Add_Argument(temp_list, MacroName,temp_list[1])
        else:
            MacroName = 1
    else:
        if (MacroName == 0):
            TB.MDT_Add(temp_list)
        else:
            Parameter = len(temp_list) - 1
            TB.MNT_Add(temp_list[0],Parameter)
            TB.Add_Argument(temp_list,MacroName,temp_list[0])
            MacroName = 0
        
    if (temp_list[0] == "MEND"):
        MacroFlag = 0
