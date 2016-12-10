#import minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from fractions import gcd

mc = minecraft.Minecraft.create()
waitTime = 9
sigDigits = 3
graphMin = -50
graphMax = 50
bah = block.WOOL.id

#first line
#x coeff
a1 = random.randint(3,5)
#y coeff
b1 = random.randint(1,a1-1)
#constant
c1 = random.randint(-25,23)

#uses rule from Bezout's Identity to make sure it displays
makeSureDisplays = c1 % gcd(a1,b1)
while makeSureDisplays > 0:
    c1 = random.randint(-25,23)
    makeSureDisplays = c1 % gcd(a1,b1)
    
#2nd line
#x coeff
a2 = random.randint(-5,a1-1)
#y coeff
b2 = random.randint(b1+1,5)
#constant
c2 = random.randint(c1+1,25)
makeSureDisplays = c2 % gcd(a2,b2)
while makeSureDisplays > 0:
    c2 = random.randint(c1+1,25)
    makeSureDisplays = c2 % gcd(a2,b2)

def numberBlocks(num,x,y,z):
    if num < 0:
        color = 14
    else:
        color = 11
    n = abs(num)
    xd = 0
    while n > 0.99:
      if n < 5:
        mc.setBlocks(x+xd,y,z,x+xd,y+n-1,z, bah, color)
        n = n-n
        xd = xd+1
      else:
        mc.setBlocks(x+xd,y,z,x+xd,y+4,z, bah, color)
        n = n - 5
        xd = xd+1

def xblock(x,y,z, color):

    mc.setBlock(x,y,z, block.WOOL.id, color)
    mc.setBlock(x,y+2,z, bah, color)
    mc.setBlock(x+1,y+1,z, bah, color)
    mc.setBlock(x+2,y,z, bah, color)
    mc.setBlock(x+2,y+2,z, bah, color)

def yblock(x,y,z, color):
    mc.setBlocks(x,y,z,x+2,y,z, bah, color)
    mc.setBlocks(x+2,y+1,z,x+2,y+3,z, bah, color)
    mc.setBlocks(x,y+2,z,x+1,y+2,z, bah, color)
    mc.setBlock(x,y+3,z, bah, color)

def equalsign(x,y,z):
    mc.setBlocks(x,y+1,z,x+3,y+1,z, bah, 15)
    mc.setBlocks(x,y+3,z,x+3,y+3,z, bah, 15)

def plussign(x,y,z):
    mc.setBlocks(x,y+2,z,x+2,y+2,z, bah, 15)
    mc.setBlocks(x+1,y+1,z,x+1,y+3,z, bah, 15)

#Open Parentheses
def parenC(x,y,z):
    mc.setBlock(x+1,y,z, bah, 15)
    mc.setBlock(x+1,y+4,z, bah, 15)
    mc.setBlocks(x,y+1,z,x,y+3,z,bah,15)

#Close Parentheses   
def parenD(x,y,z):
    mc.setBlock(x,y,z, bah, 15)
    mc.setBlock(x,y+4,z, bah, 15)
    mc.setBlocks(x+1,y+1,z,x+1,y+3,z,bah,15)


# ax + by = c
def equationAXBYC(a,b,c,h,color):
    pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(a,pos.x-19,pos.y+h,pos.z-dBack)
    xblock(pos.x-17,pos.y+h,pos.z-dBack,color)
    plussign(pos.x-12,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)

# ax = c + by
def equationAXCBY(a,b,c,h,color):
    pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(a,pos.x-7,pos.y+h,pos.z-dBack)
    xblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x+17,pos.y+h,pos.z-dBack)
    yblock(pos.x+19,pos.y+h,pos.z-dBack,color)

# a(c+by) + by = c
def equationAcbyBYC(a,b1,c1,b2,c2,h,color):
    pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(a,pos.x-49,pos.y+h,pos.z-dBack)
    #Openparentheses
    parenC(pos.x-42,pos.y+h,pos.z-dBack)
    numberBlocks(c1,pos.x-39,pos.y+h,pos.z-dBack)
    plussign(pos.x-32,pos.y+h,pos.z-dBack)
    numberBlocks(b1,pos.x-27,pos.y+h,pos.z-dBack)
    yblock(pos.x-20,pos.y+h,pos.z-dBack,color)
    parenD(pos.x-15,pos.y+h,pos.z-dBack)
    #closeParentheses
    plussign(pos.x-12,pos.y+h,pos.z-dBack)
    numberBlocks(b2,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)

# c+ by = c2
def equationCBYC(b,c1,c2,h,color):
    pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(c1,pos.x-19,pos.y+h,pos.z-dBack)
    plussign(pos.x-12,pos.y+h,pos.z-dBack)
    numberBlocks(b2,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)

#by = c + c
def equationBYCC(b,c1,c2,h,color):
    pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(b2,pos.x-12,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    numberBlocks(c1,pos.x+17,pos.y+h,pos.z-dBack)

#by = c
def equationBYC(b,c, h,color):
    pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(b2,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)

    
line2 = str(a2) + "x + " + str(b2) + "y = " + str(c2)

# Graph Paper
mc.setBlocks(graphMin,1,graphMin, graphMax,101,graphMax, block.AIR.id)
mc.setBlocks(graphMin,0,graphMin, graphMax,0,graphMax, block.WOOL.id, 0)
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if xi % 2 == 0:
            if yi % 2 == 0:
                mc.setBlock(xi,0,yi, block.WOOL.id, 8)
        if xi % 2 == 1:
            if yi % 2 == 1:
                mc.setBlock(xi,0,yi, block.WOOL.id, 8)

# axis
mc.setBlocks(graphMin,0,   0, graphMax,0,  0, block.WOOL.id, 15)
mc.setBlocks(   0,0,graphMin,   0,0,graphMax, block.WOOL.id, 15)

#Line 1
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if (xi*a1 + yi*b1 == c1):
                mc.setBlock(xi,1,yi, block.WOOL.id, 1)

line1 = str(a1) + "x + " + str(b1) + "y = " + str(c1)
mc.postToChat(line1)
pos = mc.player.getPos()
leftMargin = 10
dBack = 12
mc.setBlocks(pos.x-leftMargin,pos.y,pos.z-dBack, pos.x+leftMargin,pos.y+12,pos.z-dBack, block.AIR.id)
equationAXBYC(a1,b1,c1,6,1)

#Line 2                
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if (xi*a2 + yi*b2 == c2):
                mc.setBlock(xi,2,yi, block.WOOL.id, 5)
mc.postToChat(line2)
equationAXBYC(a2,b2,c2,0,5)

time.sleep(waitTime)

#solve equation1 for x
mc.postToChat("Solve equation1 for x")

line1x = str(a1) + "x = " + str(c1) + " - " + str(b1) + "y"
pos = mc.player.getPos()
mc.setBlocks(pos.x, pos.y, pos.z+3, pos.x, pos.y+a1, pos.z+3, block.WOOL.id, 11)
time.sleep(waitTime)
mc.postToChat(line1x)
equationAXCBY(a1,0-b1,c1,6,1)

line1x = "x = " + str(c1) + "/" + str(a1) + " - " + str(b1) + "y/" + str(a1)
time.sleep(waitTime)
mc.postToChat(line1x)
equationAXCBY(a1/a1,0-b1/a1,c1/a1,6,1)

line1x = "x = " + str(round(c1/a1,sigDigits))  + " - " + str(round(b1/a1,sigDigits)) + "y" 
time.sleep(waitTime)
mc.postToChat(line1x)


#plug it into equation 2 for x
time.sleep(waitTime)
mc.postToChat("Plug it into equation 2 for x")
line2y = str(a2) + "(" + str(round(c1/a1,sigDigits))  + " - " + str(round(b1/a1,sigDigits)) + ")y + " + str(b2) + "y = " + str(c2)
time.sleep(waitTime)
mc.postToChat(line2y)
equationAcbyBYC(a2,0-b1/a1,c1/a1,b2,c2,0,5)

#solve equation2  for y
mc.postToChat("Solve equation2 for y")

time.sleep(waitTime)
mc.postToChat("Distribute")
line2y = str(a2) + "(" + str(round(c1/a1,sigDigits))  + ") - " + str(a2) + "(" + str(round(b1/a1,sigDigits)) + "y) + " + str(b2) + "y = " + str(c2)
mc.postToChat(line2y)
equationAcbyBYC(1,0-a2*b1/a1,a2*c1/a1,b2,c2,0,5)


line2y = str(round(a2*c1/a1,2))  + " - (" + str(round(a2*b1/a1,sigDigits)) + ")y + " + str(b2) + "y = " + str(c2)
time.sleep(waitTime)
mc.postToChat(line2y)

time.sleep(waitTime)              
mc.postToChat("Combine like terms")
line2y = str(round(a2*c1/a1,sigDigits))  + " + " + str(round(b2 - a2*b1/a1,sigDigits)) + "y = " + str(c2)
mc.postToChat(line2y)
equationCBYC(b2-a2*b1/a1,a2*c1/a1,c2,0,5)

line2y = str(round(b2-a2*b1/a1,sigDigits)) + "y = " + str(c2) + " - " + str(round(a2*c1/a1,sigDigits))
time.sleep(waitTime)
mc.postToChat(line2y)
equationBYCC(b2-a2*b1/a1,0-a2*c1/a1,c2,0,5)

line2y =str(round(b2 - a2*b1/a1,sigDigits)) + "y = " + str(round(c2- a2*c1/a1,sigDigits))
time.sleep(waitTime)
mc.postToChat(line2y)
equationBYC(b2-a2*b1/a1, c2-a2*c1/a1, 0,5)

line2y = "y = " + str(round((c2 - a2*c1/a1)/(b2 - a2*b1/a1),sigDigits))
ySolution = (c2 - a2*c1/a1)/(b2 - a2*b1/a1)
time.sleep(waitTime)
mc.postToChat(line2y)
equationBYC(1, ySolution,0,5)

#plug y back in to equation 1
mc.postToChat("Plug it back in to equation 1 for y")

line1x = "x = " + str(round(c1/a1,sigDigits))  + " - " + str(round(b1/a1,sigDigits)) + "(" + str(round(ySolution,sigDigits)) + ")"
time.sleep(waitTime)
mc.postToChat(line1x)

mc.postToChat("Solve for x")

line1x = "x = " + str(round(c1/a1,sigDigits))  + " - " + str(round(b1/a1*ySolution,sigDigits))
time.sleep(waitTime)
mc.postToChat(line1x)

xSolution = c1/a1 - b1/a1*ySolution
line1x = "x = " + str(round(xSolution,sigDigits))
time.sleep(waitTime)
mc.postToChat(line1x)


solution = "(" + str(round(xSolution,sigDigits)) + ", " + str(round(ySolution,sigDigits)) + ")"
time.sleep(waitTime)
mc.postToChat(solution)
mc.setBlock(xSolution, 3, ySolution, block.GOLD_BLOCK.id) 
