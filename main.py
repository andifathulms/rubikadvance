from vpython import *
import time

def Cube(colorFront, colorBack, colorUp, colorDown, colorRight, colorLeft):
    colorFront = colorFront
    colorBack = colorBack
    colorUp = colorUp
    colorDown = colorDown
    colorLeft = colorLeft
    colorRight = colorRight

    container = box(pos=vector(0.5,0,0), size=vector(1,1,1), color=vector(0.5,0.5,0.5))
    side1 = pyramid(pos=vector(0,0,0), size=vector(0.9,0.9,0.9), color=colorLeft)
    side2 = pyramid(pos=vector(1,0,0), size=vector(0.9,0.9,0.9), axis=vector(-1,0,0), color=colorRight)
    side3 = pyramid(pos=vector(0.5,-0.5,0), size=vector(0.9,0.9,0.9), axis=vector(0,1,0), color=colorDown)
    side4 = pyramid(pos=vector(0.5,0.5,0), size=vector(0.9,0.9,0.9), axis=vector(0,-1,0), color=colorUp)
    side5 = pyramid(pos=vector(0.5,0,-0.5), size=vector(0.9,0.9,0.9), axis=vector(0,0,1), color=colorBack)
    side6 = pyramid(pos=vector(0.5,0,0.5), size=vector(0.9,0.9,0.9), axis=vector(0,0,-1), color=colorFront)

    return compound([container,side1,side2,side3,side4,side5,side6])

class Corner:
    def __init__(self, position, correct_position, name, orientation1, correct_orientation1, orientation2, correct_orientation2, orientation3, correct_orientation3):
        self.position = position
        self.correct_position = correct_position
        self.name = name
        self.orientation1 = orientation1
        self.correct_orientation1 = correct_orientation1
        self.orientation2 = orientation2
        self.correct_orientation2 = correct_orientation2
        self.orientation3 = orientation3
        self.correct_orientation3 = correct_orientation3
    def doF(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,1,0)

            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(1,0,0)    
            elif self.orientation3 == vector(1,0,0):    
                self.orientation3 = vector(0,-1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(-1,0,0)
            elif self.orientation3 == vector(-1,0,0): 
                self.orientation3 = vector(0,1,0)
        if self.position == vector(0,2,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,2,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,0,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doFp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,-1,0)

            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(-1,0,0)    
            elif self.orientation3 == vector(1,0,0):    
                self.orientation3 = vector(0,1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(1,0,0)
            elif self.orientation3 == vector(-1,0,0): 
                self.orientation3 = vector(0,-1,0)

        if self.position == vector(0,2,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,2,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,0,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doR(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,-1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,-1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,1,0)
                
            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(0,0,-1)    
            elif self.orientation3 == vector(0,0,-1):    
                self.orientation3 = vector(0,-1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(0,0,1)
            elif self.orientation3 == vector(0,0,1): 
                self.orientation3 = vector(0,1,0)
        if self.position == vector(2,0,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,2,0):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,2,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,-2):
            self.position = vector(2,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doRp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,-1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,-1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,-1,0)

            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(0,0,1)    
            elif self.orientation3 == vector(0,0,-1):    
                self.orientation3 = vector(0,1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(0,0,-1)
            elif self.orientation3 == vector(0,0,1): 
                self.orientation3 = vector(0,-1,0)
        if self.position == vector(2,0,0):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
  
        elif self.position == vector(2,2,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,2,-2):
            self.position = vector(2,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doLp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,-1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,-1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,1,0)

            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(0,0,-1)    
            elif self.orientation3 == vector(0,0,-1):    
                self.orientation3 = vector(0,-1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(0,0,1)
            elif self.orientation3 == vector(0,0,1): 
                self.orientation3 = vector(0,1,0)
        if self.position == vector(0,0,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,2,0):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,2,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,0,-2):
            self.position = vector(0,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doL(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,-1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,-1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,-1,0)
            
            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(0,0,1)    
            elif self.orientation3 == vector(0,0,-1):    
                self.orientation3 = vector(0,1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(0,0,-1)
            elif self.orientation3 == vector(0,0,1): 
                self.orientation3 = vector(0,-1,0)
        if self.position == vector(0,0,0):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(0,2,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,2,-2):
            self.position = vector(0,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,0,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doU(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,-1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,-1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,1)

            if self.orientation3 == vector(0,0,1):
                self.orientation3 =  vector(-1,0,0)    
            elif self.orientation3 == vector(-1,0,0):    
                self.orientation3 = vector(0,0,-1) 
            elif self.orientation3 == vector(0,0,-1): 
                self.orientation3 = vector(1,0,0)
            elif self.orientation3 == vector(1,0,0): 
                self.orientation3 = vector(0,0,1)
        if  self.position == vector(2,2,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(0,2,0):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(0,2,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(2,2,-2):
            self.position = vector(2,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

    
    def doUp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,-1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,-1)

            if self.orientation3 == vector(0,0,1):
                self.orientation3 =  vector(1,0,0)    
            elif self.orientation3 == vector(-1,0,0):    
                self.orientation3 = vector(0,0,1) 
            elif self.orientation3 == vector(0,0,-1): 
                self.orientation3 = vector(-1,0,0)
            elif self.orientation3 == vector(1,0,0): 
                self.orientation3 = vector(0,0,-1)
        if  self.position == vector(2,2,0):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(0,2,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(0,2,-2):
            self.position = vector(0,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif  self.position == vector(2,2,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

    
    def doDp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,-1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,-1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,1)

            if self.orientation3 == vector(0,0,1):
                self.orientation3 =  vector(-1,0,0)    
            elif self.orientation3 == vector(-1,0,0):    
                self.orientation3 = vector(0,0,-1) 
            elif self.orientation3 == vector(0,0,-1): 
                self.orientation3 = vector(1,0,0)
            elif self.orientation3 == vector(1,0,0): 
                self.orientation3 = vector(0,0,1)
        if  self.position == vector(0,0,0):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,0,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,-2):
            self.position = vector(2,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doD(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,-1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,-1)

            if self.orientation3 == vector(0,0,1):
                self.orientation3 =  vector(1,0,0)    
            elif self.orientation3 == vector(-1,0,0):    
                self.orientation3 = vector(0,0,1) 
            elif self.orientation3 == vector(0,0,-1): 
                self.orientation3 = vector(-1,0,0)
            elif self.orientation3 == vector(1,0,0): 
                self.orientation3 = vector(0,0,-1)
        if  self.position == vector(0,0,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,0,-2):
            self.position = vector(0,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,0):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doBp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,1,0)

            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(1,0,0)    
            elif self.orientation3 == vector(1,0,0):    
                self.orientation3 = vector(0,-1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(-1,0,0)
            elif self.orientation3 == vector(-1,0,0): 
                self.orientation3 = vector(0,1,0)
        if self.position == vector(0,0,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,2,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,2,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)


    def doB(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,-1,0)

            if self.orientation3 == vector(0,1,0):
                self.orientation3 =  vector(-1,0,0)    
            elif self.orientation3 == vector(1,0,0):    
                self.orientation3 = vector(0,1,0) 
            elif self.orientation3 == vector(0,-1,0): 
                self.orientation3 = vector(1,0,0)
            elif self.orientation3 == vector(-1,0,0): 
                self.orientation3 = vector(0,-1,0)
        if self.position == vector(0,0,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0,2,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
   
        elif self.position == vector(2,2,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2,0,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

class Edge:
    def __init__(self,position, correct_position, name, orientation1, correct_orientation1, orientation2, correct_orientation2):
        self.position = position
        self.correct_position = correct_position
        self.name = name
        self.orientation1 = orientation1
        self.correct_orientation1 = correct_orientation1
        self.orientation2 = orientation2
        self.correct_orientation2 = correct_orientation2
    def doF(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(1,0,0):
            self.position = vector(0,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,0):
            self.position = vector(1,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,0):
            self.position = vector(2,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,0):
            self.position = vector(1,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doFp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,-1,0)

        if self.position == vector(1,0,0):
            self.position = vector(2,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,0):
            self.position = vector(1,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,0):
            self.position = vector(0,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,0):
            self.position = vector(1,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doR(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,-1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,-1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(2,1,0):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,2,-1):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(2,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doRp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,-1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,-1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,-1,0)
        if self.position == vector(2,1,0):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,2,-1):
            self.position = vector(2,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    
    def doLp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,-1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,-1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(0,1,0):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,2,-1):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(0,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        

    def doL(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,-1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,-1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,-1,0)
        if self.position == vector(0,1,0):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,2,-1):
            self.position = vector(0,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
       
    def doU(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,-1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,-1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,1)
        if  self.position == vector(1,2,0):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(0,2,-1):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(1,2,-2):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(2,2,-1):
            self.position = vector(1,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    
    def doUp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,-1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,-1)
        
        if  self.position == vector(1,2,0):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(0,2,-1):
            self.position = vector(1,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(1,2,-2):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(2,2,-1):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doDp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,-1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,-1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,1)
        if  self.position == vector(1,0,0):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,0,-2):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(1,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doD(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,-1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,-1)
        if  self.position == vector(1,0,0):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(1,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,0,-2):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doBp(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(1,0,-2):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,-2):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def doB(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,-1,0)
        if self.position == vector(1,0,-2):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,-2):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)

class Scramble():
    def __init__(self,scramble):
        self.scr_li = list(scramble.split(" "))
    
    def __getitem__(self,key):
        return self.scr_li[key]
    
    def getLength(self):
        return len(self.scr_li)
    
    def showScramble(self):
        print(self.scr_li)

def slider(s):
    time = s

time1 = 0.1
def front_rotation_clock(pieces):
    for i in range(len(pieces)):
        pieces[i].doF()
    time.sleep(time1)
def front_rotation_counter(pieces):
    for i in range(len(pieces)):
        pieces[i].doFp()
    time.sleep(time1)

def back_rotation_clock(pieces):
    for i in range(len(pieces)):
        pieces[i].doB()
    time.sleep(time1)
def back_rotation_counter(pieces):
    for i in range(len(pieces)):
        pieces[i].doBp()
    time.sleep(time1)

def top_rotation_counter(pieces):
    for i in range(len(pieces)):
        pieces[i].doUp()
    time.sleep(time1)

def top_rotation_clock(pieces):
    for i in range(len(pieces)):
        pieces[i].doU()
    time.sleep(time1)
def down_rotation_clock(pieces):
    for i in range(len(pieces)):
        pieces[i].doD()
    time.sleep(time1)
def down_rotation_counter(pieces):
    for i in range(len(pieces)):
        pieces[i].doDp()
    time.sleep(time1)

def right_rotation_clock(pieces):
    for i in range(len(pieces)):
        pieces[i].doR()
    time.sleep(time1)
def right_rotation_counter(pieces):
    for i in range(len(pieces)):
        pieces[i].doRp()
    time.sleep(time1)

def left_rotation_clock(pieces):
    for i in range(len(pieces)):
        pieces[i].doL()
    time.sleep(time1)
def left_rotation_counter(pieces):
    for i in range(len(pieces)):
        pieces[i].doLp()
    time.sleep(time1)
def runScramble(pieces,scramble):
    s = scramble
    for i in range(0,s.getLength()):
        if s[i] in ["F", "F'", "R", "R'", "L", "L'", "B", "B'", "U", "U'", "D", "D'"]:
            if s[i] == "R":
                 right_rotation_clock(pieces)
            elif s[i] == "R'":
                right_rotation_counter(pieces)
            elif s[i] == "L":
                left_rotation_clock(pieces)
            elif s[i] == "L'":
                left_rotation_counter(pieces)
            elif s[i] == "U":
                top_rotation_clock(pieces)
            elif s[i] == "U'":
                top_rotation_counter(pieces)
            elif s[i] == "D":
                down_rotation_clock(pieces)
            elif s[i] == "D'":
                down_rotation_counter(pieces)
            elif s[i] == "F":
                front_rotation_clock(pieces)
            elif s[i] == "F'":
                front_rotation_counter(pieces)
            elif s[i] == "B":
                back_rotation_clock(pieces)
            elif s[i] == "B'":
                back_rotation_counter(pieces)


            
#Define All 26 cubes,Orientation : Green Front, Yellow Top
# F B U D R L
cube1 = Cube(color.green, color.black, color.yellow, color.black, color.black, color.red) #C - GYR    #0-2-0
cube2 = Cube(color.green, color.black, color.yellow, color.black, color.black, color.black) #E - GY   #1-2-0
cube3 = Cube(color.green, color.black, color.yellow, color.black, color.orange, color.black) #C - GYO #2-2-0
cube4 = Cube(color.green, color.black, color.black, color.black, color.black, color.red) #E - GR      #0-1-0
cube5 = Cube(color.green, color.black, color.black, color.black, color.orange, color.black) #E - GO   #2-1-0
cube6 = Cube(color.green, color.black, color.black, color.black, color.black, color.black) #X - G     #1-1-0
cube7 = Cube(color.green, color.black, color.black, color.white, color.black, color.red) #C - GRW     #0-0-0
cube8 = Cube(color.green, color.black, color.black, color.white, color.black, color.black) #E - GW    #1-0-0
cube9 = Cube(color.green, color.black, color.black, color.white, color.orange, color.black) #C - GOW  #2-0-0
cube10 = Cube(color.black, color.black, color.yellow, color.black, color.orange, color.black) #E - OY #2-2-(-1)
cube11 = Cube(color.black, color.blue, color.yellow, color.black, color.orange, color.black) #C - OYB #2-2-(-2)
cube12 = Cube(color.black, color.black, color.black, color.black, color.orange, color.black) #X - O   #2-1-(-1)
cube13 = Cube(color.black, color.blue, color.black, color.black, color.orange, color.black) #E - OB   #2-1-(-2)
cube14 = Cube(color.black, color.black, color.black, color.white, color.orange, color.black) #E - OW  #2-0-(-1)
cube15 = Cube(color.black, color.blue, color.black, color.white, color.orange, color.black) #C - OBW  #2-0-(-2)
cube16 = Cube(color.black, color.blue, color.yellow, color.black, color.black, color.black) #E - BY   #1-2-(-2)
cube17 = Cube(color.black, color.blue, color.black, color.black, color.black, color.black) #X - B     #1-1-(-2)
cube18 = Cube(color.black, color.blue, color.black, color.white, color.black, color.black) #E - BW    #1-0-(-2)
cube19 = Cube(color.black, color.blue, color.yellow, color.black, color.black, color.red) #C - BYR    #0-2-(-2)
cube20 = Cube(color.black, color.blue, color.black, color.black, color.black, color.red) #E - BR      #0-1-(-2)
cube21 = Cube(color.black, color.blue, color.black, color.white, color.black, color.red) #C - BWR     #0-0-(-2)
cube22 = Cube(color.black, color.black, color.yellow, color.black, color.black, color.red) #E - YR    #0-2-(-1)
cube23 = Cube(color.black, color.black, color.black, color.black, color.black, color.red) #X - R      #0-1-(-1)
cube24 = Cube(color.black, color.black, color.black, color.white, color.black, color.red) #E - WR     #0-0-(-1)
cube25 = Cube(color.black, color.black, color.yellow, color.black, color.black, color.black) #X - Y   #1-2-(-1)
cube26 = Cube(color.black, color.black, color.black, color.white, color.black, color.black) #X - W    #1-0-(-1)

#All possible vector
v1 = vector(0,2,0) 
v2 = vector(1,2,0)
v3 = vector(2,2,0)
v4 = vector(0,1,0)
v5 = vector(2,1,0)
v6 = vector(1,1,0)
v7 = vector(0,0,0)
v8 = vector(1,0,0)
v9 = vector(2,0,0)
v10 = vector(2,2,-1)
v11 = vector(2,2,-2)
v12 = vector(2,1,-1)
v13 = vector(2,1,-2)
v14 = vector(2,0,-1)
v15 = vector(2,0,-2)
v16 = vector(1,2,-2)
v17 = vector(1,1,-2)
v18 = vector(1,0,-2)
v19 = vector(0,2,-2)
v20 = vector(0,1,-2)
v21 = vector(0,0,-2)
v22 = vector(0,2,-1)
v23 = vector(0,1,-1)
v24 = vector(0,0,-1)
v25 = vector(1,2,-1)
v26 = vector(1,0,-1)

originWhite = vector(0,1,0)
originBlue = vector(0,0,1)
originYellow = vector(0,-1,0)
originRed = vector(-1,0,0)
originOrange = vector(1,0,0)
originGreen = vector(0,0,-1)
cubes = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14,
         cube15, cube16, cube17, cube18, cube19, cube20, cube21, cube22, cube23, cube24, cube25, cube26]

vectors = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14,
           v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26]

for i in range(len(cubes)):
    cubes[i].pos = vectors[i]

c1 = Corner(v1,v1,cube1, originYellow,originYellow, originRed, originRed, originGreen, originGreen)
c2 = Edge(v2,v2,cube2, originYellow, originYellow, originGreen, originGreen)
c3 = Corner(v3,v3,cube3, originYellow,originYellow, originOrange, originOrange, originGreen, originGreen)
c4 = Edge(v4,v4,cube4, originRed, originRed, originGreen, originGreen)
c5 = Edge(v5,v5,cube5, originOrange, originOrange,originGreen, originGreen)
#c6
c7 = Corner(v7,v7,cube7, originGreen, originGreen, originRed, originRed, originWhite, originWhite)
c8 = Edge(v8,v8,cube8, originWhite, originWhite, originGreen, originGreen)
c9 = Corner(v9,v9,cube9, originOrange, originOrange, originGreen, originGreen, originWhite, originWhite)
c10 = Edge(v10,v10,cube10, originYellow,originYellow, originOrange, originOrange)
c11 = Corner(v11,v11,cube11, originYellow,originYellow, originOrange, originOrange, originBlue, originBlue)
#c12
c13 = Edge(v13,v13,cube13, originBlue, originBlue, originOrange, originOrange)
c14 = Edge(v14,v14,cube14, originWhite, originWhite, originOrange, originOrange)
c15 = Corner(v15,v15,cube15,originWhite, originWhite, originOrange, originOrange, originBlue, originBlue)
c16 = Edge(v16,v16,cube16,originYellow,originYellow,originBlue,originBlue)
#c17
c18 = Edge(v18,v18,cube18,originWhite, originWhite, originBlue, originBlue)
c19 = Corner(v19,v19,cube19, originYellow,originYellow, originRed, originRed, originBlue, originBlue)
c20 = Edge(v20,v20,cube20,originBlue,originBlue, originRed, originRed)
c21 = Corner(v21,v21,cube21,originWhite, originWhite, originRed, originRed, originBlue, originBlue)
c22 = Edge(v22,v22,cube22, originYellow, originYellow, originRed, originRed)
#c23
c24 = Edge(v24,v24,cube24, originWhite, originWhite, originRed, originRed)
#c25 #c26

pieces = [c1,c2,c3,c4,c5,c7,c8,c9,c10,c11,c13,c14,c15,c16,c18,c19,c20,c21,c24]


if __name__ == '__main__':
    #s = Scramble("F R U R' U' F' D L")
    s = Scramble("L")
    runScramble(pieces,s)