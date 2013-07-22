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
        dt = 1/60

        #The layers this scene has.
        self.bg = levels.Background()
        self.levelMain = levels.Level(self.clock)
        self.interface = interface.Interface()


        #Add the layers to the scene.
        self.add(self.bg, z=0)
        self.add(self.levelMain, z=1)
        self.add(self.interface, z=2)



        self.clock.schedule(self.levelMain.update)