import numpy as np
import pyglet


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


    # 画出手臂，被抓物体，位置颜色信息
    def __init__(self):
        # vsync=False to not use the monitor FPS, we can speed up training
        super(Viewer, self).__init__(width=400, height=400, resizable=False, caption='Arm', vsync=False)
        pyglet.gl.glClearColor(1, 1, 1, 1)

        self.batch = pyglet.graphics.Batch()    # display whole batch at once
        self.point = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,    # 4 corners
            ('v2f', [10, 50,            # location
                     10, 100,
                     100, 100,
                     100, 50 ]),
            ('c3B', (86, 109, 249) * 4))    # color
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,                # location
                     250, 300,
                     260, 300,
                     260, 250]),
            ('c3B', (249, 86, 86) * 4,))    # color
        self.arm2 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [100, 150,              # location
                     100, 160,
                     200, 160,
                     200, 150]), ('c3B', (249, 86, 86) * 4,))
        self.arm3 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [200, 20,  # location
                     200, 30,
                     300, 30,
                     300, 20]), ('c3B', (249, 86, 86) * 4,))
    # 刷新并呈现屏幕
    def render(self):
        self._update_arm() # 更新手臂内容
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()
    # 刷新手臂位置
    def on_draw(self):
        self.clear()
        self.batch.draw() # 显示batch里内容
    # 更新手臂位置坐标信息
    def _update_arm(self):
        pass


if __name__ == '__main__':
    env = ArmEnv()
    while True:
        env.render()