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
zS = random.randint(gameMin,gameMax)

#first line
#x coeff
a1 = random.randint(coeffMin,coeffMax)
#y coeff
b1 = random.randint(coeffMin,coeffMax)
if a1 == b1:
    b1 = random.randint(coeffMin,coeffMax)
c1 = random.randint(coeffMin,coeffMax)
if c1 == a1 or c1 == b1:
    c1 = random.randint(coeffMin,coeffMax)
#constant
d1 = a1*xS + b1*yS + c1*zS

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
c2 = random.randint(coeffMin,coeffMax)
if c2 == b2 or c2 == a2:
    c2 = random.randint(coeffMin,coeffMax)
if c1 == c2:
    c2 = random.randint(coeffMin,coeffMax)
#constant
d2 = a2*xS + b2*yS + c2*zS

#3rd line
#x coeff
a3 = random.randint(coeffMin,coeffMax)
if a1 == a3 or a2 == a3:
    a3 = random.randint(coeffMin,coeffMax)
#y coeff
b3 = random.randint(coeffMin,coeffMax)
if a3 == b3:
    b3 = random.randint(coeffMin,coeffMax)
if b3 == b1 or b3 == b2:
    b3 = random.randint(coeffMin,coeffMax)
c3 = random.randint(coeffMin,coeffMax)
if c3 == b3 or c3 == a3:
    c3 = random.randint(coeffMin,coeffMax)
if c3 == c1 or c3 == c2:
    c3 = random.randint(coeffMin,coeffMax)
#constant
d3 = a3*xS + b3*yS + c3*zS


# Maze
#air
mc.setBlocks(gameMin-2,gameMin-2,gameMin-2, gameMax+2,gameMax+2,gameMax+2, block.AIR.id)
#glowstone
mc.setBlocks(gameMin-2,gameMin-2,gameMin-2, gameMax+2,gameMax+2,gameMin-2, 89)  
mc.setBlocks(gameMin-2,gameMin-2,gameMin-2, gameMin-2,gameMax+2,gameMax+2, 89) 
mc.setBlocks(gameMax+2,gameMin-2,gameMin-2, gameMax+2,gameMax+2,gameMax+2, 89)  
mc.setBlocks(gameMin-2,gameMin-2,gameMax+2, gameMax+2,gameMax+2,gameMax+2, 89) 

for i in range(gameMin,gameMax):
  if i%height == 0:
    if i == 0:
      mc.setBlocks(gameMin,i,gameMin, gameMax,i,gameMax, block.WOOL.id, 10)
    elif i < 0:
      mc.setBlocks(gameMin,i,gameMin, gameMax,i,gameMax, block.WOOL.id, 14)
    elif i > 0:
      mc.setBlocks(gameMin,i,gameMin, gameMax,i,gameMax, block.WOOL.id, 3)
      

for xi in range(gameMin,gameMax):
    for yi in range(gameMin, gameMax):
        if xi % 2 == 0:
            if yi % 2 == 0:
                if xi == 0 or yi == 0:
                  mc.setBlocks(xi, gameMin, yi, xi, gameMax, yi, block.WOOL.id, 10)
                elif xi < 0:
                  if yi < 0:
                   mc.setBlocks(xi, gameMin, yi, xi, gameMax, yi, block.WOOL.id, 14)
                  elif yi > 0:
                   mc.setBlocks(xi, gameMin, yi, xi, gameMax, yi, block.WOOL.id, 1)
                
                elif xi > 0:
                  if yi < 0:
                    mc.setBlocks(xi, gameMin, yi, xi, gameMax, yi, block.WOOL.id, 9)
                  elif yi > 0:
                    mc.setBlocks(xi, gameMin, yi, xi, gameMax, yi, block.WOOL.id, 13)

        '''if xi % 2 == 1:
            if yi % 2 == 1:
                mc.setBlock(xi,height,yi, block.AIR.id)'''
#stairs
for yi in range(gameMin-1, gameMax+2):
  if yi > 0:
      color = 3
  elif yi == 0:
      color = 10
  elif yi < 0:
      color = 14
  mc.setBlock(yi,yi,gameMin-1, block.WOOL.id, color)
  mc.setBlock(yi,yi,gameMax+1, block.WOOL.id, color)
  mc.setBlock(gameMax+1,yi,yi, block.WOOL.id, color)
  mc.setBlock(gameMin-1,yi,yi, block.WOOL.id, color)

# axis
mc.setBlocks(gameMin,0,0, gameMax,0,0, block.WOOL.id, 10)
mc.setBlocks(0,0,gameMin, 0,0,gameMax, block.WOOL.id, 10)
mc.setBlocks(0,gameMin,0, 0,gameMax,0, block.WOOL.id, 10)

#GoldBlock
mc.setBlock(xS, yS, zS, block.GOLD_BLOCK.id)

#Equations
mc.player.setPos(random.randint(gameMin,gameMax),gameMax+2,random.randint(gameMin,gameMax))
line1 = str(a1) + "x + " + str(b1) + "y + " + str(c1) + "z = " + str(d1)
line2 = str(a2) + "x + " + str(b2) + "y + " + str(c2) + "z = " + str(d2)
line3 = str(a3) + "x + " + str(b3) + "y + " + str(c3) + "z = " + str(d3)
mc.postToChat("Write this down quick!")

#Post equations
mc.postToChat(str(line1))
mc.postToChat(str(line2))
mc.postToChat(str(line3))
time.sleep(waitTime)
mc.postToChat(str(line1))
mc.postToChat(str(line2))
mc.postToChat(str(line3))
time.sleep(waitTime)
mc.postToChat(str(line1))
mc.postToChat(str(line2))
mc.postToChat(str(line3))