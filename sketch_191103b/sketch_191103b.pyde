add_library('minim')

minim = Minim(this)
beat = BeatDetect()

def setup():
    size(687, 690)
    global img
    img = loadImage("Prime Time.png")

    global start
    start = minim.loadSample("Prime Time.mp3")
    
    #for convert2circle mode
    global eRadius
    eRadius = 1.1
    global num
    num = 10


def draw():
    background(80)
    noStroke()
    
    Convert2Circle()
    Noise()
    
def keyPressed():
    if key == 'k': start.trigger()
    
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

        
