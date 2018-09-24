def CommandLineParser(inputStr):
    list1 = inputStr.split(" ")
    print ("Command: %s" %list1[0])
    #flagPositions = []
    flags =[]
    flagArguments = []
    for x in range(len(list1)):         #check for flags "-" or "--"
        if list1[x][0]=="-":
            if list1[x][1]=="-":        #long version of flag: '--'

                indexOfEqualsign = list1[x].find("=")
                flags.append(list1[x][:indexOfEqualsign])
                flagArguments.append(list1[x][indexOfEqualsign:])


            else:                       #short version of flag: '-'
                flags.append(list1[x][0:2])
                if list1[x+1][0]=="-":                    #flag without argument
                    flagArguments.append("")
                else:                                   #flag with argument
                    if len(list1[x]) > 2:
                        flagArguments.append(list1[x][2:])
                    else:
                        flagArguments.append(list1[x+1])






    for x in range(len(flags)):
        print("Flag %s: %s, Argument: %s" %(x,flags[x],flagArguments[x]))


    print("Main Argument: %s" %list1[-1])


inputString = "sort -r Filename.txt -o Output.txt"
inputString2 = "sort -rFilename.txt"
inputString3 = "sort -r Filename.txt --output=out_file -oOutput.txt example_file"
CommandLineParser(inputString3)




#x = 12.3456789
#print('The value of x is %3.2f' %x)