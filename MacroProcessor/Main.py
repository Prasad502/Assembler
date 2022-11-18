from InstructionParser import Instruction_Parser
import re
import TableGenerator as TB
import os


def main():
    if os.path.exists("output.txt"):
        os.remove("output.txt")

    txt_file = open("Script.txt", "r")
    file_content = txt_file.read()
    content_list = file_content.split("\n")
    txt_file.close()                        

    LC = 0

    for i in content_list:
        delimiters = " ",",","+"
        regexPattern = '|'.join(map(re.escape, delimiters))
        temp_list = re.split(regexPattern, i)
        LC = Instruction_Parser(temp_list,LC)


    TB.PrintTable()


if __name__ == '__main__':
    main()
    