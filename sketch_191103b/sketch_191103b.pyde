add_library('minim')
add_library('video')
#add_library('opencv')


minim = Minim(this)
beat = BeatDetect()
cam = None
opencv = None

def setup():
    size(640, 480)
    
    global img
    img = loadImage("Prime Time.png")

    global start
    start = minim.loadSample("Prime Time.mp3")
    
    #Control modes with keyboard
    global cmode, snapmode, nmode, fmode
    cmode = 0
    snapmode = 0
    nmode = 0
    fmode = 0
    
    
    #for convert2circle mode
    global eRadius
    eRadius = 1.1
    global num
    num = 10
    
    #for snapshot func
    global cam
    #global opencv
    cam = Capture(this,640, 480)
    cam.start()
    #opencv = OpenCV(this, 640 / 2, 480 / 2)
    #opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)
       


def draw():
    background(80)
    noStroke()
    
    if(snapmode == 1):
        SnapShot()
        
    if(cmode == 1):
        Convert2Circle()
    
    if(nmode == 1):
        Noise()
    
    if(fmode == 1):
        Fountain()
        
    
    
def Convert2Circle():
    global num,eRadius
    
    beat.detect(start.mix)
    if(beat.isOnset()):
        #eRadius = 2
        num = 50
    
    for y in range(0,height,num):
        for x in range(0,width, num):
            bright_value = int(brightness(img.get(x,y)))
            map_value = map(bright_value,0,255,1,num)
            fill(img.get(x,y))
            #if(map_value>9):
            #    num = 20
                #ellipse(x,y,map_value*eRadius,map_value*eRadius)
            #else:
                #ellipse(x,y,map_value,map_value)
            ellipse(x,y,map_value,map_value)
    
    #eRadius *= 0.8
    #if(eRadius<1):
    #   eRadius=1
    if(num==50):
        num = 10

        
                        
def Noise():
    for y in range(0,height,8):
        for x in range(0,width,8):
            fill(random(230),50)
            noStroke()
            rect(x,y,8,8)

def SnapShot():
    image(cam,0,0)

def captureEvent(c):
    c.read()

#fountain mode
def Fountain():
    if(keyPressed('a')):
           print('hi')
    
            
def mousePressed():
    global img
    save("Face.jpg")
    img = loadImage("Face.jpg")
    print("saved!")
    
#Control with Keyboard
def keyPressed():
    global cmode, snapmode, nmode, fmode
    
    #Convert2Circle
    if(key=='c' and cmode==1):
        cmode = 0
    elif(key=='c'and cmode==0):
        cmode = 1
   
    #Snap mode
    if(key=='s' and snapmode==1):
        snapmode = 0
    elif(key=='s'and snapmode==0):
        snapmode = 1
    
    #Noise mode
    if(key=='n' and nmode==1):
        nmode = 0
    elif(key=='n'and nmode==0):
        nmode = 1    
        
    #Fountain mode
    if(key=='f' and fmode==1):
        fmode = 0
    elif(key=='f'and fmode==0):
        fmode = 1    
          
        
    if key == 'k': start.trigger()
    
        
