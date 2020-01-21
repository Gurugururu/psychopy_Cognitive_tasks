#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------- #

    #1. **IMPORTANT** since the csv file contains french accents, when saving as csv file, you need to be carefule to select "UTF-8" type of csv, or error will happen
    
    #2. **IMPORTANT**: format note:
    
        #   **IMPORTANT** the condition file must contain the headers:
        
            #  ===============================================================
            #  ||    img_1     img_2    img_3    txt_1    txt_2    txt_3    ||
            #  ===============================================================
            
                #   img_* are the path for the picture, including the post-fix of picture at the end
                #   put the slash in file path as "\\", or may not work in some cases (like on my PC
                #   txt_* are the words displayed
                
            # it's case sensitive, and mustn't be other names
            # the order doesn't mater
            # Everything that is in the original csv file (e.g. the name of the trial) will be saved automatically in the resulting data file (THANKS YOU PSYCHOPY!)
            # only csv files are allowed
        
                
    #3. If you are certain about your path and want to avoid user interface popping up everytime:
    
            # 1) around line 210, comment out these lines 
            
                # conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  
                 # if not conditionFile:
                #   core.quit
            
            # 2.1) place "  conditionFile[0]=["YOUR_FILE_PATH"] " after the above commented lines
            
            # OR:
            
            # 2.2) around line433, replace "conditionFile[0]" in "trialList=data.importConditions(conditionFile[0]),"  with your condition file path
                # path is a string type
                # remember to replace "/" with "\\" in windows (sometimes error occurs)
                
    #4. unit of lengh = height (relative to the height of the screen)
        # (0,0) is at the center
        # may need adjustment according to computers
        
    #5. for the introduction picture, contain the picture in the same folder as the py file, and assign the name of the picture to the variable "placeboName"
        # name including the type of picture (e.g. picture_A.jpg)
        # Don't include the directory
    
        
# ----------------------------------------------------------------------------------------------- #


from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, event
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
from psychopy.visual import Circle, Rect



from pyglet.window import key  # used to detect and record key presses

# -----some-functions-----

    # function for Updating txt and img
def componentUpdate(win, component, time, frameN):
  
    # if the component is not started
    if component.status == NOT_STARTED:
        # keep track of start time/frame for later
        #component.setAutoDraw(True)     # start the component
        component.tStart = time
        component.frameNStart = frameN
        win.timeOnFlip(component, 'tStartRefresh')

    # if the component is started
    if component.status == STARTED:
        # keep track of stop time/frame for later
        component.tStop = time# not accounting for scr refresh
        component.frameNStop = frameN  # exact frame index
        win.timeOnFlip(component, 'tStopRefresh')  # time at next scr refresh
    
        
        
# function for updating component fade in, used in image fading in

def imgFadeIn(component, frameN, timeFadePara):
    if component.status == STARTED:
        opim = (frameN-component.frameNStart)/timeFadePara  # calculate the opacity
        if opim >= 1:
            opim = 1
        component.setOpacity(opim, log=False)  # update the opacity at each frame
    
    
    
# function for initialization of component
def initiateComponent(Component):
    Component.tStart = None
    Component.tStop = None
    Component.tStartRefresh = None
    Component.tStopRefresh = None
    if hasattr(Component, 'status'):
        Component.status = NOT_STARTED

def imageSwitch(countDown, trialsClock, image1, image2, image3, text1, text2, text3, frameN, timeFadeIn, timeFadeInImg3, slider, sliderRating):
    
    # use componentUpdate in each condition for accuracy
    
    # start image2 if image1 is shown
    if countDown.getTime() <= 0 and image1.status == STARTED and image2.status == NOT_STARTED and image3.status == NOT_STARTED:
        
        # set text 1 false
        text1.setAutoDraw(False)
        t = trialsClock.getTime()
        
        # update slider record
        sliderRating.append([slider.getRating(), t])
        
        # update current time and frame record  
        componentUpdate(win, image1, t, frameN)
        componentUpdate(win, text1, t, frameN)
        componentUpdate(win, image2, t, frameN)
        componentUpdate(win, text2, t, frameN)
        componentUpdate(win, image3, t, frameN)
        componentUpdate(win, text3, t, frameN)
        componentUpdate(win, slider, t, frameN)
        
        image2.setAutoDraw(True)
        text2.setAutoDraw(True)
        
        # reset countdown timer
        countDown.reset(timeFadeIn)
        
    # start image3 if image2 is shown, disable text2
    if countDown.getTime() <= 0 and image1.status == STARTED and image2.status == STARTED and image3.status == NOT_STARTED:
        
        
        t = trialsClock.getTime()
        # set text2 and slider = false
        text2.setAutoDraw(False)
        slider.setAutoDraw(False)
        sliderRating.append([slider.getRating(), t])    # update slider
        
        # update slider record
        componentUpdate(win, image1, t, frameN)
        componentUpdate(win, text1, t, frameN)
        componentUpdate(win, image2, t, frameN)
        componentUpdate(win, text2, t, frameN)
        componentUpdate(win, image3, t, frameN)
        componentUpdate(win, text3, t, frameN)
        componentUpdate(win, slider, t, frameN)
        
        # start img3 and text3
        image3.setAutoDraw(True)
        text3.setAutoDraw(True)
        
        # reset countdown timer
        countDown.reset(timeFadeInImg3)
        
    # record end time if image3 is shown
    if countDown.getTime() <= 0 and image1.status == STARTED and image2.status == STARTED and image3.status == STARTED:
        
        t = trialsClock.getTime()
        
        # update current time and frame record  
        componentUpdate(win, image1, t, frameN)
        componentUpdate(win, text1, t, frameN)
        componentUpdate(win, image2, t, frameN)
        componentUpdate(win, text2, t, frameN)
        componentUpdate(win, image3, t, frameN)
        componentUpdate(win, slider, t, frameN)
        componentUpdate(win, text3, t, frameN)
                
# ---------------------------------------------some-variables---------------------------------------------

# ----- coordinate parameter ------

introImgSizeRatio = 0.6
introImgX = 0
introImgY = 0.125

goodbyeTextH = 0.05
goodbyeTextX = 0
goodbyeTextY = 0

expTitleH = 0.05
expTitleX = 0
expTitleY = 0.40

introTextH = 0.025
introTextX = 0
introTextY = -0.25

text123H = 0.05
text1H = text123H
text2H = text123H
text3H = text123H
text123X = 0
text123Y = -0.25

screenTextH = 0.05
screenTextX = 0
screenTextY = 0

screenText2H = 0.05
screenText2X = 0
screenText2Y = 0

#====Time parameters(unit: s)====


timeFadeIn = 5          #  time for the image to fade in
timeFadeInImg3 = 1      # img3 fade-in time
timeFadePara = timeFadeIn * 60  # the parameter to divided with

timeStartOne = 0.0     # the starting time for the first picture to emerge
timeBuffering = 0      # Time for blank screen between each condition, set constant buffering for convenience

timeWaited = 1
timeImg3 = timeFadeInImg3

#====slider parameters(unit: height)====


# speed of the marker movement (sensitivity)

sliderSpeed = 0.01


# start and end points of slider
# note: if want multiple ticks, need to modify the script in initialization section

sliderLeftP = 0  # left end
sliderRightP = 1  #right end

sliderStartP = (sliderRightP + sliderLeftP)*0.5 # the initial position (any number between start and end)


# text to display at start and end of slider

sliderLeftT = "100% NON"
sliderRightT = "100% OUI"


#====Instruction text & goodbye text====

placeboName1 = "picBADE1.png"
placeboName2 = "picBADE2.png"

expTitleT = "Tâche d’Images"

instructionTextP1 = """Dans cette tâche, vous devrez identifier des images.\n
                    \nVous allez voir graduellement une image, avec un mot écrit en-dessous. Évaluez si vous croyez que le mot décrit de manière adéquate l’image entière. Une fois que vous avez répondu, plus de détails de l’image commenceront à apparaître. Reconsidérez l’évaluation que vous avez faite. Vous pouvez changer votre évaluation autant que vous le voulez. Une fois votre deuxième évaluation faite, vous verrez l’image entière et le mot correct. Vous ne devez pas répondre à l’image entière.\n"""

instructionTextP2 = """Vous allez utiliser le clavier, pour faire vos évaluations. Appuyez et maintenez les touches des flèches de haut et de bas, pour déplacer l’évaluation vers oui ou non, respectivement. Vous pouvez faire vos évaluations à n’importe quel endroit sur l’échelle, dépendamment à quel point vous êtes confiant de votre réponse. Essayez de répondre le plus vite que vous pouvez.\n
                    \nVous allez maintenant compléter plusieurs essais de pratique, avant de commencer l’exercice."""

goodbyeTextT = "Merci de votre participation."

screenTextT = "Prêt à commencer? Questions?"     # text appear on a blank screen after practice trial
screenText2T = "Pour les prochains essais de pratique, vous aurez quelques secondes pour répondre à chaque image."     # text appear on a blank screen after practice trial


# ==== sequenec for display ====


# added practice trial

numPractice = 8     # number of practice trials in the csv file
numPracticeWaited = 4 # number of practice trials waited for response

#sequenceA = [18, 53, 44, 1, 46, 45, 67, 17, 76, 41, 54, 32, 4, 79, 64, 3, 5, 9, 16, 30, 51, 58, 42, 7, 21, 62, 72, 78, 31, 56, 52, 43, 48, 39, 50, 63, 20, 77, 40, 35]
#sequenceB = [14, 61, 47, 19, 74, 28, 23, 29, 65, 38, 12, 8, 10, 71, 75, 24, 34, 66, 69, 49, 26, 59, 15, 2, 6, 11, 60, 73, 70, 37, 80, 27, 55, 57, 68, 25, 33, 36, 13, 22]

#practice = [n for n in range(1, numPractice+1)]
#sequenceA = [x+numPractice for x in sequenceA]
#sequenceB = [x+numPractice for x in sequenceB]
#sequenceTotal = practice + sequenceA + sequenceB

# shift 1
#sequenceTotal = [x - 1 for x in sequenceTotal]

# Ensure that relative paths start from the same directory as this script

# Store info about the experiment session
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


placeboDir1 = _thisDir + os.sep + placeboName1
placeboDir2 = _thisDir + os.sep + placeboName2



psychopyVersion = '3.1.2'
expName = "Experiment" 
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion



# ==== select condition file ====


#conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  # a list object, save the path(including the name) of the file selected, conditionFile[0] gives the file name string
#   
#if not conditionFile:
#    core.quit
#    

conditionFile=["C:\\Users\\CRISPlab\\Documents\\CognitiveBiasesStudy\\Tasks\\1-PictureBADE\\PicBADEconditions.csv"]

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

#--------------------#
#---initialization---#
#--------------------#

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size = (1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    

# initialize pyglet trick
# Some newer method is available (using key hardware), but this trick still works
# not sure how to detect key press and release using keyboard hardware class

    
frameDur = None # place holder

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
kb = keyboard.Keyboard()

# using keyState
keyState = key.KeyStateHandler()
win.winHandle.push_handlers(keyState)

# add mouse
myMouse = event.Mouse(newPos = (1,1))
myMouse.setVisible(False)
pos = myMouse.getPos()  # add the position



expTitle = visual.TextStim(win=win, name='introText',
    text = expTitleT,    
    font='Arial',
    pos=(expTitleX, expTitleY), height=expTitleH, bold=True, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
    
introImg = visual.ImageStim(
    win=win,
    name='introImg', 
    image=None, mask=None,
    ori=0, pos=(introImgX, introImgY),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


introText = visual.TextStim(win=win, name='introText',
    text = instructionTextP1,    
    font='Arial',
    pos=(introTextX, introTextY), height=introTextH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

screenText = visual.TextStim(win=win, name='screenText',
    text=screenTextT,
    font='Arial',
    pos=(screenTextX, screenTextY), height=screenTextH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
screenText2 = visual.TextStim(win=win, name='screenText2',
    text=screenText2T,
    font='Arial',
    pos=(screenText2X, screenText2Y), height=screenText2H, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


goodbyeText = visual.TextStim(win=win, name='goodbyeText',
    text=goodbyeTextT,
    font='Arial',
    pos=(goodbyeTextX, goodbyeTextY), height=goodbyeTextH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine

slider = visual.Slider(win=win, name='slider',
    size=(0.04, 0.6), pos=(0.5, 0),
    labels=(sliderLeftT, sliderRightT), ticks=(sliderLeftP,sliderRightP),
    granularity=0, style=['slider'],
    color='black', font='HelveticaBold',
    flip=True, units="height")
    
#  notice that the "size" of the slider controls whether the slider is verticle or horizontal
#  change to desired style, using the in-built visual stimulus from psychopy
    
slider.marker = Circle(win, 
                        radius = slider.size[0]*0.5,  # The radius should be half the width 
                        edges = 32, 
                        fillColor = 'black', 
                        lineColor = 'gray')
                        
slider.line = Rect(win, units=slider.units,
                        pos=slider.pos,
                        width=slider.size[0],
                        height=slider.size[1]+0.005,  # +0.005 just to make the rectangule looks better
                        lineColor='black', 
                        fillColor = 'gray',
                        autoLog=False)
    


text1 = visual.TextStim(win=win, name='text1',
    text='default text',
    font='Arial',
    pos=(text123X, text123Y), height=text1H, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
    
text2 = visual.TextStim(win=win, name='text2',
    text='default text',
    font='Arial',
    pos=(text123X, text123Y), height=text2H, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
    
text3 = visual.TextStim(win=win, name='text3',
    text='default text',
    font='Arial',
    pos=(text123X, text123Y), height=text3H, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
    
    
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=0.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
    
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=0.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
    
image3 = visual.ImageStim(
    win=win,
    name='image3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
    
# instructionclock also later re-used for goodbye message
InstructionClock = core.Clock()
globalClock = core.Clock()

#---------------------------------------------------------------------------#
#-----------------------------------INTRO-----------------------------------#
#---------------------------------------------------------------------------#


# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
count = 0
# initialize the instruction text
initiateComponent(expTitle)
initiateComponent(introText)
initiateComponent(introImg)

introImg.setImage(placeboDir1)
introImg.size = introImg.size * introImgSizeRatio


# -------Start Routine "Instruction"-------
while True:
    
    
    if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:  # Fixate the mouse to the upper-right conor
        myMouse.setPos(newPos = (1,1))
        
    # get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(win, expTitle, t, frameN)
        componentUpdate(win, introText, t, frameN)
        componentUpdate(win, introImg, t, frameN)
        
        introText.setAutoDraw(True)
        expTitle.setAutoDraw(True)        
        introImg.setAutoDraw(True)
        
    # check for quit (typically the Esc key)
    if endExpNow or kb.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if kb.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        count += 1
        
        if count == 1:
            introText.setText(instructionTextP2)
            introImg.setImage(placeboDir2)
            
        if count == 2:
            introText.setAutoDraw(False)
            expTitle.setAutoDraw(False)        
            introImg.setAutoDraw(False)
            break
          
    # refresh the screen
    win.flip()

win.flip()  # get a blank screen
#core.wait(timeBuffering)  # buffering for participant

#---------------------------------------------------------------------------------------------------#
#-------------------------------------------FORMAL-TRIALS-------------------------------------------#
#---------------------------------------------------------------------------------------------------#

# set up handler to look after randomisation of conditions etc

Repeat = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditionFile[0]),
    seed=None, name='Repeat')
    
    
    
thisExp.addLoop(Repeat)  # add the loop to the experiment
thisRepeat = Repeat.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
if thisRepeat != None:
    for paramName in thisRepeat:
        exec('{} = thisRepeat[paramName]'.format(paramName))

#--------------------#
#-------Repeat-------#
#--------------------#

for thisRepeat in Repeat:

    
    event.clearEvents(eventType='keyboard')
    
    currentLoop = Repeat
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
            
    if Repeat.thisN == numPracticeWaited:
        
        initiateComponent(screenText2)
        screenText.setText(screenText2T)
        screenClock = core.Clock()
        t = 0
        frameN = -1
        screenClock.reset()
            
        while True:
            
            # get current time
            t = screenClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            
            # update/draw components on each frame
            screenText2.setAutoDraw(True)
            componentUpdate(win, screenText2, t, frameN)
                
            # check for quit (typically the Esc key)
            if endExpNow or kb.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if kb.getKeys(keyList=["space"]): 
                screenText2.setAutoDraw(False)
                win.flip()
                break
                
            win.flip()
            
        
    if Repeat.thisN == numPractice:
        
        initiateComponent(screenText)
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
            screenText.setAutoDraw(True)
            componentUpdate(win, screenText, t, frameN)
                
            # check for quit (typically the Esc key)
            if endExpNow or kb.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if kb.getKeys(keyList=["space"]): 
                screenText.setAutoDraw(False)
                win.flip()
                break
                
            win.flip()    
            
    #--------------------#
    #-------Trials-------#
    #--------------------#

    # update component parameters for each repeat
    slider.reset()
    text1.setText(txt_1)
    text2.setText(txt_2)
    text3.setText(txt_3)
    image1.setImage(img_1)
    image2.setImage(img_2)
    image3.setImage(img_3)
    slider.recordRating(sliderStartP)           # set starting point at the middle

    image1.setOpacity(0)
    image2.setOpacity(0)
    
    # ------Prepare to start Routine "Trials"-------
    
    sliderRating = []                           # store here the rating and the time at point wanted
    keyRecord = []                              # record respond
    responded = False
    entering = 0;
    
    TrialsComponents = [slider, text1, text2, text3, image1, image2, image3] # keep track of which components have finished
    
    for thisComponent in TrialsComponents:
        initiateComponent(thisComponent)        # set the values to None

    core.wait(timeBuffering)                    # blank screen for time buffering
    continueRoutine = True                      # check if continue routine or not
    
    #kb = keyboard.Keyboard()
    
    frameN = -1
    t = 0
    
    # initialize some clocks
    trialsClock = core.Clock()                    #  Create some handy timers
    countDown = core.CountdownTimer(timeFadeIn)   # Used to detect whether we reached the timeConfidence
    kb.getKeys(keyList=['up', 'down'], waitRelease=False, clear =True) # clean up key presses
    
    # reset the clocks to starting time
    trialsClock.reset()              # clock of the trial
    countDown.reset(timeFadeIn)      # clock for timeConfidence
    globalClock.reset()              # to track the trial duration
    kb.clearEvents()                 # clean up buffer
    kb.clock.reset()                 # reset clock for keyboard (reset for only img1)
    
    if Repeat.thisN >= numPracticeWaited:
        while continueRoutine:
            
            # img1
                # force respond
                # wait for confidence time
            t = trialsClock.getTime()
            frameN += 1
            
            # fixate the mouse
            if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:
                myMouse.setPos(newPos = (1,1))
            
            
            #update stop/start time
            t = trialsClock.getTime()
            componentUpdate(win, image1, t, frameN)
            componentUpdate(win, text1, t, frameN)
            componentUpdate(win, image2, t, frameN)
            componentUpdate(win, text2, t, frameN)
            componentUpdate(win, image3, t, frameN)
            componentUpdate(win, text3, t, frameN)
            componentUpdate(win, slider, t, frameN)
            
            
            # start image1 and text1 and slider
            if image1.status == NOT_STARTED:
                image1.setAutoDraw(True)
                text1.setAutoDraw(True)
                slider.setAutoDraw(True)
                
                
            # fade in image1 and 2 if they are started; image3 is not faded in, and is set to autodraw in imageSwitch
            imgFadeIn(image1, frameN, timeFadePara)
            
                    
            if image2.status == STARTED:
                # fade in image2
                imgFadeIn(image2, frameN, timeFadePara)
            
            imageSwitch(countDown, trialsClock, image1, image2, image3,text1, text2, text3, frameN, timeFadeIn, timeFadeInImg3, slider, sliderRating)
                
            if image3.status == STARTED and countDown.getTime()<=0:
                # record reaction times with keyboard hardware class (more accurate)
                keyRecord = kb.getKeys(keyList=['up', 'down'], waitRelease=False, clear=True)           # whole chunk of keys
                kb.clearEvents()                                                                          # clean up buffer
                currentkeyUp = []
                currentKeyDown = []
                trialDuration = globalClock.getTime()
                continueRoutine = False
            

            
            # ----- moving slider ----- 
            
            # detecting movement with keyState
            
            if keyState[key.DOWN]:
                newRat = slider.rating - sliderSpeed
                slider.rating = newRat
                
            if keyState[key.UP]:
                newRat = slider.rating + sliderSpeed
                slider.rating = newRat
                
            
            #--------------------------------#
            #----check-special-conditions----#
            #--------------------------------#
            
            
            # check for quit (typically the Esc key)
            if endExpNow or kb.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
                
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
    else:
        
        countDown.reset(timeWaited)      # clock for timeConfidence
        countDown2 = core.CountdownTimer(timeImg3)   # Used to detect whether we reached the timeConfidence

        while continueRoutine:
            # img1
            # force respond
            # wait for confidence time
            
            t = trialsClock.getTime()
            frameN += 1
            
            # fixate the mouse
            if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:
                myMouse.setPos(newPos = (1,1))
            
            #update stop/start time
            t = trialsClock.getTime()
            componentUpdate(win, image1, t, frameN)
            componentUpdate(win, text1, t, frameN)
            componentUpdate(win, image2, t, frameN)
            componentUpdate(win, text2, t, frameN)
            componentUpdate(win, image3, t, frameN)
            componentUpdate(win, text3, t, frameN)
            
            
            # start image1 and text1 and slider
            if image1.status == NOT_STARTED:
                image1.setAutoDraw(True)
                text1.setAutoDraw(True)
                slider.setAutoDraw(True)
                
            # fade in image1 and 2 if they are started; image3 is not faded in, and is set to autodraw in imageSwitch
            imgFadeIn(image1, frameN, timeFadePara)
            
            if image2.status == STARTED:
                # fade in image2
                imgFadeIn(image2, frameN, timeFadePara)
            
            # start img2
            if image2.status == NOT_STARTED and responded and countDown.getTime()<=0 and image1.opacity == 1:
                entering += 1
                componentUpdate(win, image1, t, frameN)
                componentUpdate(win, text1, t, frameN)
                componentUpdate(win, image2, t, frameN)
                componentUpdate(win, text2, t, frameN)
                componentUpdate(win, image3, t, frameN)
                componentUpdate(win, text3, t, frameN)
                componentUpdate(win, slider, t, frameN)
                text1.setAutoDraw(False)
                image2.setAutoDraw(True)
                text2.setAutoDraw(True)
                responded = False
                # update slider record
                sliderRating.append([slider.getRating(), t])
                countDown.reset(timeWaited)
            
            if image3.status == NOT_STARTED and responded and countDown.getTime()<=0 and image2.opacity == 1:
                entering += 1
                componentUpdate(win, image1, t, frameN)
                componentUpdate(win, text1, t, frameN)
                componentUpdate(win, image2, t, frameN)
                componentUpdate(win, text2, t, frameN)
                componentUpdate(win, image3, t, frameN)
                componentUpdate(win, text3, t, frameN)
                componentUpdate(win, slider, t, frameN)
                text2.setAutoDraw(False)
                image3.setAutoDraw(True)
                text3.setAutoDraw(True)
                slider.setAutoDraw(False)

                # update slider record
                sliderRating.append([slider.getRating(), t])
                countDown2.reset(timeImg3)
                responded = False
              
            if image3.status == STARTED and countDown2.getTime()<=0 and image2.opacity == 1:
                # update slider record
                t = trialsClock.getTime()
                componentUpdate(win, image1, t, frameN)
                componentUpdate(win, text1, t, frameN)
                componentUpdate(win, image2, t, frameN)
                componentUpdate(win, text2, t, frameN)
                componentUpdate(win, image3, t, frameN)
                componentUpdate(win, text3, t, frameN)
                componentUpdate(win, slider, t, frameN)
                keyRecord = kb.getKeys(keyList=['up', 'down'], waitRelease=False, clear=True)           # whole chunk of keys
                kb.clearEvents()                                                                          # clean up buffer
                currentkeyUp = []
                currentKeyDown = []
                trialDuration = globalClock.getTime()
                continueRoutine = False
            
            # ----- moving slider ----- 
            
            # detecting movement with keyState
            
            if keyState[key.DOWN]:
                newRat = slider.rating - sliderSpeed
                slider.rating = newRat
                countDown.reset(timeWaited)
                responded = True
                
            if keyState[key.UP]:
                newRat = slider.rating + sliderSpeed
                slider.rating = newRat
                countDown.reset(timeWaited)
                responded = True
            
            # check for quit (typically the Esc key)
            if endExpNow or kb.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
                
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
           
        
        
        
        
        
        
        
    #---------------------------#
    #-----end-and-save-data-----#
    #---------------------------#
    
    
    
    # -------Ending Routine "Trials"-------
    for thisComponent in TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # place holder
    addKeys1 = []
    addKeys2 = []
    keyRecord_add = []
    img1_pressTime = 0
    img2_pressTime = 0
    img1_direction = 0
    img2_direction = 0
    img1_showTime = image2.tStart - image1.tStart
    img2_showTime = image3.tStart - image2.tStart
    img3_showTime = trialDuration - image3.tStart
    
    # classify key presses into addkeys according to key reaction time and timeFadeIn
    # both measured from the start of img1 (never reset clock in keyboard between pictures)
    
    for k in keyRecord:
        
        keyRecord_add.append([k.name, k.rt, k.duration])        # the total record
        
        # img1
        if k.rt < image2.tStart:
            
            tmp = k.duration
            if tmp == None or (k.rt + k.duration > image2.tStop):
                tmp = img1_showTime + img2_showTime - k.rt
            
            addKeys1.append([k.name, k.rt, tmp])
            
        # img2
        elif k.rt >= image2.tStart and k.rt < image3.tStart:        # extract press between img 2 and 3
            
            # in the case where input is interrupted, k.duration = None
            
            # img1_showtime + img2_showtime)-img1_Firstkey_rt
            
            tmp = k.duration
            if tmp == None or (k.rt + k.duration > image2.tStop):
                tmp = img1_showTime + img2_showTime - k.rt
            
            addKeys2.append([k.name, k.rt,tmp])
    
    # calculate press time and direction
    # note that there sohuldn't be any none valus, either rt or duration
    
    for kl in addKeys1:
        
        img1_pressTime += kl[2]
        
        if k.name == "up":
            img1_direction += kl[2]    # add when up
        elif k.name == "down":
            img1_direction -= kl[2]    # minus when down
            
    for kl in addKeys2:
                
        img2_pressTime += kl[2]
        
        if k.name == "up":
            img2_direction += kl[2]    # add when up
        if k.name == "down":
            img2_direction -= kl[2]    # minus when down
            
    
    
    
    # ----- timeFadeIn
    Repeat.addData("timeFadeIn", timeFadeIn)
    
    
    # ----- slider record
    Repeat.addData("slider.history_rating", sliderRating)    # the slider rating at timeFadeIn and 2*timeFadeIn, with time
    
    # Ratings of each image, seperate in different columns
    Repeat.addData("img1_rating", sliderRating[0][0])    # img1_rating
    Repeat.addData("img2_rating", sliderRating[1][0])    # img2_rating 
    
    
    
    # ----- data for img1
    
    if addKeys1 == []:
        
        # Reaction time 
        Repeat.addData("img1_FirstKey_rt", -88)
        
        # img duration (total pressing time)
        Repeat.addData("img1_duration", -88)
        
        # img direction sum up (+ if up, - if down)
        Repeat.addData("img1_direction", -88)
        
    else:
        
        # Reaction time 
        Repeat.addData("img1_FirstKey_rt", addKeys1[0][1])     
        
         # img duration (total pressing time)
        Repeat.addData("img1_duration", img1_pressTime)
        
        # img direction sum up (+ if up, - if down)
        if img1_direction > 0: 
            img1_direction = 1
        else:
            img1_direction = -1
            
                
        Repeat.addData("img1_direction", img1_direction)        
        
        
    # ----- data for img2
    
    if addKeys2 == []:
        
        # Reaction time 
        Repeat.addData("img2_FirstKey_rt", -88)
        
        # img duration (total pressing time)
        Repeat.addData("img2_duration", -88)
         
        Repeat.addData("img2_direction", -88)        
        
    else:
        
        # Reaction time 
        Repeat.addData("img2_FirstKey_rt", addKeys2[0][1])     
        
        # img duration (total pressing time)
        Repeat.addData("img2_duration", img2_pressTime)
        
        # img direction sum up (+ if up, - if down)
        if img2_direction > 0: 
            img2_direction = 1
        else:
            img2_direction = -1
            
        
        # img direction sum up (+ if up, - if down)
        Repeat.addData("img2_direction", img2_direction)       
    
        
    # ----- Other data that may be needed
    
    # entire trial time
    Repeat.addData("trialDuration", trialDuration)              # trial duration
        
    # tracking starting time
    Repeat.addData("image1_tStart", image1.tStart)
    Repeat.addData("image2_tStart", image2.tStart)
    Repeat.addData("image3_tStart", image3.tStart)
    
    # img showing time
    Repeat.addData("img1_showTime", img1_showTime)
    Repeat.addData("img2_showTime", img2_showTime)
    Repeat.addData("img3_showTime", img3_showTime)
    
    # key record
    Repeat.addData("img1_keyboard.record_name_rt_duration", addKeys1)   # record for img1
    Repeat.addData("img2_keyboard.record_name_rt_duration", addKeys2)   # record for img2
    

    win.flip()
    thisExp.nextEntry()
    
    # completed 1 repeats of 'Repeat'
    
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
win.saveFrameIntervals(fileName = "allFrameTimes.txt", clear = True)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit



#---------------------------------------------------------------------------#
#----------------------------------Goodbye----------------------------------#
#---------------------------------------------------------------------------#

# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # reusing the clock for instruction
frameN = -1
continueRoutine = True

# initialize goodbye text
initiateComponent(goodbyeText)

# -------Start Routine "goodBye"-------

while True:
    
    # get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(win, goodbyeText, t, frameN)
        goodbyeText.setAutoDraw(True)
                
    # check for quit (typically the Esc key)
    if endExpNow or kb.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if kb.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        goodbyeText.setAutoDraw(False)
        goodbyeText.status = FINISHED
        
        break
    
    # refresh the screen
    win.flip()
    

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
win.close()
core.quit()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

