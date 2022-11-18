import TableGenerator as TB

MacroFlag = 0   # Global Flag to Switch from Normal Instruction to Macro Instruction.

def OutWrite(LC,temp_list):
    Str1 = ' '.join(map(str,temp_list))
    f = open("output.txt", "a")
    f.write(str(LC) + " " + Str1 + '\n')
    f.close()
    

def Instruction_Parser(temp_list,LC):
    
    global MacroFlag
    
    if (MacroFlag == 0):
        
        if (temp_list[0] == 'MACRO'):
            MacroFlag = 1
        
        
    
    else:
        print("Going to Macro.")
        if (temp_list[0] == "MEND"):
            MacroFlag = 0
