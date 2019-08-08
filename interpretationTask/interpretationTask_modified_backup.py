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


#----------------------------------------------------------------------



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
    k = 0 # k = 0,1,2,3, looping number. originRatings[0] = the original rating of slider1

    for thisSlider in sliders:
        if thisSlider.rating != originRatings[k]:
            return True  # if there is any movement, consider it as "has responded"
        k += 1
    return False  # if everything is untouched, it's not responded
    
    
# some variables

# starting point and ending point of the sliders

startP = 0  # starting value of all sliders
endP = 1   # ending value of all sliders
startT = "0%"  # text displayed at at the starting point of the slider
endT = "100%"  # text displayed at the end of the slider

# physical properties of the sliders

stateH = 0.03  # The height of the statement (text size)
sliderH = 0.03  # The height of the slider 
sliderSH = 0.03  # The height of the slider statement (text size)

stateX = 0  # The x-position of the statement

# the y-position of the first component (slider, statement, sliderStatements)

stateP1 = 0.40 # The y-position of the first statment
sliderP1 = -0.03  # The y-position of the first slider
sliderSP1 = 0 # each statement should be on the top of the slider

# the distance between each component
# calculate to make sure they are evenly spread
# height/2+distance = the distance between each identical component

dis = 0.047

stateD = stateH/2 + dis
sliderD = sliderH/2 + dis*2
sliderSD = sliderSH/2 + dis*2


timeBetween = 2  # time between each trial





#----------------------------------------------------------------------











# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)









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




conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  # a list object, save the path(including the name) of the file selected, conditionFile[0] gives the file name string
    






# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    #originPath='C:\\Users\\que_d\\Documents\\McGill\\LepageLab\\psychopyExperiment_github\\interpretationTask\\interpretationTask.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp











# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color="lightGray", colorSpace='rgb',
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

introText = visual.TextStim(win=win, name='introText',
    text='Instructions, press space to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"


#-----Statements-----
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
    
    
#-----sliders-----
slider1 = visual.Slider(win=win, name='slider1',
    size=(1.4, sliderH), pos=(0, sliderP1),
    ticks=(startP, endP),labels=(startT, endT),
    granularity=0, style=['rating'],
    color='DarkGray', font='HelveticaBold',
    flip=False)
slider2 = visual.Slider(win=win, name='slider2',
    size=(1.4, sliderH), pos=(0, sliderP1-sliderD),
    ticks=(startP, endP), labels=(startT, endT),
    granularity=0, style=['rating'],
    color='DarkGray', font='HelveticaBold',
    flip=False)
slider3 = visual.Slider(win=win, name='slider3',
    size=(1.4,sliderH), pos=(0, sliderP1-sliderD*2),
    ticks=(startP, endP), labels=(startT, endT),
    granularity=0, style=['rating'],
    color='DarkGray', font='HelveticaBold',
    flip=False)
slider4 = visual.Slider(win=win, name='slider4',
    size=(1.4, sliderH), pos=(0, sliderP1-sliderD*3),
    ticks=(startP, endP), labels=(startT, endT),
    granularity=0, style=['rating'],
    color='DarkGray', font='HelveticaBold',
    flip=False)
    
    
sliderComponents = [slider1, slider2, slider3,slider4]

for thisSlider in sliderComponents:
    thisSlider.marker.fillColor, thisSlider.marker.lineColor = "black", "black"
    #thisSlider.marker.lineColor = "black"

#-----slider-statements-----
sliderS1 = visual.TextStim(win=win, name='sliderS1',
    text='default text', 
    font='Arial',
    pos=(stateX, sliderSP1), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
sliderS2 = visual.TextStim(win=win, name='sliderS2',
    text='default text',
    font='Arial',
    pos=(stateX, sliderSP1-sliderSD), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
sliderS3 = visual.TextStim(win=win, name='sliderS3',
    text='default text',
    font='Arial',
    pos=(stateX, sliderSP1-sliderSD*2), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
sliderS4 = visual.TextStim(win=win, name='sliderS4',
    text='default text',
    font='Arial',
    pos=(stateX, sliderSP1-sliderSD*3), height=sliderSH, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);



# Initialize components for Routine "goodbye_"


goodbyeText = visual.TextStim(win=win, name='goodbyeText',
    text='Thank you for participating, press space to quit.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



#Button (composed of a rectangle and a text stimuli)
nextButton = visual.Rect(win, name="nextButton", 
                    width=0.1, height =0.05, pos=(0,-0.45))
nextButton.setFillColor("white")

nextText = visual.TextStim(win, text="NEXT", 
                pos=(0,-0.45), color="black", height=0.03)





#-------------------------#
#----------INTRO----------#
#-------------------------#



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# initialize the instruction text
initiateComponent(introText)


#indicate whether participant has moved any of the sliders
hasRespond = False



# -------Start Routine "Instruction"-------
while True:
    
    # flow contro variable

    
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(introText, t, frameN)
        
        
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if defaultKeyboard.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        introText.setAutoDraw(False)
        introText.status = FINISHED
        
        break
        
        
    # refresh the screen
    win.flip()
    
    

win.flip()  # get a blank screen
#core.wait(timeBuffering)  # buffering for participant





#--------------------------#
#----------TRIALS----------#
#--------------------------#


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
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    
    
    startSecond = False
    startThird = False
    hasRecord1 = False
    hasRecord2 = False
    hasRecord3 = False
    

    
    
    
    # update component parameters for each repeat
    statement1.setText(state1)
    statement2.setText(state2)
    statement3.setText(state3)
    slider1.reset()
    slider2.reset()
    slider3.reset()
    slider4.reset()
    sliderS1.setText(sliderState1)
    sliderS2.setText(sliderState2)
    sliderS3.setText(sliderState3)
    sliderS4.setText(sliderState4)
    
    
    
    
    
    
    # keep track of which components have finished
    trialComponents = [statement1, statement2, statement3, slider1, slider2, slider3, slider4, sliderS1, sliderS2, sliderS3, sliderS4, nextButton, nextText]
    for thisComponent in trialComponents:
        initiateComponent(thisComponent)
        
    for thisSlider in sliderComponents:
        thisSlider.recordRating(startP)
    
    
    
    sliderRecord0 = [startP, startP, startP, startP] # initial value
    sliderRecord1 = [] # placeholder for the first set of response
    sliderRecord2 = [] # second
    sliderRecord3 = [] # third
    

    

    
    
    # -------Start Routine "trial"-------
    while continueRoutine:

        
        while not defaultMouse.isPressedIn(nextButton, buttons=[0]):   # do this until we click on the button
        # get current time
            t = trialClock.getTime()
            frameN = frameN + 1 
             # number of completed frames (so 0 is the first frame)
        
        
        # update/draw components on each frame
        
        
        
            
            # --------------------Updates--------------------
            # componentUpdate updates the time and frameN of the component, and set it to autoDraw could have used single "draw" statement to save resources and time
            # use the function ust in case it's demanded
            
            
            
            
            # --------------------Statements-update--------------------
            
            componentUpdate(statement1, t, frameN)
               
                     
            if startSecond:
                componentUpdate(statement2, t, frameN)
                
            if startThird:
                # keep track of stop time/frame for later
                componentUpdate(statement3, t, frameN)
        
        
            
            # --------------------button--------------------
            componentUpdate(nextButton, t, frameN)
            componentUpdate(nextText, t, frameN)
            
            
            # --------------------Sliders--------------------
            # *slider1* updates
            # keep track of start time/frame for later
            componentUpdate(slider1, t, frameN)
            componentUpdate(slider2, t, frameN)
            componentUpdate(slider3, t, frameN)
            componentUpdate(slider4, t, frameN)
            
            # --------------------slider-statements--------------------
            # *sliderS1* updates
            # keep track of start time/frame for later
            componentUpdate(sliderS1, t, frameN)
            componentUpdate(sliderS2, t, frameN)
            componentUpdate(sliderS3, t, frameN)
            componentUpdate(sliderS4, t, frameN)
            


            
            #event.clearEvents(eventType = "mouse")
        
            #---------------check for special keys and conditions---------------
            


            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            if continueRoutine:
                win.flip()
                
                

        hasRespond = checkSlider(sliderComponents, sliderRecord0) # will stay True if ther is any response
        
        # after the clicking on the button
        
        if hasRespond: # for the first respond, we force the participant to make a response
            
            if not hasRecord1 and statement2.status == NOT_STARTED and statement3.status == NOT_STARTED:
                for thisSlider in sliderComponents:
                    sliderRecord1.append(thisSlider.getRating()) # record current rating
                        
                startSecond = True # used in drawing the second component
                hasRecord1 = True
                
                
                
                
                
            
        if not hasRecord2 and statement2.status == STARTED and statement3.status == NOT_STARTED:

            for thisSlider in sliderComponents:
                sliderRecord2.append(thisSlider.getRating()) # record current rating 
           
            startThird = True # used in drawing the third component
            hasRecord2 = True

        if not hasRecord3 and statement2.status == STARTED and statement3.status == STARTED:
            
            for thisSlider in sliderComponents:
                sliderRecord3.append(thisSlider.getRating()) # record current rating
                
            hasRecord3 = True
            continueRoutine = False # end the trial after the third statement is rated
        
        
        
        
        
        #---------------check for special keys and conditions---------------
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
            
            
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('statement1_rating', sliderRecord1)
    trials.addData('statement2_rating', sliderRecord2)
    trials.addData('statement3_rating', sliderRecord3)


    win.flip()  # clear the screen 
    core.wait(timeBetween)  # wait for some time between tria

    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'















# ------Prepare to start Routine "goodbye_"-------
t = 0
goodbye_Clock.reset()  # clock
frameN = -1
continueRoutine = True
initiateComponent(goodbyeText)












#-------------------------#
#---------Goodbye---------#
#-------------------------#




# ------Prepare to start Routine "Instruction"-------
t = 0
goodbye_Clock.reset()  # reusing the clock for instruction
frameN = -1
continueRoutine = True


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
        goodbyeText.status = FINISHED
        
        break
    
    # refresh the screen
    win.flip()
    
    
    
    
    
    
    
    
    
# -------Ending Routine "goodbye_"-------
goodbyeText.setAutoDraw(False)



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
