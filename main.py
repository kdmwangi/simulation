import pyglet.text

from pyglet.window import Window,mouse,key
from pyglet.resource import media
from pyglet import shapes

# create a window
window = Window(width=700, height=425)
# the window style is generated from the pyglet.window.Window constructor in all caps
# window = Window(style=pyglet.window.Window.WINDOW_STYLE_TOOL)
# code below resizes the window programmatically
window.set_size(1280,720)
# set the title of the window
window.set_caption("My game")

circle = shapes.Circle(x=400, y=450, radius=100, color=(255, 225, 255))
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))

# you can move the window manually by getting the  initial location of
# x and y position and setting a new x nad y position
# window.get_location
x,y = window.get_location()
print(x,y)
window.set_location(x-50,y+20)
# set the window to be resizable
# window = Window(resizable=True)
label = pyglet.text.Label("Hello world", font_name="Times New Roman",font_size=36,x=window.width//2,y=window.height//2,
                          anchor_x='center', anchor_y='center')
image = pyglet.resource.image("spida.jpeg")
# img = pyglet.image.load("beach.jpg",)
# load the icon image
icon = pyglet.resource.image("icon.png")
icon2 = pyglet.resource.image("icon2.png")
# render the icon to your window
window.set_icon(icon,icon2)


# prints all the event listeners when the app is run, that take place within the window
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

# decorator for event functions to work
# what it does is it adds the function to a dictionary which is a queue
# with the function name for the mainloop to read and execute
@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    circle.draw()

    label.draw()
@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.A:
        print("The key 'A' was pressed.")
    if modifiers == key.MOD_CTRL:
        print("The 'CTRL' modifier was pressed.")

@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        print("The left mouse was pressed")
        print(x,y)
@window.event
def on_mouse_motion(x,y, dx,dy):
    print(x,y,dx,dy)

# hide the mouse cursor
# window.set_mouse_visible(False)
# change the mouse cursor
# get hold of the different mouse cursor provided by your operating system ie
# cursor = window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
# use the set_mouse_cursor()
# window.set_mouse_cursor(cursor)
# creating your own image as the cursor image
# img = pyglet.resource.image('icon.png')
# cursor = pyglet.window.ImageMouseCursor(img,16,8)
# window.set_mouse_cursor(cursor)

# how to disable the mouse exclusively, this allows you to have more control over the window
# by preventing it from being used by the user

# window.set_exclusive_mouse(True)
# on_text() shows all the keystrokes pressed by user on the keyboard, it ia useful when determining
# a string from keystrokes
@window.event
def on_text(text):
    print(text)

# used for detecting continuous special key presses eg the left arrow to move through the text and pageup or pagedown
# the key are stores in the motion parameter
@window.event
def on_text_motion(motion):
    print("###")
    print(motion)
    print("##")
music = media("woman.mp3")
# music.play()

# storing short sound in memory

sound = pyglet.resource.media("urban.wav", streaming=False)
sound.play()

# drawing of shapes using the pyglet.gl module adn its constants

# pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
#     ('v2i', (100, 15, 30, 35))
# )
pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2i',(100,40, 20,70)))


pyglet.app.run()