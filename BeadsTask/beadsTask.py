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
        # two questions (2 text objects)                                                        -> buttonS, sliderS
        
        # Namings of the variables will follow the rules semantically:
            # e.g. sliderH => slider height; sliderSH => slider subject height
    
    #5. unit of lengh = height (relative to the height of the screen)
        # (0,0) is at the center
        # may need adjustment according to computers
        
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

# generate a selection list for the condition file
    # makesure that "1" will alsways be at list[1].
    # 1. randomize 0th,2nd,3rd condition inside the condition filename
    # 2. insert "1" to the second position
    # 3. returns the list
def selectionGenerator(ramDistractor):
    
    if ramDistractor:
        thisList = [0,2,3] # since there are only 3 conditions which has no certian place
        np.random.shuffle(thisList) # shuffle elements
        thisList.insert(1, 1) # insert the second trial into the list[1]
        return thisList
    else:
        return [0,1,2,3]
    

# ---------------------------------------------some-variables---------------------------------------------

# ---------------option for random trial---------------

# If set this to False, the distractor trials will be in-order
# If true, the order of distractor trial will be randomized (with the target trial always be at the second trial)

ramDistractor = False 

# --------------- timing parameters (unit = second) ---------------

timePopUp = 1   # time between each ball popping up
waitingTime = 2 # time between each trial

# --------------- instruction text ---------------

introTextT = "This is the instruction, press space to start"
expTitleText = "Beads Task"
goodbyeTextT = 'Thank you for participating, press space to quit.'

buttonSText = "Which jar was the ball drawn? Please click on the button:"
sliderSText = "How confident are you with your decision?"

# --------------- physical properties ---------------

# ----- slider values -----

sliderStartP = 0            # starting value
sliderEndP = 1              # ending value
sliderStartT = "0%"         # text on the right
sliderEndT = "100%"         # text on the left

# -----size(width and height)-----

# intro and title
expTitleH = 0.1     # text size
introTextH = 0.03   # text size
introTextW = 1.5    # wrap width of the introduction text

# ball
ballD = 0.15        # distance between each ball, from center to center
ballR = 0.04        # radius of the ball

# button subject
buttonSH = 0.03     # text size of first question

# button box
buttonBH = 0.05     # height of box
buttonBW = 0.14     # width of box

# button text
buttonTH = 0.03     # size of text on the button

# slider subject
sliderSH = 0.03     # size of text of the second question

# slider
sliderW = 1.4       # width of slider
sliderH = 0.03      # height of slider

# goodbyeText
goodbyeTextH = 0.1


# -----positions and distance-----

# img position
imgX = 0
imgY = 0.2

# ball
ballX1 = -5*ballD+ballD/2     # The x-position of the first ball, note that this needs to be stated after ballD
ballY = 0                     # y-position of all the balls

# button subject
buttonSX = 0                  # x-position of the first question
buttonSY = -0.1               # y-position of the first question
    
# button box and text
button1X = -0.3               # x-position of the jarA button and the text
button2X = 0.3                # x-position of the jarB button and the text
buttonY = -0.2                # y-position of the buttons and the texts


pos1 = (button1X, buttonY)
pos2 = (button2X, buttonY)


# slider and the slider subject
sliderX = 0                   # x-position of slider
sliderY = -0.35               # y-position of slider
sliderSX = 0                  # the x-position of the slider subject
sliderSY = -0.3               # y-position of the slider subject

# goodbyeText
goodbyeTextX = 0
goodbyeTextY = 0



# ---------------------------------------------------------------------------------------------------------



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'beedTask'  # from the Builder filename that created this script
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
conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv") 
if not conditionFile:  # if there is no selection, quit experiment
    core.quit
    


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


introText = visual.TextStim(win=win, name='introText',
    text = introTextT,    
    font='Arial',
    pos=(0, -0.05), height=introTextH, wrapWidth=introTextW, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


expTitle = visual.TextStim(win=win, name='introText',
    text = expTitleText,    
    font='Arial',
    pos=(0, 0.40), height=expTitleH, bold=True, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# ---------- Initialize components for Routine "Trial" ----------

# -----image-----

image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None,
    ori=0, pos=(imgX, imgY),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


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
    text = "JAR A",    
    font='Arial',
    pos=pos1, height=buttonTH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
buttonT2 = visual.TextStim(win=win, name='buttonT2',
    text = "JAR B",    
    font='JAR B',
    pos=pos2, height=buttonTH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# -----button box-----
buttonB1 = visual.Rect(win, name="A",
        width=buttonBW, height =buttonBH, pos=pos1, fillColor="white")
buttonB2 = visual.Rect(win, name="B", 
        width=buttonBW, height =buttonBH, pos=pos2,fillColor="white")

buttonComponents = [buttonS, buttonB1, buttonB2, buttonT1, buttonT2, ]


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

sliderComponents = [sliderS, slider]


# ---------- Initialize components for Routine "Goodbye" ----------

goodbyeText = visual.TextStim(win=win, name='goodbyeText',
    text=goodbyeTextT,
    font='Arial',
    pos=(goodbyeTextX, goodbyeTextY), height=goodbyeTextH, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# ---------- some timers ----------

instructClock = core.Clock()
TrialClock = core.Clock()
popUpTimer = core.CountdownTimer(timePopUp)



#---------------------------------------------------------------------------#
#-----------------------------------INTRO-----------------------------------#
#---------------------------------------------------------------------------#


# ------Prepare to start Routine "intro"-------
t = 0
instructClock.reset()  # clock
frameN = -1
# update component parameters for each repeat

# initialize the instruction text
initiateComponent(expTitle)
initiateComponent(introText)


# -------Start Routine "Instruction"-------
while True:
    
    # flow contro variable

    
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    # update/draw components on each frame
    componentUpdate(expTitle, t, frameN)
    componentUpdate(introText, t, frameN)
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if defaultKeyboard.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        introText.setAutoDraw(False)
        expTitle.setAutoDraw(False)
        break
        
        
    # refresh the screen
    win.flip()
    
    
    
    
    
win.flip()  # get a blank screen
#----------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------- -----------------#
#-------------------------------------------Trial-------------------------------------------#
#-------------------------------------------------------------------------------------------#


# ---------- usefule lists ----------


TrialComponents = [image] + sliderComponents + buttonComponents + ballComponents

# repeaet the trial for 5 times, range(0,5) = [0,1,2,3,4]
for k in range(0,5):

    # ----- trial preparation -----
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conditionFile[0], selection=selectionGenerator(ramDistractor)),
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
        
        
        # ----- record trial dominant color -----
        
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
            domiJar = "JarA"
        else:
            domiJar = "JarB"
        
        # ----------------Prepare to start Routine "Trial"-----------------
        
        t = 0
        frameN = -1
        
        # ----- set trial properties-----
        
        slider.reset()                  # reset slider
        image.setImage(jarPicture)      # set image
        trialBallComponents = ballComponents.copy()             # copy the ball component s.t. the original copy will not be messed around
        for thisBall,thisColor in zip(ballComponents,colorSequence):
            exec("thisBall.fillColor = {}".format(thisColor))           #corlor the ball with the sequence given
        trialBallComponents.reverse()    # reverse the list s.t the last one is the first, convinience for popping up
        
        
        # ----- initiate components -----
        
        for thisComponent in TrialComponents:
            initiateComponent(thisComponent)
        
        # ----- place-holders -----
        
        mouseClicks=[]              # lists for mouse clicks and time stamped
        clickTimes=[]     
        prevButtonState = []
        buttonClick = []
        sliderRecord = None         # slider rating
        buttonClicked = None        # jar selected
        ballStop = None             # number of balls before clicking
        
        # ----- wait before start each trial -----
        
        core.wait(waitingTime)
        
        # ----- reset the timers just before start -----
        
        event.clearEvents()
        myMouse.clickReset()        # reset the mouse timing point to 0 (the time stamp will be based on this)
        myMouse2.clickReset()        # reset the mouse timing point to 0 (the time stamp will be based on this)
        TrialClock.reset()          # reset the trial clock
        popUpTimer.reset()          # reset the popUpTimer (time between each ball)
        
        
        
        # --------------- Start Routine "Trial" ---------------
        
        # outer loop for checking whether the slider has been rated
        # any rating = instant finishi this trial

        while sliderRecord==None:
            
            
            
            # inner loop for poping up ball
            # any click on the mouse will end the loop
            
            while not sum(mouseClicks)>0:
                
                # --------------- update/draw components on each frame ---------------
                t = TrialClock.getTime()            # get current time in second
                frameN = frameN + 1                 # number of completed frames (so 0 is the first frame)
                
                # ----- image updates -----
                
                componentUpdate(image, t, frameN)
                
                # ----- pop up balls -----
                
                if popUpTimer.getTime() < 0 and len(trialBallComponents)!=0:
                    componentUpdate(trialBallComponents.pop(), t, frameN)
                    popUpTimer.reset()                                               # reset the poping up timer everytime you popped up a ball
                
                if len(trialBallComponents)<10:                                     # wait until the first ball has been poppd up
                    mouseClicks, clickTimes = myMouse.getPressed(getTime=True)      # check whether is any mouse clicks, save clicks and times
                
                # ----- check number of balls -----
                
                ballStop = 10-len(trialBallComponents)                           # calculate how many balls have popped up
                if ballStop == 10 and popUpTimer.getTime()<0:                   #if after the 10 ball and the popping up time there is still no click, set ballStop = 11 and exit this loop
                    ballStop = 11
                    break
                    
                # ----- check special keys -----
                
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):    # check for quit (typically the Esc key)
                    core.quit()
                
                win.flip()    # flip fo to next frame
            
            
            
            if ballStop == 11:      
                break       # end trial, skip everything below
                
            current = myMouse.getPressed()
            
            if current!=mouseClicks and slider.status == NOT_STARTED:        # after lifted, before start of the slider
                
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
                        break
                    if myMouse.isPressedIn(buttonB2):
                        buttonClicked = buttonB2.name          # store jar selected
                        break
                        
                    # ----- check special keys -----
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                        
                    win.flip()
            
            
            t = TrialClock.getTime()             # get current time
            frameN = frameN + 1                  # number of completed frames (so 0 is the first frame)
            
            if buttonClicked != None:
                componentUpdate(slider, t, frameN)      # start slider subject
                componentUpdate(sliderS, t, frameN)     # start slider
                
            # ----- check and store the rating on the slider -----
            
            sliderRecord = slider.getRating()       # wait for the rating
            
            # ----- check special keys -----
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):        # check for quit (typically the Esc key)
                core.quit()
            
            win.flip()   # go to the next fram in the outer loop
            
            
        # ---------- Ending Trial ----------
        
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ---------- record data ----------
        
        trials.addData("ClickedAfterBall#", ballStop)          # number of balls before click, 11 if no clicks happend
        trials.addData("ClickTime", clickTimes)                # time of the deicison
        trials.addData("JarSelected", buttonClicked)           # button clicked, store "jarA" or "jarB"
        trials.addData("ConfidenceRating",sliderRecord)        # rating of confidence from the slider
        trials.addData("DominantJar", domiJar)                 # which one is the dominant jar, jarA or jarB
        trials.addData("trialDomiColor", A)                    # dominant color
        trials.addData("trialNonDomiColor", B)                 # non-dominant color
        trials.addData("isRandomDistractor", ramDistractor)    # non-dominant color
        
        thisExp.nextEntry()      # enter next experiment
        win.flip()               # flip for next frame
        
    # completed 1 repeats of 'trials'
    

#----------------------------------------------------------------------------------------------------









#---------------------------------------------------------------------------#
#----------------------------------Goodbye----------------------------------#
#---------------------------------------------------------------------------#




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
