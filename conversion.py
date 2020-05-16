'''
Objective : Python Script which converts the image into art depending on the pixel intensity.

'''

#import necessary modules
import imageio
import numpy as np

# function which converts the pixel to either black or white depending on the mean of pixel intensity
def convertRowToBW(row):
    newRow=[]
    for pixel in row:
        avg=(int(pixel[0])+int(pixel[1])+int(pixel[2]))/3
        if avg>125:
            newRow.append([255,255,255])
        else:
            newRow.append([0,0,0])
    return newRow

# function do above operation for the whole image
def convertFileToBW(file):
    newFile=[]
    for row in file:
        newFile.append(convertRowToBW(row))
    return np.array(newFile).astype('uint8')

# function to covert black pixel to '.' and white pixel to ' '
def convertTextRow(row):
    newRow=""
    for pixel in row:
        if pixel[0]==0:
            newRow=newRow+"."
        else:
            newRow=newRow+" "
    return newRow

# function do above operation for the whole pixels
def convertTextFile(blackAndWhiteFile):
    newText = ""
    for row in blackAndWhiteFile:
        newText=newText+convertTextRow(row)+'\n'
    return newText

# main function
def convertFile(fileName):
    file=imageio.imread(fileName)
    BWFile=convertFileToBW(file)
    imageio.imwrite('Black-White'+fileName, BWFile)
    strippedName=fileName.split('.')[0]
    textFile=open('Art'+strippedName+'.txt', 'wb')
    textFile.write(str.encode(convertTextFile(BWFile)))
    textFile.close()

convertFile("photo.png")