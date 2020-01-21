#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on July 30, 2019, at 14:12
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
    
        # ==============================================================================================
        # ||    state1    state2    state3    sliderSub1    sliderSub2    sliderSub3    sliderSub4    ||
        # ==============================================================================================
        
            # "state1"~"state3" are the three statements that will appear on the top of screen one-by-one
            # "sliderSub1"~"sliderSub4" are the four questions that're on the sliders
        
        # the names are case-sensitive, and mustn't be other names
        # order doesn't matter
        # Everything that is in the original csv file (e.g. the name of the trial) will be saved automatically in the resulting data file (THANKS YOU PSYCHOPY!)
        
        
    #3. If you are certain about your path and want to avoid user interface popping up everytime:
    
            # 1) around line 220, comment out these lines 
            
                # conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  
                 # if not conditionFile:
                #   core.quit
            
            # 2.1) place "  conditionFile[0]=["YOUR_FILE_PATH"] " after the above commented lines
            
            # OR:
            
            # 2.2) around line733, replace "conditionFile[0]" in "trialList=data.importConditions(conditionFile[0]),"  with your condition file path
                # path is a string type
                # remember to replace "/" with "\\" in windows (sometimes error occurs)
                
    #4. If you want to read codes, in case of naming, there are these objects displayed:
    
        # statements (3 of them, text objects)              -> state1 ~ state3
        # slider (4 of them, slider objects)                -> slider1 ~ slider4
        # slider subject (4 of them, text objects)          -> sliderS1 ~ sliderS4
        # slider values (4 of them, text objects)           -> sliderV1 ~ sliderV4
        
        # a button (composed of 2 objects)                  -> nextButton and nextText
        # a box around statements (a rectangular object)    -> stateBox
        
        # Namings of the variables will follow the rules semantically:
            # e.g. sliderH => slider height; sliderSH => slider subject height
            # e.g. stateBoxX => The x-position of the box
    
    #5. unit of lengh = height (relative to the height of the screen)
        # (0,0) is at the center
        # may need adjustment according to computers
        
        
    #6. for the introduction picture, contain the picture in the same folder as the py file, and assign the name of the picture to the variable "placeboName"
        # name including the type of picture (e.g. picture_A.jpg)
        # Don't include the directory
    
    
# ----------------------------------------------------------------------------------------------- #

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import random as ram
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# ----------------------------------------------------------------------------------------------- #


# -----some-functions-----

# function for initialization of component
def initiateComponent(Component):
    Component.tStart = None
    Component.tStop = None
    Component.tStartRefresh = None
    Component.tStopRefresh = None
    if hasattr(Component, 'status'):
        Component.status = NOT_STARTED
        
        
# function for updating components
def componentUpdate(component, time, frameN):
  
    # if the component is not started
    if component.status == NOT_STARTED:
        component.setAutoDraw(True)  #start the component (will set status = started)
        component.tStart = time
        component.frameNStart = frameN
        win.timeOnFlip(component, 'tStartRefresh')
        
    # if the component is started
    if component.status == STARTED:
        # keep track of stop time/frame for later
        component.tStop = time# not accounting for scr refresh
        component.frameNStop = frameN  # exact frame index
        win.timeOnFlip(component, 'tStopRefresh')  # time at next scr refresh
    
# check if the slider has been moved or not
def checkSlider(sliders, originRatings):
   
    for thisSlider, thisR in zip(sliders, originRatings):
        if thisSlider.rating != thisR:
            return True  # if there is any movement, consider it as "has responded"

    return False  # if everything is untouched, it's not responded

# ---------------------------------------------some-variables---------------------------------------------


# --------------- physical properties ---------------

# ----- position of the intro image & texts & goodbyeText-----

expTitleH = 0.05
expTitlePos = (0, 0.40)

introTextH = 0.0225
introTextPos = (0, -0.25)

introImgSizeRatio = 0.5
introImgX = 0
introImgY = 0.125

goodbyeTextH = 0.05
goodbyeTextX = 0
goodbyeTextY = 0

screenTextX = 0
screenTextY = 0
screenTextH = 0.1


# ----- statements -----

stateH = 0.03        # The height of the statement (text size
stateP1 = 0.35       # The y-position of the first statment

# ----- sliders -----

sliderH = 0.03       # The height of the slider 
sliderW = 1.4        # The width of the slider
sliderX = 0          # The x-position of the sliders
sliderP1 = -0.01     # The y-position of the first slider

# ----- slider statement -----

sliderSH = 0.03      # The height of the slider subject (text size)
sliderSX = 0         # The x-position of the slidersubject
sliderSP1 = 0.02     # each slider subject should be on the top of the slider (larger than sliderP1)

# ----- slider values -----

sliderVH = 0.02      # The height of the slider values (text size)
sliderVX = sliderW/2 + sliderSX + 0.05   # The x-position of the values
sliderVP1 = sliderP1   # slider value has the same y-position as the slider

# ----- position of the button & buttonBox -----

buttonBoxH = 0.055   # The height of the button box
buttonBoxW = 0.22    # The width of the button box

buttonX = 0
buttonY = -0.45


# ----- the distance between each component -----
    # calculate to make sure they are evenly spread
        # (when use them below in object initialization, use the multiple of *D values)
    # height/2 + distance =  about distance between each identical component, just an evaluation

dis = 0.05 # Change this to control the spread, or modify the function below if you want

stateD = stateH/2 + dis
sliderD = sliderH/2 + dis*2.2
sliderSD = sliderSH/2 + dis*2.2
sliderVD = sliderD              # The distance between the values should be the same as the slider

# ----- position of the box around statement -----


stateBoxX = 0
stateBoxY = stateP1-stateD



# -----Other-parameters-----

numPractice = 2

timeBetween = 0      # time between each trial (unit: second)

# starting point and ending point of the sliders

startP = 0       # starting value of all sliders
endP = 1         # ending value of all sliders
startT = "0%"    # text displayed at at the starting point of the slider
endT = "100%"    # text displayed at the end of the slider


# name of the placebo picture, including the picture type

placeboName = "BADE.jpg"

# experiment title

expTitleT = "Tâche d'Histoires"

# two parts of instructions

instructionTextP1 =  """Trois énoncés vous seront montrés, un à la fois. Chacun décrit un événement ou une personne. Chaque nouvel énoncé apportera de l’information additionnelle à propos de l’événement ou de la personne décrit(e). Sous les énoncés, vous verrez aussi quatre interprétations de l’événement ou de la personne décrit(e) dans le(les) énoncé(s). Chaque interprétation a sa propre échelle (de 0 – 100%), vous aurez donc à évaluer la probabilité que chaque interprétation décrive l’énoncé, selon les informations données.\n
                     \nÉvaluez à quel point vous pensez que chaque interprétation se rapporte à l’évènement ou la personne décrite dans l’(les) énoncé(s). Il est important d’évaluer chacune des quatre interprétations indépendamment les unes des autres. Ne comparez pas les interprétations entres elles.\n
                    """

instructionTextP2 =  """À chaque nouvel énoncé présenté, reconsidérez les évaluations que vous avez assignées à chaque interprétation. Les évaluations des interprétations peuvent être changées autant que vous le voulez, vous pouvez aussi les laisser intactes, si vous avez l’impression qu’elles n’ont pas changées avec l’addition de nouveaux énoncés. Il est possible qu’aucune ou que plusieurs interprétations soi(en)t un bon pairage avec les énoncés.\n
                     \nVous utiliserez la souris pour faire vos évaluations. Appuyez sur ‘Suivant’ pour afficher le prochain énoncé. Après avoir vu tous les trois énoncés, appuyez sur ‘Complété’, pour accéder à l’essai suivant. Vous allez maintenant faire 2 essais de pratique, avant de commencer l’exercice."""

goodbyeTextT = "Merci de votre participation."

screenTextT = "Prêt à commencer? Questions?"     # text appear on a blank screen after practice trial

# text on the button (will change fron suivant to comencer at the third trial)

nextText1 = "SUIVANT"
nextText2 = "COMMENCER"
nextText3 = "FIN"

# the color of the text & line & box when click & unclick

# not clicked colors

buttonBoxColor1 = "white"
buttonLineColor1 = "white"
buttonTextColor1 = "black"

# clicked colors

buttonBoxColor2 = "black"
buttonLineColor2 = "white"
buttonTextColor2 = "white"


#--------------------------------------------------------------------------------------------------------------


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

placeboDir = _thisDir + os.sep + placeboName

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'interpretationTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])


#conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  # a list object, save the path(including the name) of the file selected, conditionFile[0] gives the file name string
 
#if not conditionFile:
#    core.quit
    

conditionFile=["C:\\Users\\CRISPlab\\Documents\\CognitiveBiasesStudy\\Tasks\\2-StoryBADE\\BADEtask_conditions.csv"]

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()


# create a default mouse

defaultMouse = event.Mouse(win=win, visible=True)



introClock = core.Clock()
trialClock = core.Clock()
goodbye_Clock = core.Clock()


# Initialize components for Routine "intro"


introImg = visual.ImageStim(
    win=win,
    name='introImg', 
    image=None, mask=None,
    ori=0, pos=(introImgX, introImgY),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)



introText = visual.TextStim(win=win, name='introText',
    text = instructionTextP1,    
    font='Arial',
    pos=introTextPos, height=introTextH, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



expTitle = visual.TextStim(win=win, name='introText',
    text = expTitleT,    
    font='Arial',
    pos=expTitlePos, height=expTitleH, bold=True, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

screenText = visual.TextStim(win=win, name='screenText',
    text=screenTextT,
    font='Arial',
    pos=(screenTextX, goodbyeTextY), height=screenTextH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# -----Statements----- #

statement1 = visual.TextStim(win=win, name='statement1',
    text='default text',
    font='Arial',
    pos=(0, stateP1), height=stateH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
statement2 = visual.TextStim(win=win, name='statement2',
    text='default text',
    font='Arial',
    pos=(0, stateP1-stateD), height=stateH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
statement3 = visual.TextStim(win=win, name='statement3',
    text='default text',
    font='Arial',
    pos=(0, stateP1-stateD*2), height=stateH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
    
    
# -----sliders----- #

slider1 = visual.Slider(win=win, name='slider1',
    size=(sliderW, sliderH), pos=(sliderX, sliderP1),
    ticks=(startP, endP),labels=(startT, endT),
    granularity=0, style=['rating'],
    color='Gray', font='HelveticaBold',
    flip=False)
slider2 = visual.Slider(win=win, name='slider2',
    size=(sliderW, sliderH), pos=(sliderX, sliderP1-sliderD),
    ticks=(startP, endP), labels=(startT, endT),
    granularity=0, style=['rating'],
    color='Gray', font='HelveticaBold',
    flip=False)
slider3 = visual.Slider(win=win, name='slider3',
    size=(sliderW,sliderH), pos=(sliderX, sliderP1-sliderD*2),
    ticks=(startP, endP), labels=(startT, endT),
    granularity=0, style=['rating'],
    color='Gray', font='HelveticaBold',
    flip=False)
slider4 = visual.Slider(win=win, name='slider4',
    size=(sliderW, sliderH), pos=(sliderX, sliderP1-sliderD*3),
    ticks=(startP, endP), labels=(startT, endT),
    granularity=0, style=['rating'],
    color='Gray', font='HelveticaBold',
    flip=False)
    
    
sliderComponents = [slider1, slider2, slider3,slider4]

for thisSlider in sliderComponents:
    thisSlider.marker.fillColor, thisSlider.marker.lineColor = "black", "black"
    #thisSlider.marker.lineColor = "black"

# -----slider-subjects----- #

sliderS1 = visual.TextStim(win=win, name='sliderS1',
    text='default text', 
    font='Arial',
    pos=(sliderSX, sliderSP1), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
sliderS2 = visual.TextStim(win=win, name='sliderS2',
    text='default text',
    font='Arial',
    pos=(sliderSX, sliderSP1-sliderSD), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
sliderS3 = visual.TextStim(win=win, name='sliderS3',
    text='default text',
    font='Arial',
    pos=(sliderSX, sliderSP1-sliderSD*2), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
sliderS4 = visual.TextStim(win=win, name='sliderS4',
    text='default text',
    font='Arial',
    pos=(sliderSX, sliderSP1-sliderSD*3), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);


# -----slider-values----- #

sliderV1 = visual.TextStim(win=win, name='sliderV1',
    text='default text',
    font='Arial',
    pos=(sliderVX, sliderVP1), height=sliderVH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
sliderV2 = visual.TextStim(win=win, name='sliderV2',
    text='default text',
    font='Arial',
    pos=(sliderVX, sliderVP1-sliderVD), height=sliderVH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
sliderV3 = visual.TextStim(win=win, name='sliderV3',
    text='default text',
    font='Arial',
    pos=(sliderVX, sliderVP1-sliderVD*2), height=sliderVH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
sliderV4 = visual.TextStim(win=win, name='sliderV4',
    text='default text',
    font='Arial',
    pos=(sliderVX, sliderVP1-sliderVD*3), height=sliderVH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

sliderVComponents = [sliderV1, sliderV2, sliderV3, sliderV4]

# Initialize components for Routine "goodbye_"

goodbyeText = visual.TextStim(win=win, name='goodbyeText',
    text=goodbyeTextT,
    font='Arial',
    pos=(goodbyeTextX, goodbyeTextY), height= goodbyeTextH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Button (composed of a rectangle and a text stimuli)

nextButton = visual.Rect(win, name="nextButton", width=buttonBoxW, height =buttonBoxH, pos=(buttonX,buttonY))
nextButton.setFillColor(buttonBoxColor1)

nextText = visual.TextStim(win, text=nextText1, 
                pos=(buttonX,buttonY), color="black", height=0.03)

# Box around the statements

stateBox = visual.Rect(win, name="stateBox", width=1.4, height=0.3, pos=(stateBoxX, stateBoxY))
stateBox.setFillColor("lightGrey")
stateBox.setLineColor("lightGrey")


#---------------------------------------------------------------------------#
#-----------------------------------INTRO-----------------------------------#
#---------------------------------------------------------------------------#

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1

# flow control variable
count = 0

# update component parameters for each repeat
# initialize the instruction text
initiateComponent(expTitle)
initiateComponent(introText)
initiateComponent(introImg)

introImg.setImage(placeboDir)
introImg.size = introImg.size*introImgSizeRatio



# -------Start Routine "Instruction"-------
while True:
    
    
    
    # get current time
    t = introClock.getTime()
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
            introText.setText(instructionTextP2)
            
        if count == 2:
            introText.setAutoDraw(False)
            expTitle.setAutoDraw(False)
            introImg.setAutoDraw(False)
        
            break
        
        
    # refresh the screen
    win.flip()
    
    

win.flip()  # get a blank screen


#--------------------------------------------------exit-introduction--------------------------------------------------



#---------------------------------------------------------------------------------------------------#
#-----------------------------------------------TRIALS----------------------------------------------#
#---------------------------------------------------------------------------------------------------#


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditionFile[0]),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))




for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    
    
    # ----- check for practice trial, loop before start of formal trial -----
    
    if trials.thisN == numPractice:
        
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
            componentUpdate(screenText, t, frameN)
                
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if defaultKeyboard.getKeys(keyList=["space"]): 
                screenText.setAutoDraw(False)
                break
                
            win.flip()
    
    
    
    
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    curMouseState=[0,0,0]
    
    #indicate whether participant has moved any of the sliders
    hasRespond = False
    startSecond = False
    startThird = False
    hasRecord1 = False
    hasRecord2 = False
    hasRecord3 = False
    

    # save the texts in order
    
    orderedSliderSubject = [sliderSub1, sliderSub2, sliderSub3, sliderSub4]
    SliderSubject = [sliderSub1, sliderSub2, sliderSub3,sliderSub4]
    

    # shuffle three times to be compelete
    
    
    
    np.random.shuffle(SliderSubject)
    

    # update component parameters for each repeat
    nextText.setText(nextText1) # change the text back to NEXT, set to "done" later
    
    nextButton.setLineColor(buttonLineColor1)
    nextButton.setFillColor(buttonBoxColor1)
    nextText.setColor(buttonTextColor1)
    
    statement1.setText(state1)
    statement2.setText(state2)
    statement3.setText(state3)
    slider1.reset()
    slider2.reset()
    slider3.reset()
    slider4.reset() 
    sliderS1.setText(SliderSubject[0])
    sliderS2.setText(SliderSubject[1])
    sliderS3.setText(SliderSubject[2])
    sliderS4.setText(SliderSubject[3])
    
    
    
    # create a dictionary, key:value paires
    # create key:value pairs
    # for example
        # if current sliderStateText is [sliderSub2, sliderSub1, sliderSub4, sliderSub1]
        # the result will be {sliderSub2:slider1, sliderSub1:slider2, sliderSub4: slider3, sliderSub1:slider4}
        # now when we call dicSlider[sliderSub1], we get slider2
        
    dicSlider = {}
    for thisSliderText, thisSlider in zip(SliderSubject, sliderComponents):
        dicSlider[thisSliderText] = thisSlider
    
    # keep track of which components have finished   
    trialComponents = [screenText, statement1, statement2, statement3, slider1, slider2, slider3, slider4, sliderS1, sliderS2, sliderS3, sliderS4,sliderV1,  sliderV2, sliderV3, sliderV4, nextButton, nextText, stateBox]
    for thisComponent in trialComponents:
        initiateComponent(thisComponent)
        
    for thisSlider in sliderComponents:
        thisSlider.recordRating(startP)
        
    sliderRecord0 = [startP, startP, startP, startP] # initial value
    sliderRecord1 = [] # placeholder for the first set of response
    sliderRecord2 = [] # second
    sliderRecord3 = [] # third
    
    
    globalClock.reset() # reset timer for trial duration
    
    # -------Start Routine "trial"-------
    while continueRoutine:

        
        while not defaultMouse.isPressedIn(nextButton, buttons=[0]) and curMouseState==[0,0,0]:   # do this until we click on the button
            
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1 
            
        
            # update/draw components on each frame
            # --------------------Updates--------------------
            # componentUpdate updates the time and frameN of the component, and set it to autoDraw could have used single "draw" statement to save resources and time
            # use the function ust in case it's demanded
            
            
             # --------------------button&statebox--------------------
            
            nextButton.setLineColor(buttonLineColor1)
            nextButton.setFillColor(buttonBoxColor1)
            nextText.setColor(buttonTextColor1)
             
            componentUpdate(nextButton, t, frameN)
            componentUpdate(nextText, t, frameN)
            componentUpdate(stateBox, t, frameN)
            
            # --------------------Statements-update--------------------
            
            componentUpdate(statement1, t, frameN)
               
                     
            if startSecond:
                componentUpdate(statement2, t, frameN)
                
            if startThird:
                # keep track of stop time/frame for later
                componentUpdate(statement3, t, frameN)
                
            
            # --------------------Sliders--------------------
            # *slider* updates
            # keep track of start time/frame for later
            componentUpdate(slider1, t, frameN)
            componentUpdate(slider2, t, frameN)
            componentUpdate(slider3, t, frameN)
            componentUpdate(slider4, t, frameN)
            
            
            
            
            # --------------------slider-statements--------------------
            # *sliderS* updates
            # keep track of start time/frame for later
            componentUpdate(sliderS1, t, frameN)
            componentUpdate(sliderS2, t, frameN)
            componentUpdate(sliderS3, t, frameN)
            componentUpdate(sliderS4, t, frameN)
            
            # --------------------slider-values--------------------
            # keep track of start time/frame for later
            componentUpdate(sliderV1, t, frameN)
            componentUpdate(sliderV2, t, frameN)
            componentUpdate(sliderV3, t, frameN)
            componentUpdate(sliderV4, t, frameN)

            sliderV1.setText("{r:1.0f}%".format(r=slider1.markerPos*100)) # 1.1f means that the number is in 0.1 precision
            sliderV2.setText("{r:1.0f}%".format(r=slider2.markerPos*100))
            sliderV3.setText("{r:1.0f}%".format(r=slider3.markerPos*100))
            sliderV4.setText("{r:1.0f}%".format(r=slider4.markerPos*100))
            
            #---------------check for special keys and conditions---------------
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                
            win.flip()
                

        
        hasRespond = checkSlider(sliderComponents, sliderRecord0) # will stay True if ther is any response
        curMouseState = defaultMouse.getPressed()   # get mouse state when outside of the loop
                                                    # expecting [0,0,0]

        
        while defaultMouse.isPressedIn(nextButton, buttons=[0]):
                
            t = trialClock.getTime()
            frameN = frameN + 1 
        
            nextButton.setLineColor(buttonLineColor2)
            nextButton.setFillColor(buttonBoxColor2)
            nextText.setColor(buttonTextColor2)
            
            win.flip()
            
        
        nextButton.setLineColor(buttonLineColor1)
        nextButton.setFillColor(buttonBoxColor1)
        nextText.setColor(buttonTextColor1)
            
        # after the clicking on the button
        
        if hasRespond: # for the first respond, we force the participant to make a response
            
            if not hasRecord1 and statement2.status == NOT_STARTED and statement3.status == NOT_STARTED:
                for thisSub in orderedSliderSubject:
                    sliderRecord1.append(dicSlider[thisSub].getRating()) # record current rating
                        
                startSecond = True # used in drawing the second component
                hasRecord1 = True
                
                
        if not hasRecord2 and statement2.status == STARTED and statement3.status == NOT_STARTED:

            for thisSub in orderedSliderSubject:
                sliderRecord2.append(dicSlider[thisSub].getRating()) # record current rating
                        
           
            startThird = True # used in starting the third component
            hasRecord2 = True
            nextText.setText(nextText3)
            if trials.thisN == numPractice-1:
                nextText.setText(nextText2)

        if not hasRecord3 and statement2.status == STARTED and statement3.status == STARTED:
            
            for thisSub in orderedSliderSubject:
                sliderRecord3.append(dicSlider[thisSub].getRating()) # record current rating
                        
                
            hasRecord3 = True
            trialDuration = globalClock.getTime()
            continueRoutine = False # end the trial after the third statement is rated
        
        
        
        
        
        #---------------check for special keys and conditions---------------
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
        if continueRoutine:
            win.flip()
            
    
    
    # -------Ending Routine "trial"-------
    
    
    
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    
    
    trials.addData('statement1_NL', sliderRecord1[0])
    trials.addData('statement1_EL', sliderRecord1[1])
    trials.addData('statement1_A', sliderRecord1[2])
    trials.addData('statement1_T', sliderRecord1[3])

    trials.addData('statement2_NL', sliderRecord2[0])
    trials.addData('statement2_EL', sliderRecord2[1])
    trials.addData('statement2_A', sliderRecord2[2])
    trials.addData('statement2_T', sliderRecord2[3])
    
    trials.addData('statement3_NL', sliderRecord3[0])
    trials.addData('statement3_EL', sliderRecord3[1])
    trials.addData('statement3_A', sliderRecord3[2])
    trials.addData('statement3_T', sliderRecord3[3])
    
    trials.addData("trialDuration", trialDuration)

    #win.flip()  # clear the screen 
    core.wait(timeBetween)  # wait for some time between tria

    # ---------------------------------completed-1-repeats-of-trials---------------------------------
    
    
    
    thisExp.nextEntry()
    


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit


# ------Prepare to start Routine "goodbye_"-------
t = 0
goodbye_Clock.reset()  # clock
frameN = -1
initiateComponent(goodbyeText)



#---------------------------------------------------------------------------#
#----------------------------------Goodbye----------------------------------#
#---------------------------------------------------------------------------#




# ------Prepare to start Routine "Instruction"-------
t = 0
goodbye_Clock.reset()  # reusing the clock for instruction
frameN = -1

# initialize goodbye text
initiateComponent(goodbyeText)


# -------Start Routine "goodBye"-------


while True:
    
    # get current time
    t = goodbye_Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(goodbyeText, t, frameN)
        
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if defaultKeyboard.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        goodbyeText.setAutoDraw(False)
        
        break
    
    # refresh the screen
    win.flip()
 

# --------------------------------Ending Routine "goodbye_"--------------------------------




# --------------------------------------------------End-the-experiment--------------------------------------------------

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
win.close()
core.quit()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
