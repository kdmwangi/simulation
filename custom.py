import random

import pyglet
from pyglet.gl import GL_LINE_STIPPLE
from pyglet.window import key, mouse

window = pyglet.window.Window(width=1240, height=800)

label = pyglet.text.Label('Hello, world', x=0, y=window.height // 2,
                          anchor_x='center', anchor_y='center')
window.set_caption("Game simulation")
game_on = True
batch = pyglet.graphics.Batch()


moving_car = ''

# line1 = pyglet.shapes.Line(x=0,y=40,x2=window.width,y2=40,width=2,color=(255,255,255))
# line2 = pyglet.shapes.Line(x=0,y=40,x2=window.width,y2=40,width=2,color=(255,255,255))
# the round-about island
island = pyglet.shapes.Circle(x=window.width / 2, y=window.height / 2, radius=40, color=(0, 255, 0))

# round-about lanes
circ1 = pyglet.shapes.Circle(x=(window.width) / 2, y=(window.height) / 2, radius=80)
circ2 = pyglet.shapes.Circle(x=(window.width) / 2, y=(window.height) / 2, radius=120)
circ3 = pyglet.shapes.Circle(x=(window.width) / 2, y=(window.height) / 2, radius=160)
circ4 = pyglet.shapes.Circle(x=(window.width) / 2, y=(window.height) / 2, radius=200)

circ1.opacity = 50
circ2.opacity = 50
circ3.opacity = 50
circ4.opacity = 50


def at_the_round(car, circ):
    print(car.x)
    print(circ.x-200)
    # if moving_car
    if (car.x) == (circ.x - 200):
        print("at the round ")


class Major:
    def __init__(self):
        self.line1 = pyglet.shapes.Line(x=0, y=10, x2=window.width, y2=10, width=4, color=(255, 255, 255), batch=batch)

        self.l = 2

    def road(self, x, y, x2, y2, width=4, color=(255, 255, 255), lane=None, batch=batch, type='normal', ca = []):
        if type == 'normal':
            self.l = 4
            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2
        if type =="lane1":
            self.cars = 2
            self.car_list = []
            self.name = type
            self.l = 4
            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'lane2':
            self.cars = 1
            self.name = type

            self.l = 4
            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == "lane3":
            self.cars = 2
            self.l = 2
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'lane4':
            self.cars = 4
            self.l = 4
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneR1':
            self.cars = 2
            self.l = 2
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneR2':
            self.cars = 1
            self.l = 1
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneR3':
            self.cars = 2
            self.l = 2
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneR4':
            self.cars = 4
            self.l = 4
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneM1':
            self.cars = 2
            self.l = 2
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneM2':
            self.cars = 1
            self.l = 1
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneM3':
            self.cars = 5
            self.l = 5
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneMU1':
            self.cars = 2
            self.l = 2
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneMU2':
            self.cars = 1
            self.l = 1
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name
        if type == 'laneMU3':
            self.cars = 5
            self.l = 5
            self.name = type

            self.line2 = pyglet.shapes.Line(x=x, y=y, x2=x2, y2=y2, width=4, batch=batch, color=color)
            return self.line2,self.cars, self.name




class Car:
    def __init__(self, x=30, y=20,width=30,height=15, color=(255, 255, 0)):
        self.car = pyglet.shapes.Rectangle(x=x, y=y, width=width, height=height, color=color, batch=batch)


# draw broken lines

def yell():
    y = 50
    y2 = 50
    for _ in range(1, 5):

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
mjl1 = Major().road(x=0, y=240, x2=(window.width / 2 - 120), y2=240)
sepMjrd = Major().road(x=0, y=400, x2=(window.width / 2 - 200), y2=400, width=5, color=(0, 255, 0), type="lane4")
sepMjrd2 = Major().road(x=(window.width / 2 + 200), y=400, x2=(window.width / 2 + 400), y2=400, width=5,
                        color=(0, 255, 0), type="laneR4")


mjl2 = Major().road(x=0, y=560, x2=(window.width / 2 - 120), y2=560)

cnts_yellow1 = Major().road(x=245, y=280, x2=460, y2=280, color=(255, 255, 0))
cnts_yellow2 = Major().road(x=245, y=320, x2=440, y2=320, color=(255, 255, 0))
cnts_yellow3 = Major().road(x=245, y=360, x2=420, y2=360, color=(255, 255, 0))

cnts_yellow4 = Major().road(x=245, y=440, x2=430, y2=440, color=(255, 255, 0),type='lane3')
cnts_yellow5 = Major().road(x=245, y=480, x2=440, y2=480, color=(255, 255, 0),type="lane2")
cnts_yellow6 = Major().road(x=245, y=520, x2=460, y2=520, color=(255, 255, 0),type="lane1")

# print(cnts_yellow6[1])


# lin = pyglet.shapes.Line(x=(window.width / 2 - 120), y=90, x2=(window.width / 2 - 120), y2=240, width=4, batch=batch)
lin = Major().road(x=(window.width / 2 - 120),y=90, x2=(window.width / 2 - 120), y2=240, width=4, batch=batch,
                   color=(255, 255, 255), type="laneM1")
lin2 = pyglet.shapes.Line(x=(window.width / 2 + 120), y=90, x2=(window.width / 2 + 120), y2=240, width=4, batch=batch)
lin3 = pyglet.shapes.Line(x=(window.width / 2), y=90, x2=(window.width / 2), y2=200, width=4, batch=batch,
                          color=(255, 255, 255))
lin4 = pyglet.shapes.Line(x=(window.width / 2 + 40), y=90, x2=(window.width / 2 + 40), y2=200, width=4, batch=batch,
                          color=(255, 255, 0))
lin5 = pyglet.shapes.Line(x=(window.width / 2 + 80), y=90, x2=(window.width / 2 + 80), y2=220, width=4, batch=batch,
                          color=(255, 255, 0))
lin6 = Major().road(x=(window.width / 2 - 80), y=90, x2=(window.width / 2 - 80), y2=220, width=4, batch=batch,
                          color=(255, 255, 0),type='laneM2')
lin7 = Major().road(x=(window.width / 2 - 40), y=90, x2=(window.width / 2 - 40), y2=200, width=4, batch=batch,
                          color=(255, 255, 0), type="laneM3")

# uplin = pyglet.shapes.Line(x=(window.width / 2), y=600, x2=(window.width / 2), y2=1000, width=4, batch=batch,
#                            color=(255, 255, 255))
uplin = Major().road(x=740, y=560, x2=740, y2=800, batch=batch, width=4, type="laneMU1")
uplin2 = Major().road(x=(window.width / 2 + 80), y=580, x2=(window.width / 2 + 80), y2=1000, width=4, batch=batch,
                            color=(255, 255, 0), type="laneMU2")
uplin3 = Major().road(x=(window.width / 2 + 40), y=600, x2=(window.width / 2 + 40), y2=1000, width=4, batch=batch,
                            color=(255, 255, 0),type="laneMU3")

uplin1 = pyglet.shapes.Line(x=(window.width / 2), y=600, x2=(window.width / 2), y2=1000, width=4, batch=batch,
                            color=(255, 255, 255))


uplin4 = pyglet.shapes.Line(x=(window.width / 2 - 80), y=580, x2=(window.width / 2 - 80), y2=1000, width=4, batch=batch,
                            color=(255, 255, 0))
uplin5 = pyglet.shapes.Line(x=(window.width / 2 - 40), y=600, x2=(window.width / 2 - 40), y2=1000, width=4, batch=batch,
                            color=(255, 255, 0))

greenfields = pyglet.shapes.Rectangle(x=30, y=105, width=400, height=120, color=(0, 255, 0), batch=batch)

lyn = pyglet.shapes.Line(x=500, y=560, x2=500, y2=800, batch=batch, width=4)

lyn3 = pyglet.shapes.Line(x=740, y=560, x2=900, y2=560, batch=batch, width=4)
lyn4 = pyglet.shapes.Line(x=740, y=240, x2=900, y2=240, batch=batch, width=4)

cnts_yellow7 = Major().road(x=780, y=280, x2=1000, y2=280, color=(255, 255, 0),type="laneR1")
cnts_yellow11 = Major().road(x=803, y=320, x2=1020, y2=320, color=(255, 255, 0),type="laneR2")

cnts_yellow8 = Major().road(x=815, y=360, x2=1020, y2=360, color=(255, 255, 0),type='laneR3')
cnts_yellow9 = Major().road(x=815, y=440, x2=1020, y2=440, color=(255, 255, 0))
cnts_yellow10 = Major().road(x=800, y=480, x2=1020, y2=480, color=(255, 255, 0))
cnts_yellow12 = Major().road(x=780, y=520, x2=1020, y2=520, color=(255, 255, 0))

# print(li)
# print("##########")
# print(line1.line1)
# print(label)
# car = Car(x=30, y=20, color=(255, 0, 255)).car
# car2 = Car(x=30, y=410, color=(255, 0, 0)).car
# car3 = Car(x=70, y=410, color=(255, 255, 0)).car
# car4 = Car(x=110, y=410, color=(255, 0, 255)).car

var = {}


def laneCars (number, lane):
    x = 30
    y=30

    print(lane)
    for cr in range(number):
        # print(lane[2])
        if lane[2] == 'lane1':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=x+340, y=530, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            x -= 40
        elif lane[2] == 'lane2':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []

            var[name] = Car(x=x+340, y=490,
                            color=(random.randrange(0, 255), random.randrange(10, 255), random.randrange(0, 255))).car
            x += 40
        elif lane[2] == 'lane3':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []

            var[name] = Car(x=x+340, y=450,
                            color=(random.randrange(0, 255), random.randrange(10, 255), random.randrange(0, 255))).car
            x -= 40
        elif lane[2] == 'lane4':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []

            var[name] = Car(x=x+340, y=410,
                            color=(random.randrange(0, 255), random.randrange(10, 255), random.randrange(0, 255))).car
            x -= 40
        elif lane[2] == "laneR1":
            # x = 840
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=x+800, y=250, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            x += 40
        elif lane[2] == 'laneR2':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=x+800, y=290, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            x += 40
        elif lane[2] == 'laneR3':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=x+800, y=330, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            x += 40
        elif lane[2] == 'laneR4':
            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=x+800, y=370, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            x += 40
        # y = 30

        elif lane[2] == 'laneM1':

            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=(window.width / 2 - 110), y=y+120,width=20,height=30, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            y += 40
        elif lane[2] == 'laneM2':

            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=(window.width / 2 - 70), y=y+140,width=20,height=30, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            y += 40
        elif lane[2] == 'laneM3':

            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=(window.width / 2 - 30), y=y-20,width=20,height=30, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            y += 40
        elif lane[2] == 'laneMU1':

            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=(window.width / 2 + 90), y=y+560,width=20,height=30, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            y += 40
        elif lane[2] == 'laneMU2':

            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=(window.width / 2 + 50), y=y+570,width=20,height=30, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            y += 40
        elif lane[2] == 'laneMU3':

            name = f"{lane[2]}{cr}"
            # Car().Car(x=30, y=410, color=(255, 0, 0)).car
            # color = []
            var[name] = Car(x=(window.width / 2 + 10), y=y+570,width=20,height=30, color=(random.randrange(0,255), random.randrange(10,255), random.randrange(0,255))).car
            y += 40

        # print(name)
    # for name in var:
    #     # name = Car(x=30, y=410, color=(255, 0, 0)).car
    #     # var.append(name)
    #     print(name)

    print(var)
    pass

laneCars(int(cnts_yellow6[1]),cnts_yellow6)
laneCars(int(cnts_yellow5[1]),cnts_yellow5)
laneCars(int(cnts_yellow7[1]),cnts_yellow7)
laneCars(int(sepMjrd[1]),sepMjrd)
laneCars(int(cnts_yellow4[1]),cnts_yellow4)
laneCars(int(cnts_yellow11[1]),cnts_yellow11)
laneCars(int(cnts_yellow8[1]),cnts_yellow8)
laneCars(int(sepMjrd2[1]),sepMjrd2)
laneCars(int(lin[1]),lin)
laneCars(int(lin6[1]),lin6)
laneCars(int(lin7[1]),lin7)
laneCars(int(uplin[1]),uplin)
laneCars(int(uplin2[1]),uplin2)
laneCars(int(uplin3[1]),uplin3)






# change line thickness
pyglet.gl.glLineWidth(4)
pyglet.gl.glPointSize(4)
# pass in the stipple function to glEnable, to allow antialiasing
pyglet.gl.glEnable(GL_LINE_STIPPLE)
# pyglet.gl.glEnable(GL_TRIANGLE_STIPPLE)

# give the pattern to the stipple function
pyglet.gl.glLineStipple(1, 0x00FF)


# pyglet.shapes.Line()

@window.event
def on_draw():
    window.clear()
    # label.x += 10
    line1.line1.draw()
    # li.draw()
    li.draw()
    # mjl1.draw()
    # label.y += 1
    # car.draw()
    # yellow.draw()
    label.draw()
    island.draw()
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 50, 200, 50)), ('c3B', (255, 255, 0, 255, 255, 0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 320, 250, 320)), ('c3B', (255, 255, 0, 255, 255, 0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 280, 250, 280)), ('c3B', (255, 255, 0, 255, 255, 0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 360, 250, 360)), ('c3B', (255, 255, 0, 255, 255, 0)))

    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 440, 250, 440)), ('c3B', (255, 255, 0, 255, 255, 0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 480, 250, 480)), ('c3B', (255, 255, 0, 255, 255, 0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2i', (0, 520, 250, 520)), ('c3B', (255, 255, 0, 255, 255, 0)))
    pyglet.graphics.draw(2, pyglet.graphics.GL_LINES, ('v2f', ((window.width / 2), 100, (window.width / 2), 140)),
                         ('c3B', (255, 255, 0, 255, 255, 0)))

    # cnts_yellow1.draw()
    batch.draw()

    pyglet.graphics.draw(3, pyglet.graphics.GL_TRIANGLES, ('v2i', (20, 100, 4, 135, 30, 170)))
    circ1.draw()
    circ2.draw()
    circ3.draw()
    circ4.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2f', ((window.width / 2 + 55), (window.height / 2 + 55), 30, 35))
                         )
    # print((circ4.x-200))
    # print(car2.x)
    if update(1):
        print(update(1))
        # window.clear()
        var['lane10'].x = 30
        var["lane10"].y = 410
        # batch.draw()


def down(dt):
    label.y -= 10


@window.event
def on_key_press(symbol, modifier):
    global moving_car
    if symbol == key.U:
        label.y += 40
    if symbol == key.LCTRL:
        pyglet.clock.unschedule(down)
    if symbol == key.RIGHT:
        print("right arrow presed")
        var[f'{moving_car}'].x += 10
    if symbol == key.PAGEUP:
        var[f'{moving_car}'].anchor_y += 40
        var[f'{moving_car}'].rotation = -90
    if symbol == key.UP:
        print("right arrow presed")
        var[f'{moving_car}'].y += 10

def select(x,y):
    global moving_car
    if 510<y <540:
        if 70 < x < 110:
            print("the last car")
            move = 'lane10'
            moving_car = move
            # window.remove_handlers(on_mouse_press)

            return move
        elif 30 < x < 60:
            move = 'lane11'
            moving_car = move
            # window.remove_handlers(on_mouse_press)

            print("the second last car")
            return move


@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        select(x,y)
        print("Left mouse pressed")
        print(x,y)


def update(dt):
    # print("a second has elapsed")
    # print(car2.y)
    # print(cnts_yellow4)
    yes = None
    if var['lane10'].y == (cnts_yellow4[0].y - 10) and var['lane10'].x >= (cnts_yellow4[0].x - 20):
        print("cant overtake")
        label_ovetake = pyglet.text.Label("Cant ovetake/change lanes", x=20, y=window.height - 100, batch=batch)
        # pyglet.app.exit()
        # remove_handlers() receives a function to freeze the event incase the condition is fulfilled
        # window.remove_handlers(on_key_press)
        yes = True
        return yes
    if moving_car != '':
        at_the_round(var[moving_car],circ4)
        # print('is empty')
    print(moving_car)
        # print(var)


    # if (car2.x) == (circ4.x - 200):
    #     print("at the round ")
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
