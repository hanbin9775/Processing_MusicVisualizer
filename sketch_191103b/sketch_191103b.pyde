add_library('minim')
add_library('video')
add_library('opencv_processing')

minim = Minim(this)
beat = BeatDetect()
cam = None
opencv = None


class Emoji:
    def __init__(self):
        self.x = random(width)
        self.s = random(30,50)
        self.xs = -1 * random(2,10)
        self.y = random(height)
        #set emoji to fish first time
        self.emoji = loadImage("fish.png")
        
    def display(self):
        stroke(0)
        for face in faces:
            #detect mouth using face informations.
            if(dist(face.x+face.width/2,face.y+face.height*3/5, self.x, self.y) <30):
                if(mode==0):
                    self.emoji = loadImage("sushi.png")
                elif(mode==1):
                    self.emoji = loadImage("a_cheese.png")
                elif(mode==2):
                    self.emoji = loadImage("b_bacon.png")
                elif(mode==3):
                    self.emoji = loadImage("c_fried.png")
                elif(mode==4):
                    self.emoji = loadImage("d_ken.png")
                elif(mode==5):
                    self.emoji = loadImage("e_noodle.png")
                elif(mode==6):
                    self.emoji = loadImage("f_haribowhite.png")
        image(self.emoji, self.x, self.y,self.s, self.s)
        if(self.s > 50):
            self.s = self.s/2
    
    def beatdetect(self):
        if(beat.isOnset()):
            self.s = self.s*2
        
    def move(self):
        self.x += self.xs
        if self.x < -self.s * 1.1:
            self.x = width + self.s * 1.1
            #need refactoring 
            if(mode==0):
                self.emoji = loadImage("fish.png")
            elif(mode==1):
                self.emoji = loadImage("a_cow.png")
            elif(mode==2):
                self.emoji = loadImage("b_pig.png")
            elif(mode==3):
                self.emoji = loadImage("c_egg.png")
            elif(mode==4):
                self.emoji = loadImage("d_chic.png")
            elif(mode==5):
                self.emoji = loadImage("e_coon.png")
            elif(mode==6):
                self.emoji = loadImage("f_bear.png")

def setup():
    size(320, 240)
    
    global bg1,bg2,bg3, sshot, rec
    bg1 = loadImage("UI1.png")
    bg2 = loadImage("choosemusic.png")
    bg3 = loadImage("UI3.png")


    global start
    start = minim.loadSample("19-2000.mp3")
    
    #State Machine
    global curState
    curState = 0
    
    #Control modes with keyboard
    global snapmode,fmode, cnt
    snapmode = 0
    fmode = 0
    cnt = 0
    
    #face tracking
    global opencv
    opencv = OpenCV(this, width, height)
    opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)
    
    #for snapshot func
    global cam
    #global opencv
    cam = Capture(this,width, height)
    cam.start()
    
    #for fish mode
    global fishes, mode
    mode =0
    fishes = list()
    for i in range(10):
        fishes.append(Emoji())
    

def draw():
    background(80)
    imageMode(CENTER)
    beat.detect(start.mix)
    if(snapmode == 1):
        SnapShot()
        Emojimove()
    SetState()
        
#Fish mode
def Emojimove():
    global fishes
    for i in range(10):
        fishes[i].display()
        fishes[i].move()
        fishes[i].beatdetect()

def SnapShot():
    opencv.loadImage(cam)
    image(cam,width/2,height/2)
    global faces
    faces = opencv.detect()

def captureEvent(c):
    c.read()

def DisplayNMusic(n):
    global curState, snapmode, fmode
    curState=2
    snapmode=1
    fmode =1
    global start
    if(n==0):
        start = minim.loadSample("19-2000.mp3")
    elif(n==1):
        start = minim.loadSample("overtime.mp3")
    elif(n==2):
        start = minim.loadSample("Explode.mp3")
    elif(n==3):
        start = minim.loadSample("waybackhome.mp3")
    elif(n==4):
        start = minim.loadSample("GoodTime.mp3")
    elif(n==5):
        start = minim.loadSample("runfree.mp3")
    start.trigger()
        
            
def mousePressed():
    global mode,curState, cnt
    print(str(mouseX) +' '+ str(mouseY))
    
    #start screen
    if(curState==0):
        curState=1
    #music select
    elif(curState==1):
        cnt =0
        if(mouseX>150 and mouseX<295 and mouseY>47 and mouseY<65):
            DisplayNMusic(0)
        if(mouseX>150 and mouseX<295 and mouseY>73 and mouseY<91):
            DisplayNMusic(1)
        if(mouseX>150 and mouseX<295 and mouseY>101 and mouseY<119):
            DisplayNMusic(2)
        if(mouseX>150 and mouseX<295 and mouseY>128 and mouseY<146):
            DisplayNMusic(3)
        if(mouseX>150 and mouseX<295 and mouseY>156 and mouseY<174):
            DisplayNMusic(4)
        if(mouseX>150 and mouseX<295 and mouseY>183 and mouseY<201):
            DisplayNMusic(5)                            
    #in game
    elif(curState==2):
        if(mouseX>107 and mouseX<125 and mouseY>206 and mouseY<224):
            mode = 1
        elif(mouseX>132 and mouseX<140 and mouseY>206 and mouseY<224):
            mode = 2
        elif(mouseX>157 and mouseX<165 and mouseY>206 and mouseY<224):
            mode = 3
        elif(mouseX>182 and mouseX<190 and mouseY>206 and mouseY<224):
            mode = 4
        elif(mouseX>207 and mouseX<215 and mouseY>206 and mouseY<224):
            mode = 5
        elif(mouseX>232 and mouseX<240 and mouseY>206 and mouseY<224):
            mode = 6
        #back to music choice
        elif(mouseX>10 and mouseX<76 and mouseY>207 and mouseY<222):
            curState=1
            start.close()
        #rewind
        elif(mouseX>257 and mouseX<311 and mouseY>208 and mouseY<223):
            start.close()
        elif(mouseX>264 and mouseX<305 and mouseY>14 and mouseY<23):
            filename = "picture" + str(cnt) + ".png"
            cnt +=1
            save(filename)
                
def SetState():
    global curState
    if(curState==0):
        image(bg1,width/2,height/2,width,height)
    if(curState==1):
        image(bg2,width/2,height/2,width,height)
    if(curState==2):
        image(bg3,width/2,height/2,width,height)    
    
            
#Control with Keyboard
def keyPressed():
    if key == 'k': start.trigger()
    
        
