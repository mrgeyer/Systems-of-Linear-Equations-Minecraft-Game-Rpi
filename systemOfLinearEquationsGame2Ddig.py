import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

repeat = 4
waitTime = 9
height = 4
gameMin = -5
gameMax = 5
coeffMin = -4
coeffMax = 4

mc = minecraft.Minecraft.create()

bah= block.WOOL.id
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

#set Solution
xS = random.randint(gameMin,gameMax)
yS = random.randint(gameMin,gameMax)

#first line
#x coeff
a1 = random.randint(coeffMin,coeffMax)
#y coeff
b1 = random.randint(-2,2)
if a1 == b1:
    b1 = random.randint(-2,2)
#constant
c1 = a1*xS + b1*yS

#2nd line
#x coeff
a2 = random.randint(coeffMin,coeffMax)
if a1 == a2:
    a2 = random.randint(coeffMin,coeffMax)
#y coeff
b2 = random.randint(-2,2)
if a2 == b2:
    b2 = random.randint(-2,2)
if b1 == b2:
    b2 = random.randint(-2,2)

    
#constant
c2 = a2*xS + b2*yS
extraSpace = gameMax - gameMin
graphMin = gameMin - extraSpace
graphMax = gameMax + extraSpace
# Graph Paper
mc.setBlocks(gameMin - extraSpace,1,gameMin - extraSpace, gameMax + extraSpace,height+1,gameMax + extraSpace, block.AIR.id)
mc.setBlocks(gameMin - extraSpace-1,0,gameMin - extraSpace-1, gameMax + extraSpace,0,gameMax + extraSpace, block.WOOL.id, 0)
mc.setBlocks(gameMin - extraSpace-1,-2,gameMin - extraSpace-1, gameMax + extraSpace,-1,gameMax + extraSpace, block.DIRT.id, 0)
for xi in range(graphMin,graphMax):
    for yi in range(graphMin,graphMax):
        if xi % 2 == 0:
            if yi % 2 == 0:
                mc.setBlock(xi,0,yi, block.WOOL.id, 8)
        if xi % 2 == 1:
            if yi % 2 == 1:
                mc.setBlock(xi,0,yi, block.WOOL.id, 8)

# quadrants
#Q1
#mc.setBlocks(2,0,2, 4,0,2, bah, cyan)
#Q2
#mc.setBlocks(2,0,-2, 4,0,-2, bah, magenta)
#mc.setBlocks(2,0,-4, 4,0,-4, bah, magenta)
#Q3
#mc.setBlocks(-2,0,-2, -4,0,-2, bah, pink)
#mc.setBlocks(-2,0,-4, -4,0,-4, bah, pink)
#mc.setBlocks(-2,0,-6, -4,0,-6, bah, pink)
#Q4
#mc.setBlocks(-2,0,2, -4,0,2, bah, magenta)
#mc.setBlock(-2,0,4, bah, magenta)
#mc.setBlock(-3,0,5, bah, magenta)
#mc.setBlock(-4,0,6, bah, magenta)
#mc.setBlock(-3,0,7, bah, magenta)
#mc.setBlock(-2,0,8, bah, magenta)

# axis
mc.setBlocks(gameMin - extraSpace,0,0, gameMax + extraSpace,0,0, block.WOOL.id, 15)
mc.setBlocks(0,0,gameMin - extraSpace, 0,0,gameMax + extraSpace, block.WOOL.id, 15)


mc = minecraft.Minecraft.create()
mc.setBlock(xS,-1, yS, block.GOLD_BLOCK.id)

mc.player.setPos(0,100,0)
line1 = str(a1) + "x + " + str(b1) + "y = " + str(c1)
line2 = str(a2) + "x + " + str(b2) + "y = " + str(c2)
mc.postToChat("Write this down quick!")
answers = str(xS) + "," + str(yS)
#mc.postToChat(answers)

for i in range(repeat):
  mc.postToChat(str(line1))
  mc.postToChat(str(line2))
  time.sleep(waitTime)
