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
        component.setAutoDraw(True)     # start the component
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
    
# ---------------------------------------------some-variables---------------------------------------------


#====Time parameters(unit: frame)====



timeConfidence = 3  # The time we believe after which the participant have made their decision


timeFadeIn = 4  #  time for the image to fade in
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

sliderLeftT = "0%"
sliderRightT = "100%"


#====Instruction text====

instructionText = """Dans cette tâche, vous devrez identifier des images.\n
                    \nVous allez voir graduellement une image, avec un mot écrit en-dessous. Évaluez si vous croyez que le mot décrit de manière adéquate l’image complète. Une fois que vous avez répondu, plus de détails de l’image commenceront à apparaître. Reconsidérez l’évaluation que vous avez faite. Vous pouvez changer votre évaluation autant que vous le voulez. Une fois votre deuxième évaluation faite, vous verrez l’image entière et le mot correct. Vous ne devez pas répondre à l’image entière.\n
                    \nVous allez utiliser le clavier, pour faire vos évaluations. Appuyez et maintenez les touches de la flèche de droite et de gauche, pour déplacer l’évaluation vers oui ou non, respectivement. Vous pouvez faire vos évaluations à n’importe quel endroit sur l’échelle, dépendamment à quel point vous êtes confiant de votre réponse. Vous pouvez prendre le temps dont vous avez besoin, mais essayez de répondre le plus vite que vous pouvez.\n
                    \nVous allez maintenant compléter plusieurs essais de pratique, avant de commencer l’exercice."""




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
   
if not conditionFile:
    core.quit
    

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

# add mouse
myMouse = event.Mouse(newPos = (1,1))
myMouse.setVisible(False)
pos = myMouse.getPos()  # add the position


expTitle = visual.TextStim(win=win, name='introText',
    text = "Picture Identification Task",    
    font='Arial',
    pos=(0, 0.40), height=0.05, bold=True, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

introText = visual.TextStim(win=win, name='introText',
    text = instructionText,    
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=1.5, ori=0, 
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
# initialize the instruction text
initiateComponent(expTitle)
initiateComponent(introText)


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
        
    # check for quit (typically the Esc key)
    if endExpNow or kb.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if kb.getKeys(keyList=["space"]):  # a forced-end of Routine when pressed space
        introText.setAutoDraw(False)
        expTitle.setAutoDraw(False)        
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
    slider.recordRating(0.5)

    image1.setOpacity(0)
    image2.setOpacity(0)
    
    # ------Prepare to start Routine "Trials"-------
    
    sliderRating = []    # store here the rating and the time at point wanted
    sliderRatingSecond = []
    currentKey = []             # The list of keys
    
    TrialsComponents = [slider, text1, text2, text3, image1, image2, image3] # keep track of which components have finished
    
    for thisComponent in TrialsComponents:
        initiateComponent(thisComponent)        # set the values to None

    core.wait(timeBuffering)                    #blank screen for time buffering
    
    hasRespond = False                         # check if the participant has responded or not
    continueRoutine = True                     # check if continue routine or not
    
    
    
    frameN = -1
    t = 0
    
    # initialize some clocks
    trialsClock = core.Clock()                        #  Create some handy timers
    countDown = core.CountdownTimer(timeConfidence)   # Used to detect whether we reached the timeConfidence
    
    
    
    
    # reset the clocks to starting time
    trialsClock.reset()              # clock of the trial
    countDown.reset(timeConfidence)  # clock for timeConfidence
    globalClock.reset()              # to track the trial duration
    kb.clock.reset()                 # reset clock for keyboard (reset for each picture)
    
    while continueRoutine:
        
        # img1
            # force respond
            # wait for confidence time
        t = trialsClock.getTime()
        frameN += 1
        

        #start image1 , text1 and slider
        
        componentUpdate(win, image1, t, frameN)
        componentUpdate(win, text1, t, frameN)
        componentUpdate(win, slider, t, frameN)
        
        # fade in image1
        imgFadeIn(image1, frameN, timeFadePara)
        
        if image2.status == STARTED:
            
            # fade in image2
            imgFadeIn(image2, frameN, timeFadePara)
            
            # update current time and frame record
            componentUpdate(win, image2, t, frameN)
            componentUpdate(win, text2, t, frameN)
            
        if image3.status == STARTED:
            
            # update time and frame record
            componentUpdate(win, image3, t, frameN)
            componentUpdate(win, text3, t, frameN)
        
        # ----- moving sliders ----- 
        
        # get current key pressed
        currentKey = kb.getKeys(keyList=["up", "down"], waitRelease=False, clear=False)
        
        
        # since getKeys() return a list, we want a non-empty list
        if currentKey!=[]:
            
            # if it's not empty, check the last one in the queue (the most current one)
            # check whether duration has been reported
            # ( duration will remain as "None" before key-release )
            
            while currentKey[-1].duration == None:
                
                # enter inner loop if it's pressed
                
                t = trialsClock.getTime()
                
                # get update on the key
                currentKey = kb.getKeys(keyList=["up", "down"], waitRelease=False, clear=False)
                
                # up => add to slider
                # down => minus from slider
                
                if currentKey[-1].name == "up":
                    slider.recordRating(slider.rating + sliderSpeed)
                    
                else:
                    slider.recordRating(slider.rating - sliderSpeed)
                
                
                # when making selection, if the images are in the process of fading in, continue to fade in
                
                imgFadeIn(image1, frameN, timeFadePara)
                
                if image2.status == STARTED:
                    
                    imgFadeIn(image2, frameN, timeFadePara)
                
                # when entered this loop, it means that there is at least one response, set hasRespond = True
                hasRespond = True
                
                # reset coun-down timer for every loop
                countDown.reset(timeConfidence)
                
                # check for quit (typically the Esc key)
                if endExpNow or kb.getKeys(keyList=["escape"]):
                    core.quit()
                
                frameN += 1
                win.flip()
        
        
        # if there is a response and have waited for timeConfidence, enter next picture & record
        
        if hasRespond and countDown.getTime()<=0:
            
            t = trialsClock.getTime()
            
            # when all three images has been shown, end the trial
            
            if image1.status == STARTED and image2.status == STARTED and image3.status == STARTED:
                
                continueRoutine = False
            
            # when first two images has been shown, start the image3 and text3
                # start img3, no fade in required
                # remove text2 and slider
                # record key presses during img2
                # record rating from the slider
                # reset countDown timer
                
            elif image1.status == STARTED and image2.status == STARTED and image3.status == NOT_STARTED:
                
                text2.setAutoDraw(False)
                slider.setAutoDraw(False)
                
                keyRecord2 = kb.getKeys(keyList=["up", "down"], waitRelease=False, clear = True)
                
                if keyRecord2 != []:
                    sliderRating.append([slider.getRating(), keyRecord2[-1].rt + keyRecord2[-1].duration])
                else:
                    sliderRating.append([slider.getRating(), -88])
                    
                componentUpdate(win, image3, t, frameN)
                componentUpdate(win, text3, t, frameN)
                countDown.reset(timeConfidence)
                
            # after img1 has been rated, start image2 and text2
                # start image2, fade in required
                # stop text1
                # record key presses during image1
                # append ratings (will be the first pair in the sliderRating)
                # reset countDown timer
                # reset keyboard inner clock (s.t. rating for image2 will be starting from 0)
                
            elif image1.status == STARTED and image2.status == NOT_STARTED and image3.status == NOT_STARTED:
                
                text1.setAutoDraw(False)
                
                keyRecord1 = kb.getKeys(keyList=["up", "down"], waitRelease=False, clear = True)
                
                sliderRating.append([slider.getRating(), keyRecord1[-1].rt + keyRecord1[-1].duration])

                componentUpdate(win, image2, t, frameN)
                componentUpdate(win, text2, t, frameN)
                countDown.reset(timeConfidence)
                
                kb.clock.reset()
            
            
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
            
    #---------------------------#
    #-----end-and-save-data-----#
    #---------------------------#
    
    trialDuration = globalClock.getTime()
    
    # -------Ending Routine "Trials"-------
    for thisComponent in TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # place holder
    addKeys1 = []
    addKeys2 = []
    img1_pressTime = 0
    img2_pressTime = 0
    img1_direction = 0
    img2_direction = 0
    
    
    # reaction time = time of the key - tStart of the figure
    
    for k in keyRecord1:
        
        addKeys1.append([k.name, k.rt, k.duration])
        
        img1_pressTime += k.duration
        
        if k.name == "up":
            img1_direction += k.duration    # add when up
        elif k.name == "down":
            img1_direction -= k.duration    # minus when down
            
    for k in keyRecord2:
        
        addKeys2.append([k.name, k.rt, k.duration])
        
        img2_pressTime += k.duration
        
        if k.name == "up":
            img2_direction += k.duration    # add when up
        if k.name == "down":
            img2_direction -= k.duration    # minus when down
            
        
    
    # Ratings of each image
    Repeat.addData("img1_rating", sliderRating[0][0])    # img1_rating
    Repeat.addData("img2_rating", sliderRating[1][0])    # img2_rating 
    
    # Reaction time 
    Repeat.addData("img1_FirstKey_rt", addKeys1[0][1])         # img1_time before first press
    if addKeys2 == []:
        Repeat.addData("img2_FirstKey_rt", -88)
    else:
        Repeat.addData("img2_FirstKey_rt", addKeys2[0][1])     # img2_time before first press if there is a selection
    
    # img duration (total pressing time)
    Repeat.addData("img1_duration", img1_pressTime)             # img1_sum of pressing time
    
    if img2_pressTime == 0:
        Repeat.addData("img2_duration", -88)                    # img2_sum of pressing time
    else:
        Repeat.addData("img2_duration", img2_pressTime)
        
    # img direction sum up (+ if up, - if down)
    Repeat.addData("img1_direction", img1_direction)            # img_sum of direction
    
    if addKeys2 == []:
         Repeat.addData("img2_direction", -88)
    else:
        Repeat.addData("img2_direction", img2_direction)        # img2_sum of direction
        
        
    # Other data that may be needed
    
    # slider record
    Repeat.addData("slider.history_rating_rt", sliderRating)    # the slider rating and time

    # entire trial time
    Repeat.addData("trialDuration", trialDuration)              # trial duration
        
    # tracking starting time
    Repeat.addData("image1_tStart", image1.tStart)
    Repeat.addData("image2_tStart", image2.tStart)
    Repeat.addData("image3_tStart", image3.tStart)
    
    # img showing time
    Repeat.addData("img1_showTime", image2.tStart-image1.tStart)
    Repeat.addData("img2_showTime", image3.tStart-image2.tStart)
    
    # key record
    Repeat.addData("img1_keyboard.record_name_rt_duration", addKeys1)   # record for img1
    Repeat.addData("img2_keyboard.record_name_rt_duration", addKeys2)   # record for img2
    
    # time confidence and time fade in parameter
    Repeat.addData("timeConfidence", timeConfidence)
    Repeat.addData("timeFadeIn", timeFadeIn)
        
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
    t = InsetructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
    # update/draw components on each frame
    # *Instruct* updates
    if t >= 0.0:
        componentUpdate(goodbyeText, t, frameN)
                
    # check for quit (typically the Esc key)
    if endExpNow or kb.getKeys(keyList=["escape"]):
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
win.close()
core.quit()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

