import numpy as np
import pyglet
from pyglet.window import key


class ArmEnv(object):
    viewer = None

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        if self.viewer is None:
            self.viewer = Viewer()
        self.viewer.render()


class Viewer(pyglet.window.Window):
    bar_thc = 5

    def __init__(self):
        # vsync=False to not use the monitor FPS, we can speed up training
        super(Viewer, self).__init__(width=400, height=400, resizable=False, caption='Arm', vsync=False)
        pyglet.gl.glClearColor(1, 1, 1, 1)
        x=1;y=0;z=1
        X, Y, Z = x + 1, y + 1, z + 1

        tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))
        self.batch = pyglet.graphics.Batch()    # display whole batch at once
        self.point1 = self.batch.add(4, pyglet.gl.GL_QUADS, None, ('v3f', (X, y, z, x, y, z, x, Y, z, X, Y, z),), tex_coords)  # back
        self.point2 = self.batch.add(4, pyglet.gl.GL_QUADS, None,  ('v3f', (x, y, Z, X, y, Z, X, Y, Z, x, Y, Z)), tex_coords)  # front

        self.point3 = self.batch.add(4, pyglet.gl.GL_QUADS, None,  ('v3f', (x, y, z, x, y, Z, x, Y, Z, x, Y, z)), tex_coords)  # left
        self.point4 = self.batch.add(4, pyglet.gl.GL_QUADS, None,  ('v3f', (X, y, Z, X, y, z, X, Y, z, X, Y, Z)), tex_coords)  # right

        self.point5 = self.batch.add(4, pyglet.gl.GL_QUADS, None,  ('v3f', (x, y, z, X, y, z, X, y, Z, x, y, Z)), tex_coords)  # bottom
        self.point6 = self.batch.add(4, pyglet.gl.GL_QUADS, None,  ('v3f', (x, Y, Z, X, Y, Z, X, Y, z, x, Y, z)), tex_coords)  # top
          # color



    def render(self):
        self._update_arm()
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def _update_arm(self):
        pass


if __name__ == '__main__':
    env = ArmEnv()
    while True:

        env.render()