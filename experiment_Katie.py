#!/usr/bin/env python
# -*- coding: utf-8 -*-




"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on June 17, 2019, at 13:56
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""




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



from pyglet.window import key  # used to detect and record key presses




# ====================================User interaction to select the file start====================================



# Ensure that relative paths start from the same directory as this script

# Store info about the experiment session
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
psychopyVersion = '3.1.2'



# ====input information====

expName = "Experiment" 

expInfo = {'participant': '', 'session': '001'}


dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
    
    
    
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion



# ==== select condition file ====


conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  # a list object, save the path(including the name) of the file selected, conditionFile[0] gives the file name string
    
    # format note: 
    #   the condition file should contain:img_1, img_2, img_3, txt_1, txt_2, txt_3
        
    #   img_* are the path for the picture, including the post-fix of picture at the end
    #       remember to put the slash in file path as "\\", or may not work in some cases (like on my PC
    #   txt_* are the words displayed
    #   for convinience, only csv files are allowed
    
    
    # consider modify into non-specific namings
    
    
if not conditionFile:
    core.quit
    



# ================================================User interaction to select the file end===========================




# reminder: if future putting the parameter and functions in other file?




# ====================================Some newly defined parameters start====================================




#====Time parameters(unit: second)====



timeConfidence = 4  # The time we believe after which the participant have made their decision


timeFadeIn = 2  #  time for the image to fade in
timeFadePara = timeFadeIn * 60  # the parameter to divided with

timeStartOne = 0.0  # the starting time for the first picture to emerge

timeBuffering = 3  # Time for blank screen between each condition, set constant buffering for convenience



#====slider parameters(unit: height)====





# speed of the marker movement (sensitivity)

sliderSpeed = 0.01





# start and end points of slider
# note: if want multiple ticks, need to modify the script in initialization section

sliderLeftP = 0  # left end
sliderRightP = 1  #right end

sliderStartP = (sliderRightP + sliderLeftP)*0.5 # the initial position (any number between start and end)


# text to display at start and end of slider

sliderLeftT = "NO"
sliderRightT = "YES"





# ====================================Some newly defined parameters end====================================







# ====================================Some newly defined functions start====================================



    # function for Updating txt and img
def componentUpdate(component, time, frameN, isFirst):
  
    # if the component is not started
    if component.status == NOT_STARTED:
        # keep track of start time/frame for later
        if isFirst == True:
            component.setAutoDraw(True)
            
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
    
    

# ====================================Some newly defined functions end====================================








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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    
    
    
# ====================================Add pyglet window start====================================
    

# initialize pyglet 

keyState = key.KeyStateHandler()
win.winHandle.push_handlers(keyState)


# ====================================Add pyglet window end====================================
    



# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()


# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()






# ====================================Own clock for record start====================================

# Used to detect whether we reached the timeConfidence

timerRecord = core.CountdownTimer()


# =====================================Own clock for record end=====================================





# ====================================Add mouse start====================================


myMouse = event.Mouse(newPos = (1,1))
myMouse.setVisible(False)
pos = myMouse.getPos()  # add the position


# ====================================Add moues start====================================



instructionText = visual.TextStim(win=win, name='instructionText',
    text='This is the instruction of the experiment\n\npress "space" to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
    

goodbyeText = visual.TextStim(win=win, name='goodbyeText',
    text='Thank you for participate, press space to quit',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
    
    
    
# Initialize components for Routine



TrialsClock = core.Clock()




slider = visual.Slider(win=win, name='slider',
    size=(1.0, 0.05), pos=(0, -0.35),
    labels=(sliderLeftT, sliderRightT), ticks=(sliderLeftP,sliderRightP),
    granularity=0, style=('triangleMarker',),
    color='LightGray', font='HelveticaBold',
    flip=False, units="height")
    
    
    
text1 = visual.TextStim(win=win, name='text1',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
    
text2 = visual.TextStim(win=win, name='text2',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
    
text3 = visual.TextStim(win=win, name='text3',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
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
    color=[1,1,1], colorSpace='rgb', opacity=0.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started


#-------------------------#
#-------Instruction-------#
#-------------------------#




# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True



# initialize the instruction text
initiateComponent(instructionText)





# -------Start Routine "Instruction"-------
while True:
    
    

    if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:# Fixate the mouse
        myMouse.setPos(newPos = (1,1))
    
    
    
    # get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    
    
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(instructionText, t, frameN, True)
        
        
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if defaultKeyboard.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        instructionText.setAutoDraw(False)
        instructionText.status = FINISHED
        
        break
        
        
    # refresh the screen
    win.flip()
    
    

win.flip()  # get a blank screen
core.wait(timeBuffering)  # buffering for participant


# -------Ending Routine "Instruction"-------
        
thisExp.addData('Instruct.started', instructionText.tStartRefresh)
thisExp.addData('Instruct.stopped', instructionText.tStopRefresh)




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


# Three images and three texts



#--------------------#
#-------Repeat-------#
#--------------------#


for thisRepeat in Repeat:


    currentLoop = Repeat
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))

    
    #--------------------#
    #-------Trials-------#
    #--------------------#
    
    
    
    # ------Prepare to start Routine "Trials"-------
    
    
    
    
    t = 0
    TrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    
    # create a keyboard to record all the keys pressed during one trial
    trialKeyboard = keyboard.Keyboard()
    
    
    
    # ==========================================clock and list for record slider start=====================================================
    
    timerRecord.reset(t=timeConfidence)
    
    sliderHistorySecond = [] # store here the rating and the time at point wanted
    
    
    # ==========================================clock and list for record slider end=====================================================

    
    
    # update component parameters for each repeat
    slider.reset()
    text1.setText(txt_1)
    text2.setText(txt_2)
    text3.setText(txt_3)
    image1.setImage(img_1)
    image2.setImage(img_2)
    image3.setImage(img_3)
    
    
    
    # ==========================================entering start=====================================================
    
    entering = 0  # for each repeat, entering start from 0
     
    # ==========================================entering end=====================================================
    

    
    
    # keep track of which components have finished
    TrialsComponents = [slider, text1, text2, text3, image1, image2, image3]
    
    for thisComponent in TrialsComponents:
        initiateComponent(thisComponent)
    
    
    
    # -------Start Routine "Trials"-------
    while continueRoutine:
        # get current time
        t = TrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        
        
        # update/draw components on each frame
        
        if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:# Fixate the mouse
            myMouse.setPos(newPos = (1,1))
        
    
    
        # ====================================Modify slider start====================================

        
        
        
        if t >= timeStartOne:
        
            #record starting position, starting slider
            if slider.status == NOT_STARTED:
                slider.recordRating(rating = sliderStartP)
                slider.setAutoDraw(True)
                
            #update slider
            componentUpdate(slider, t,frameN, False)
        
        
            
    

        # Movement and record updates
        if keyState[key.LEFT]:
            newRat = slider.rating - sliderSpeed
            slider.rating = newRat
            timerRecord.reset(t = timeConfidence)
        
        if keyState[key.RIGHT]:
            newRat = slider.rating + sliderSpeed
            slider.rating = newRat
            timerRecord.reset (t = timeConfidence)
            
            
        
        
        # see whether the decision is made, more specifically: 
        #    when non of the keys are pressed for the confidence time, record the rating, redo clock
        #    add count for entering this, set the True/False value accordingly for image and text
                
        #    when entering = 1, image1 & txt1 finished, image2 & txt2 starts
        #    when entering = 2, image2 & txt2 finished, image3 & txt3 starts, and freeze the slider
        #    when entering = 3, image3 & txt3 finished, stop the entire trial
        
        
        
        if timerRecord.getTime() <= 0:
            
            sliderHistorySecond.append([slider.getRating(), (TrialsClock.getTime()-timeConfidence)])  # record rating and the time of decision
            
            entering += 1  #implement by 1
            command = None  #place holder
            
            if entering < 3:
                 
                command = "text{}.setAutoDraw(False)\nimage{}.setAutoDraw(True)\ntext{}.setAutoDraw(True)".format(str(entering), str(entering+1), str(entering+1))  # starts the next image
                
            if entering == 2:
                
                
                command = command + "\nslider.setAutoDraw(False)"  # remove the slider in the third picture
                
                
            if entering == 3:
                
                command = "continueRoutine = False"  # stop the routine
                
                
                
                
            exec(command)
            
            timerRecord.reset(t = timeConfidence)  # reset the clock at the end s.t can count again
            
        
        
        
        # ====================================Modify slider end====================================
        
        

        
        
        
        # text1 + image 1 updates after the "timeStartedOne"
        if t >= timeStartOne:
            
            componentUpdate(text1, t,frameN, True)
            componentUpdate(image1, t, frameN, True)
            
            

        #update opacity of img1
        imgFadeIn(image1, frameN, timeFadePara)
        
        
        
        
        # text2 + image2 updates
        componentUpdate(text2, t, frameN, False)
        componentUpdate(image2, t, frameN, False)
        
        # update opacity of img2
        imgFadeIn(image2, frameN, timeFadePara)
        
        
        
        
        # text3 + image3 updates
        componentUpdate(text3, t, frameN, False)
        componentUpdate(image3, t, frameN, False)
        
        # update opacity of img3
        imgFadeIn(image3, frameN, timeFadePara)
        







        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    
    # end this condition, save data
    
    
    # -------Ending Routine "Trials"-------
    for thisComponent in TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            
    Repeat.addData('slider.started', slider.tStartRefresh)
    Repeat.addData('slider.stopped', slider.tStopRefresh)
    Repeat.addData('text1.started', text1.tStartRefresh)
    Repeat.addData('text1.stopped', text1.tStopRefresh)
    Repeat.addData('text2.started', text2.tStartRefresh)
    Repeat.addData('text2.stopped', text2.tStopRefresh)
    Repeat.addData('text3.started', text3.tStartRefresh)
    Repeat.addData('text3.stopped', text3.tStopRefresh)
    Repeat.addData('image1.started', image1.tStartRefresh)
    Repeat.addData('image1.stopped', image1.tStopRefresh)
    Repeat.addData('image2.started', image2.tStartRefresh)
    Repeat.addData('image2.stopped', image2.tStopRefresh)
    Repeat.addData('image3.started', image3.tStartRefresh)
    Repeat.addData('image3.stopped', image3.tStopRefresh)
    
    
    
    
    # ==========================================Added custom data start=====================================================
    
    
    
    keyRecord = trialKeyboard.getKeys(['left','right'])
    
    
    addKeys = []
    for k in keyRecord:
        addKeys.append([k.name, k.rt, k.duration])
    
    
    Repeat.addData("slider.history_rating_timePoint", sliderHistorySecond)  # the slider rating and time, no movement for confidence time
    Repeat.addData("keyboard.record_name_rt_duration", addKeys) #the entire keyboard record
    
    
    
    # ==========================================Added custom data end=====================================================
    
    
    
    
    win.flip()
    
    core.wait(timeBuffering) # will be blank screen after end for the time required
    
    thisExp.nextEntry()
    
    
    # completed 1 repeats of 'Repeat'
    
    
    
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()








#-------------------------#
#---------Goodbye---------#
#-------------------------#




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
        componentUpdate(goodbyeText, t, frameN, True)
        
        
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
    
    


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()


# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit


win.close()
core.quit()
