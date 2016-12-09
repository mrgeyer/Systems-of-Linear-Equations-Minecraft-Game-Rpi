#import minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from fractions import gcd

mc = minecraft.Minecraft.create()
waitTime = 9
sigDigits = 3

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

#solve equation1 for x
mc.postToChat("Solve equation1 for x")

line1x = str(a1) + "x = " + str(c1) + " - " + str(b1) + "y"
time.sleep(waitTime)
mc.postToChat(line1x)

line1x = "x = " + str(c1) + "/" + str(a1) + " - " + str(b1) + "y/" + str(a1)
time.sleep(waitTime)
mc.postToChat(line1x)

line1x = "x = " + str(round(c1/a1,sigDigits))  + " - " + str(round(b1/a1,sigDigits)) + "y" 
time.sleep(waitTime)
mc.postToChat(line1x)


#plug it into equation 2 for x
time.sleep(waitTime)
mc.postToChat("Plug it into equation 2 for x")
line2y = str(a2) + "(" + str(round(c1/a1,sigDigits))  + " - " + str(round(b1/a1,sigDigits)) + ")y + " + str(b2) + "y = " + str(c2)
time.sleep(waitTime)
mc.postToChat(line2y)

#solve equation2  for y
mc.postToChat("Solve equation2 for y")

mc.postToChat("Distribute")
line2y = str(a2) + "(" + str(round(c1/a1,sigDigits))  + ") - " + str(a2) + "(" + str(round(b1/a1,sigDigits)) + "y) + " + str(b2) + "y = " + str(c2)
time.sleep(waitTime)
mc.postToChat(line2y)

line2y = str(round(a2*c1/a1,2))  + " - (" + str(round(a2*b1/a1,sigDigits)) + ")y + " + str(b2) + "y = " + str(c2)
time.sleep(waitTime)
mc.postToChat(line2y)
              
mc.postToChat("Combine like terms")

line2y = str(round(a2*c1/a1,sigDigits))  + " + " + str(round(b2 - a2*b1/a1,sigDigits)) + ")y = " + str(c2)
time.sleep(waitTime)
mc.postToChat(line2y)

line2y = str(round(b2 - a2*b1/a1,sigDigits)) + ")y = " + str(c2) + " - " + str(round(a2*c1/a1,sigDigits))
time.sleep(waitTime)
mc.postToChat(line2y)

line2y =str(round(b2 - a2*b1/a1,sigDigits)) + ")y = " + str(round(c2- a2*c1/a1,sigDigits))
time.sleep(waitTime)
mc.postToChat(line2y)

line2y = "y = " + str(round((c2 - a2*c1/a1)/(b2 - a2*b1/a1),sigDigits))
ySolution = (c2 - a2*c1/a1)/(b2 - a2*b1/a1)
time.sleep(waitTime)
mc.postToChat(line2y)



solution = "(" + str(round(xSolution,sigDigits)) + ", " + str(round(ySolution,sigDigits)) + ")"
time.sleep(waitTime)
mc.postToChat(solution)
mc.setBlock(xSolution, 3, ySolution, block.GOLD_BLOCK.id) 
