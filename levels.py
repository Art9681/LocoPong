from pyglet.window import key, mouse
import cocos
from cocos import layer
import pymunk
import interface
import ball
import player


class Level(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self, clock):
        super( Level, self ).__init__()

        self.clock = clock
        self.dt = 1/60

        #Create the pymunk space that will simulate the physics.
        self.space = pymunk.Space()

        '''Used to reduce oscillating contacts and keep the collision
        cache warm. Defaults to 0.1. If you have poor simulation quality,
        increase this number as much as possible without allowing visible
        amounts of overlap.'''
        self.space.collision_slop = 0.3
        self.space.gravity = (0, 0)

        #The map boundaries.
        self.boundary_top = pymunk.Segment(self.space.static_body, (0, 770), (1370, 770), 1)
        self.boundary_bottom = pymunk.Segment(self.space.static_body, (0, 0), (1370, 0), 1)
        self.boundary_left = pymunk.Segment(self.space.static_body, (0, 0), (0, 770), 1)
        self.boundary_right = pymunk.Segment(self.space.static_body, (1370, 0), (1370, 770), 1)
        self.boundary_top.friction = self.boundary_bottom.friction = self.boundary_left.friction = self.boundary_right.friction = 10
        self.boundary_top.elasticity = self.boundary_bottom.elasticity = self.boundary_left.elasticity = self.boundary_right.elasticity = 0.9

        #Create actors and other physics objects.
        self.ball = ball.Ball()
        self.player = player.Player()

        #BatchNode to render all sprites.
        self.batch = cocos.batch.BatchNode()
        self.batch.add(self.ball.image)
        self.add(self.batch)


        #Add physics objects to our space.
        self.space.add(
                        self.boundary_top,
                        self.boundary_bottom,
                        self.boundary_left,
                        self.boundary_right,
                        self.ball.body,
                        self.ball.shape,
                        self.player.body,
                        self.player.shape,
                        self.player.spring,
                        )


    def update(self, dt):
        self.space.step(dt)
        self.player.update()
        self.ball.update()

    #Detects key presses and releases and fires events accordingly.
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.ball.body.apply_impulse(pymunk.Vec2d(-400, 0), (0, 0))
        if symbol == key.W:
            self.player.body.velocity.y = 800
        if symbol == key.S:
            self.player.body.velocity.y = -800
        if symbol == key.D:
            self.player.body.apply_impulse(pymunk.Vec2d(30000, 0), (0, 45))
        if symbol == key.A:
            self.player.body.apply_impulse(pymunk.Vec2d(-30000, 0), (0, 45))

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.player.body.velocity.y = 0
        if symbol == key.S:
            self.player.body.velocity.y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print "Hey Guys"

    def draw(self):
        self.player.draw()
        self.ball.draw()

#Handles the scrolling manager. Physics layers get added to this and this class gets added to the scene.
class GameLayer(object):
    def __init__(self, clock):
        super(GameLayer, self).__init__()
        global gameLayer

        gameLayer = cocos.layer.Layer()
        self.level1 = Level(clock)

        gameLayer.add(self.map)
        gameLayer.add(self.level1)

        self.gameLayer = gameLayer

    def update(self, dt):
        self.level1.update(dt)
