import pyglet
import cocos
import levels
import interface


class MyGame(cocos.scene.Scene):
    def __init__(self):
        super(MyGame, self).__init__()


        #Create the clock and delta time variables.
        #The clock ticks 60 times a second.
        self.clock = pyglet.clock
        #dt = 1/60

        #The layers this scene has.
        self.levelMain = levels.Level(self.clock)
        self.bg = self.levelMain.bg
        self.particle_layer = levels.ParticleLayer()
        self.interface = interface.Interface()


        #Add the layers to the scene.
        self.add(self.bg, z=0)
        self.add(self.particle_layer, z=1)
        self.add(self.levelMain, z=2)
        self.add(self.interface, z=3)

        self.clock.schedule(self.levelMain.update)
