class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  def __str__(self):
    return "Radius: "+ str(self.radius) + ", Height: " + str(self.height)
 
  def getRadius(self):
    return self.radius
  def setRadius(self):
    self.radius=radius
  def setHeight(self):
    self.height=height    
  def getHeight(self):
    return self.height
  def getVolume(self):
    return self.radius*self.radius*3.14*self.height
  def getArea(self):
    return (self.height*self.radius*2*(3.14)+3.14*(self.radius**2)*2)    
 
#Creating a cylinder object from the Cylinder class
cd=Cylinder(5,10)
 

print("It's volume is "+str(cd.getVolume()))
print("It's area is "+str(cd.getArea()))