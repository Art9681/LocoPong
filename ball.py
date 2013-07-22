import pymunk

class Ball(object):
    def __init__(self):
        super(Ball, self).__init__()

        self.mass = 0.5
        self.radius = 25
        self.moment = pymunk.moment_for_circle(self.mass, 0,self.radius, (0, 0))
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = 500,500
        self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
        self.shape.elasticity = 0.9
        self.shape.friction = 0.1
        self.shape.collision_type = 1
        self.body.velocity_limit = 1500
