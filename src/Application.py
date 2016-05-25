from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from GuiBuilder import GuiHandler, GuiFromXml
from direct.gui.OnscreenImage import OnscreenImage


class Application(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		
		#Home Scene
		files = ["../textures/IMG-20160225-WA025.jpg"]
		OnscreenImage(  files[0],
						scale = Vec3(1,1,1),
						pos = Vec3(0,0,0),
						hpr = Vec3(0,0,0)
						)		
		# UI
		handler = MyHandler()
		GuiFromXml("gui.xml", handler)
	
		
						
		
class MyHandler(GuiHandler):
	def __init__(self):
		GuiHandler.__init__(self)
	
	def setName(self):
		title= self
		
			
		
		
				
	