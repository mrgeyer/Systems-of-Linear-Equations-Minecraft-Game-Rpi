import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
waitTime = 1

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

#multiply row2 by -a1/a2
m = -a1/a2
step1 = "multiply equation2 by " + str(m)
time.sleep(waitTime)
mc.postToChat(step1)
ma2 = m*a2
mb2 = m*b2
mc2 = m*c2
newline2b = "[" + line2 + "] * " + str(m)
time.slep(waitTime)
mc.postToChat(newline2b)
newline2 = str(ma2) + "x + " + str(mb2) + "y = " + str(mc2)
time.sleep(waitTime)
mc.postToChat(newline)

time.sleep(waitTime)
mc.postToChat("Add new equation to first equation")
mc.postToChat(line1)
addnewline = "+ " + newLine
mc.postToChat(addnewline)
mc.postToChat("______________________________")

#add new row2 to row1
sa = ma2 + a1
sb = mb2 + b1
sc = mc2 + c1
sumline =  str(sa) + "x + " + str(sb) + "y = " + str(sc)
time.sleep(waitTime)
mc.postToChat("Solve for y")
#solve for y
solveForYstep1 =  "y = " + str(sc) + "/" + str(sb)
mc.postToChat(solveForYstep1)
time.sleep(waitTime)
ySolution = sc/sb
solveForYstep2 =  "y = " + str(ySolution)
mc.postToChat(solveForYstep2)
time.sleep(waitTime)

#Plug y back in to first equation
mc.postToChat("Plug y back in to first equation")
solveForXstep1 = str(a1) + "x + " + str(b1) + "*" + str(ySolution) + " = " + str(c1)
mc.postToChat(solveForXstep1)
time.sleep(waitTime)
mc.postToChat("Solve for x")

#solve for x
xSolution = (c1 - ySolution*b1)/a1
solveForXstep2 = str(a1) + "x + " + str(b1 * ySolution) + " = " + str(c1)
mc.postToChat(solveForXstep2)
solveForXstep3 = str(a1) + "x = " + str(c1) + " - " + str(b1 * ySolution)
mc.postToChat(solveForXstep3)
solveForXstep4 = str(a1) + "x = " + str(xSolution)
mc.postToChat(solveForXstep4)

solution = "(" + str(xSolution) + ", " + ySolution + ")"
mc.postToChat(solution)
mc.setBlock(xSolution, 0, ySolution, block.GOLD_BLOCK.id) 
