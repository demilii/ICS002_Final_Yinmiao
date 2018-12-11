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
s1 = audio.loadSample(path+"data/s1.wav")
s2 = audio.loadSample(path+"data/s2.wav")
s3 = audio.loadSample(path+"data/s3.wav")
s4 = audio.loadSample(path+"data/s4.wav")
s5 = audio.loadSample(path+"data/s5.wav")
s6 = audio.loadSample(path+"data/s6.wav")
s7 = audio.loadSample(path+"data/s7.wav")
s8 = audio.loadSample(path+"data/s8.wav")
s9 = audio.loadSample(path+"data/s9.wav")
s10 = audio.loadSample(path+"data/s10.wav")
s11 = audio.loadSample(path+"data/s11.wav")
s12 = audio.loadSample(path+"data/s12.wav")
a1 = False
global a2r 
a2r = 50
a2 = False
a3 = False
a4 = False
a5 = False
a6 = False
startAngle = 0
angle_4 = 0
# # class for each grid of rhythm machine
# class Rect:
#     def __init__(self,r,c):
#         self.r = r
#         self.c = c
#         self.w = 28
#         self.h = 60
#         self.cover = False
        
#     def display(self):
#         if self.cover == False:
#             noStroke()
#             fill(255,150)
#         else:
#             noStroke()
#             fill(100,200)
            
#         rect(self.r,self.c,self.w,self.h)
        
# # drum machine
# class drum:
#     pass

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
        if g:
            
            if g.v == 0 :
                global a1
                a1 = True
                global st1
                st1 = millis()
                s1.trigger()
            if g.v == 1:
                s2.trigger()
                global a2
                a2 = True
            if g.v == 2:
                s3.trigger()
                global a3,st3
                a3 = True
                st3 = millis()
            if g.v == 3:
                s4.trigger()
                global a4
                a4 = True
                
            if g.v == 4:
                s5.trigger()
                global a5
                a5 = True
                global st5
                st5 = millis()
                
            if g.v == 5:
                s6.trigger()
                global a6
                a6 = True
                global st6
                st6 = millis()
    
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
def draw():
    if game_start == False:
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
        global a1,a2,a3
        if a1:
            animate1()
            global st1
            if millis()-st1 >400:
                global a1
                a1 = False
                
        if a2:
            animate2(c_list[(c_num+3)%7])
            
        if a3:
            animate3(1.15,c_list[(c_num+1)%7])
            global st3
            if millis()-st3 >1000:
                global a3
                a3 = False
                
        if a4:
            animate4(900,400,[color(190,211,168),color(74,90,107),color(234,159,169),color(233,155,100)])

        if a5:
            animate5([600,400,800],[200,500,650],c_list[(c_num+2)%7])
            global st5
            if millis()-st5>1000:
                global a5
                a5 = False
                
        if a6:
            animate6(300,700,PI/16,c_list[4])
            global st6
            if millis()-st6 >800:
                global a6
                a6 = False
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

def mouseClicked():
    m.clicked()
    global game_start,gcnt
    if game_start and gcnt == 0:
        bgm.loop()
        gcnt+=1

def keyPressed():
    if key == 'a':
        s1.trigger()
        global a1
        a1 = True
        global st1
        st1 = millis()
        
    if key == 'b':
        s2.trigger()
        global a2
        a2 = True
        
    if key =='c':
        s3.trigger()
        global a3,st3
        a3 = True
        st3 = millis()
    if key == 'd':
        s4.trigger()
        global a4
        a4 = True
        
    if key == 'e':
        s5.trigger()
        global a5
        a5 = True
        global st5
        st5 = millis()
        
    if key == 'f':
        s6.trigger()
        global a6
        a6 = True
        global st6 
        st6 = millis()
        
def animate1():
    for i in range(3):
        a = random(width)
        b = random(height)
        stroke(random(255),random(255),random(255),250)
        strokeWeight(4)
        noFill()
        rect(a, b, 50, 50)
    
def animate2(c):
    global a2r
    noStroke()
    fill(c)
    ellipse(width/2,height/2,a2r,a2r)
    a2r+=15
    if a2r >400:
        global a2,a2r
        a2 = False
        a2r = 50
    
def animate3(scl,c):
    global startAngle
    angle = startAngle
    for i in range(0,width,10):
        y = sin(angle)*150+height/2
        y+=sin(angle*scl)*70
        stroke(c)
        strokeWeight(10)
        point(i,y)
        angle+=.1
        
    startAngle += .02
    
def animate4(x,y,c):
    
    global angle_4
    
    with pushStyle():
        noFill()
        strokeWeight(10)
        stroke(c[0])
        translate(x,y)
        rotate(angle_4)
        rectMode(CENTER)  
        rect(0,0,300,300)
    # noFill()
    # strokeWeight(10)
    # stroke(c[0])
    # rectMode(CENTER)   
    # translate(x[0],y[0])
    # rotate(angle_4)
    # rect(0,0,200,200)
    # popMatrix()

    with pushStyle():
        noFill()
        strokeWeight(10)
        stroke(c[1])
        translate(0,0)
        rotate(angle_4)
        rectMode(CENTER)  
        rect(0,0,300,300)
    # popStyle()
    with pushStyle():
        noFill()
        strokeWeight(10)
        stroke(c[2])
        translate(0,0)
        rotate(angle_4)
        rectMode(CENTER)  
        rect(0,0,280,280)
    with pushStyle():
        noFill()
        strokeWeight(10)
        stroke(c[3])
        translate(0,0)
        rotate(angle_4)
        rectMode(CENTER)  
        rect(0,0,280,280)
    angle_4 += PI/200
   
    
    # for i in range(len(x)):
    #     stroke(c[i])
    #     pushStyle()
    #     rectMode(CENTER)
    #     translate(x[i],y[i])
    #     rotate(angle_4)
    #     rect(0,0,200,200)
    #     popStyle()
    
    
    if angle_4 > PI/2:
        
        global a4
        a4 = False
        angle_4 = 0
        
        
def animate5(x,y,c):
    noFill()
    strokeWeight(10)
    stroke(c,random(255))
    global st5
    with beginShape():
        for i in range(len(x)):
            vertex(x[i],y[i])
        vertex(x[0],y[0])
        
def animate6(x,y,a,c):
    strokeWeight(80)
    pushStyle()
    stroke(c)
    translate(x,y)
    rotate(a)
    line(-200,-200,+200,+200)
    line(-200,+200,+200,-200)
    popStyle()
    
    
