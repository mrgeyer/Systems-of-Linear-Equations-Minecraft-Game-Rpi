#import minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from fractions import gcd

mc = minecraft.Minecraft.create()
waitTime = 9
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

#first line
#x coeff
a1 = random.randint(1,5)
#y coeff
b1 = random.randint(-5,a1-1)
#constant
c1 = random.randint(-15,13)

#uses rule from Bezout's Identity to make sure it displays
makeSureDisplays = c1 % gcd(a1,b1)
while makeSureDisplays > 0:
    c1 = random.randint(-15,13)
    makeSureDisplays = c1 % gcd(a1,b1)
    
#2nd line
#x coeff
a2 = random.randint(-5,a1-1)
#y coeff
b2 = random.randint(b1+1,5)
#constant
c2 = random.randint(c1+1,15)
makeSureDisplays = c2 % gcd(a2,b2)
while makeSureDisplays > 0:
    c2 = random.randint(c1+1,15)
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

def divsign(x,y,z):
    mc.setBlocks(x,y,z,x,y+2,z, bah, 15)
    mc.setBlocks(x+1,y+3,z,x+1,y+5,z, bah, 15)

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

# (ax + by = c)
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

#Line 1
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if (xi*a1 + yi*b1 == c1):
                mc.setBlock(xi,1,yi, block.WOOL.id, 1)

line1 = str(a1) + "x + " + str(b1) + "y = " + str(c1)
equationAXBYC(a1,b1,c1,17,1,posp)
                
mc.postToChat(line1)

#Line 2 
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if (xi*a2 + yi*b2 == c2):
                mc.setBlock(xi,2,yi, block.WOOL.id, 5)
equationAXBYC(a2,b2,c2,11,5,posp)
line2 = str(a2) + "x + " + str(b2) + "y = " + str(c2)

mc.postToChat(line2)

time.sleep(waitTime)

#multiply row2 by -a1/a2
m = -a1/a2
step1 = "multiply equation2 by -" + str(a1) + "/" + str(a2)
mc.postToChat(step1)
ma2 = m*a2
mb2 = m*b2
mc2 = m*c2
newline2b = "[" + line2 + "] * " + str(round(m,2))
equationMAXBYC(a2,b2,c2,0-a1/a2,11,5,posp)


mc.postToChat(newline2b)
newline2 = str(round(ma2,2)) + "x + " + str(round(mb2,2)) + "y = " + str(round(mc2,2))
time.sleep(waitTime)
equationAXBYC(ma2,mb2,mc2,11,5,posp)
mc.postToChat(newline2)

time.sleep(waitTime)
mc.postToChat("Add new equation to first equation")

line1n = "      " + str(round(a1,2)) + "x +   " + str(round(b1,2)) + "y =   " + str(round(c1,2))
mc.postToChat(line1n)
addnewline = "+ " + newline2
mc.postToChat(addnewline)
mc.postToChat("______________________________")

#add new row2 to row1
sa = ma2 + a1
sb = mb2 + b1
sc = mc2 + c1
sumline =  "   " + str(round(sa,2)) + "x + " + str(round(sb,2)) + "y = " + str(round(sc,2))

#clear(10,posp)
equationAXBYC(sa,sb,sc,4,yellow,posp)

mc.postToChat(sumline)
time.sleep(waitTime)
equationBYC(sb,sc,4,yellow,posp)

#solve for y
mc.postToChat("Solve for y")
solveForYstep1 =  "y = " + str(round(sc,2)) + "/" + str(round(sb,2))
equationYCdB(sb,sc,4,yellow,posp)

mc.postToChat(solveForYstep1)
time.sleep(waitTime)
ySolution = sc/sb
solveForYstep2 =  "y = " + str(round(ySolution,2))
equationBYC(0,ySolution,4,yellow,posp)
mc.postToChat(solveForYstep2)
time.sleep(waitTime)

#Plug y back in to first equation
mc.postToChat("Plug y back in to first equation")
solveForXstep1 = str(round(a1,2)) + "x + " + str(round(b1,2)) + "*" + str(round(ySolution,2)) + " = " + str(round(c1,2))
equationAXByC(a1,b1,c1,ySolution,17,1,posp)
mc.postToChat(solveForXstep1)
time.sleep(waitTime)
mc.postToChat("Solve for x")

#solve for x
xSolution = (c1 - ySolution*b1)/a1
solveForXstep2 = str(round(a1,2)) + "x + " + str(round(b1 * ySolution,2)) + " = " + str(round(c1,2))
equationAXByC(a1,0,c1,ySolution*b1,17,1,posp)
mc.postToChat(solveForXstep2)

solveForXstep3 = str(round(a1,2)) + "x = " + str(round(c1,2)) + " - " + str(round(b1 * ySolution,2))
time.sleep(waitTime)
equationAXCB(a1,0-ySolution*b1,c1,17,1,posp)
mc.postToChat(solveForXstep3)

solveForXstep4 = str(round(a1,2)) + "x = " + str(round(c1-ySolution*b1,2))
time.sleep(waitTime)
equationAXC(a1,c1-ySolution*b1,17,1,posp)
mc.postToChat(solveForXstep4)

solveForXstep5 = "x = " + str(round(xSolution))
time.sleep(waitTime)
equationAXC(0,xSolution,17,1,posp)
mc.postToChat(solveForXstep5)

#solution
solution = "(" + str(round(xSolution,2)) + ", " + str(round(ySolution,2)) + ")"
time.sleep(waitTime)
mc.postToChat(solution)
mc.setBlock(xSolution, 3, ySolution, block.GOLD_BLOCK.id) 
