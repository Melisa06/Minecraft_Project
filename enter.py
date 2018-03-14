from mcpi.minecraft import Minecraft

mc = Minecraft.create()
teclado = raw_input ("Enter your message: ")

mc.postToChat(teclado)
