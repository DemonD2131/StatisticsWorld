import pygame
import math
import numpy as np
def getData(length):
    list = []
    for i in range(length):
        list.append(float(input("Data " + str(i) + " (give a float): ")))
    return list
def meanFind(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    return round(sum / len(data), 1)
def medianFind(tempdata):
    sortDat(tempdata)

    length = len(tempdata)
    midone = tempdata[0 + int(length/2)]
    midtwo = tempdata[length-1 - int(length/2)]
    return (midone + midtwo)/2
def highest(list, choice):
    #choice determines highest or lowest, 0 is highest 1 is lowest
    highest = list[0]
    lowest = list[0]
    for e in range(0, len(list)):
        if list[e] <= lowest:
            lowest = list[e]
        if (list[e] >= highest):
            highest = list[e]

    if choice == 0:
        return highest
    elif choice == 1:
        return lowest
    return None
def getClassnum(data, datalen):
    if(datalen <= 0):
        return None
    k = 1
    while(math.pow(2, k) < datalen):
        k += 1
    return k
def getRoundvalue(data):
    max = 0
    for i in range(len(data)):
        value = int(str(data[i]).split(".")[1])
        if(value != 0 and len(str(value)) > max):
            max = len(str(value))
    return max
def sortDat(dat):
    for i in range(len(dat)):
        for j in range(len(dat)-1):
            if(dat[i] < dat[j]):
                temp = dat[i]
                dat[i] = dat[j] 
                dat[j] = temp
    return dat
pygame.init()

size = (800, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Statistics!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

clock = pygame.time.Clock()
fps = 25
done = False

#variables relevant
font = pygame.font.SysFont('Calibri', 10, True, False)




grouped = False

datalength = int(input("What is the length of the dataset?\n"))
data = getData(datalength)

chooseOperation = int(input("What would you like to do?\n0 for grouped classes, 1 for quartiles: "))
if chooseOperation == 0:
    
    roundVal = getRoundvalue(data)
    classnum = int(getClassnum(data, datalength))
    print(classnum)
    minimum = highest(data,1)
    maximum = highest(data,0)
    #print(str(minimum) + "-" + str(maximum))
    crange = (maximum)- (minimum) 
    #print(crange)
    width = int((crange/classnum) +0.5)
    print(width)
    classFreq = []
    classLimits = []
    for i in range(classnum):
        classLimits.append(((minimum + (width * i)) - 0.5, (minimum + width + (width * i) )- 0.5))
        classFreq.append(0)
    print(classLimits)
    for e in range(classnum):
        for j in range(len(data)):
            if(data[j] >= classLimits[e][0] and data[j] < classLimits[e][1]):
                classFreq[e] += 1
    print(classFreq)
    print("Mean " + str(meanFind(data)))

    limitstring = ""
    for e in range(len(classLimits)):
        limitstring += str(classLimits[e][0])
        limitstring += "-" + str(classLimits[e][1]) + "\n"
    limittext = font.render(limitstring, True, BLACK)
    grouped = True
elif chooseOperation == 1:
    data = sortDat(data)
    q2 = medianFind(data)
    
    tempDat = []
    pos = 0
    while (data[pos] <= q2):
        tempDat.append(data[pos])
        pos += 1
    q1 = medianFind(tempDat)

    tempDat = []
    pos = len(data) -1
    while (data[pos] > q2):
        tempDat.append(data[pos])
        pos -= 1
    q3 = medianFind(tempDat)

    q4 = data[len(data)-1]
    q0 = data[0]
    iqr = q3 - q1

    print(data)
    outliers = []
    for i in range(len(data)):
        if(data[i] < q1 - 1.5*iqr or data[i] > q3 + 1.5*iqr):
            outliers.append(data[i])

    print("Outliers: " + str(outliers))

datatext = font.render("Data: " + str(data), True, BLACK)






while done == False:

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                done = True
    screen.fill(WHITE)
    #display

    screen.blit(datatext, [10, 10])
    if(grouped):
        screen.blit(limittext, [10, 50])
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()