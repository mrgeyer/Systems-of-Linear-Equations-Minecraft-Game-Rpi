#import minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from fractions import gcd

mc = minecraft.Minecraft.create()
waitTime = 9

#first line
#x coeff
a1 = random.randint(1,9)
#y coeff
b1 = random.randint(-9,7)
#constant
c1 = random.randint(-25,23)

#uses rule from Bezout's Identity to make sure it displays
makeSureDisplays = c1 % gcd(a1,b1)
while makeSureDisplays > 0:
    c1 = random.randint(-25,23)
    makeSureDisplays = c1 % gcd(a1,b1)
    
#2nd line
#x coeff
a2 = random.randint(-9,a1-1)
#y coeff
b2 = random.randint(b1+1,9)
#constant
c2 = random.randint(c1+1,25)
makeSureDisplays = c2 % gcd(a2,b2)
while makeSureDisplays > 0:
    c2 = random.randint(c1+1,25)
    makeSureDisplays = c2 % gcd(a2,b2)

line1 = str(a1) + "x + " + str(b1) + "y = " + str(c1)
line2 = str(a2) + "x + " + str(b2) + "y = " + str(c2)

# Graph Paper
mc.setBlocks(-101,1,-101, 101,101,101, block.AIR.id)
mc.setBlocks(-101,0,-101, 101,0,101, block.WOOL.id, 0)
for xi in range(-101,101):
    for yi in range(-101,101):
        if xi % 2 == 0:
            if yi % 2 == 0:
                mc.setBlock(xi,0,yi, block.WOOL.id, 8)
        if xi % 2 == 1:
            if yi % 2 == 1:
                mc.setBlock(xi,0,yi, block.WOOL.id, 8)

# axis
mc.setBlocks(-101,0,   0, 101,0,  0, block.WOOL.id, 15)
mc.setBlocks(   0,0,-101,   0,0,101, block.WOOL.id, 15)

#Line 1
for xi in range(-101,101):
    for yi in range(-101,101):
        if (xi*a1 + yi*b1 == c1):
                mc.setBlock(xi,1,yi, block.WOOL.id, 11)
mc.postToChat(line1)

#Line 2                
for xi in range(-101,101):
    for yi in range(-101,101):
        if (xi*a2 + yi*b2 == c2):
                mc.setBlock(xi,2,yi, block.WOOL.id, 14)
mc.postToChat(line2)

time.sleep(waitTime*3)

#multiply row2 by -a1/a2
m = -a1/a2
step1 = "multiply equation2 by -" + str(a1) + "/" + str(a2)
mc.postToChat(step1)
ma2 = m*a2
mb2 = m*b2
mc2 = m*c2
newline2b = "[" + line2 + "] * " + str(round(m,2))

mc.postToChat(newline2b)
newline2 = str(round(ma2,2)) + "x + " + str(round(mb2,2)) + "y = " + str(round(mc2,2))
time.sleep(waitTime)
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
mc.postToChat(sumline)
time.sleep(waitTime)

#solve for y
mc.postToChat("Solve for y")
solveForYstep1 =  "y = " + str(round(sc,2)) + "/" + str(round(sb,2))
mc.postToChat(solveForYstep1)
time.sleep(waitTime)
ySolution = sc/sb
solveForYstep2 =  "y = " + str(round(ySolution,2))
mc.postToChat(solveForYstep2)
time.sleep(waitTime)

#Plug y back in to first equation
mc.postToChat("Plug y back in to first equation")
solveForXstep1 = str(round(a1,2)) + "x + " + str(round(b1,2)) + "*" + str(round(ySolution,2)) + " = " + str(round(c1,2))
mc.postToChat(solveForXstep1)
time.sleep(waitTime)
mc.postToChat("Solve for x")

#solve for x
xSolution = (c1 - ySolution*b1)/a1
solveForXstep2 = str(round(a1,2)) + "x + " + str(round(b1 * ySolution,2)) + " = " + str(round(c1,2))
mc.postToChat(solveForXstep2)
solveForXstep3 = str(round(a1,2)) + "x = " + str(round(c1,2)) + " - " + str(round(b1 * ySolution,2))
time.sleep(waitTime)
mc.postToChat(solveForXstep3)
solveForXstep4 = str(round(a1,2)) + "x = " + str(round(c1-ySolution*b1,2))
time.sleep(waitTime)
mc.postToChat(solveForXstep4)
solveForXstep5 = "x = " + str(round(xSolution))
time.sleep(waitTime)
mc.postToChat(solveForXstep4)


solution = "(" + str(round(xSolution,2)) + ", " + str(round(ySolution,2)) + ")"
time.sleep(waitTime)
mc.postToChat(solution)
mc.setBlock(xSolution, 3, ySolution, block.GOLD_BLOCK.id) 
