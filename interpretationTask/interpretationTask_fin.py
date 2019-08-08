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

    #1. since the csv file contains french accents, when export to csv file, you need to be carefule to select "UTF-8" type of csv, or error will happen
    
    #2. the headers of the csv file need to contain the following:
    
        # state1    state2    state3    sliderSub1  sliderSub2    sliderSub3    sliderSub4 """
        
        # the names are case-sensitive, no need to follow the order
        # Everything that is in the original csv file (e.g. the name of the trial, or comments) will be saved automatically in the resulting data file (THANKS YOU PSYCHOPY!)
        
        
    #3. If you are sure about your path and want to avoid user interface popping up everytime:
    
            # 1) comment out these lines
            
                # conditionFile = gui.fileOpenDlg(".", prompt = "Please Select the Condition File", allowed = "*.csv")  # a list object, save the path(including the name) of the file selected, conditionFile[0] gives the file name string
                 # if not conditionFile:
                #   core.quit
            # 2) replace "conditionFile[0]" in "trialList=data.importConditions(conditionFile[0])," around line740 with your condition file path
                # path is a string type
                # remember to replace "/" with "\\" in windows (sometimes error occurs)
                
    #4. If you want to read codes, in case of naming, there are six objects displayed in the task:
    
        # statements (3 of them, text objects)       -> state1 ~ state3
        # slider (4 of them, slider objects)         -> slider1 ~ slider4
        # slider subject (4 of them, text objects)   -> sliderS1 ~ sliderS4
        # slider values (4 of them, text objects)    -> sliderV1 ~ sliderV4
        
        # a button (composed of 2 objects)           -> nextButton and nextText
        
        # My namings of the variables will follow the rules semantically:
            # e.g. sliderH => slider height; sliderSH => slider subject height
            
        
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


# ----physical properties (height and width of statements(state), sliders(slider) and slider statements(SliderS))----
    # unit: height (the size relative to the height of the computer screen)
    # (0,0) is at the center
    # may need adjustment according to computers

# height of the components

stateH = 0.03       # The height of the statement (text size)
sliderH = 0.03      # The height of the slider 
sliderW = 1.4       # The width of the slider
sliderSH = 0.03     # The height of the slider subject (text size)
sliderVH = 0.03     # The height of the slider values (text size)

# The x-position of the components

sliderX = -0.05                # The x-position of the sliders
sliderSX = -0.05               # The x-position of the slidersubject
sliderVX = sliderW/2 + 0.05   # The x-position of the values

# the y-position of the first component (slider, statement, sliderSub)

stateP1 = 0.35      # The y-position of the first statment
sliderP1 = -0.03    # The y-position of the first slider
sliderSP1 = 0       # each slider subject should be on the top of the slider (larger than sliderP1)
sliderVP1 = sliderP1   # slider value has the same y-position as the slider

# the distance between each component
    # calculate to make sure they are evenly spread
        # (when use them below in object initialization, use the multiple of *D values)
    # height/2 + distance =  about distance between each identical component, just an evaluation


dis = 0.048 # Change this to control the spread, or modify the function below if you want


stateD = stateH/2 + dis
sliderD = sliderH/2 + dis*2
sliderSD = sliderSH/2 + dis*2
sliderVD = sliderD # The distance between the values should be the same as the slider


# position of the button

buttonX = sliderX
buttonY = -0.45



# -----Other-parameters-----

# starting point and ending point of the sliders

startP = 0       # starting value of all sliders
endP = 1         # ending value of all sliders
startT = "0%"    # text displayed at at the starting point of the slider
endT = "100%"    # text displayed at the end of the slider



timeBetween = 2      # time between each trial (unit: second)

instructionText =  """Trois énoncés vous seront montrés, un à la fois. Chacun décrit un événement ou une personne. Chaque nouvel énoncé apportera de l’information additionnelle à propos de l’événement ou de la personne décrit(e). Sous les énoncés, vous verrez aussi quatre interprétations de l’événement ou de la personne décrit(e) dans le(les) énoncé(s). Chaque interprétation a sa propre échelle (de 0 – 100%), vous aurez donc à évaluer la probabilité que chaque interprétation décrive l’énoncé, selon les informations données.\n
                     \nÉvaluez à quel point vous pensez que chaque interprétation se rapporte à l’évènement ou la personne décrite dans l’(les) énoncé(s). Il est important d’évaluer chacune des quatre interprétations indépendamment les unes des autres. Ne comparez pas les interprétations entres elles.\n
                     \nÀ chaque nouvel énoncé présenté, reconsidérez les évaluations que vous avez assignées à chaque interprétation. Les évaluations des interprétations peuvent être changées autant que vous le voulez, vous pouvez aussi les laisser intactes, si vous avez l’impression qu’elles n’ont pas changées avec l’addition de nouveaux énoncés. Il est possible qu’aucune ou que plusieurs interprétations soi(en)t un bon pairage avec les énoncés.\n
                     \nVous utiliserez la souris pour faire vos évaluations. Appuyez sur ‘Suivant’ pour afficher le prochain énoncé. Après avoir vu tous les trois énoncés, appuyez sur ‘Complété’, pour accéder à l’essai suivant. Vous allez maintenant faire 2 essais de pratique, avant de commencer l’exercice."""



#--------------------------------------------------------------------------------------------------------------











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
 
if not conditionFile:
    core.quit
    






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
    fullscr=True, screen=0, 
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
    text = instructionText,    
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Initialize components for Routine "trial"


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
    text='Thank you for participating, press space to quit.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



#Button (composed of a rectangle and a text stimuli)
nextButton = visual.Rect(win, name="nextButton", 
                    width=0.12, height =0.05, pos=(buttonX,buttonY))
nextButton.setFillColor("white")

nextText = visual.TextStim(win, text="NEXT", 
                pos=(buttonX,buttonY), color="black", height=0.03)





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


#--------------------------------------------------exit-introduction--------------------------------------------------




#----------------------------------------------------------------------------------------------#
#-------------------------------------------Practice-------------------------------------------#
#----------------------------------------------------------------------------------------------#



# In these two practice trial, nothing is recorded

statements = [["Danielle n'est vraiment pas fiable.", "Danielle n'aime pas la critique.","Danielle a été impolie avec sa patronne." ],["Cindy danse.", "Cindy porte une petite robe.", "Les hommes applaudissent et sifflent quand Cindy danse."]]
orderedSliderSubjectList = [["Danielle oublie souvent ses devoirs.", "Danielle est une mauvaise mère.", "Danielle n'est pas une bonne cuisinière.", "Danielle a été renvoyée de son emploi."],
                            ["Cindy est à un party.", "Cindy est droguée dans un rave.", "Cindy est un membre d'un groupe de musique populaire.", "Cindy est une stripteaseuse."]]

for i in range(2):
    
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    startSecond = False
    startThird = False
    
    
    # extract the statements and the slider subjects
    
    
    state = statements[i]
    orderedSliderSubject = orderedSliderSubjectList[i]
    sliderSubject = orderedSliderSubjectList[i]
    
    
    # shuffle to make the position of target subject random
    
    np.random.shuffle(sliderSubject)


    # update component parameters for each repeat
    
    nextText.setText("NEXT") # change the text back to NEXT, set to "done" later
    statement1.setText(state[0])
    statement2.setText(state[1])
    statement3.setText(state[2])
    slider1.reset()
    slider2.reset()
    slider3.reset()
    slider4.reset()
    sliderS1.setText(sliderSubject[0])
    sliderS2.setText(sliderSubject[1])
    sliderS3.setText(sliderSubject[2])
    sliderS4.setText(sliderSubject[3])
    
    
    # create a dictionary, key:value paires
    # create key:value pairs
    # for example
        # after shuffle, the statements are not in their original position.
        # if current sliderStateText is [sliderSub2, sliderSub1, sliderSub4,sliderSub3]
        # the result will be {sliderSub2:slider1, sliderState1:slider2, sliderState4: slider3, sliderState1:slider4}
        # now when we call dicSlider[sliderSub1], we get slider2
        
    dicSlider = {}
    
    for thisSliderSub, thisSlider in zip(sliderSubject, sliderComponents):
        dicSlider[thisSliderSub] = thisSlider
        
        
    # keep track of which components have finished
    trialComponents = [statement1, statement2, statement3, slider1, slider2, slider3, slider4, sliderS1, sliderS2, sliderS3, sliderS4, sliderV1, sliderV2, sliderV3, sliderV4, nextButton, nextText]
    
    for thisComponent in trialComponents:
        initiateComponent(thisComponent)
        
    for thisSlider,thisSliderV in zip(sliderComponents,sliderVComponents):
        thisSlider.recordRating(startP) # Set initial rating s.t. the tick will appear at the start
        thisSliderV.setText(str(startP*100) + "%") # Set initial text slider value

    sliderRecord0 = [startP, startP, startP, startP] # initial value
    
    
    # -------Start Routine "trial"------- #
    
    while continueRoutine:

        
        while not defaultMouse.isPressedIn(nextButton, buttons=[0]):   # do this until we click on the button
            
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1 
            
            # --------------------Updates--------------------
            # componentUpdate updates the time and frameN of the component, and set it to autoDraw could have used single "draw()" statement to save resources and time
            # update/draw components on each frame
            # use the function just for convenience and in case timing is demanded later
            
            
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
            
            # --------------------slider-subjects--------------------
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
            
            sliderV1.setText("{r:1.1f}%".format(r=slider1.markerPos*100))
            sliderV2.setText("{r:1.1f}%".format(r=slider2.markerPos*100))
            sliderV3.setText("{r:1.1f}%".format(r=slider3.markerPos*100))
            sliderV4.setText("{r:1.1f}%".format(r=slider4.markerPos*100))
            
            
            #---------------check for special keys and conditions---------------
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                
                
                
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            if continueRoutine:
                win.flip()
                
                
        # When clicked, exit the while loop above
        
        hasRespond = checkSlider(sliderComponents, sliderRecord0) # will stay True if ther is any response
        
        # after the clicking on the button
        
        if hasRespond: # for the first respond, we force the participant to make a response
            
            if statement2.status == NOT_STARTED and statement3.status == NOT_STARTED:
                startSecond = True # used in drawing the second component
                
            
        if statement2.status == STARTED and statement3.status == NOT_STARTED:

            startThird = True # used in drawing the third component
            
            if i == 0:
                nextText.setText("NEXT")
            if i == 1:
                nextText.setText("START") # after the second selection in the second practice trial, set the text on the button to "start"

        if statement2.status == STARTED and statement3.status == STARTED:
            
            continueRoutine = False # end the trial after it's pressed the third time
        
        
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


    win.flip()  # clear the screen 
    core.wait(timeBetween)  # wait for some time between trial
    
# ------------------------------------------------------------------practice-trials-completed------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------#
#-------------------------------------------FORMAL-TRIALS-------------------------------------------#
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
    

    # save the texts in order
    
    orderedSliderSubject = [sliderSub1, sliderSub2, sliderSub3, sliderSub4]

    SliderSubject = [sliderSub1, sliderSub2, sliderSub3,sliderSub4]
    

    # shuffle three times to be compelete
    
    
    
    np.random.shuffle(SliderSubject)
    

    # update component parameters for each repeat
    nextText.setText("NEXT") # change the text back to NEXT, set to "done" later
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
    trialComponents = [statement1, statement2, statement3, slider1, slider2, slider3, slider4, sliderS1, sliderS2, sliderS3, sliderS4,sliderV1,  sliderV2, sliderV3, sliderV4, nextButton, nextText]
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
            
            # --------------------slider-values--------------------
            # keep track of start time/frame for later
            componentUpdate(sliderV1, t, frameN)
            componentUpdate(sliderV2, t, frameN)
            componentUpdate(sliderV3, t, frameN)
            componentUpdate(sliderV4, t, frameN)

            sliderV1.setText("{r:1.1f}%".format(r=slider1.markerPos*100)) # 1.1f means that the number is in 0.1 precision
            sliderV2.setText("{r:1.1f}%".format(r=slider2.markerPos*100))
            sliderV3.setText("{r:1.1f}%".format(r=slider3.markerPos*100))
            sliderV4.setText("{r:1.1f}%".format(r=slider4.markerPos*100))
            
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
                for thisText in orderedSliderText:
                    sliderRecord1.append(dicSlider[thisText].getRating()) # record current rating
                        
                startSecond = True # used in drawing the second component
                hasRecord1 = True
                
                
        if not hasRecord2 and statement2.status == STARTED and statement3.status == NOT_STARTED:

            for thisText in orderedSliderText:
                sliderRecord2.append(dicSlider[thisText].getRating()) # record current rating
                        
           
            startThird = True # used in starting the third component
            hasRecord2 = True
            nextText.setText("DONE")

        if not hasRecord3 and statement2.status == STARTED and statement3.status == STARTED:
            
            for thisText in orderedSliderText:
                sliderRecord3.append(dicSlider[thisText].getRating()) # record current rating
                        
                
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

    # ---------------------------------completed-1-repeats-of-trials---------------------------------
    
    
    
    thisExp.nextEntry()
    











# ------Prepare to start Routine "goodbye_"-------
t = 0
goodbye_Clock.reset()  # clock
frameN = -1
continueRoutine = True
initiateComponent(goodbyeText)



#---------------------------------------------------------------------------#
#----------------------------------Goodbye----------------------------------#
#---------------------------------------------------------------------------#




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
    
    
    
    
    
    
# --------------------------------Ending Routine "goodbye_"--------------------------------
goodbyeText.setAutoDraw(False)



# --------------------------------------------------End-the-experiment--------------------------------------------------

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


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
