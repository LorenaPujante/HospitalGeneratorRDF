
from classes import *
from datetime import datetime, timedelta
import random
from random import randrange
import math

def parseSteps(dicPatients):

    step = 0

    with open(".\\Input\\salida.csv") as file:
        for lineString in file:
            
            lineString = str(lineString)
            line = lineString.split(';')
            
            step = int(line[0])

            i = 1
            places = False
            while i<len(line) and not places:
                # line[i]      ->  patient_id
                # line[i+1]    ->  patient_state
                # line[i+2]    ->  locationId
                # line[i+3]    ->  location_infected   :   Don't usec
                if line[i]=='places' or line[i+1]=='places' or line[i+2]=='places' or line[i+3]=='places':
                    places = True
                else:
                    patientId = int(line[i])
                    locationId = int(line[i+2])
                    seirState = int(line[i+1])

                    patient = dicPatients[patientId]
                    patient.stepLocations[step] = locationId
                    
                        # It is ONLY intended for PATIENTS WITH 1 EPISODE
                    if patient.seir[seirState] is None:
                        patient.seir[seirState] = step

                    i += 4 

    file.close()

    return step



###################################
# CREATION OF EPISODES AND EVENTS #
###################################

def createEpisode(nEpisode, idPatient, start, end, events, index):
    description = "ep{}_p{}".format(nEpisode,idPatient)
    ep = Episode(index, description, start, end)
    ep.events = events
    
    index += 1
    nEpisode += 1
    
    return ep, nEpisode, index

def createEvent(nEvent, nEpisode, idPatient, start, end, location, index, dicBeds):
    
    type = TypeEvent.Hospitalization   
    if dicBeds[location].type is TypeBed.Radiology:
        type = TypeEvent.Radiology     
    elif dicBeds[location].type is TypeBed.Surgery:
        type = TypeEvent.Surgery       
    description = "ev{}_ep{}_p{}".format(nEvent, nEpisode, idPatient)
    hu = dicBeds[location].hospUnit
    ev = Event(index, description, start, end, location, hu, type)

    index += 1
    nEvent += 1

    return ev, nEvent, index

def createEventDeath(nEpisode, idPatient, datetimeDeath, index):
    type = TypeEvent.Death     
    description = "death_ep{}_p{}".format(nEpisode, idPatient)
    ev = Event(index, description, datetimeDeath, datetimeDeath, None, None, type)

    index += 1

    return ev, index


# MAIN
def createEpisodesAndEventsPerPacient(dicPatients, dicBeds, startDateTime, index):

    for patient in dicPatients.values():
        path = patient.stepLocations
        steps = list(path.keys())
        if len(steps)>0:    # In case there is a Patient without Events
            i = 0
            
            lastStep = steps[0]-1
            startEp = getRandomDateTime(startDateTime, steps[0], 0, 240)    # The Episode starts between the FIRST 4 HOURS  ->  (0 ,     4*60=240)
            endEp = startEp
            nEpisode = 0
            events = []
            
            nEvent = 0
            startEv = startEp
            lastLoc = path[steps[0]]

            while i<len(steps):
                step = steps[i]

                # An Event is created when the Location (Bed) is changed
                location = path[step]
                if location != lastLoc:
                    if nEvent==0:
                        startEv = startEp
                    endEv = startDateTime + timedelta(hours=8*lastStep, minutes=479)    # 8*60-1 = 479
                    ev, nEvent, index = createEvent(nEvent, nEpisode, patient.id, startEv, endEv, lastLoc, index, dicBeds)
                    events.append(ev)
                    
                    startEv = startDateTime + timedelta(hours=8*step)

                # An Episode is created with the events up to the previous step
                if step != lastStep+1:
                    # The last Event of the Episode is created
                    if nEvent==0:
                        startEv = startEp
                    endEv = getRandomDateTime(startDateTime, lastStep, 240, 479)    # The Episode ends within the LAST 4 HOURS   ->  (4*60=240 ,     # 8*60-1 = 480-1 = 479)
                    ev, nEvent, index = createEvent(nEvent, nEpisode, patient.id, startEv, endEv, lastLoc, index, dicBeds)
                    events.append(ev)

                    # The Episode is created
                    endEp = endEv 
                    ep, nEpisode, index = createEpisode(nEpisode, patient.id, startEp, endEp, events, index)
                    patient.episodes.append(ep)

                    startEp = getRandomDateTime(startDateTime, step, 0, 240)    # The Episode starts between the FIRST 4 HOURS   ->  (0 ,     4*60=240)
                    events = []
                    nEvent = 0

                    
                lastLoc = location
                lastStep = step
                i += 1  


            # Create last Event
            endEv = getRandomDateTime(startDateTime, lastStep, 240, 479)    # The Episode ends within the LAST 4 HOURS  ->  (4*60=240 ,     # 8*60-1 = 480-1 = 479)
            ev, nEvent, index = createEvent(nEvent, nEpisode, patient.id, startEv, endEv, lastLoc, index, dicBeds)
            events.append(ev)

            # If the Patient dies, an Event is created for it
            if patient.death:
                ev, index = createEventDeath(nEpisode, patient.id, endEv, index) # The date and time of death is the 'end' of the last Episode/Event
                events.append(ev)

            # Create last Episode
            endEp = endEv
            ep, nEpisode, index = createEpisode(nEpisode, patient.id, startEp, endEp, events, index)
            patient.episodes.append(ep)        
        
    return index     


# Time Functions
def getRandomMinutos(start,end):
    return random.randint(start, end)

def getRandomDateTime(startDateTime, steps, startMinutes, endMinutes):
    minutos = getRandomMinutos(startMinutes, endMinutes)
    datetimeRandom = startDateTime + timedelta(hours=8*steps, minutes=minutos)

    return datetimeRandom


##############
# TEST MICRO #
##############

def randomMDR():
    start = -1
    end = 1
    peak = -0.5
    mdr = random.triangular(start,end,peak)
    if mdr <= 0:
        return False
    return True

def createEventTestMicro(idPatient, datetimeTest, microorg, index):
    type = TypeEvent.TestMicro     
    description = "testMicro_p{}".format(idPatient)
    ev = Event(index, description, datetimeTest, datetimeTest, None, None, type)
    ev.extra1 = microorg
    ev.extra2 = randomMDR()

    index += 1

    return ev, index

# Add a positive TestMicro in the step in which the Patient's status becomes Infected
def createTestMicro_StartInfected(dicPatients, dicMicroorganisms, startDateTime, index):
    keysMicroorg = list(dicMicroorganisms.keys())
    microorg = dicMicroorganisms[keysMicroorg[0]]   # Since there is only one Microorganism, it is taken directly from the dictionary
    
    for patient in dicPatients.values():
        
        if patient.seir[2] is not None:  # Patient as been infected
            stepI = patient.seir[2]
            if patient.seir[1] is not None:  # Patient has gone from Exposed -> Infected
                datetimeTest  = startDateTime + timedelta(hours=8*stepI)
            else:   # Patient has been directly admitted in an Infected state
                datetimeTest  = patient.episodes[0].start
            ev, index = createEventTestMicro(patient.id, datetimeTest, microorg, index)
            
            # Find which Episode the Event belongs to
            found = False
            i = 0
            while not found and i<len(patient.episodes):
                episode = patient.episodes[i]
                if ev.start >= episode.start  and  ev.start <= episode.end:
                    found = True
                else: 
                    i += 1
            if found:
                patient.episodes[i].events.append(ev)
    
    return index


# Add a positive TestMicro while the Patient is Infected (from the first second they are infected to half the time they are infected)
def createTestMicro_DuringInfected(dicPatients, dicMicroorganisms, startDateTime, index):
    keysMicroorg = list(dicMicroorganisms.keys()) 
    microorg = dicMicroorganisms[keysMicroorg[0]]   # Since there is only one Microorganism, it is taken directly from the dictionary
    
    for patient in dicPatients.values():
        
        if patient.seir[2] is not None:  # Patient has been Infected
            stepI = patient.seir[2]
            
            if patient.seir[1] is not None:  # Patient has gone from Exposed -> Infected
                stepI_start  = startDateTime + timedelta(hours=8*stepI)
            else:   # Patient has been directly admitted in an Infected state
                stepI_start  = patient.episodes[0].start
            startRandom = stepI_start.timestamp()

            if patient.seir[3] is not None: # Patient has gone from Infected -> Recovered
                stepI_end  = startDateTime + timedelta(hours=8*patient.seir[3])
            else:   # Patient has left the hospital (alive or dead) in an Infected state
                stepI_end = patient.episodes[0].end
            endI = stepI_end.timestamp()
            diffStartEnd = endI-startRandom
            mitadDiff = math.floor(diffStartEnd/2)  # As a limit, the test is carried out halfway through the period that the Patient is Infected.
            endRandom = startRandom+mitadDiff
            randomSeconds = randrange(startRandom, endRandom)   
            datetimeTest = datetime.fromtimestamp(randomSeconds)
            ev, index = createEventTestMicro(patient.id, datetimeTest, microorg, index)
            
            # Find which Episode the Event belongs to
            found = False
            i = 0
            while not found and i<len(patient.episodes):
                episode = patient.episodes[i]
                if ev.start >= episode.start  and  ev.start <= episode.end:
                    found = True
                else: 
                    i += 1
            if found:
                patient.episodes[i].events.append(ev)
    
    return index