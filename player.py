import math
import pyglet
from pyglet.gl import *
import pymunk
import cocos

class Player(object):
    def __init__(self):
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
        self.body.position = 20, 55
        self.shape = pymunk.Poly(self.body, self.verts)
        #self.shape.group = 1
        #self.shape.layers = 1
        #self.shape.collision_type = 1
        self.shape.friction = 0.1

    def draw(self):
        points = self.shape.get_points()
        #points = [points[0]] + points + [points[0], points[0]]
        boxVerts = []
        for p in points:
            boxVerts.append(p.x)
            boxVerts.append(p.y)
        pyglet.graphics.draw(len(points), GL_QUADS, ('v2f', boxVerts))

    def update(self):
        #Restrict movement to Y axis and do not allow rotation.
        self.body.velocity.x = 0
        if self.body.angle != 0.0:
            self.body.angle = 0.0




