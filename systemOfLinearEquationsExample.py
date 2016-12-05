import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

mc = minecraft.Minecraft.create()
#first line
#x coeff
a1 = 5
#y coeff
b1 = 6
#constant
c1 = 22

#2nd line
#x coeff
a2 = 4
#y coeff
b2 = 7
#constant
c2 = 23

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
#Line 2                
for xi in range(-101,101):
    for yi in range(-101,101):
        if (xi*a2 + yi*b2 == c2):
                mc.setBlock(xi,2,yi, block.WOOL.id, 14)
#multiply row2 by -a1/a2
m = -a1/a2
ma2 = m*a2
mb2 = m*b2
mc2 = m*c2

#add new row2 to row1
sa = ma2 + a1
sb = mb2 + b1
sc = mc2 + c1

#solve for y
ySolution = sc/sb

#solve for x
xSolution = (c1 - ySolution*b1)/a1

mc.setBlock(xSolution, 0, ySolution, block.GOLD_BLOCK.id)


notFound = 1
while notFound == 1:
  playerTile = mc.player.getTilePos()
  if playerTile.x < xSolution + 2 and playlerTile.z < ySolution + 2:
     if playerTile.x > xSolution - 2 and playlerTile.z < ySolution - 2:
       notFound = 0
       mc.postToChat("You found it! (", str(xSolution), ", ", str(ySolution), ")")
  
