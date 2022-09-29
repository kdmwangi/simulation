import pyglet.window
from pyglet import window


# create a hello world window using subclassing

class C:
    def __init__(self,a):
        print("init method called automatically")
        print(a)

    def heey(self):

        print("hello there")


class HelloWorld(C):
    def __int__(self,a):
        # a = C.heey()
        super(HelloWorld).__init__(a)
        # return a

s = HelloWorld(1)
print(s)


# class HelloThere(pyglet.window.Window):
#     def __init__(self):
#
#         super(HelloThere, self).__init__()
#         # print("heeeey")
#         self.label = pyglet.text.Label("Hello There")
#     def on_draw(self):
#         self.clear()
#         self.label.draw()
#         # HelloThere()
#
# if __name__ == "__main__":
#     m = HelloThere()
#     pyglet.app.run()
#

