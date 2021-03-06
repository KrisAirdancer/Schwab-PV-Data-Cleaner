import traceback
import sys

# Schwab Personal Value Data Cleaner

#inputFilePath = input('Enter the Input Filepath: ') #Comment these out
#outputFilePath = input('Enter the Output Filepath: ') #Comment these out
holidaysFilePath = 'src\\Holidays List.txt' #Leave this line functional
#INSERT EASY-RUN CODE FROM OBSIDIAN HERE (See Programming Project Documentation Register)

try:
    rawData = open(inputFilePath, 'r')
    cleanData = open(outputFilePath, 'w') #Note: file must be empty - contain no data
    holidaysData = open(holidaysFilePath, 'r') #Note: Holidays file must have data formatted correctly - see extant file for proper format

    holidays = holidaysData.readlines()

    #Process data in PV Data file
    for line in rawData :
        line = line.rstrip() # Remove newline character from all lines
        splitLine = line.split() #Make a list to contain all separate elements (words & numbers) in the current line
        del splitLine[-1] #Remove dollar amount from current line (it is the last item in the line)

        dateOnly = ''
        index = 0
        while index < len(splitLine) : # Convert splitLine back into string
            dateOnly = dateOnly + ' ' + splitLine[index]
            index += 1
        
        if line.startswith('Saturday') or line.startswith('Sunday') :
            continue

        #Check if curent line is a holiday
        isHoliday = False
        for date in holidays :
            date = date.rstrip()
            dateOnly = dateOnly.rstrip()
            if date in dateOnly :
                isHoliday = True
                continue
        if not isHoliday :
            line = line + '\n' # Add newline character back for proper file formatting
            cleanData.write(line)

    # Close files
    rawData.close()
    cleanData.close()
    holidaysData.close()
except Exception:
    print(traceback.format_exc())
    print('Invalid File.')
    



