
import numpy

def checkPoint(x,y):
    cr1=(x-2)**2+(y-2)**2
    cr2=x**2+(y-2)**2
    cr3=x**2+y**2
    if((cr1 > 1) and (cr2 < 4) and (cr3 < 9)):
        return True
    else:
        return False



def counting(xmin, xmax,height, nstep):
    count=0
    for i in numpy.arange (xmin,xmax,nstep):
        for j in numpy.arange (0.0,height,nstep):
            if(checkPoint(i,j)):
               count+=1
    return count




xmin=-2.0
xmax=2.0
height=3.0
n=0.1
numPoints=counting(xmin,xmax,height,n)
area=numpoints*(n**2)
print(area)
