import os
path = os.getcwd()+"/"
# game_start = False
def setup():
    fullScreen()
    global font
    font = createFont("Bellefair-Regular.ttf",32)
    global game_start
    game_start = False
    global ins
    ins = False
def draw():
    if game_start == False:
        gstart()
        g_boolean()
        if ins:
            drawIns()
    else:
        # draw
        background(151, 202, 203)
    
def gstart():
    background(151, 202, 203)
    textAlign(CENTER)
    textFont(font,45)
    fill(255)
    text("MELODY",width/2,height/2-height/16)
    textFont(font,35)
    fill(255)
    text("start",width/2,height/2)
    textFont(font,35)
    fill(255)
    text("instruction",width/2,height/2+2*height/64)
    
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
    rect(width/2, height/2,500,100)
    fill(255)
    text("click on the screen or press keys",width/2,height/2)
        
