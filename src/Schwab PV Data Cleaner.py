# Schwab Personal Value Data Cleaner

#rawfilepath = input('Input Raw Filepath: ')
#cleanfilepath = input('Input Clean Filepath: ')
#INSERT TESTING CODE FROM OBSIDIAN HERE

try:
    rawData = open(rawfilepath, 'r')
    cleanData = open(cleanfilepath, 'r')
    #fileAsString = rawData.read()
    #print('FILE CONTENTS: ', fileAsString)

    for line in rawData :
        print(line)



    rawData.close()
    cleanData.close()
except:
    print('Invalid File.')



