import math
import pyglet
from pyglet.gl import *
import pymunk
import cocos

class Player(object):
    def __init__(self):
        super(Player, self).__init__()
        self.v1 = 50
        #Pymunk physics variables.
        self.verts = [(self.v1, self.v1), (self.v1, -self.v1), (-self.v1, -self.v1), (-self.v1, self.v1)]
        self.mass = 100
        self.friction = 9
        self.elasticity = 0
        self.moment = pymunk.moment_for_poly(self.mass, self.verts)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = 150,300
        self.shape = pymunk.Poly(self.body, self.verts)
        #self.shape.group = 1
        #self.shape.layers = 1
        #self.shape.collision_type = 1
        self.shape.friction = 0.1

    def draw(self):
        ps = self.shape.get_points()
        ps = [ps[0]] + ps + [ps[0], ps[0]]
        xs = []
        for p in ps:
            xs.append(p.x)
            xs.append(p.y)
        pyglet.graphics.draw(len(ps), GL_LINE_STRIP, ('v2f', xs))




