#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
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
from psychopy.visual import Circle, Rect



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







# ====================================Some newly defined functions start====================================



    # function for Updating txt and img
def componentUpdate(component, time, frameN, isFirst):
  
    # if the component is not started
    if component.status == NOT_STARTED:
        # keep track of start time/frame for later
        if isFirst == True:
            event.clearEvents()  # Clean up the keyboard buffering s.t. anything before the component start is not recorded (or you will get negative reaction time)
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
    

# initialize pyglet trick

keyState = key.KeyStateHandler()
win.winHandle.push_handlers(keyState)


# ====================================Add pyglet window end====================================
    




frameDur = None


# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess




# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()




# ====================================Some newly defined parameters start====================================



#====Time parameters(unit: frame)====



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




slider = visual.Slider(win=win, name='slider',
    size=(0.05, 0.6), pos=(0.5, 0),
    labels=(sliderLeftT, sliderRightT), ticks=(sliderLeftP,sliderRightP),
    granularity=0, style=['slider'],
    color='black', font='HelveticaBold',
    flip=False, units="height")
    
    
    #  notice that the "size" of the slider controls whether the slider is verticle or horizontal
    
    
    
#  change to desired style, using the in-built visual stimulus from psychopy
    
    
    
slider.marker = Circle(win, 
                        radius = slider.size[0]*0.5,  # The radius should be half the width 
                        edges = 32, 
                        fillColor = 'gray', 
                        lineColor = 'gray')
                        
slider.line = Rect(win, units=slider.units,
                        pos=slider.pos,
                        width=slider.size[0],
                        height=slider.size[1]+0.005,  # +0.005 just to make the rectangule looks better
                        lineColor='black', 
                        fillColor = 'black',
                        autoLog=False)
    
    
    
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





# instructionclock also later re-used for goodbye message
InstructionClock = core.Clock()



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
    
    

    if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:  # Fixate the mouse to the upper-right conor
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
#core.wait(timeBuffering)  # buffering for participant


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

    
    event.clearEvents(eventType='keyboard')
    
    currentLoop = Repeat
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
            
            
            
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    # ------Prepare to start Routine "Trials"-------
    
    
    
    
    sliderHistorySecond = [] # store here the rating and the time at point wanted
    
    TrialsComponents = [slider, text1, text2, text3, image1, image2, image3] # keep track of which components have finished
    
    for thisComponent in TrialsComponents:
        initiateComponent(thisComponent)  # set the values to None
    

    
    core.wait(timeBuffering)  #blank screen for time buffering
    
    
    #hasRespond = False  # check if the participant has responded or not
    continueRoutine = True  # check if continue routine or not
    
    frameN = -1
    t = 0
    entering = 0  # for each repeat, entering start from 0, therefore need to be initialized outside of the loop
    
    
    # initialize some clocks
    TrialsClock = core.Clock()  #  Create some handy timers
    countDown = core.CountdownTimer()   # Used to detect whether we reached the timeConfidence
    
    
    # create a keyboard to record all the keys pressed during one repeat
    trialKeyboard = keyboard.Keyboard()
    
    
    event.clearEvents()  # clean up buffer before entering to the loop (not sure why it couldn't remove the keys with negative reaction time, and this is why I added getKeys() to remove)
    trialKeyboard.getKeys()  # to remove the keys that was pressed during the buffering periods, or we will get negative reaction time for those keys
    
    
    # reset the clocks to starting time
    TrialsClock.reset()  # clock of the trial
    countDown.reset(t=timeConfidence)  # clock for timeConfidence
    
    
    
    
    
    # -------Start Routine "Trials"-------
    while continueRoutine:
        # get current time
        
        
        t = TrialsClock.getTime()  # current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

    
    
    
        
        if myMouse.getPos()[0]!= 1 or myMouse.getPos()[1] != 1:# Fixate the mouse
            myMouse.setPos(newPos = (1,1))
            
            # notice: I added this step because on my computer the setVisible of mouse event didn't work
            # may be due to the mouse initialization in the slider class
            # Therefore I just fixiated it s.t. it won't be used
            
            
            
            
        # update/draw components on each frame
        
        
        
        #---------------#
        #---------------#
        #-slider-update-#
        #---------------#
        #---------------#
        
        
        #  Movement and record updates
        #  changed to DOWN and UP according since it's a verticle slider
        #  only detect during the first two pictures
        
        if entering < 2 :
            
            
            if keyState[key.DOWN]:
                newRat = slider.rating - sliderSpeed
                slider.rating = newRat
                countDown.reset(t = timeConfidence)
                hasRespond = True
            
            if keyState[key.UP]:
                newRat = slider.rating + sliderSpeed
                slider.rating = newRat
                countDown.reset (t = timeConfidence)
                hasRespond = True
                
            
        if t >= timeStartOne:
        
            #record starting position, starting slider
            if slider.status == NOT_STARTED:
                slider.recordRating(rating = sliderStartP)
                slider.setAutoDraw(True)
                
            #update slider
            componentUpdate(slider, t, frameN, False)
        
        
        
        
        #-------------------------#
        #-------------------------#
        #-switch-between-pictures-#
        #-------------------------#
        #-------------------------#
        
        
        #    see whether the decision is made, more specifically: 
        #       Not entering unles the participant has responded
        #       when non of the keys are pressed for the confidence time, record the rating, redo clock
        #       add count for entering this, set the True/False value accordingly for image and text
        #       note that when setAutoDraw = True, status changes to STARTED automatically
        
        #    when entering = 1, image1 & txt1 finished, image2 & txt2 starts
        #    when entering = 2, image2 & txt2 finished, image3 & txt3 starts, and set the slider to read-only
        #    when entering = 3, image3 & txt3 finished, stop the entire trial
        
        
        
        #if countDown.getTime() <= 0 and hasRespond:  # countDown is a count-down timer, with parameter "timeConfidence"
        if countDown.getTime() <= 0:  # countDown is a count-down timer, with parameter "timeConfidence"
            
            
                 
            
            entering += 1  #implement by 1
            command = "pass"  #place holder
            

            #entering = 1, 2
            
            if entering < 3:
                
                
                #hasRespond = False  # flip it back to false
                 
                command = "text{}.setAutoDraw(False)\nimage{}.setAutoDraw(True)\ntext{}.setAutoDraw(True)".format(str(entering), str(entering+1), str(entering+1))  # starts the next image
                command +="\nkeyRecord{} = trialKeyboard.getKeys(['up','down'])".format(str(entering))#  get the keys here (getKeys get the respond starting from the last call of getKeys)
                
                
                if entering == 2: # after the end of the second image
                    
                    
                    command += "\nslider.readOnly = True"  # set slider to read only for the third picture
                    
                    #hasRespond = True  # When we are at the second image, set it True for the third image
                    
                    
                    
                    # Note: since the keyboards seems to be using the same buffer, if stop recording the keyboard input here, the defaultKeyboard won't be able to catch escape and space for exiting the program later
                    
                    
                exec(command)
                exec("tmp = image{}.tStart".format(str(entering)))
                
                
                sliderHistorySecond.append([slider.getRating(), (t-timeConfidence-tmp)])  # record rating and the time of decision, append it to the list
                # This is the rating and time for making the decision, should get two pairs since there shouldn't be any rating for the third picture
               
                
            
            #entering = 3
            
            if entering == 3:
                
                continueRoutine = False  # stop the routine
                
            
            
            countDown.reset(t = timeConfidence)  # reset the clock at the end s.t can count down again
            
            
            
            
            
            
        #------------------------#
        #------------------------#
        #-image-and-text-updates-#
        #------------------------#
        #------------------------#
        
        
        # Notice that this can't be moved before the switching, because
        
        
        # text1 + image 1 updates after the "timeStartedOne"
        if t >= timeStartOne:
            
            componentUpdate(text1, t, frameN, True)
            componentUpdate(image1, t, frameN, True)
            
            
            
        # update opacity of img1
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
        
        
        
        
        #--------------------------------#
        #--------------------------------#
        #----check-special-conditions----#
        #--------------------------------#
        #--------------------------------#
        
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    
    
    
    
    #---------------------------#
    #---------------------------#
    #-----end-and-save-data-----#
    #---------------------------#
    #---------------------------#
    
    
    # -------Ending Routine "Trials"-------
    for thisComponent in TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    
    Repeat.addData('slider.started', slider.tStart)
    Repeat.addData('slider.stopped', slider.tStop)
    Repeat.addData('text1.started', text1.tStart)
    Repeat.addData('text1.stopped', text1.tStop)
    Repeat.addData('text2.started', text2.tStart)
    Repeat.addData('text2.stopped', text2.tStop)
    Repeat.addData('text3.started', text3.tStart)
    Repeat.addData('text3.stopped', text3.tStop)
    Repeat.addData('image1.started', image1.tStart)
    Repeat.addData('image1.stopped', image1.tStop)
    Repeat.addData('image2.started', image2.tStart)
    Repeat.addData('image2.stopped', image2.tStop)
    Repeat.addData('image3.started', image3.tStart)
    Repeat.addData('image3.stopped', image3.tStop)
    
    
    
    # place holder
    addKeys1 = []
    addKeys2 = []
    
    
    # reaction time = time of the key - tStart of the figure
    
    for k in keyRecord1:
        addKeys1.append([k.name, k.rt-image1.tStart, k.duration])
        
    for k in keyRecord2:
        addKeys2.append([k.name, k.rt-image2.tStart, k.duration])
    
    
    
    Repeat.addData("slider.history_rating_timePoint", sliderHistorySecond)   # the slider rating and time, no movement for confidence time
    Repeat.addData("keyboard.record_name_rt_duration_img1", addKeys1)  #record for img 1
    Repeat.addData("keyboard.record_name_rt_duration_img2", addKeys2)
    
    
    
    
    
    
    win.flip()
    thisExp.nextEntry()
    
    
    # completed 1 repeats of 'Repeat'
    
    
    
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
win.saveFrameIntervals(fileName = "allFrameTimes.txt", clear = True)
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
