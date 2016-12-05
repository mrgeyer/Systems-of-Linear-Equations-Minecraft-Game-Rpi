import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random

repeat = 2
waitTime = 9
height = 4
gameMin = -20
gameMax = 20
coeffMin = -9
coeffMax = 9

mc = minecraft.Minecraft.create()

#set Solution
xS = random.randint(gameMin,gameMax)
yS = random.randint(gameMin,gameMax)

#first line
#x coeff
a1 = random.randint(coeffMin,coeffMax)
#y coeff
b1 = random.randint(coeffMin,coeffMax)
if a1 == b1:
    b1 = random.randint(coeffMin,coeffMax)
#constant
c1 = a1*xS + b1*yS

#2nd line
#x coeff
a2 = random.randint(coeffMin,coeffMax)
if a1 == a2:
    a2 = random.randint(coeffMin,coeffMax)
#y coeff
b2 = random.randint(coeffMin,coeffMax)
if a2 == b2:
    b2 = random.randint(coeffMin,coeffMax)
if b1 == b2:
    b2 = random.randint(coeffMin,coeffMax)

    
#constant
c2 = a2*xS + b2*yS

# Graph Paper
mc.setBlocks(gameMin,1,gameMin, gameMax,height+1,gameMax, block.AIR.id)
mc.setBlocks(gameMin-1,0,gameMin-1, gameMax,0,gameMax, block.WOOL.id, 0)
mc.setBlocks(gameMin,height,gameMin, gameMax,height,gameMax, block.WOOL.id, 0)
for xi in range(gameMin,gameMax):
    for yi in range(gameMin, gameMax):
        if xi % 2 == 0:
            if yi % 2 == 0:
                mc.setBlocks(xi, 1, yi, xi,height,yi, block.WOOL.id, 0)
        if xi % 2 == 1:
            if yi % 2 == 1:
                mc.setBlock(xi,height,yi, block.AIR.id)

# axis
mc.setBlocks(gameMin,0,0, gameMax,0,0, block.WOOL.id, 15)
mc.setBlocks(0,0,gameMin, 0,0,gameMax, block.WOOL.id, 15)


mc = minecraft.Minecraft.create()
mc.setBlock(xS, random.randint(1,height-1), yS, block.GOLD_BLOCK.id)

mc.player.setPos(gameMin-1,1,gameMin-1)
line1 = str(a1) + "x + " + str(b1) + "y = " + str(c1)
line2 = str(a2) + "x + " + str(b2) + "y = " + str(c2)
mc.postToChat("Write this down quick!")


mc.postToChat(str(line1))
mc.postToChat(str(line2))
time.sleep(waitTime)
mc.postToChat(str(line1))
mc.postToChat(str(line2))
time.sleep(waitTime)
mc.postToChat(str(line1))
mc.postToChat(str(line2))