from direct.showbase.ShowBase import ShowBase
#from Picker import Picker

class Application(ShowBase):
	
	def __init__(self):
		
		ShowBase.__init__(self)
		
		mousePicker = Picker()
		
		#load the models
		obj1 = loader.loadModel('panda')
		obj2 = loader.loadModel('teapot')
		obj3 = loader.loadModel('box')
		
		obj1.reparentTo(render)
		obj1.setPos(camera,0,100,0)
		
		obj2.reparentTo(render)
		obj2.setPos(obj1, -30, 0, 0)
		
		obj3.reparentTo(render)
		obj3.setPos(obj1, 30,0,0)
		
		mousePicker.makePickable(obj1)
		mousePicker.makePickable(obj2)
		mousePicker.makePickable(obj3)
		
		ShowBase.destroy()
		
				
	