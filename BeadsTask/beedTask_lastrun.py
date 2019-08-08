#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on August 08, 2019, at 14:20
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

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\que_d\\Documents\\McGill\\LepageLab\\psychopyExperiment_github\\BeadsTask\\beedTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(-0.8, 0),
    lineWidth=1, lineColor=[1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_3 = visual.Polygon(
    win=win, name='polygon_3',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(-0.6, 0),
    lineWidth=1, lineColor=[0.004,1.000,1.000], lineColorSpace='rgb',
    fillColor=[0.004,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_4 = visual.Polygon(
    win=win, name='polygon_4',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(-0.4, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_5 = visual.Polygon(
    win=win, name='polygon_5',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(-0.2, 0),
    lineWidth=1, lineColor=[1.000,1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon_6 = visual.Polygon(
    win=win, name='polygon_6',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,0.004,0.506], lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.506], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon_7 = visual.Polygon(
    win=win, name='polygon_7',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(0.2, 0),
    lineWidth=1, lineColor=[0.004,0.004,1.000], lineColorSpace='rgb',
    fillColor=[0.004,0.004,1.000], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
polygon_8 = visual.Polygon(
    win=win, name='polygon_8',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(0.4, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
polygon_9 = visual.Polygon(
    win=win, name='polygon_9',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(0.6, 0),
    lineWidth=1, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
polygon_10 = visual.Polygon(
    win=win, name='polygon_10',
    edges=36, size=(0.2, 0.2),
    ori=0, pos=(0.8, 0),
    lineWidth=1, lineColor=[-0.498,0.004,0.004], lineColorSpace='rgb',
    fillColor=[-0.498,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [polygon, polygon_2, polygon_3, polygon_4, polygon_5, polygon_6, polygon_7, polygon_8, polygon_9, polygon_10]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t  # not accounting for scr refresh
        polygon.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    
    # *polygon_2* updates
    if t >= 0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t  # not accounting for scr refresh
        polygon_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *polygon_3* updates
    if t >= 2 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t  # not accounting for scr refresh
        polygon_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *polygon_4* updates
    if t >= 4 and polygon_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_4.tStart = t  # not accounting for scr refresh
        polygon_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
        polygon_4.setAutoDraw(True)
    
    # *polygon_5* updates
    if t >= 6 and polygon_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_5.tStart = t  # not accounting for scr refresh
        polygon_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    
    # *polygon_6* updates
    if t >= 8 and polygon_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_6.tStart = t  # not accounting for scr refresh
        polygon_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    
    # *polygon_7* updates
    if t >= 10 and polygon_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_7.tStart = t  # not accounting for scr refresh
        polygon_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
        polygon_7.setAutoDraw(True)
    
    # *polygon_8* updates
    if t >= 12 and polygon_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_8.tStart = t  # not accounting for scr refresh
        polygon_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
        polygon_8.setAutoDraw(True)
    
    # *polygon_9* updates
    if t >= 14 and polygon_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_9.tStart = t  # not accounting for scr refresh
        polygon_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
        polygon_9.setAutoDraw(True)
    
    # *polygon_10* updates
    if t >= 16 and polygon_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_10.tStart = t  # not accounting for scr refresh
        polygon_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
        polygon_10.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('polygon_4.started', polygon_4.tStartRefresh)
thisExp.addData('polygon_4.stopped', polygon_4.tStopRefresh)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('polygon_6.started', polygon_6.tStartRefresh)
thisExp.addData('polygon_6.stopped', polygon_6.tStopRefresh)
thisExp.addData('polygon_7.started', polygon_7.tStartRefresh)
thisExp.addData('polygon_7.stopped', polygon_7.tStopRefresh)
thisExp.addData('polygon_8.started', polygon_8.tStartRefresh)
thisExp.addData('polygon_8.stopped', polygon_8.tStopRefresh)
thisExp.addData('polygon_9.started', polygon_9.tStartRefresh)
thisExp.addData('polygon_9.stopped', polygon_9.tStopRefresh)
thisExp.addData('polygon_10.started', polygon_10.tStartRefresh)
thisExp.addData('polygon_10.stopped', polygon_10.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
