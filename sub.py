from abc import ABC

import pyglet.window
import pyglet.shapes
from pyglet import shapes
from pyglet.gl import GL_LINE, GL_LINE_STIPPLE, GL_LINES, GL_LINE_SMOOTH

batch = pyglet.graphics.Batch()
circle = shapes.Circle(x=100, y=150, radius=100, color=(255, 225, 255), batch=batch)
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255), batch=batch)

document = pyglet.text.document.UnformattedDocument("heey")
d = pyglet.text.decode_text("hello")

print(d.text)


# batch.add(2, pyglet.text.Label("Hello World", bold=True, color=(255, 215, 0, 255), italic=True), None,
#           ('v2f', (0, 0, 0, 0)))

class HelloWorld(pyglet.window.Window):
    def __init__(self):
        super(HelloWorld, self).__init__()
        self.label = pyglet.text.Label("Hello World", bold=True, color=(255, 215, 0, 255), italic=True, batch=batch)
        # html string and style
        print(HelloWorld.get_size(self)[0])
        self.html = pyglet.text.HTMLLabel(
            '<font face="Times New Roman" size="4">Hello, <i>world</i></font>',
            x=HelloWorld.get_size(self)[0] // 2, y=HelloWorld.get_size(self)[1]// 2,
            anchor_x='center', anchor_y='center', batch=batch)

    #     pyglet.text.Label() constructor alsa accepts a batch parameter
    # what this does is it adds the text to a labels toa group for rendering much later on, it's a functionality from
    # OpenGl that ensure the resources of your hardware are not strained by calling the draw() method everytime

    def on_draw(self):
        self.clear()
        # self.label.draw()
        batch.draw()
        # pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v2i', (100, 40, 40, 70,20,20)),('c3B',(0,250,0,250,0,0,0,
        # 0,250)))

        # pyglet provides the shapes constructor to build common shapes such as circle, triangle and squares
        # it takes x, y coordinates color parameters
        # additionally it has an opacity attribute which you can access using the instance of the class shapes
        # the instance also has a draw method which can be called inside the on_draw() method that is decorated
        # it is mainly recommended to use the Batch() method to add all the shapes and render them all at once without
        # consuming much of the vidoe card resources
        # circle = shapes.Circle(x=100, y=150, radius=100, color=(255, 225, 255))
        # square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))
        # circle.draw()
        # square.draw()
        pyglet.gl.glEnable(GL_LINE_SMOOTH)
        pyglet.gl.glLineWidth(4)
        pyglet.gl.glLineStipple(3,0xAAAA)
        pyglet.gl.glEnable(GL_LINE_STIPPLE)
        # pyglet.gl.glLineWidth()

        a = pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ('v2i', (100, 40,160, 40 ))
                             )
        # notworking gllinestipple
        # pyglet.gl.glLineStipple(1, a)


        # pyglet.graphics.draw_indexed(2, pyglet.gl.GL_POINTS,
        #                              [0, 1],
        #                              ('v2i', (10, 15, 30, 35))
        #                              )

        # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        #                              [0, 1, 2, 0, 2, 3],
        #                              ('v2i', (100, 100,
        #                                       150, 100,
        #                                       150, 150,
        #                                       100, 150))
        #                              )
        #


if __name__ == "__main__":
    HelloWorld()

    pyglet.app.run()
