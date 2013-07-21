import math
import pyglet
from pyglet.gl import *
import pymunk
import cocos

class Ball(object):
    def __init__(self):
        super(Ball, self).__init__()

        self.image = cocos.sprite.Sprite('Content/ball.png')

        self.mass = 0.5
        self.radius = 25
        self.moment = pymunk.moment_for_circle(self.mass, 0,self.radius, (0, 0))
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = 500,500
        self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
        self.shape.elasticity = 0.9
        self.shape.friction = 0.1

    def draw(self):
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            angle = 2 * math.pi * i / 360
            x = math.cos(angle)
            y = math.sin(angle)
            glVertex2d(x, y)
        glEnd()

    def update(self):
        self.image.position = self.body.position




