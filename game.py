import pyglet
from pyglet.gl import GL_LINE_STIPPLE

window = pyglet.window.Window()
pyglet.gl.glEnable()
# create a batch to display all graphics all at once
batch = pyglet.graphics.Batch()

# draw a circle in the center if the screen
circle = pyglet.shapes.Circle(x=window.width // 2, y=window.height // 2, radius=40, batch=batch, color=(0, 255, 0))
circle2 = pyglet.shapes.Arc(x=600, y=320, radius=60, batch=batch, start_angle=0, angle=90)
# l = pyglet.graphics.draw(2, pyglet.graphics.GL_LINE_STIPPLE_REPEAT,('v2i',(100,40, 20,70)))

# pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2i',(100,40, 20,70)))
# create a broken line for overtaking
pyglet.gl.glLineWidth(4)
pyglet.gl.glEnable(GL_LINE_STIPPLE)
pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2i',(0,)))

#
@window.event
def on_draw():
    # batch.add(l)
    batch.draw()
    # pyglet.graphics.draw(2, pyglet.gl.GL_QUADS,
    #                      ('v2i', (30, 60, 60, 35))
    #                      )
    vertex_list = pyglet.graphics.vertex_list(2,
                                              ('v2i', (10, 15, 30, 35)),
                                              ('c3B', (0, 0, 255, 0, 255, 0))
                                              )
    vertex_list.draw(pyglet.gl.GL_POINTS)

    # l.draw()


if __name__ == "__main__":
    pyglet.app.run()
