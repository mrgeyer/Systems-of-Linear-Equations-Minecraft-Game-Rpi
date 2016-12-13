#import minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from fractions import gcd

mc = minecraft.Minecraft.create()
sigDigits = 3
waitTime = 8.46651
graphMin =-50
graphMax = 50
bah= block.WOOL.id 
posp = mc.player.getPos()

#wool colors
white = 0
lightGrey = 8
grey = 7
black = 15
pink = 6
red = 14
yellow = 4
orange = 1
lime = 5
lightBlue = 3
blue = 11
cyan = 9
purple = 10
magenta = 2
brown = 12

xSolution = random.randint(-9,9)
ySolution = random.randint(-9,9)

if xSolution == 0:
    yIntercept1 = ySolution
    yIntercept2 = ySolution
else:
  if ySolution > 2:
    yIntercept1 = random.randint(2,ySolution-1)
    yIntercept2 = random.randint(0,yIntercept1-1)
  else:
    yIntercept1 = random.randint(ySolution+1,3)
    yIntercept2 = random.randint(yIntercept1+1,5)
    
d1 = gcd(ySolution-yIntercept1, xSolution)
#slopenumerator
if d1 != 0:
  mn1 = (ySolution - yIntercept1)/d1
else:
  mn1 = ySolution - yIntercept1
#slopedenominator
if d1 != 0:
  md1 = xSolution/d1
else:
   md1 = xSolution
m1 = mn1/md1

d2 = gcd(ySolution-yIntercept2, xSolution)
#slopenumerator
if d2 != 0:
  mn2 = (ySolution - yIntercept2)/d2
else:
    mn2 = (ySolution - yIntercept2)
#slopedenominator
if d2 != 0:
 md2 = xSolution/d2
else:
    md2 = xSolution
m2 = mn2/md2

# y = m1*x + yIntercept1
# mn1/md1*x - y = -yIntercept1
# mn1*x - md1*y = -yIntercept
d1b = gcd(mn1, gcd(md1, yIntercept1))
d2b = gcd(mn2, gcd(md2, yIntercept2))

#first line
#x coeff
a1 = mn1/d1b
#y coeff
b1 = 0 - md1/d1b
#constant
c1 = 0 - yIntercept1*md1/d1b

#first line
#x coeff
a2 = mn2/d2b
#y coeff
b2 = 0 - md2/d2b
#constant
c2 = 0 - yIntercept2*md2/d2b
    


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
    mc.setBlocks(x+1,y,z,x+1,y+1,z, bah, color)
    mc.setBlocks(x+2,y+2,z,x+2,y+3,z, bah, color)
    mc.setBlocks(x,y+2,z,x+1,y+2,z, bah, color)
    mc.setBlock(x,y+3,z, bah, color)

def equalsign(x,y,z):
    mc.setBlocks(x,y+1,z,x+3,y+1,z, bah, 15)
    mc.setBlocks(x,y+3,z,x+3,y+3,z, bah, 15)

def plussign(x,y,z):
    mc.setBlocks(x,y+2,z,x+2,y+2,z, bah, 15)
    mc.setBlocks(x+1,y+1,z,x+1,y+3,z, bah, 15)

def divsign(x,y,z):
    mc.setBlocks(x,y,z,x,y+2,z, bah, 15)
    mc.setBlocks(x+1,y+3,z,x+1,y+4,z, bah, 15)

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

#Open Brackets
def braC(x,y,z):
    mc.setBlock(x+1,y,z, bah, 15)
    mc.setBlock(x+1,y+4,z, bah, 15)
    mc.setBlocks(x,y,z,x,y+4,z,bah,15)

#Close Brackets   
def braD(x,y,z):
    mc.setBlock(x,y,z, bah, 15)
    mc.setBlock(x,y+4,z, bah, 15)
    mc.setBlocks(x+1,y,z,x+1,y+4,z,bah,15)

def clear(h,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    
# ax + by = c
def equationAXBYC(a,b,c,h,color,pos):
    #pos = mc.player.getPos()
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

# (ax + by = c)m
def equationMAXBYC(a,b,c,m,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    braC(pos.x-22,pos.y+h,pos.z-dBack)
    numberBlocks(a,pos.x-19,pos.y+h,pos.z-dBack)
    xblock(pos.x-17,pos.y+h,pos.z-dBack,color)
    plussign(pos.x-12,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    braD(pos.x+13,pos.y+h,pos.z-dBack)
    numberBlocks(m,pos.x+16,pos.y+h,pos.z-dBack)

# ax + b(y) = c
def equationAXByC(a,b,c,y,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)

    numberBlocks(a,pos.x-28,pos.y+h,pos.z-dBack)
    xblock(pos.x-26,pos.y+h,pos.z-dBack,color)

    plussign(pos.x-20,pos.y+h,pos.z-dBack)

    numberBlocks(b,pos.x-15,pos.y+h,pos.z-dBack)
    parenC(pos.x-13,pos.y+h,pos.z-dBack)
    numberBlocks(y,pos.x-10,pos.y+h,pos.z-dBack)
    parenD(pos.x-3,pos.y+h,pos.z-dBack)
    
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)

# ax = c + by
def equationAXCBY(a,b,c,h,color,pos):
    #pos = mc.player.getPos()
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


# by = c + ax
def equationBYECAX(a,b,c,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(b,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    numberBlocks(a,pos.x+17,pos.y+h,pos.z-dBack)
    xblock(pos.x+19,pos.y+h,pos.z-dBack,color)

    # y = b + (m/n)x
def equationBMX(b,m,n,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)

    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    parenC(pos.x+17,pos.y+h,pos.z-dBack)
    numberBlocks(m,pos.x+21,pos.y+h,pos.z-dBack)
    divsign(pos.x+23,pos.y+h,pos.z-dBack)
    numberBlocks(n,pos.x+25,pos.y+h,pos.z-dBack)
    parenD(pos.x+27,pos.y+h,pos.z-dBack)
    xblock(pos.x+29,pos.y+h,pos.z-dBack,color)

# a(c+by) + by = c
def equationAcbyBYC(a,b1,c1,b2,c2,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(a,pos.x-41,pos.y+h,pos.z-dBack)
    #Openparentheses
    parenC(pos.x-39,pos.y+h,pos.z-dBack)
    numberBlocks(c1,pos.x-34,pos.y+h,pos.z-dBack)
    plussign(pos.x-27,pos.y+h,pos.z-dBack)
    numberBlocks(b1,pos.x-22,pos.y+h,pos.z-dBack)
    yblock(pos.x-20,pos.y+h,pos.z-dBack,color)
    parenD(pos.x-15,pos.y+h,pos.z-dBack)
    #closeParentheses
    plussign(pos.x-12,pos.y+h,pos.z-dBack)
    numberBlocks(b2,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)

# x = c + b(y)
def equationXCBY(b,c,y,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    xblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x+17,pos.y+h,pos.z-dBack)
    parenC(pos.x+19,pos.y+h,pos.z-dBack)
    numberBlocks(y,pos.x+21,pos.y+h,pos.z-dBack)
    parenD(pos.x+28,pos.y+h,pos.z-dBack)


# ax = c + b
def equationAXCB(a,b,c,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(a,pos.x-7,pos.y+h,pos.z-dBack)
    xblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x+17,pos.y+h,pos.z-dBack)

# ax = c
def equationAXC(a,c,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 49
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(a,pos.x-7,pos.y+h,pos.z-dBack)
    xblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)

# c+ by = c2
def equationCBYC(b,c1,c2,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(c1,pos.x-19,pos.y+h,pos.z-dBack)
    plussign(pos.x-12,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)

#by = c + c
def equationBYCC(b,c1,c2,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(b,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c2,pos.x+5,pos.y+h,pos.z-dBack)
    plussign(pos.x+12,pos.y+h,pos.z-dBack)
    numberBlocks(c1,pos.x+17,pos.y+h,pos.z-dBack)

#by = c
def equationBYC(b,c,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    numberBlocks(b,pos.x-7,pos.y+h,pos.z-dBack)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)

#y = c(b)
def equationYCb(b,c,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    parenC(pos.x+8,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x+11,pos.y+h,pos.z-dBack)
    parenD(pos.x+13,pos.y+h,pos.z-dBack)

#y = c/b
def equationYCdB(b,c,h,color,pos):
    #pos = mc.player.getPos()
    leftMargin = 50
    dBack = 20
    mc.setBlocks(pos.x-leftMargin,pos.y+h,pos.z-dBack, pos.x+leftMargin,pos.y+h+5,pos.z-dBack, block.AIR.id)
    yblock(pos.x-5,pos.y+h,pos.z-dBack,color)
    equalsign(pos.x,pos.y+h,pos.z-dBack)
    numberBlocks(c,pos.x+5,pos.y+h,pos.z-dBack)
    divsign(pos.x+13,pos.y+h,pos.z-dBack)
    numberBlocks(b,pos.x+16,pos.y+h,pos.z-dBack)

# Graph Paper
mc.setBlocks(graphMin,1,graphMin, graphMax,125,graphMax, block.AIR.id)
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

line1 = str(a1) + "x + " + str(b1) + "y = " + str(c1)
equationAXBYC(a1,b1,c1,11,1,posp)
                
# quadrants
#Q1
mc.setBlocks(2,0,2, 4,0,2, bah, cyan)
#Q2
mc.setBlocks(2,0,-2, 4,0,-2, bah, magenta)
mc.setBlocks(2,0,-4, 4,0,-4, bah, magenta)
#Q3
mc.setBlocks(-2,0,-2, -4,0,-2, bah, pink)
mc.setBlocks(-2,0,-4, -4,0,-4, bah, pink)
mc.setBlocks(-2,0,-6, -4,0,-6, bah, pink)
#Q4
mc.setBlocks(-2,0,2, -4,0,2, bah, magenta)
mc.setBlock(-2,0,4, bah, magenta)
mc.setBlock(-3,0,5, bah, magenta)
mc.setBlock(-4,0,6, bah, magenta)
mc.setBlock(-3,0,7, bah, magenta)
mc.setBlock(-2,0,8, bah, magenta)


equationAXBYC(a2,b2,c2,4,5,posp)
line2 = str(a2) + "x + " + str(b2) + "y = " + str(c2)
mc.postToChat(line1)
mc.postToChat(line2)
time.sleep(waitTime)
time.sleep(waitTime)
mc.postToChat(line1)
mc.postToChat(line2)
time.sleep(waitTime)


#convert to slope intercept form
mc.postToChat("We need to convert to slope intercept form")
time.sleep(waitTime)

#equation1
mc.postToChat("Solve equation1 for y")
mc.postToChat(line1)
time.sleep(waitTime)

step = "Subtract " + str(a1) + "x from both sides"
mc.postToChat(step)
time.sleep(waitTime)

newline1 = str(b1) + "y = " + str(c1) + " - " + str(a1) + "x" 
equationBYECAX(0-a1,b1,c1,11,1,posp)
mc.postToChat(newline1)
time.sleep(waitTime)

if a1 < 0:
  newline1 = str(b1) + "y = " + str(c1) + " + " + str(0-a1) + "x" 
  mc.postToChat(newline1)
  time.sleep(waitTime)

step = "Divide both sides by " + str(b1)
mc.postToChat(step)
time.sleep(waitTime)

newline1 = str(b1) + "y/" + str(b1) + " = " + str(c1) + "/"  + str(b1) + " + " + str(0-a1) + "x/"  + str(b1)    
mc.postToChat(newline1)
time.sleep(waitTime)

dab1 = gcd(a1,b1)
newline1 = "y = " + str(round(c1/b1,sigDigits)) + " + (" + str(0-a1/dab1) + "/" + str(b1/dab1) + ")x"
#equationBYECAX(0-a1/b1,0,c1/b1,11,1,posp)
equationBMX(c1/b1,mn1,md1,11,1,posp)
mc.postToChat(newline1)
time.sleep(waitTime)

#equation2
mc.postToChat("Solve equation2 for y")
mc.postToChat(line2)
time.sleep(waitTime)

step = "Subtract " + str(a2) + "x from both sides"
mc.postToChat(step)
time.sleep(waitTime)

newline2 = str(b2) + "y = " + str(c2) + " - " + str(a2) + "x" 
equationBYECAX(0-a2,b2,c2,4,5,posp)
mc.postToChat(newline2)
time.sleep(waitTime)

if a2 < 0:
  newline2 = str(b2) + "y = " + str(c2) + " + " + str(0-a2) + "x" 
  mc.postToChat(newline2)
  time.sleep(waitTime)


step = "Divide both sides by " + str(b2)
mc.postToChat(step)
time.sleep(waitTime)

newline2 = str(b2) + "y/" + str(b2) + " = " + str(c2) + "/"  + str(b2) + " + " + str(0-a2) + "x/"  + str(b2)    
mc.postToChat(newline2)
time.sleep(waitTime)

dab2 = gcd(a2,b2)
newline2 = "y = " + str(round(c2/b2,sigDigits)) + " + (" + str(0-a2/dab2) + "/" + str(b2/dab2) + ")x"
#equationBYECAX(0-a2/b2,0,c2/b2,4,5,posp)
equationBMX(c2/b2,mn2,md2,4,5,posp)
mc.postToChat(newline2)
time.sleep(waitTime)

#graph it
msg = "Now let's graph " + newline1
mc.postToChat(msg)
time.sleep(waitTime)

msg = "Go to the y-intercept (0, " + str(c1/b1) + ")"
mc.postToChat(msg)
mc.setBlock(c1/b1,1,0, bah, 1)
mc.player.setPos(c1/b1,2,0)
time.sleep(waitTime)

if (m1<0):
  msg = "Go down " + str(abs(a1/dab1))
else:
  msg = "Go up " + str(abs(a1/dab1))
msg = msg + " and over " + str(abs(b1/dab1))
mc.postToChat(msg)
mc.setBlock(c1/b1-a1/dab1,1,b1/dab1, bah, 1)
#mc.player.setPos(c1/b1-a1/dab1,2,b1/dab1)
time.sleep(waitTime)

msg = "Now draw the line"
mc.postToChat(msg)
#Line 1
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if (xi*b1 + yi*a1 == c1):
                mc.setBlock(xi,1,yi, block.WOOL.id, 1)
time.sleep(waitTime)

msg = "Now let's graph " + newline2
mc.postToChat(msg)
time.sleep(waitTime)

msg = "Go to the y-intercept (0, " + str(c2/b2) + ")"
mc.postToChat(msg)
mc.setBlock(c2/b2,2,0, bah, 5)
mc.player.setPos(c2/b2,3,0)
time.sleep(waitTime)

if (m2 <0):
  msg = "Go down " + str(abs(a2/dab2))
else:
  msg = "Go up " + str(abs(a2/dab2))
msg = msg + " and over " + str(abs(b2/dab2))
mc.postToChat(msg)
mc.setBlock(c2/b2-a2/dab2,2,b2/dab2, bah, 5)
#mc.player.setPos(c2/b2-a2/dab2,3,b2/dab2)
time.sleep(waitTime)

msg = "Now draw the line"
mc.postToChat(msg)
#Line 2 
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if (xi*b2 + yi*a2 == c2):
                mc.setBlock(xi,2,yi, block.WOOL.id, 5)
time.sleep(waitTime)
msg = "Do you see the intersection?"
mc.postToChat(msg)
time.sleep(waitTime)

#solution
solution = "(" + str(round(xSolution,2)) + ", " + str(round(ySolution,2)) + ")"
time.sleep(waitTime)
mc.postToChat(solution)
mc.setBlock(ySolution, 3, xSolution, block.GOLD_BLOCK.id) 
