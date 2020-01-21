#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on August 09, 2019, at 11:18
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------Some-notes------------------------------------------ #

    # 0. This version requires the participant to right-click or left-click

    #1. **IMPORTANT** since the csv file contains french accents, when saving as csv file, you need to be carefule to select "UTF-8" type of csv, or error will happen
    
    #2. **IMPORTANT** format note: the header of the csv file must contain the following:
    
        # =================================================
        # ||    jarPicture    A    B    colorSequence    ||
        # =================================================
        
            # "jarPicture" stores the path of images of the jar
            # "A" is the dominant color in jarA
            # "B" stores the dominant color in jarB
            # "colorSequence" is a 10-character string, composed of A and B, indicating the sequence of the color
            
        # the names are case-sensitive, and mustn't be other names
        # order doesn't matter
        # Everything that is in the original csv file (e.g. the name of the trial) will be saved automatically in the resulting data file (THANKS YOU PSYCHOPY!)
        
    #3. If you are certain about your path and want to avoid user interface popping up everytime:
    
            # 1) around line 260, comment out these lines 
            
                # conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  
                 # if not conditionFile:
                #   core.quit
            
            # 2.1) place "  conditionFile[0]=["YOUR_FILE_PATH"] " after the above commented lines
            
            # OR:
            
            # 2.2) around line490, replace "conditionFile[0]" in "trialList=data.importConditions(conditionFile[0], selection=selectionGenerator(ramDistractor)),"  with your condition file path
                # path is a string type
                # remember to replace "/" with "\\" in windows (sometimes error occurs)
                
    #4. If you want to read codes, in case of naming, there are these objects displayed:
    
        # image (1 image object)                                                                -> image
        # balls (10 of them, circle shape objects)                                              -> ball0~ball9
        # 2 buttons subject (composed of 2 rectangular shape objects and two text objects)      -> buttonB1, buttonB2, buttonT1, buttonT2
        # slider                                                                                -> slider
        # slider value displayed                                                                -> sliderV
        # two questions (2 text objects)                                                        -> buttonS, sliderS
        
        # Namings of the variables will follow the rules semantically:
            # e.g. sliderH => slider height; sliderSH => slider subject height
    
    #5. unit of lengh = height (relative to the height of the screen)
        # (0,0) is at the center
        # may need adjustment according to computers
        
    #6. for the introduction picture, contain the picture in the same folder as the py file, and assign the name of the picture to the variable "placeboName"
        # name including the type of picture (e.g. picture_A.jpg)
        # Don't include the directory
    
        
# ----------------------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------------------- #


from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


# ----------------------------------------------------------------------------------------------- #


# -----some-functions-----

# function for initialization of component, or the object won't exit
def initiateComponent(Component):
    Component.tStart = None
    Component.tStop = None
    Component.tStartRefresh = None
    Component.tStopRefresh = None
    if hasattr(Component, 'status'):
        Component.status = NOT_STARTED
        
def initiateComponents(componentList):
    for thisComponent in componentList:
        initiateComponent(thisComponent)

# start and update time and frame of the component
def componentUpdate(component, time, frameN):
    
     # set the component to start
    if component.status == NOT_STARTED:
        # keep track of stop time/frame for later
        component.setAutoDraw(True)  #start the component (will set status = started)
        component.tStart = time
        component.frameNStart = frameN
        win.timeOnFlip(component, 'tStartRefresh')
        
    # update if the component has started
    if component.status == STARTED:
        # keep track of stop time/frame for later
        component.tStop = time# not accounting for scr refresh
        component.frameNStop = frameN  # exact frame index
        win.timeOnFlip(component, 'tStopRefresh')  # time at next scr refresh
        
def adjustImg(img, img_dir, sizeRatio):
    img.setImage(img_dir)
    img.size = img.size*sizeRatio


# ---------------------------------------------some-variables---------------------------------------------

# number of practice

numPractice = 0

# ---------------option for random trial---------------

# If set this to False, the distractor trials will be in-order
# If true, the order of distractor trial will be randomized (with the target trial always be at the second trial)

ramDistractor = False 

# --------------- timing parameters (unit = second) ---------------

waitingTime = 0        # time between each trial
timeConfidence = 1.5     # time waited after rating on the slider

# --------------- text ---------------

placeboName = "Beadspic.png"
cornerImgName = "mouse_instr.png"
cornerImg2Name = "mouse_instr.png"

expTitleText = "Tâche de Billes"

introTextTP1 = """Dans cet exercice, nous vous montrerons deux pots remplis de 100 billes colorées similaires à ceux ci-haut. Un pot contiendra 85% de billes d’une seule couleur (dans ce cas-ci, jaune) et 15% de billes d’une autre couleur (dans ce cas-ci, rouge). L’autre pot contiendra des billes colorées dans le ratio opposé.\n"""
introTextTP2 = """Pour chaque essai, un des pots sera sélectionné au hasard et vous ne saurez pas lequel. L’ordinateur va piger des billes dans le pot sélectionné. Votre tâche est de décider de quel pot sont pigées les billes. Vous pouvez continuer de demander des billes jusqu’à ce que vous vous sentiez confiant de votre décision. Les pots ne seront pas échangés au milieu du jeu."""
goodbyeTextT = 'Merci de votre participation.'


screenTextT = "Prêt à commencer? Questions?"    # text appear on a blank screen after practice trial


ballSText = ""      # The test displayed as instructions during trial if needed
ballSText2 = ""     # text displayed at the last ball
buttonSText = "De quel pot viennent les billes? SVP selectionnez:"
sliderSText = "SVP évaluer votre degré de confiance:"

# ----- color of the button -----

# ----- default -----
buttonBox1Color1 = "white"
buttonBox1LColor1 = "white"
buttonBox2Color1 = "white"
buttonBox2LColor1 = "white"
buttonT1Color1 = "black"
buttonT2Color1 = "black"

# ----- clicked -----
buttonBox1Color2 = "black"
buttonBox1LColor2 = "black"
buttonBox2Color2 = "black"
buttonBox2LColor2 = "black"
buttonT1Color2 = "white"
buttonT2Color2 = "white"

# --------------- physical properties ---------------

# ----- slider values -----

sliderStartP = 0            # starting value
sliderEndP = 1              # ending value
sliderStartT = "0%"         # text on the right
sliderEndT = "100%"         # text on the left

# -----------------position and sizes-----------------

# -----intro img-----

introImgSizeRatio = 1  # shrinking or manifiying the size of the image

introImgX = 0
introImgY = 0.15

# ----- corner img -----

cornerImgSizeRatio = 0.5
cornerImgX = 0
cornerImgY = -0.35

# ----- the corner img during trial -----

cornerImg2SizeRatio = 0.5
cornerImg2X = -0.7
cornerImg2Y = 0.4

# ----- title & introText & blank screen & goodbyeText & screen text-----

# title
expTitleH = 0.05     # text size
expTitlePos = (0, 0.40)

# intro
introTextH = 0.03   # text size
introTextW = 1.5    # wrap width of the introduction text
introTexPos = (0, -0.20)

# goodbye
goodbyeTextH = 0.05
goodbyeTextX = 0
goodbyeTextY = 0

# screentext
screenTextX = 0
screenTextY = 0
screenTextH = 0.1


# ----- trial image -----

imgX = 0
imgY = 0.3

# ----- ball & ball subject-----

# ball

ballD = 0.15        # distance between each ball, from center to center
ballR = 0.04        # radius of the ball

ballX1 = -5*ballD+ballD/2     # The x-position of the first ball, note that this needs to be stated after ballD
ballY = 0                     # y-position of all the balls

# ball subject 
ballSH = 0.02
ballSX = 0
ballSY = 0.1

# ----- buttonbox & text & question(subject) -----

# button box & text
buttonTH = 0.03     # size of text on the button

buttonBH = 0.05     # height of box
buttonBW = 0.14     # width of box
button1X = -0.15               # x-position of the jarA button and the text
button2X = 0.15                # x-position of the jarB button and the text
buttonY = -0.2                # y-position of the buttons and the texts

pos1 = (button1X, buttonY)
pos2 = (button2X, buttonY)

# button subject
buttonSH = 0.03     # text size of first question
buttonSX = 0                  # x-position of the first question
buttonSY = -0.1               # y-position of the first question

    
# ----- slider & slider subject & value -----

# slider
sliderH = 0.03      # height of slider
sliderW = 1.4       # width of slider
sliderX = 0                   # x-position of slider
sliderY = -0.35               # y-position of slider

# slider subject
sliderSH = 0.03     # size of text of the second question
sliderSX = 0                  # the x-position of the slider subject
sliderSY = -0.3               # y-position of the slider subject

# slider value
sliderVH = 0.020
sliderVX = 0                 
sliderVY = -0.4               # should be lower than the slider


# ---------------------------------------------------------------------------------------------------------



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

placeboDir = _thisDir + os.sep + placeboName
cornerImgDir = _thisDir + os.sep + cornerImgName
cornerImg2Dir = _thisDir + os.sep + cornerImg2Name

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'beadsTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
    
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])


# user interface to open up a condition file
    # a list object, save the path(including the name) of the file selected, conditionFile[0] gives the file name string
#conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv") 
#if not conditionFile:  # if there is no selection, quit experiment
#    core.quit
    
conditionFile=["C:\\Users\\CRISPlab\\Documents\\CognitiveBiasesStudy\\Tasks\\3-Beads\\beadsTaskConditions.csv"]

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)    # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp


# Start Code - component code to be run before the window creation
# Setup the Window
win = visual.Window(
    size = (1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color="Gainsboro", colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


defaultKeyboard = keyboard.Keyboard()       # create a default keyboard (e.g. to check for escape)
myMouse = event.Mouse(win=win)              # create a default mouse
myMouse2 = event.Mouse(win=win)             # second mouse for second question

# ---------- Initialize components for Routine "Instruction" ----------


# -----image-----

introImg = visual.ImageStim(
    win=win,
    name='introImg', 
    image=None, mask=None,
    ori=0, pos=(introImgX, introImgY),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

cornerImg = visual.ImageStim(
    win=win,
    name='cornerImg', 
    image=None, mask=None,
    ori=0, pos=(cornerImgX, cornerImgY),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
cornerImg2 = visual.ImageStim(
    win=win,
    name='cornerImg2', 
    image=None, mask=None,
    ori=0, pos=(cornerImg2X, cornerImg2Y),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)



introText = visual.TextStim(win=win, name='introText',
    text = introTextTP1,    
    font='Arial',
    pos=introTexPos, height=introTextH, wrapWidth=introTextW, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


expTitle = visual.TextStim(win=win, name='introText',
    text = expTitleText,    
    font='Arial',
    pos=expTitlePos, height=expTitleH, bold=True, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

instructionComponents = [introImg, cornerImg, introText, expTitle]

# ---------- Initialize components for Routine "Trial" ----------


screenText = visual.TextStim(win=win, name='screenText',
    text=screenTextT,
    font='Arial',
    pos=(screenTextX, goodbyeTextY), height=screenTextH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None,
    ori=0, pos=(imgX, imgY),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# -----ball subject-----
ballS = visual.TextStim(win=win, name='ballS',
    text = ballSText,    
    font='Arial',
    pos=(ballSX, ballSY), height=ballSH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    

# -----balls-----
ballComponents = []
    # create 10 balls (ball0 to ball9), default fillColor = white, lineColor = black
    # and add all balls into the ballComponents list
for i in range(10):
    exec("ball{num} = visual.Circle(win, radius={r}, colorSpace='rgb', fillColor='White', lineColor='Black', pos=({posX},{posY}))\nballComponents.append(ball{num})".format(num=i, r=ballR, posX=ballX1+ballD*i, posY=ballY))


# -----button-subject-----
buttonS = visual.TextStim(win=win, name='buttonS',
    text = buttonSText,    
    font='Arial',
    pos=(buttonSX, buttonSY), height=buttonSH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# -----button text-----

buttonT1 = visual.TextStim(win=win, name='buttonT1',
    text = "POT A",    
    font='Arial',
    pos=pos1, height=buttonTH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
buttonT2 = visual.TextStim(win=win, name='buttonT2',
    text = "POT B",    
    font='Arial',
    pos=pos2, height=buttonTH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# -----button box-----

buttonB1 = visual.Rect(win, name="A",
        width=buttonBW, height =buttonBH, pos=pos1, fillColor="white")
buttonB2 = visual.Rect(win, name="B", 
        width=buttonBW, height =buttonBH, pos=pos2,fillColor="white")

buttonComponents = [buttonS, buttonB1, buttonB2, buttonT1, buttonT2]


# -----slider subject-----
sliderS = visual.TextStim(win=win, name='sliderS',
    text = sliderSText,    
    font='Arial',
    pos=(sliderSX, sliderSY), height=sliderSH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
# -----slider-----
slider = visual.Slider(win=win, name='slider',
    size=(sliderW, sliderH), pos=(sliderX, sliderY),
    ticks=(sliderStartP, sliderEndP),labels=(sliderStartT, sliderEndT),
    granularity=0, style=['rating'],
    color='Gray', font='HelveticaBold',
    flip=False)
    
# -----slider value-----

sliderV = visual.TextStim(win=win, name='sliderV1',
    text='',
    font='Arial',
    pos=(sliderVX, sliderVY), height=sliderVH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

sliderComponents = [sliderS, slider, sliderV]


# ---------- Initialize components for Routine "Goodbye" ----------

goodbyeText = visual.TextStim(win=win, name='goodbyeText',
    text=goodbyeTextT,
    font='Arial',
    pos=(goodbyeTextX, goodbyeTextY), height=goodbyeTextH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# ---------- some timers ----------


instructClock = core.Clock()
TrialClock = core.Clock()
globalClock = core.Clock()
sliderTimer = core.CountdownTimer(timeConfidence)





#---------------------------------------------------------------------------#
#-----------------------------------INTRO-----------------------------------#
#---------------------------------------------------------------------------#


# ------Prepare to start Routine "intro"-------
t = 0
frameN = -1

# flow control variable
count = 0

# update component parameters for each repeat
# initialize the instruction text
initiateComponents(instructionComponents)
adjustImg(introImg, placeboDir, introImgSizeRatio)
adjustImg(cornerImg, cornerImgDir, cornerImgSizeRatio)

instructClock.reset()

# -------Start Routine "Instruction"-------
while True:
    
    
    
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(expTitle, t, frameN)
        componentUpdate(introText, t, frameN)
        componentUpdate(introImg, t, frameN)
        
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if defaultKeyboard.getKeys(keyList=["space"], clear=True):  # a forced-end of Routine when pressed space
        
        count += 1
        
        if count == 1:
            introText.setText(introTextTP2)
            componentUpdate(cornerImg, t, frameN)
            
        if count == 2:
            introText.setAutoDraw(False)
            expTitle.setAutoDraw(False)
            introImg.setAutoDraw(False)
            cornerImg.setAutoDraw(False)
            
            break
        
        
    # refresh the screen
    win.flip()
    
    

#----------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------- -----------------#
#-------------------------------------------Trial-------------------------------------------#
#-------------------------------------------------------------------------------------------#


# ---------- usefule lists ----------

adjustImg(cornerImg2, cornerImg2Dir, cornerImg2SizeRatio)


TrialComponents = [cornerImg2, image,screenText, ballS] + sliderComponents + buttonComponents + ballComponents
globalClock.reset()             # reset global clock, record the time for the entire trial

# ----- trial preparation -----

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditionFile[0]),
    seed=None, name='trials')
    
thisExp.addLoop(trials)                 # add the loop to the experiment
thisTrial = trials.trialList[0]         # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName)) 

# ----- enter one trial -----

for thisTrial in trials:
    currentLoop = trials
    
    if thisTrial != None:               # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    
    # ----- initiate components -----
    
    initiateComponents(TrialComponents)
    
    
    # ----- check for practice trial, loop before start of formal trial -----
    if trials.thisN == numPractice:
        
        screenText.setText(screenTextT)
        screenClock = core.Clock()
        
        t = 0
        frameN = -1
        screenClock.reset()
            
        while True:
            
            # get current time
            t = screenClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            
            # update/draw components on each frame
            componentUpdate(screenText, t, frameN)
                
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if defaultKeyboard.getKeys(keyList=["space"]): 
                screenText.setAutoDraw(False)
                
                break
                
            win.flip()
    
    
    
    
    
    # ----- record trial dominant color -----
    
    isMatch = None      # place holder, whether the selected jar matches the dominant jar
    domiJar = None      # place holder
    oriA = A            # store original colors
    oriB = B
    
    # randomize color A and B
        # notice that this is "pseudo-random"
        # p[0~0.5) = 50%
        # p[0.5~1) = 50%
    if np.random.random()>=0.5:     # generate a floating point between 0(inclusive) and 1(exclusive)
        A,B = B,A                   # switch the color
    
    # check whether color after switch equals original color
        # if switch, the dominant jar is jarB (since originally it's jarA)
    if oriA == A:
        domiJar = "A"
    else:
        domiJar = "B"
    
    # ----------------Prepare to start Routine "Trial"-----------------
    
    t = 0
    frameN = -1
    
    # ----- set trial properties-----
    
    slider.reset()                  # reset slider
    sliderV.setText("")                 # reset text
    image.setImage(jarPicture)      # set image
    ballS.setText(ballSText)        # Change instruction
    
    buttonB1.setFillColor(buttonBox1Color1)
    buttonB1.setLineColor(buttonBox1LColor1)
    buttonB2.setFillColor(buttonBox2Color1)
    buttonB2.setLineColor(buttonBox2LColor1)
    buttonT1.setColor(buttonT1Color1)
    buttonT2.setColor(buttonT2Color1)
    
    trialBallComponents = ballComponents.copy()                       # copy the ball component s.t. the original copy will not be messed around
    for thisBall,thisColor in zip(ballComponents,colorSequence):
        exec("thisBall.fillColor = {}".format(thisColor))             #corlor the ball with the sequence given
    
    trialBallComponents.reverse()                                     # reverse the list s.t the last one is the first, convinience for popping up
    firstBall = trialBallComponents.pop()                             # get the first ball, now 9 balls are left in the list
    
    # ----- place-holders -----
    
    mouseClicks=[0,0,0]       # lists for mouse clicks
    sliderRecord = None       # slider rating
    sliderOri = None          # original slider rating (used for check whether changes has been made)
    buttonClicked = None      # jar selected
    ballStop = 1              # number of balls before clicking
    
    # ----- wait before start each trial -----
    
    core.wait(waitingTime)
    
    # ----- reset the timers just before start -----
        
    myMouse.clickReset()                # reset the mouse timing point to 0 (the time stamp will be based on this)
    TrialClock.reset()                  # reset the trial clock
    globalClock.reset()
    
    # --------------- Start Routine "Trial" ---------------
    
    # outer loop for checking whether the slider has been rated
    # any rating = instant finishi this trial

   # while True:
        
        # inner loop for poping up ball
        # any click on the mouse will end the loop
        
    while sliderRecord == None:
        
        while mouseClicks[2] != 1 and ballStop!=11:        # when there is no right click
            
            # --------------- update/draw components on each frame ---------------
            
            t = TrialClock.getTime()            # get current time in second
            frameN = frameN + 1                 # number of completed frames (so 0 is the first frame)
            
            # ----- image & question updates -----
            
            componentUpdate(cornerImg2, t, frameN)
            componentUpdate(image, t, frameN)
            componentUpdate(ballS, t, frameN)
            
            if len(trialBallComponents) == 0 :
                ballS.setText(ballSText2)                     # Change instruction at the 10th bead
            
            
            # ----- show the first ball -----
            
            componentUpdate(firstBall, t, frameN)
            
            # ----- check click -----
            
            mouseClicks = myMouse.getPressed()
            
            # ----- pop up balls -----
            
            if mouseClicks[0]==1:                           # when there is a left click, if there are balls in the list, pop up the next one
                
                if len(trialBallComponents)>0:
                    
                    while True:
                        
                        t = TrialClock.getTime()            # get current time in second
                        frameN = frameN + 1                 # number of completed frames (so 0 is the first frame)
                       
                        if myMouse.getPressed()==[0,0,0]:                                    # only show the ball after release
                            
                            componentUpdate(trialBallComponents.pop(), t, frameN)             # pop up a ball
                            ballStop = 10-len(trialBallComponents)                            # update ballStop
                            
                            break
                        
                        win.flip()
                        
                elif len(trialBallComponents)==0:
                    
                    while True:
                        
                        frameN = frameN + 1                       # number of completed frames (so 0 is the first frame)
                        
                        if myMouse.getPressed()==[0,0,0]:       # only show the ball after release
                            ballStop = 11
                            
                            break
                    
                        win.flip()
                        
                            
            # ----- check right click and special keys -----
                
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):    # check for quit (typically the Esc key)
                core.quit()
                
            
            win.flip()    # flip fo to next frame
        
        
        if ballStop == 11:      
               break       # end trial, skip everything below
        
        current = myMouse.getPressed()                                     # check current state of mouse, avoid continueous activation
        
        if current != mouseClicks and slider.status == NOT_STARTED:        # after release of mouse press, before start of the slider
            
            while True:
                
                t = TrialClock.getTime()             # get current time
                frameN = frameN + 1                  # number of completed frames (so 0 is the first frame)
                
                # ----- start two buttons and the first question -----
                
                for thisComponent in buttonComponents:
                    componentUpdate(thisComponent, t, frameN)
                
                # ----- After selection of which jar -----
                # if pressed on any of the button, exit the loop
                
                if myMouse.isPressedIn(buttonB1):          
                    
                    buttonClicked = buttonB1.name          # store jar selected
                    componentUpdate(slider, t, frameN)      # start slider subject
                    componentUpdate(sliderS, t, frameN)     # start slider
                    componentUpdate(sliderV, t, frameN)     # start slider
                    
                    buttonB1.setFillColor(buttonBox1Color2)
                    buttonB1.setLineColor(buttonBox1LColor2)
                    buttonT1.setColor(buttonT1Color2)
                    
                    break
                
                if myMouse.isPressedIn(buttonB2):
                    
                    buttonClicked = buttonB2.name          # store jar selected
                    componentUpdate(slider, t, frameN)      # start slider subject
                    componentUpdate(sliderS, t, frameN)     # start slider
                    componentUpdate(sliderV, t, frameN)     # start slider
                    
                    buttonB2.setFillColor(buttonBox2Color2)
                    buttonB2.setLineColor(buttonBox2LColor2)
                    buttonT2.setColor(buttonT2Color2)
                    
                    break
                    
                # ----- check special keys -----
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    
                win.flip()
        
        
        
        # ----- check and store the rating on the slider -----
        
        if slider.status == STARTED:
            
            hasRated = False
            
            while True:       # wait for the rating
                
                # when has not rated, check change in selection
                if not hasRated:
                    
                    if myMouse.isPressedIn(buttonB1):          
                        
                        buttonClicked = buttonB1.name          # store jar selected
                        componentUpdate(slider, t, frameN)      # start slider subject
                        componentUpdate(sliderS, t, frameN)     # start slider
                        componentUpdate(sliderV, t, frameN)     # start slider
                        
                        buttonB1.setFillColor(buttonBox1Color2)
                        buttonB1.setLineColor(buttonBox1LColor2)
                        buttonT1.setColor(buttonT1Color2)

                        buttonB2.setFillColor(buttonBox2Color1)
                        buttonB2.setLineColor(buttonBox2LColor1)
                        buttonT2.setColor(buttonT2Color1)
                        
                    
                    if myMouse.isPressedIn(buttonB2):
                        
                        buttonClicked = buttonB2.name          # store jar selected
                        componentUpdate(slider, t, frameN)      # start slider subject
                        componentUpdate(sliderS, t, frameN)     # start slider
                        componentUpdate(sliderV, t, frameN)     # start slider
                        
                        buttonB2.setFillColor(buttonBox2Color2)
                        buttonB2.setLineColor(buttonBox2LColor2)
                        buttonT2.setColor(buttonT2Color2)
                        
                        buttonB1.setFillColor(buttonBox2Color1)
                        buttonB1.setLineColor(buttonBox2LColor1)
                        buttonT1.setColor(buttonT2Color1)
                        
                        
                        
                
                sliderRecord = slider.getRating()
                sliderMark = slider.markerPos
                
                
                if sliderMark != sliderRecord:            # when marker is moving
                    sliderV.setText("{r:1.0f}%".format(r=slider.markerPos*100))     # set percentage value
                    sliderTimer.reset(timeConfidence)           # reset cound-down timer
                    
                if sliderRecord != sliderOri:            # when the slider rating has been changed
                    sliderOri = sliderRecord             # update sliderOri
                    sliderTimer.reset(timeConfidence)    # update countdown timer
                    hasRated = True
                
                if sliderTimer.getTime()<=0:
                    break
                
                # ----- check special keys -----
            
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):        # check for quit (typically the Esc key)
                    core.quit()
                    
                win.flip()
            
    
        # ----- check special keys -----
        
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):        # check for quit (typically the Esc key)
            core.quit()
        
        
        frameN += 1
        win.flip()
    # ---------- Ending Trial ----------
    
    trialDuration = globalClock.getTime()       # ge ending time
    
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ---------- record data ----------
    
    
    
    trials.addData("DrawsToDecision", ballStop)          # number of balls before click, 11 if no decision happend
    trials.addData("SelectedJar", buttonClicked)           # button clicked, store "jarA" or "jarB"
    
    if buttonClicked != None:
        if buttonClicked == domiJar:
            trials.addData("match", 1)                         # whether selected jar matches the dominant jar
        else:
            trials.addData("match", 0)                         # no match
    else:
        trials.addData("match", -88)                          # when they didn't respond even after the 10th bead
    
    if sliderRecord == None:
        sliderRecord = -88
    
    trials.addData("TrialDuration", trialDuration)         # duration of entier trial
    trials.addData("ConfidenceRating",sliderRecord)        # rating of confidence from the slider
    trials.addData("DominantJar", domiJar)                 # which one is the dominant jar, jarA or jarB
    trials.addData("TrialDomiColor", A)                    # dominant color
    trials.addData("TrialNonDomiColor", B)                 # non-dominant color
    trials.addData("IsRandomDistractor", ramDistractor)    # whether the trial has been randomized
    trials.addData("AllowedDecisionTime", timeConfidence)  # the waiting time for slider
    
    thisExp.nextEntry()      # enter next experiment
    win.flip()               # flip for next frame
    
# completed 1 repeats of 'trials'
    

#----------------------------------------------------------------------------------------------------









#---------------------------------------------------------------------------#
#----------------------------------Goodbye----------------------------------#
#---------------------------------------------------------------------------#


win.flip()  # move to next frame

# ------Prepare to start Routine "Instruction"-------
t = 0
instructClock.reset()                  # reusing the clock for intro
frameN = -1



initiateComponent(goodbyeText)      # initialize goodbye text


# -------Start Routine "goodBye"-------


while True:
    
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    
    # update/draw components on each frame
    componentUpdate(goodbyeText, t, frameN)
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if defaultKeyboard.getKeys(keyList=["space"]): 
        goodbyeText.setAutoDraw(False)
        
        break
    
    # refresh the screen
    win.flip()


#----------------------------------------------------------------------------------------------------




# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
