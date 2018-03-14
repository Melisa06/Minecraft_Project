from mcpi.minecraft import Minecraft
##from mcpi import block 
mc = Minecraft.create()
pos = mc.player.getTilePos()
##block = mc.getBlock()


mc.postToChat("Hello Minecraft word")
mc.postToChat(pos)
##mc.postToChat(block)
