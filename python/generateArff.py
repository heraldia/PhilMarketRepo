import os
import shutil
import re
from string import join
import operator
import itertools
import numpy as np

def generateArff(relationString = 'fbank', lowerR = 0.1, higherR = 0.95, columnNum = 13 ):
    folderList = []
    flod = []
    for i, e in enumerate(os.listdir(relationString)):
        #print i, e
        flod.append(e.replace('_mfcc.csv',''))
        folderList.append( '\'%s\','%e.replace('_mfcc.csv',''))
    folderList = join(folderList)[:-1]

    outputFileArff = open('%s.arff'%relationString,'w+')
    relation = '@relation '+"'"+relationString+"'\n\n"
    outputFileArff.writelines(relation)

    columnNum += 1  # see [line70]
    for i in xrange(1,columnNum):
        s = '@attribute \'term%d\' numeric\n'%i
        outputFileArff.writelines(s)

    s = '@attribute \'class\' { %s}\n'%folderList
    outputFileArff.writelines(s)
    outputFileArff.writelines('\n@data\n')

    def loadData(relationString):
        count = 0
        lineNumberSum = 0
        linenumIncrementList = []
        fileNumInFolderList = []
        #totalCountLineList = []
        filesList = []
        for root,dirs,files in os.walk(relationString):
            fileNumInFolder = 0
            for elefile in files:
                fileNumInFolder += 1
                currentLineNum = 0
                totalCountLine = len(open(relationString+'\\'+elefile,'rU').readlines())
                #totalCountLineList.append(totalCountLine)
                #print elefile+' ; '+str(totalCountLine)
                filesList.append(elefile.replace('_%s.csv'%relationString,''))

                inputFile = open(relationString+'\\'+elefile,'r+')
                sub_count_line = 0
                for line in inputFile:
                    if int(lowerR* totalCountLine) <= currentLineNum < int(higherR*totalCountLine) and line.split():
                        line = line.replace('\n','')
                        '''
                        i = line.index(',')+1  #[line70]
                        line = line[i:]
                        '''
                        if relationString == 'fp':
                            outputFileArff.write(line+'%s\n'%flod[count])
                        else:
                            outputFileArff.write(line+',%s\n'%flod[count])
                        sub_count_line += 1
                    #print line.rstrip()+',%d'%count
                    currentLineNum += 1
                inputFile.close()
                lineNumberSum += sub_count_line
                linenumIncrementList.append(lineNumberSum)
                fileNumInFolderList.append(fileNumInFolder)
                count += 1

        #print linenumIncrementList, fileNumInFolderList, filesList
        return linenumIncrementList, fileNumInFolderList, filesList

    x,y,z = loadData(relationString)

    outputFileArff.close()
    return x,y,z,flod

def generateArffCombineType(relationString = 'fbank', lowerR = 0.1, higherR = 0.95, columnNum = 13 ):
    folderList = []

    flod = []
    for i, e in enumerate(os.listdir(relationString)):
        #print i, e
        flod.append(filter(str.isalpha,e.replace('_mfcc.csv','')))
        folderList.append( '\'%s\','%(filter(str.isalpha, e.replace('_mfcc.csv',''))))
    folderListNoRedun = set(folderList)
    folderListNoRedun = join(folderListNoRedun)[:-1]

    outputFileArff = open('%s.arff'%relationString,'w+')
    relation = '@relation '+"'"+relationString+"'\n\n"
    outputFileArff.writelines(relation)

    columnNum += 1  # see [line70]
    for i in xrange(1,columnNum):
        s = '@attribute \'term%d\' numeric\n'%i
        outputFileArff.writelines(s)


    s = '@attribute \'class\' { %s}\n'%folderListNoRedun
    outputFileArff.writelines(s)
    outputFileArff.writelines('\n@data\n')

    def loadData(relationString):
        count = 0
        lineNumberSum = 0
        linenumIncrementList = []
        fileNumInFolderList = []
        #totalCountLineList = []
        filesList = []
        for root,dirs,files in os.walk(relationString):
            fileNumInFolder = 0
            for elefile in files:
                fileNumInFolder += 1
                currentLineNum = 0
                totalCountLine = len(open(relationString+'\\'+elefile,'rU').readlines())
                #totalCountLineList.append(totalCountLine)
                #print elefile+' ; '+str(totalCountLine)
                filesList.append(elefile.replace('_%s.csv'%relationString,''))

                inputFile = open(relationString+'\\'+elefile,'r+')
                sub_count_line = 0
                for line in inputFile:
                    if int(lowerR* totalCountLine) <= currentLineNum < int(higherR*totalCountLine) and line.split():
                        line = line.replace('\n','')
                        '''
                        i = line.index(',')+1  #[line70]
                        line = line[i:]
                        '''
                        if relationString == 'fp':
                            outputFileArff.write(line+'%s\n'%flod[count])
                        else:
                            outputFileArff.write(line+',%s\n'%flod[count])
                        sub_count_line += 1
                    #print line.rstrip()+',%d'%count
                    currentLineNum += 1
                inputFile.close()
                lineNumberSum += sub_count_line
                linenumIncrementList.append(lineNumberSum)
                fileNumInFolderList.append(fileNumInFolder)
                count += 1

        #print linenumIncrementList, fileNumInFolderList, filesList
        return linenumIncrementList, fileNumInFolderList, filesList

    x,y,z = loadData(relationString)

    outputFileArff.close()
    return folderListNoRedun

def generateArffTest(relationString = 'mfcc', lowerR = 0.1, higherR = 0.95, columnNum = 13, folderListNoRedunFromPassing ='hello' ):

    lineNumberSum = 0
    linenumIncrementList = []
    fileNumInFolderList  = []
    #totalCountLineList  = []
    filesList = []

    newfolder = 'test_arff'
    if not os.path.exists(newfolder):
        os.mkdir(newfolder)
    for root,dirs,files in os.walk(relationString):
        fileNumInFolder = 0
        columnNumx = columnNum + 1
        for elefile in files:
            outputFileArff = open('test_arff\%s.arff'%elefile.replace('.csv',''),'w+')
            relation = '@relation '+"'"+elefile+"'\n\n"
            outputFileArff.writelines(relation)

            for i in xrange(1, columnNumx):
                s = '@attribute \'term%d\' numeric\n'%i
                outputFileArff.writelines(s)


            s = '@attribute \'class\' { %s }\n'%folderListNoRedunFromPassing
            outputFileArff.writelines(s)
            outputFileArff.writelines('\n@data\n')

            fileNumInFolder += 1
            currentLineNum = 0
            totalCountLine = len(open(relationString+'\\'+elefile,'rU').readlines())
            #totalCountLineList.append(totalCountLine)
            #print elefile+' ; '+str(totalCountLine)
            filesList.append(elefile.replace('_%s.csv'%relationString,''))

            inputFile = open(relationString+'\\'+elefile,'r+')
            sub_count_line = 0
            for line in inputFile:
                if int(lowerR* totalCountLine) <= currentLineNum < int(higherR*totalCountLine) and line.split():
                    line = line.replace('\n','')
                    outputFileArff.write(line+',%s\n'%folderListNoRedunFromPassing.split(',')[0]) #+',%s\n'%(elefile.split('_')[0]))
                    sub_count_line += 1
                #print line.rstrip()+',%d'%count
                currentLineNum += 1
            inputFile.close()
            lineNumberSum += sub_count_line
            linenumIncrementList.append(lineNumberSum)
            fileNumInFolderList.append(fileNumInFolder)

            outputFileArff.close()

    pass


def repl (x):
    return x.replace('_mfdwc','')

from collections import Counter
def proba(linenumIncrementList, fileNumInFolderList, filesList, flod, option=0):
    '''
    2015-11-26 15:16:46
    '''
    targetIter = 0
    predictedList = []
    #frameIndex = 0

    fileIndexInType = 0
    fileNumInFolderList = np.cumsum(fileNumInFolderList)

    typeIter = 0
    resultTupleList = []
    read = False
    output_csv = open('allList.csv','w')
    for line in open('input.txt'):
        if line == '\n':
            continue

        if read and line[0] == '=':
            read = False
            continue

        if not read and line[0] == 'i':
            read = True
            continue

        if read and line != '\n':
            line = re.sub(' +', ' ', line)
            linelist =  line.replace('\n','').split(' ')
            lineNum,actual,predicted = int(linelist[1]),linelist[2],linelist[3]

            if lineNum<=linenumIncrementList[targetIter]:
                predictedList.append(predicted)
            elif lineNum == linenumIncrementList[targetIter]+1:
                if targetIter == fileNumInFolderList [typeIter]:
                    typeIter += 1
                resultList = []
                print filesList[targetIter]+',',
                output_csv.write(filesList[targetIter]+',')
                resultList.append(filesList[targetIter])

                if option == 1:
                    print flod[typeIter]+',',
                    print Counter(predictedList).most_common(1)[0][0]
                    output_csv.write(flod[typeIter]+',')
                    output_csv.write(Counter(predictedList).most_common(1)[0][0])
                    output_csv.write('\n')
                    resultList.append(flod[typeIter])
                    resultList.append(Counter(predictedList).most_common(1)[0][0] )
                    resultTupleList.append(resultList)
                elif option == 0:
                    print flod[typeIter]+','
                    output_csv.write(flod[typeIter]+',')
                    print Counter(predictedList)
                    output_csv.write(str(Counter(predictedList)))
                    output_csv.write('\n')
                else:
                    continue
                targetIter += 1
                predictedList = [] # bug here missing
            else:
                pass

        #frameIndex += 1
        #     print frameIndex

    output_csv.close()
    return resultTupleList

def transl(ststring):
    if ststring:
        s=1
    pass

def getCrossTypeMcrFileLevel(resultTupleList,flod):
    if resultTupleList :
        actualList = []
        predictedList = []
        for ele in resultTupleList:
            actualList.append(ele[1].replace('water','flushing3'))
            predictedList.append(ele[2].replace('water','flushing3'))
            #predictedList.append(ele[2])

        errors = 0
        for i in range(0,len(actualList)):
            x = actualList[i][:2]
            y = predictedList[i]
            if not x in y:
                errors +=1

        crossTypeMcr = 1.0 * errors/len(resultTupleList) * 100

        print 'crossTypeMcr\n%.2f%% file ' %crossTypeMcr
        #matrixP(flod, actualList, predictedList)

def compareFileLevel():
    '''
    get most error cross typs
    '''
    #shutil.copyfile('xresult.txt','xresult.csv')
    fp = open('allList.csv','r')
    for line in fp:
        line = line.split(',')
        line[2] = line[2].replace('\n','')
        if line[1].strip()[:3] not in line[2]:
            if (line[1].strip()[:4] in 'water' and 'flus' in line[2]):
                continue
            if (line[1].strip()[:4] in 'flus' and 'wate' in line[2]):
                continue

            print line

def compareFrameLevel(debug = 0):
    fp = open('input.txt','r')
    error = 0
    total = 0
    read = False
    for line in fp:
        if line == '\n':
            continue

        if read and line[0] == '=':
            read = False
            continue

        if not read and line[0] == 'i':
            read = True
            continue

        if read and line != '\n':
            line = re.sub(' +', ' ', line)
            linelist =  line.replace('\n','').split(' ')
            actual,predicted = linelist[2],linelist[3]
            if actual[0] not in predicted:
                if ('wate' in actual and 'flus' in predicted) :
                    continue
                if ('flus' in actual and 'wate' in predicted):
                    continue
                if ('flushi' in actual and 'flushi' in predicted):
                    continue
                if debug == 1:
                    print line.replace('\n','')
                error += 1

            total += 1

    print 'crossTypeMcr\n%.2f%% frame ' % (1.0 * error/total *100)

    pass


def dispatch(option = 0, columnNum = 13, foldername = 'mfcc',\
        folderListNoRedunFromPassing = "'placeCupTable', 'cough', 'movingChair','clap'"\
        ):
    if option == 0:
        #foldername = filter(lambda x: x.ischr(),foldername)
        linenumIncrementList, fileNumInFolderList, filesList, flod =\
        generateArff(foldername,0.01,0.95, columnNum)
        #resultTupleList = proba(linenumIncrementList, fileNumInFolderList,
        #        filesList, flod, 1)
        #getCrossTypeMcrFileLevel(resultTupleList,flod)
    elif option == 1:  # 4 seed arff training
        folderListNoRedun = generateArffCombineType(foldername,0.01,0.95, columnNum)
        #compareFrameLevel(0)
        return folderListNoRedun
    elif option == 2:  # 4 test single arff
        #folderListNoRedunFromPassing = "'placeCupTable', 'cough', 'movingChair'"
        generateArffTest(foldername,0.01,0.95, columnNum, folderListNoRedunFromPassing)
        pass
    else:
        #compareFileLevel()
        pass

if __name__ == '__main__':
    dispatch(2, 12, 'mp3_mfcc')


