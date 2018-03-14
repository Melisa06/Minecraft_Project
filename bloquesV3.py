from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()

while True:
    mc.setBlock(pos.x+3, pos.y, pos.z, 15)
    time.sleep(3)
    mc.setBlock(pos.x+3, pos.y, pos.z, 1)
    time.sleep(3)
    
