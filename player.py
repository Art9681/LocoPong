import math
import pyglet
from pyglet.gl import *
import pymunk
import cocos

class Player(object):
    def __init__(self, position):
        super(Player, self).__init__()
        self.v1 = 50
        self.v2 = 15
        #Pymunk physics variables.
        self.verts = [(-self.v2, -self.v1), (-self.v2, self.v1), (self.v2, self.v1), (self.v2, -self.v1)]
        self.mass = 100
        self.friction = 9
        self.elasticity = 0
        self.moment = pymunk.moment_for_poly(self.mass, self.verts)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = position
        self.shape = pymunk.Poly(self.body, self.verts)
        #self.shape.group = 1
        #self.shape.layers = 1
        #self.shape.collision_type = 1
        self.shape.friction = 0.1
        self.shape.elasticity = 0.9
        self.shape.collision_type = 2
        self.pin_body = pymunk.Body()
        self.pin_body.position = self.body.position
        self.spring = pymunk.DampedRotarySpring(self.body, self.pin_body, 0, 20000000, 900000)

        self.groove_body = pymunk.Body()
        self.groove_body.position = (self.body.position.x, 0)
        self.groove = pymunk.GrooveJoint(self.groove_body, self.body, (0, 0), (0, 768), (0,0))

    def update(self, xpos):
        #Restrict movement to Y axis and do not allow rotation.
        #self.body.position.x = xpos
        pass
