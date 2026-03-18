from cmu_graphics import *
background1 = Image('https://t3.ftcdn.net/jpg/04/73/34/22/360_F_473342226_mGRsjBL2bTou0qLefOEnOMAb2lTRI0wm.jpg',0,-43,height=460,width=450)
background2 =Image('https://directbravo.com/Flappy-Bird-Game/images/bg.png',0,-36,height=436,visible=False)
background3 = Image('https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/1d295c47434117.59621209cf137.gif',0,-66,height=470,visible=False)
#Rect(140,0,70,70,fill=rgb(130,193,207))
###
bird = Group()

birdBody=Oval(80,300,28,23,fill='black',border='black',borderWidth=1)
bodyShadow=Arc(80,303,23,14,90,180,fill='whitesmoke')
birdWing=Oval(69,303,15,10,fill='black',border='black',borderWidth=1,rotateAngle=12)
birdEye=Oval(87,297,14,12,fill='white',rotateAngle=-110,border='black',borderWidth=1)
birdEyeLine=Line(88,295,88.2 ,300,lineWidth=1.4)
birdBeak=Oval(90,305,17,8,fill='coral',border='black',borderWidth=1)
birdBeakLine=Line(98,305,84,305,lineWidth=1.4)
bird.add(birdBody)
bird.add(bodyShadow)
bird.add(birdEye)
bird.add(birdEyeLine)
bird.add(birdWing)
bird.add(birdBeak)
bird.add(birdBeakLine)


###

#15 apart 
pole1LowerBase=Line(220,314,220,214,fill=gradient('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),lineWidth=40)
pole1LowerTop=Rect(220,216,45,17,
    fill=gradient
    ('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),
    align='bottom',borderWidth=2,border='black')

pole1TopBase=Line(220,0,220,99,fill=gradient('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),lineWidth=40)
pole1TopTop=Rect(220,116,45,17,
    fill=gradient
    ('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),
    align='bottom',borderWidth=2,border='black')
    
    
###
pole2LowerBase=Line(440,314,440,214,fill=gradient('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),lineWidth=40)
pole2LowerTop=Rect(440,216,45,17,
    fill=gradient
    ('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),
    align='bottom',borderWidth=2,border='black')

pole2TopBase=Line(440,0,440,99,fill=gradient('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left'),lineWidth=40)
pole2TopTop=Rect(440,116,45,17,
    fill=gradient
    ('black','white','powderblue','powderblue','powderblue','skyblue','powderblue',start='left'),
    align='bottom',borderWidth=2,border='black')





pole1 = Group(pole1LowerBase,pole1LowerTop,pole1TopBase,pole1TopTop)

pole2 = Group(pole2LowerBase,pole2LowerTop,pole2TopBase,pole2TopTop)

pole1.visible=False
pole2.visible=False


###
pauseButton = Group()
PSB=Rect(6,6,30,32,fill='steelblue')
PSBB=Rect(8,8,26,26,fill='powderblue',border='white')
PSL1=Line(18,16,18,28,fill='white',lineWidth=3.2 )
PSL2=Line(24,28,24,16,fill='white',lineWidth=3.2)
pauseButton.add(PSB)
pauseButton.add(PSBB)
pauseButton.add(PSL1)
pauseButton.add(PSL2)

###

playButton = Group()
PB = Rect(6,6,30,32,fill='steelblue')
PBB = Rect(8,8,26,26,fill='powderblue',border='white')
playButtonbutton= Polygon(16,16,26,22,16,28,fill='white')


playButton.add(PB)
playButton.add(PBB)
playButton.add(playButtonbutton)
playButtonbutton.centerX+=1
playButton.visible=False
playButton.centerX=180
playButton.centerY=180
###

gameMessage = Label(
    'Click To Start',
    200,100,
    fill='steelblue',border='white',borderWidth=1,
    size=25,
    bold=True,
    font='orbitron'
    )
    ###
#movement
bird.centerX=115
bird.centerY=200
bird.dy=0
pole1.dx=0
pole2.dx=0
###
score = Label(0,200,23,size=40,fill='white',border='black',borderWidth=.6,bold=True,)#font='orbitron' )
endBox = Group(Rect(48,148,254,135,fill=rgb(55,64,85)),
    Rect(50,150,250,125,fill=rgb(221,217,149)),
    Rect(51,151,248,124,fill=rgb(221,217,149),border=rgb(224,221,158),borderWidth=4),
    Rect(51,151,248,124,fill=None,border='white',borderWidth=4,opacity=30),
    Label('SCORE',252,175,fill=rgb(206,172,89),font='monospace',size=15,bold=True),
    Label('BEST',255,230,fill=rgb(206,172,89),font='monospace',size=15,bold=True),
    Label('MEDAL',100,175,fill=rgb(206,172,89),font='monospace',size=15,bold=True),
    Line(55,156,295,156,fill=rgb(206,174,88)),
    Line(55,156,55,271,fill=rgb(206,174,88)),
    Line(300,276,50,276,fill=rgb(206,174,88),lineWidth=3),
    Circle(100,223.5,25,fill=rgb(208,204,140))
    )
endBox.visible=False
endBox.centerX=200
endBox.centerY=200

bestscore = Label(0,288,242.5,size=25,fill='white',border='black',borderWidth=.6,bold=True)
bestscore.visible=False

okbutton= Group()
RBB=Rect(73,203,104,35,fill='steelblue')
RB=Rect(75,205,100,28,fill='powderblue',border='white')
RBL=Label('OK',125,220,size=23,fill='white',bold=True,font='monospace',borderWidth=1)


newBird= Group()
NBB=Rect(73,203,104,35,fill='steelblue')
NB=Rect(75,205,100,28,fill='powderblue',border='white')
NBL=Label('???',125,220,size=23,fill='white',bold=True,font='monospace',borderWidth=1)

okbutton.add(RBB)
okbutton.add(RBL)
okbutton.add(RB)
RBL.toFront()
newBird.add(NBB)
newBird.add(NBL)
newBird.add(NB)
NBL.toFront()


okbutton.centerY=700
okbutton.centerX=280
newBird.centerY=700
newBird.centerX=280
okbutton.dy=0
newBird.dy=0
gameEndMessage = Label('GAME OVER',200,-400,bold=True,fill='steelblue',border='white',borderWidth=1,size=25,visible=False,font='orbitron')
gameEndMessage.dy=0

def retryGame():
    bird.centerX=115
    bird.centerY=200
    bird.rotateAngle=0
    bird.dy=0
    pole1.dx=0
    pole2.dx=0
    pole1.centerX=220
    pole2.centerX=440
    pole1.visible=False
    pole2.visible=False
    okbutton.visible=False
    newBird.visible=False

    gameEndMessage.visible=False
    gameMessage.visible=True
    endBox.visible=False
    okbutton.centerX=200
    okbutton.centerY=700
    
    newBird.centerY=700
    score.centerX=200
    score.size=40
    score.centerY=23
    score.value=0
    bestscore.visible=False
    gameEndMessage.centerY=-400
    pauseButton.visible=True

def endGame():
    pauseButton.visible=False
    okbutton.centerX=260
    newBird.centerX=140
    endBox.visible=True
    score.centerY=187.5
    score.centerX=288
    score.size=25
    
    bestscore.centerY=242.5
    bestscore.centerX=288
    bestscore.size=25
    okbutton.visible=True
    newBird.visible=True
    
    bird.toFront()
    pole1.dx=0
    pole2.dx=0
    bird.dy=0
    bird.centerY=305
    bird.rotateAngle=90
    gameEndMessage.toFront()
    okbutton.toFront()
    score.toFront()
    newBird.toFront()
    
    gameEndMessage.visible=True
    if gameEndMessage.centerY<100:
        gameEndMessage.dy=20
    else:
        gameEndMessage.dy=0
    
    if okbutton.centerY>305:
        okbutton.dy=-10
        score.visible=False
    else:
        okbutton.dy=0
        score.visible=True
        bestscore.visible=True
    if newBird.centerY>305:
        newBird.dy=-10
    else:
        newBird.dy=0
    
def onStep():
    
    pole2.centerX+=pole2.dx
    pole1.centerX+=pole1.dx
    bird.centerY+=bird.dy
    okbutton.centerY+=okbutton.dy
    newBird.centerY+=newBird.dy
    gameEndMessage.centerY+=gameEndMessage.dy
    
    if score.value>bestscore.value:
        bestscore.value=score.value
    

        
        
    if gameMessage.visible==False:
        pole1.dx=-4
        pole2.dx=-4
        bird.dy+=.7
        if bird.bottom>=315 or bird.bottom<=0:
            endGame()
        if pole1.visible==True and pole2.visible==True:
            if bird.hitsShape(pole1) or bird.hitsShape(pole2):
                endGame()
    
            
    if pole1.right<0:
        pole1.left=400
        pole1LowerBase.y2=randrange(102,314)
        pole1LowerTop.bottom=pole1LowerBase.top
        pole1TopBase.y2=pole1LowerBase.y2-119
        pole1TopTop.top=pole1TopBase.bottom
        if pole1.visible==False:
            pole1.visible=True
    if pole2.right<0:
        pole2.left=400
        pole2LowerBase.y2=randrange(102,314)
        pole2LowerTop.bottom=pole2LowerBase.top
        pole2TopBase.y2=pole2LowerBase.y2-119
        pole2TopTop.top=pole2TopBase.bottom
        if pole2.visible==False:
            pole2.visible=True
        
    if pole1.right==93:
        score.value+=1
    if pole2.right==93:
        score.value+=1
    
    if bird.dy>0:
        if bird.rotateAngle<=45:
            bird.rotateAngle+=11
    elif bird.dy<0:
        bird.rotateAngle=-45
    
def onMousePress(mouseX,mouseY):  
    if gameMessage.visible==True:
        gameMessage.visible=False
    if app.stepsPerSecond==30:
        bird.dy=0
        bird.dy-=6
    
    if pauseButton.contains(mouseX,mouseY):
         app.stepsPerSecond=0
         pauseButton.visible=False
         playButton.visible=True
         score.centerX=220
         score.centerY=180
    if playButton.contains(mouseX,mouseY):
        
        pauseButton.visible=True
        playButton.visible=False
        score.centerX=200
        score.centerY=23
        app.stepsPerSecond=30
    if okbutton.contains(mouseX,mouseY):
        retryGame()
        
    if newBird.contains(mouseX,mouseY) and background1.visible==True:
        birdBody.fill='gold'
        bodyShadow.fill='orange'
        birdWing.fill='khaki'
        background1.visible=False
        background2.visible=True
        PSB.fill=rgb(85, 48, 6)
        PSBB.fill='coral'
        PB.fill=rgb(85, 48, 6)
        PBB.fill='coral'
        pole1.fill=gradient('black','lightgreen','green','green','green','darkgreen','green','black',start='left')
        pole2.fill=gradient('black','lightgreen','green','green','green','darkgreen','green','black',start='left')
        gameEndMessage.fill='coral'
        gameMessage.fill='coral'
        RBB.fill=rgb(85, 48, 6)
        RB.fill='coral'
        NBB.fill=rgb(85, 48, 6)
        NB.fill='coral'
    elif newBird.contains(mouseX,mouseY) and background2.visible==True:
        birdBody.fill='black'
        birdBody.border=rgb(60,60,60)
        bodyShadow.fill='black'
        birdWing.fill='black'
        birdWing.border=rgb(60,60,60)
        birdBeak.fill='black'
        birdBeak.border=rgb(60,60,60)
        birdBeakLine.fill=rgb(60,60,60)
        birdEye.fill='black'
        birdEye.border=rgb(60,60,60)
        birdEyeLine.fill='crimson'
        background2.visible=False
        background3.visible=True
        
        PSB.fill=rgb(80,80,80)
        PSBB.fill='gray'
        PB.fill=rgb(80,80,80)
        PBB.fill='gray'
        pole1.fill=gradient('black','gray','dimgray','dimgray','dimgray',rgb(80,80,80),'dimgray','black',start='left')
        pole2.fill=gradient('black','gray','dimgray','dimgray','dimgray',rgb(80,80,80),'dimgray','black',start='left')
        gameEndMessage.fill='gray'
        gameMessage.fill='gray'
        RBB.fill=rgb(80,80,80)
        RB.fill='gray'
        NBB.fill=rgb(80,80,80)
        NB.fill='gray'
    elif newBird.contains(mouseX,mouseY) and background3.visible==True:
        birdBody.fill='black'
        birdBody.border='black'
        bodyShadow.fill='whitesmoke'
        birdWing.fill='black'
        birdWing.border='black'
        birdBeak.fill='coral'
        birdBeak.border='black'
        birdBeakLine.fill='black'
        birdEye.fill='white'
        birdEye.border='black'
        birdEyeLine.fill='black'
        background3.visible=False
        background1.visible=True
        
        PSB.fill='steelblue'
        PSBB.fill='powderblue'
        PB.fill='steelblue'
        PBB.fill='powderblue'
        pole1.fill=gradient('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left')
        pole2.fill=gradient('black','white','powderblue','powderblue','powderblue','skyblue','powderblue','black',start='left')
        gameEndMessage.fill='steelblue'
        gameMessage.fill='steelblue'
        RBB.fill='steelblue'
        RB.fill='powderblue'
        NBB.fill='steelblue'
        NB.fill='powderblue'
#     
def onKeyPress(key): #alternate controls
    if key=='space':
        if gameMessage.visible==True:
            gameMessage.visible=False
        if app.stepsPerSecond==30:
            bird.dy=0
            bird.dy-=6

cmu_graphics.run()