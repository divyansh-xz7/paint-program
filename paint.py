import pygame as pg
import math
pg.init()

a=960
b=800

d=pg.display.set_mode((a,b))


blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)

color=black

w=1
i=0

mode="rect"
bucket=False

crashed=False
clock=pg.time.Clock()

d.fill(white)

######menu######

i1=pg.image.load('pencil.png')
i2=pg.image.load('square.png')
i3=pg.image.load('circle.png')
i4=pg.image.load('bucket.png')
i5=pg.image.load('text.png')
i6=pg.image.load('eraser.png')
i7=pg.image.load('clr.png')


######display text######
def text_objects(text, font):
    textsurface=font.render(text ,True ,black)
    return textsurface, textsurface.get_rect()

def message_display(text,h,k,size):
    largetext=pg.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect=text_objects(text, largetext)
    TextRect.center=(h,k)
    d.blit(TextSurf, TextRect)
    pg.display.update()


rectm=pg.Rect(0,0,160,b)
cx=0
cy=0
cz=0
lr=575
lg=575
lb=575

while crashed==False:

    color=(cx,cy,cz)

    

    #####menu#####
    d.fill(white,rectm)
    
    d.blit(i1,(0,0))
    d.blit(i2,(80,0))
    d.blit(i3,(80,80))
    d.blit(i4,(0,80))
    d.blit(i5,(0,160))
    d.blit(i6,(80,160))
    pg.draw.polygon(d,black,((0,240),(40,240),(40,280),(0,280)),0)
    pg.draw.polygon(d,blue,((40,240),(80,240),(80,280),(40,280)),0)
    pg.draw.polygon(d,red,((80,240),(120,240),(120,280),(80,280)),0)
    pg.draw.polygon(d,green,((120,240),(160,240),(160,280),(120,280)),0)
    pg.draw.aaline(d,color,(160,0),(162,b),4)
    d.blit(i7,(0,280))
    pg.draw.polygon(d,black,((22,320),(44,320),(44,575),(22,575)),1)
    pg.draw.polygon(d,black,((66,320),(88,320),(88,575),(66,575)),1)
    pg.draw.polygon(d,black,((110,320),(132,320),(132,575),(110,575)),1)
    
    rectcx=pg.Rect(23,lr,20,cx)
    d.fill(red,rectcx)
    
    rectcy=pg.Rect(67,lg,20,cy)
    d.fill(green,rectcy)
    
    rectcz=pg.Rect(111,lb,20,cz)
    d.fill(blue,rectcz)

    pg.draw.polygon(d,color,((22,600),(132,600),(132,700),(22,700)),0)
    

    


    ###mode highlight####
    if mode=="pencil":
        pg.draw.polygon(d,blue,((0,0),(0,80),(80,80),(80,0)),4)

    if mode=="rect":
        pg.draw.polygon(d,blue,((80,0),(156,0),(156,80),(80,80)),4)

    if mode=="circle":
        pg.draw.polygon(d,blue,((80,80),(156,80),(156,160),(80,160)),4)

    if bucket==True:
        pg.draw.polygon(d,blue,((0,80),(80,80),(80,160),(0,160)),4)

    if mode=="text":
        pg.draw.polygon(d,blue,((0,160),(80,160),(80,240),(0,240)),4)

    if mode=="eraser":
        pg.draw.polygon(d,blue,((80,160),(156,160),(156,240),(80,240)),4)
        

    
    
    
    
    x=pg.mouse.get_pos()
    pg.display.update()

    for event in pg.event.get():
        x=pg.mouse.get_pos()
        
        if event.type==pg.QUIT:
            crashed=True

        #####buttons######
        local=bucket
        if ((x[0] in range(0,int(a*0.16667))) and (event.type==(pg.MOUSEBUTTONDOWN or pg.MOUSEBUTTONUP))):
            if event.type==pg.MOUSEBUTTONDOWN:
                x=pg.mouse.get_pos()
                
                if (x[0] in range(0,80)) and (x[1] in range(0,80)):
                    mode="pencil"

                if (x[0] in range(80,160)) and (x[1] in range(0,80)):
                    mode="rect"

                if (x[0] in range(80,160)) and (x[1] in range(80,160)):
                    mode="circle"

                if (x[0] in range(0,80)) and (x[1] in range(80,160)):
                    if local==False:
                        bucket=True
                    elif local==True:
                        bucket=False

                if (x[0] in range(0,80)) and (x[1] in range(160,240)):
                    mode="text"

                if (x[0] in range(80,160)) and (x[1] in range(160,240)):
                    mode="eraser"

                if (x[0] in range(0,40)) and (x[1] in range(240,280)):
                    cx=0
                    cy=0
                    cz=0
                    
                if (x[0] in range(40,80)) and (x[1] in range(240,280)):
                    cx=0
                    cy=0
                    cz=255
                    lb=320

                if (x[0] in range(80,120)) and (x[1] in range(240,280)):
                    cx=255
                    cy=0
                    cz=0
                    lr=320

                if (x[0] in range(120,160)) and (x[1] in range(240,280)):
                    cx=0
                    cy=255
                    cz=0
                    lg=320

                if (x[0] in range(0,160)) and (x[1] in range(280,320)):
                    d.fill(white)

                if (x[0] in range(22,44)) and (x[1] in range(320,575)):
                    cx=575-x[1]
                    lr=x[1]

                
                if (x[0] in range(66,88)) and (x[1] in range(320,575)):
                    cy=575-x[1]
                    lg=x[1]

                if (x[0] in range(110,132)) and (x[1] in range(320,575)):
                    cz=575-x[1]
                    lb=x[1]

                
                    
        
            
        ######pencil######
        if x[0] in range(0,int(a*0.16667)):
            i=0
        if mode=="pencil" and (x[0] in range(int(a*0.16667),a)):
            if event.type==pg.MOUSEBUTTONDOWN:
                i=1
                x=pg.mouse.get_pos()
                pg.draw.circle(d,color,x,w)
            
            if event.type==pg.MOUSEBUTTONUP:
                i=0

            if i==1:
                x=pg.mouse.get_pos()
                pg.draw.circle(d,color,x,w)
                pg.display.update()


        ######circle######
        if mode=="circle" and (x[0] in range(int(a*0.16667),b)):
            if event.type==pg.MOUSEBUTTONDOWN:
                x1=pg.mouse.get_pos()
                i=1
            if x[0] in range(0,int(a*0.16667)):
                i=0
            if i==1:
                if event.type==pg.MOUSEBUTTONUP:
                    x2=pg.mouse.get_pos()
                    r=math.sqrt((((x1[0]-x2[0])**2)+((x1[1]-x2[1])**2)))
                    if bucket==False:
                        pg.draw.circle(d,color,x1,int(r))
                        pg.draw.circle(d,white,x1,int(r-w))
                    elif bucket==True:
                        pg.draw.circle(d,color,x1,int(r))
                        
                        
            pg.display.update()
                    
        #####rectangle#####
        if mode=="rect" and (x[0] in range(int(a*0.16667),a)):
            if event.type==pg.MOUSEBUTTONDOWN:
                x1=pg.mouse.get_pos()
                i=1
            if x[0] in range(0,int(a*0.16667)):
                i=0
            if i==1:
                if event.type==pg.MOUSEBUTTONUP:
                    x2=pg.mouse.get_pos()
                    if bucket==False:
                        pg.draw.polygon(d,color,((x1),(x1[0],x2[1]),(x2),(x2[0],x1[1])),w)
                    elif bucket==True:
                        pg.draw.polygon(d,color,((x1),(x1[0],x2[1]),(x2),(x2[0],x1[1])),0)
                        
                    pg.display.update()


        #####text######

        if mode=="text" and (x[0] in range(int(a*0.16667),a)):
            print("1")


        #######eraser#####

        if mode=="eraser" and (x[0] in range(int(a*0.16667),a)):
            if event.type==pg.MOUSEBUTTONDOWN:
                i=1
            if event.type==pg.MOUSEBUTTONUP:
                i=0
            if i==1:
                eh=50
                ew=50
                x=pg.mouse.get_pos()
                recte=pg.Rect(x[0]-ew,x[1]-eh,2*ew,2*eh)
                pg.draw.rect(d,black,recte,1)
                pg.display.update()
                d.fill(white,recte)
            
            
                    
        clock.tick(1200)
                
        
            







pg.quit()
quit()
    
    





