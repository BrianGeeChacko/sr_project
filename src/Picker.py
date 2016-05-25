import direct.directbase.DirectStart
#for the events
from direct.showbase import DirectObject
#for collision
from pandac.PandaModules import *

class Picker(DirectObject.DirectObject):
	def __init__(self):
		
		self.picker = CollisionTraverser()
		self.queue = CollisionHandlerQueue()
		
		self.pickerNode = CollisionNode('mouseRay')
		self.pickerNP = camera.attachNewNode(self.pickerNode)
		
		self.pickernode.setFromCollideMask(GeomNode.getDefaultCollideMask())
		
		self.pickerRay = CollisionRay()
		
		self.pickerNode.addSolid(self.pickerRay)
		
		self.picker.addCollider(self.pickerNode, self.queue)
		
		self.pickedObj=None
		
		self.accept('mouse1',self.printMe)
		
	def makePickable(self,newObj):
		newObj.setTag('pickable','true')
		
	def getObjectHit(self,mpos):
		self.pickedObj=None
		self.pickerRay.setFromLens(base.camNode, mpos.getX(),mpos.getY())
		self.picker.traverse(render)
		if self.queue.getNumEntries() > 0:
			self.queue.sortEntries()
			self.pickedObj=self.queue.getEntry(0).getIntoNodePath()
			
			parent=self.pickedObj.getParent()
			self.pickedObj=None
			
			while parent != render:
				if parent.getTag('pickable')=='true':
					self.pickedObj=parent
					return parent
				else:
					parent=parent.getParent()
		return None
	
	def getPickedObj(self):
		return self.pickedObj
		
	def printMe(self):
		self.getObjectHit( base.mouseWatcherNode.getMouse())
		print self.pickedObj
		
