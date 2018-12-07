add_library('minim')
import os
path = os.getcwd() + "/"
numRow = 4
numCol = 6
w_grid = 280
h_grid = 196.875
c_list = [color(151, 202, 203),color(232,80,120),color(87,79,86),color(58,134,151),color(219,97,133),color(240,213,202),color(77,167,157)]
audio = Minim(this)
out = None
kick = None
snare = None
hat = None
kick = audio.loadSample(path+"data/BD.wav")
snare = audio.loadSample(path+"data/SD.wav")
hat = audio.loadSample(path+"data/CHH.wav")
bgm = audio.loadFile(path+"data/bgm.mp3")


class Tile:
    def __init__(self, r, c,v):
        self.r = r
        self.c = c
        self.w = w_grid
        self.h = h_grid
        self.v = v
        # self.cover = False # check if the tile is cover
    
    def cover(self):
        noStroke()
        fill(220, 80)
        rect(self.c * self.w, self.r * self.h,self.w, self.h)

class Melody:

    def __init__(self):
        self.grid = []
        cnt = 0
        for r in range(numRow):
            for c in range(numCol):
                self.grid.append(Tile(r, c,cnt))
                cnt+=1

    def getTile(self, r, c):
        for g in self.grid:
            if g.r == r and g.c == c:
                return g
        return False

    def clicked(self):
        r = mouseY // h_grid
        c = mouseX // w_grid
        g = self.getTile(r,c)
        if g.v == 0:
            kick.trigger()
    
    def show(self):
        r = mouseY // h_grid
        c = mouseX // w_grid
        g = self.getTile(r, c)
        if g != False:
            g.cover()


m = Melody()
def setup():
    fullScreen( )
    global font
    font = createFont("Bellefair-Regular.ttf", 32)
    global game_start
    game_start = False
    global ins
    ins = False
    global h
    h = 3 * height / 4
    global w
    w = width
    global c_num
    c_num = 0
    global gcnt
    gcnt = 0
    # set up for minim library
    global out
    out = audio.getLineOut()
    out.setTempo(125)
    # bgm.loop()
    # bgm.setGain(0)
def draw():
    if game_start == False:
        bgm.setGain(0)
        gstart()
        g_boolean()
        if ins:
            drawIns()
    else:

        if frameCount% 1000 == 0:
            global c_num
            c_num+=1
        global c_num
        background(c_list[c_num%7])
        # println(m.grid)
        # bgm.loop()
        
        m.show()
        noStroke()
        fill(220,100)
        rect(0, h, width, height - h)
def gstart():
    background(151, 202, 203)
    textAlign(CENTER)
    textFont(font, 45)
    fill(255)
    text("MELODY", width / 2, height / 2 - height / 16)
    textFont(font, 35)
    fill(255)
    text("start", width / 2, height / 2)
    textFont(font, 35)
    fill(255)
    text("instruction", width / 2, height / 2 + 2 * height / 64)

def g_boolean():
    if mousePressed == True:
        if (mouseX > 800 and mouseX < 860) and (mouseY > 510 and mouseY < 530):
            global game_start
            game_start = True
        else:
            global game_start
            game_start = False

        if (mouseX > 750 and mouseX < 910) and (mouseY > 540 and mouseY < 560):
            global ins
            ins = True
        else:
            global ins
            ins = False

def drawIns():
    noStroke()
    fill(151, 202, 203)
    rectMode(CENTER)
    rect(width / 2, height / 2, 500, 100)
    fill(255)
    text("click on the screen or press keys", width / 2, height / 2)

def animate1():
    pass
    
def mouseClicked():
    m.clicked()
    global game_start,gcnt
    if game_start and gcnt == 0:
        bgm.loop()
        gcnt+=1
