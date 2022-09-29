import pyglet
from pyglet.gl import GL_LINE_STIPPLE
from pyglet.window import key

window = pyglet.window.Window(width=1240, height=800)
label = pyglet.text.Label('Hello, world', x=0, y=window.height // 2,
                          anchor_x='center', anchor_y='center')
window.set_caption("Game simulation")
game_on = True
batch = pyglet.graphics.Batch()


# line1 = pyglet.shapes.Line(x=0,y=40,x2=window.width,y2=40,width=2,color=(255,255,255))
# line2 = pyglet.shapes.Line(x=0,y=40,x2=window.width,y2=40,width=2,color=(255,255,255))
# the round-about island
island = pyglet.shapes.Circle(x=window.width/2, y=window.height/2,radius=40,color=(0, 255,0))

# round-about lanes
circ1 = pyglet.shapes.Circle(x=(window.width)/2,y=(window.height)/2,radius=80)
circ2 = pyglet.shapes.Circle(x=(window.width)/2,y=(window.height)/2,radius=120)
circ3 = pyglet.shapes.Circle(x=(window.width)/2,y=(window.height)/2,radius=160)
circ4 = pyglet.shapes.Circle(x=(window.width)/2,y=(window.height)/2,radius=200)


circ1.opacity = 50
circ2.opacity = 50
circ3.opacity = 50
circ4.opacity = 50

class Major:
    def __init__(self):
        self.line1 = pyglet.shapes.Line(x=0, y=10, x2=window.width, y2=10, width=4, color=(255, 255, 255), batch=batch)

        self.l = 2

    def road(self, x, y, x2, y2,width=4, color=(255,255,255)):
        self.l = 4
        self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
        return self.line2


class Car:
    def __init__(self,x=30,y=20,color=(255,255,0)):
        self.car = pyglet.shapes.Rectangle(x=x, y=y, width=30, height=15, color=color, batch=batch)


# draw broken lines

def yell():
    y = 50
    y2 = 50
    for _ in range(1, 5):
        print("@@")

        pyglet.shapes.Line(x=0, y=y, x2=10, y2=y2, width=4, color=(255, 255, 0), batch=batch)

        @window.event
        def on_draw():
            batch.draw()

        y += 10
        y2 += 10


# l = pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (100, 40, 20, 70)))
line1 = Major()
lll = Major()
li = lll.road(x=0, y=90, x2=window.width, y2=90)
mjl1 = Major().road(x=0,y=240,x2=(window.width/2-120),y2=240)
sepMjrd =Major().road(x=0,y=400,x2=(window.width/2-200),y2=400, width=5, color=(0,255,0))
sepMjrd2 =Major().road(x=(window.width/2 +200),y=400,x2=(window.width/2+400),y2=400, width=5, color=(0,255,0))

mjl2 = Major().road(x=0,y=560,x2=(window.width/2-120),y2=560)
cnts_yellow1 = Major().road(x=245,y=320,x2=440,y2=320,color=(255,255,0))
cnts_yellow2 = Major().road(x=245,y=280,x2=460,y2=280,color=(255,255,0))
cnts_yellow3 = Major().road(x=245,y=360,x2=420,y2=360,color=(255,255,0))

cnts_yellow4 = Major().road(x=245,y=440,x2=430,y2=440, color=(255,255,0))
cnts_yellow5 = Major().road(x=245,y=480,x2=440,y2=480, color=(255,255,0))
cnts_yellow6 = Major().road(x=245,y=520,x2=460,y2=520,color=(255,255,0))

lin = pyglet.shapes.Line(x=(window.width/2-120),y=90,x2=(window.width/2-120),y2=240, width=4,batch=batch)
lin2 = pyglet.shapes.Line(x=(window.width/2+120),y=90,x2=(window.width/2+120),y2=240, width=4,batch=batch)
lin3 = pyglet.shapes.Line(x=(window.width/2),y=90,x2=(window.width/2),y2=200, width=4,batch=batch, color=(255,255,255))
lin4 = pyglet.shapes.Line(x=(window.width/2+40),y=90,x2=(window.width/2+40),y2=200, width=4,batch=batch, color=(255,255,0))
lin5 = pyglet.shapes.Line(x=(window.width/2+80),y=90,x2=(window.width/2+80),y2=220, width=4,batch=batch, color=(255,255,0))
lin6 = pyglet.shapes.Line(x=(window.width/2-80),y=90,x2=(window.width/2-80),y2=220, width=4,batch=batch, color=(255,255,0))
lin7 = pyglet.shapes.Line(x=(window.width/2-40),y=90,x2=(window.width/2-40),y2=200, width=4,batch=batch, color=(255,255,0))

uplin = pyglet.shapes.Line(x=(window.width/2),y=600,x2=(window.width/2),y2=1000, width=4,batch=batch, color=(255,255,255))
uplin1 = pyglet.shapes.Line(x=(window.width/2),y=600,x2=(window.width/2),y2=1000, width=4,batch=batch, color=(255,255,255))
uplin2 = pyglet.shapes.Line(x=(window.width/2+40),y=600,x2=(window.width/2+40),y2=1000, width=4,batch=batch, color=(255,255,0))
uplin4 = pyglet.shapes.Line(x=(window.width/2+80),y=580,x2=(window.width/2+80),y2=1000, width=4,batch=batch, color=(255,255,0))
uplin5 = pyglet.shapes.Line(x=(window.width/2-80),y=580,x2=(window.width/2-80),y2=1000, width=4,batch=batch, color=(255,255,0))
uplin6 = pyglet.shapes.Line(x=(window.width/2-40),y=600,x2=(window.width/2-40),y2=1000, width=4,batch=batch, color=(255,255,0))





greenfields = pyglet.shapes.Rectangle(x=30,y=105,width=400,height=120,color=(0,255,0),batch=batch)

lyn = pyglet.shapes.Line(x=500,y=560,x2=500,y2=800,batch=batch, width=4)
lyn2 = pyglet.shapes.Line(x=740,y=560,x2=740,y2=800,batch=batch, width=4)

lyn3 = pyglet.shapes.Line(x=740,y=560,x2=900,y2=560,batch=batch, width=4)
lyn4 = pyglet.shapes.Line(x=740,y=240,x2=900,y2=240,batch=batch, width=4)

cnts_yellow7 = Major().road(x=780,y=280,x2=1000,y2=280,color=(255,255,0))
cnts_yellow8 = Major().road(x=815,y=360,x2=1020,y2=360,color=(255,255,0))
cnts_yellow9 = Major().road(x=815,y=440,x2=1020,y2=440, color=(255,255,0))
cnts_yellow10 = Major().road(x=800,y=480,x2=1020,y2=480, color=(255,255,0))
cnts_yellow11 = Major().road(x=803,y=320,x2=1020,y2=320,color=(255,255,0))
cnts_yellow12 = Major().road(x=780,y=520,x2=1020,y2=520,color=(255,255,0))




print(li)
print("##########")
print(line1.line1)
print(label)
car = Car(x=30, y=20, color=(255, 0, 255)).car
car2 = Car(x=30, y=410, color=(255, 0, 0)).car

# change line thickness
pyglet.gl.glLineWidth(4)
pyglet.gl.glPointSize(4)
# pass in the stipple function to glEnable, to allow antialiasing
pyglet.gl.glEnable(GL_LINE_STIPPLE)
# pyglet.gl.glEnable(GL_TRIANGLE_STIPPLE)

# give the pattern to the stipple function
pyglet.gl.glLineStipple(1,0x00FF)

# pyglet.shapes.Line()

@window.event
def on_draw():
    window.clear()
    # label.x += 10
    line1.line1.draw()
    # li.draw()
    li.draw()
    mjl1.draw()
    mjl2.draw()
    sepMjrd.draw()
    # label.y += 1
    car.draw()
    # yellow.draw()
    label.draw()
    island.draw()
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 50, 200, 50)),('c3B',(255, 255, 0,255,255,0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 320, 250, 320)),('c3B',(255, 255, 0,255,255,0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 280, 250, 280)),('c3B',(255, 255, 0,255,255,0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 360, 250, 360)),('c3B',(255, 255, 0,255,255,0)))

    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 440, 250, 440)),('c3B',(255, 255, 0,255,255,0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 480, 250, 480)),('c3B',(255, 255, 0,255,255,0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 520, 250, 520)),('c3B',(255, 255, 0,255,255,0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2f', ((window.width/2),100,(window.width/2),140)),('c3B',(255, 255, 0,255,255,0)))


    cnts_yellow1.draw()
    batch.draw()




    pyglet.graphics.draw(3, pyglet.graphics.GL_TRIANGLES, ('v2i', (20, 100, 4, 135,30,170)))
    circ1.draw()
    circ2.draw()
    circ3.draw()
    circ4.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2f', ((window.width/2+55), (window.height/2+55), 30, 35))
                         )
    if update(1):
        print(update(1))
        window.clear()
        # batch.draw()



def down(dt):
    label.y -= 10


@window.event
def on_key_press(symbol, modifier):

    if symbol == key.U:
        label.y += 40
    if symbol == key.LCTRL:
        pyglet.clock.unschedule(down)
    if symbol == key.RIGHT:
        print("right arrow presed")
        car2.x += 10
    if symbol == key.PAGEUP:
        car2.anchor_y += 40
        car2.rotation = -90
    if symbol == key.UP:
        print("right arrow presed")
        car2.y += 10






def update(dt):
    # print("a second has elapsed")
    # print(car2.y)
    # print(cnts_yellow4.y)
    yes = None
    if car2.y == (cnts_yellow4.y-10) and car2.x >= (cnts_yellow4.x -20):
        print("cant overtake")
        label_ovetake = pyglet.text.Label("Cant ovetake/change lanes",x=20,y=window.height-100, batch=batch)
        # pyglet.app.exit()
        # remove_handlers() receives a function to freeze the event incase the condition is fulfilled
        window.remove_handlers(on_key_press)
        yes = True
        return yes
        # pyglet.clock.unschedule(on_key_press)



    # pass


# calling a function periodically after a certain time has elapsed
#  use th clock module provided by pyglet
def call_once(dt):
    # print("one sec ahas passed")
    pass


# pyglet.clock.schedule_interval(update, 0.1)
# makes your program run at the highest possible frequency when creating an animation
# pyglet.clock.schedule_interval(update, 1)
# the unschedule() function is useful assume you do not want to run a function when a user provides a certain input
# pyglet.clock.unschedule(update)
# pyglet.clock.schedule(update,1)
pyglet.clock.schedule_interval(down, 2)
pyglet.clock.schedule_interval(update, 1)

pyglet.app.run()
