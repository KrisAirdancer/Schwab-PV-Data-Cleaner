import traceback
import sys

# Schwab Personal Value Data Cleaner

rawfilepath = input('Input Raw Filepath: ')
cleanfilepath = input('Input Clean Filepath: ')
#INSERT EASY-RUN CODE FROM OBSIDIAN HERE

try:
    rawData = open(rawfilepath, 'r')
    cleanData = open(cleanfilepath, 'w') # Note: file must be empty - contain no data
    holidaysData = open(holidaysfilepath, 'r')

    holidays = holidaysData.readlines()

    for line in rawData :
        line = line.rstrip() # Remove newline character from all lines
        splitLine = line.split()
        del splitLine[-1]

        dateOnly = ''
        index = 0
        while index < len(splitLine) : # Convert splitLine back into string
            dateOnly = dateOnly + ' ' + splitLine[index]
            index += 1
        
        if line.startswith('Saturday') or line.startswith('Sunday') :
            continue

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
    



