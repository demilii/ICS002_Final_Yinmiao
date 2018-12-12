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
a7 = False
a8 = False
a9 = False
a10 = False
a11 = False
a12 = False
a13 = False
a14 = False
a15 = False
a16 = False
a17 = False
a18 = False
a19 = False
a20 = False
a21 = False
a22 = False
a23 = False
a24 = False
a25 = False
a26 = False
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
            
            if g.v == 0 and game_start:
                s1.trigger()
                global a1
                a1 = True
                global st1
                st1 = millis()
                
            if g.v == 1 and game_start:
                s2.trigger()
                global a2
                a2 = True
                
            if g.v == 2 and game_start:
                s3.trigger()
                global a3,st3
                a3 = True
                st3 = millis()
                
            if g.v == 3 and game_start:
                s4.trigger()
                global a4
                a4 = True
                
            if g.v == 4 and game_start:
                s9.trigger()
                global a5
                a5 = True
                global st5
                st5 = millis()
                
            if g.v == 5 and game_start:
                s6.trigger()
                global a6
                a6 = True
                global st6
                st6 = millis()
                
            if g.v == 6 and game_start:
                s7.trigger()
                global a7
                a7 = True
                global st7
                st7 = millis()
                
            if g.v == 7 and game_start:
                s3.trigger()
                global a8
                a8 = True
                
            if g.v == 8 and game_start:
                s9.trigger()
                global a9
                a9 = True
                global st9
                st9 = millis()
                
            if g.v == 9 and game_start:
                s10.trigger()
                global a10
                a10 = True
            
            if g.v == 10 and game_start:
                s11.trigger()
                global a11
                a11 = True
                global st11
                st11 = millis()
            if g.v == 11 and game_start:
                s1.trigger()
                global a12
                a12 = True
                global st12
                st12 = millis()

            if g.v == 12 and game_start:
                s2.trigger()
                global a13
                a13 = True
                global st13
                st13 = millis()
                
            if g.v == 13 and game_start:
                s6.trigger()
                global a14
                a14 = True
                global st14
                st14 = millis()
                
            if g.v == 14 and game_start:
                s7.trigger()
                global a15
                a15 = True
                
            if g.v == 15 and game_start:
                s1.trigger()
                global a16
                a16 = True
                global st16
                st16 = millis()

            if g.v == 16 and game_start:
                s10.trigger()
                global a17
                a17 = True
                global st17
                st17 = millis()
                
            if g.v == 17 and game_start:
                s9.trigger()
                global a18
                a18 = True
                
                
            if g.v == 18 and game_start:
                s11.trigger()
                global a19 
                a19 = True
                global st19
                st19 = millis()
                
            if g.v == 19 and game_start:
                s4.trigger()
                global a20
                a20 = True
                global st20
                st20 = millis()
                
            if g.v == 20 and game_start:
                s11.trigger()
                global a21
                a21 = True
                global st21
                st21 = millis()
            if g.v == 21 and game_start:
                s2.trigger()
                global a22
                a22 = True
                
                
            if g.v == 22 and game_start:
                s1.trigger()
                global a23
                a23 = True
                global st23
                st23 = millis()
                
            if g.v == 23 and game_start:
                s4.trigger()
                global a24
                a24 = True
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
                
        if a7:
            animate3(2.15,c_list[(c_num+3)%7])
            global st7
            if millis()-st7>1000:
                global a7
                a7 = False
                
        if a8:
            animate4(450,700,[color(234,190,173),color(215,131,138),color(161,130,223),color(170,171,237)])
            
        if a9:
            animate1()
            global st9
            if millis() - st9 > 1500:
                global a9
                a9 = False
                
        if a10:
            animate2(c_list[(c_num+2)%7])
            
        if a11:
            animate5([500,650,950,1100,950,650],[500,240,240,500,760,760],color(248,212,186))
            global st11
            if millis() - st11 > 1000:
                global a11
                a11 = False
        
        if a12:
            animate6(1200,400,-PI/32,color(133,161,224))
            global st12
            if millis() - st12 > 800:
                global a12
                a12 = False
                
        if a13:
            animate5([300,400,650,800],[700,400,300,700],color(133,161,224))
            global st13
            if millis() - st13 >1000:
                global a13
                a13 = False
                
        if a14:
            animate1()
            if millis()-st14 > 800:
                global a14
                a14 = False
                
        if a15:
            animate2(color(79,150,119))
                
        if a16:
            animate3(3,color(208,226,245))
            global st16
            if millis()-st16>1000:
                global a16
                a16 = False
        if a17:
            animate6(1000,700,-PI/12,color(117,129,164))
            if millis() - st17 > 800:
                global a17
                a17 = False
        
        if a18:
            animate4(600,500,[color(238,191,66),color(215,219,183),color(229,95,56),color(214,88,89)])     
        
        if a19:
            animate1()
            global st19
            if millis() - st19 >1000:
                global a19
                a19 = False
                
        if a20:
            animate3(3.75,color(153,133,177))
            global st20
            if millis()-st20 > 1000:
                global a20
                a20 = False
                
        if a21:
            animate5([500,846,1192,846],[500,350,500,650],color(197,173,135))
            global st21
            if millis() - st21 > 800:
                global a21
                a21 = False
                
        if a22:
            animate2(color(131,107,162)) 
            
        if a23:
            animate6(300, 250,PI/12,color(217,111,93))
            if millis() - st23 > 800:
                global a23
                a23 = False
        if a24:
            animate4(1020,480,[color(169),color(236,201,153),color(245,235,201),color(207,219,204)])    
        
        if a25:
            animate3(5,color(198,86,71))
            if millis() - st25 > 1000:
                global a25
                a25 = False
                
        if a26:
            animate6(800,500,-PI/10,color(160,168,153))
            if millis() - st26 > 1000:
                global a26
                a26 = False
                
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
    pushStyle()
    noStroke()
    fill(151, 202, 203)
    rectMode(CENTER)
    rect(width / 2, height / 2, 500, 100)
    fill(255)
    text("click on the screen or press keys from 'a' to 'z'", width / 2, height / 2)
    popStyle()
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
        s9.trigger()
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
        
    if key == 'g':
        s7.trigger()
        global a7
        a7 = True
        global st7
        st7 = millis()

    if key == 'h':
        s3.trigger()
        global a8
        a8 = True
        
    if key == 'i':
        s9.trigger()
        global a9
        a9 = True
        global st9
        st9 = millis()
        
    if key == 'j':
        s10.trigger()
        global a10
        a10 = True
        
    if key == 'k':
        s11.trigger()
        global a11
        a11 = True
        global st11
        st11 = millis()
        
    if key == 'l':
        s1.trigger()
        global a12
        a12 = True
        global st12
        st12 = millis()
    if key == 'm':
        s2.trigger()
        global a13
        a13 = True
        global st13
        st13 = millis()
        
    if key == 'n':
        s6.trigger()
        global a14
        a14 = True
        global st14
        st14 = millis()
        
    if key == 'o':
        s7.trigger()
        global a15
        a15 = True
        
    if key == 'p':
        s1.trigger()
        global a16
        a16 = True
        global st16
        st16 = millis()
        
    if key == 'q':
        s10.trigger()
        global a17
        a17 = True
        global st17
        st17 = millis()
        
    if key == 'r':
        s9.trigger()
        global a18
        a18 = True
        
    if key == 's':
        s11.trigger()
        global a19 
        a19 = True
        global st19
        st19 = millis()
        
    if key == 't':
        s4.trigger()
        global a20
        a20 = True
        global st20
        st20 = millis()
        
    if key == 'u':
        s11.trigger()
        global a21
        a21 = True
        global st21
        st21 = millis()
    if key == 'v':
        s2.trigger()
        global a22
        a22 = True
        
    if key == 'w':
        s1.trigger()
        global a23
        a23 = True
        global st23
        st23 = millis()
    if key == 'x':
        s4.trigger()
        global a24
        a24 = True

    if key == 'y':
        s9.trigger()
        global a25
        a25 = True
        global st25
        st25 = millis()
        
    if key == 'z':
        s1.trigger()
        global a26
        a26 = True
        global st26
        st26 = millis()
        
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
        global a2,a2r,a10,a15,a22
        a2 = False
        a10 = False
        a15 = False
        a22 = False
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

    with pushStyle():
        noFill()
        strokeWeight(10)
        stroke(c[1])
        translate(0,0)
        rotate(angle_4)
        rectMode(CENTER)  
        rect(0,0,300,300)

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
    if angle_4 > PI/2:
        
        global a4,a8,a18,a24
        a4 = False
        a8 = False
        a18 = False
        a24 = False
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
    
    
