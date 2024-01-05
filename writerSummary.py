import os
from classes import *

global summaryFolder

##################
# INITIALIZATION #
##################

def setFolderSummary(folder):
    global summaryFolder
    summaryFolder = folder
    if (not os.path.exists(summaryFolder)):
        os.makedirs(summaryFolder)


####################
# HOSPITAL SUMMARY #
####################

def printSummaryHospital(n_floors, dicFloors, dicBeds):
    file = open(summaryFolder + '\\HospitalSummary.txt', 'w')
    
    toWrite = "\tHOSPITAL SUMMARY:\n\n"
    toWrite = toWrite + " - The hospital will have {} Floors\n".format(n_floors)
    toWrite = toWrite + "\n  Floors:\n"
    for floor in dicFloors.values():
        if floor.description=="f0":
            toWrite = printFloor0(toWrite, floor, dicBeds)    
        else:
            toWrite = printFloorOrd(toWrite, floor, dicBeds)


    file.write(toWrite)
    file.close()


def printFloor0(toWrite, f0, dicBeds):
    toWrite = toWrite + "  + {} (id: {}) has: 1 Row (Unit) y 2 Column (Blocks)\n".format(f0.description, f0.id)
        
    toWrite = toWrite + "\n   Hospitalization Units ({}):\n".format(len(f0.hospUnits))
    toWrite = printHospUnits(toWrite, f0.hospUnits)
    
    toWrite = toWrite + "\n   Areas:"
    for area in f0.areas:
        toWrite = toWrite + "\n   - {} (id: {})\n".format(area.description, area.id)
        
        toWrite = toWrite + "    Horizontal Corridors:\n".format()
        toWrite = printCorridors(toWrite, area.corridorsHoriz, dicBeds)
            
    return toWrite

def printFloorOrd(toWrite, floor, dicBeds):
    nUnits = len(floor.units)
    nBlocks = len(floor.blocks)
    toWrite = toWrite + "\n  + {} (id: {}) has: {} Rows (Unit) y {} Columns (Blocks)\n".format(floor.description, floor.id, nUnits, nBlocks)

    toWrite = toWrite + "\n   Hospitalization Units ({}):\n".format(len(floor.hospUnits))
    toWrite = printHospUnits(toWrite, floor.hospUnits)
    

    toWrite = toWrite + "\n   Areas:"
    for area in floor.areas:
        toWrite = toWrite + "\n   * {} (id: {})\tTipo: {}\n".format(area.description, area.id, area.type)
        
        toWrite = toWrite + "\n    Horizontal Corridors:\n".format()
        toWrite = printCorridors(toWrite, area.corridorsHoriz, dicBeds)
        toWrite = toWrite + "\n    Vertical Corridors:\n".format()
        toWrite = printCorridors(toWrite, area.corridorsVert, dicBeds)

    toWrite = toWrite + "\n   Units:"
    toWrite = printUnitsBlocks(toWrite, floor.units)
    toWrite = toWrite + "\n   Blocks:"
    toWrite = printUnitsBlocks(toWrite, floor.blocks)

    return toWrite    


def printHospUnits(toWrite, hospUnits):
    for hu in hospUnits:
        serv = hu.service
        toWrite = toWrite + "   - {} - {} (id: {})\tRooms: {}   --Service->   {} - {} (id: {})\n".format(hu.abrev, hu.description, hu.id, hu.rooms, serv.abrev, serv.description, serv.id)
    
    return toWrite

def printCorridors(toWrite, corridors, dicBeds):
    i=0
    for corridor in corridors:
        if i!=0:
            toWrite = toWrite + "\n"
        else:
            i += 1
        toWrite = toWrite + "    - {} (id: {})".format(corridor.description, corridor.id)
        
        toWrite = toWrite + "\n\t\tNextTo: {"
        for id,value in corridor.nextTo.items():
            if value is not None:
                toWrite = toWrite + "'{}': {}, ".format(id, value)
        toWrite = toWrite + "}"
        
        toWrite = toWrite + "\n\t\tRoomsBorder: {"
        for id,value in corridor.roomsBorder.items():
            if value is not None:
                toWrite = toWrite + "'{}': {}, ".format(id, value.id)
        toWrite = toWrite + "}\n"
        

        toWrite = toWrite + "\n     Rooms:\n"
        j=0
        for room in corridor.rooms:
            if j!=0:
                toWrite = toWrite + "\n"
            else:
                j += 1
            toWrite = toWrite + "     - {} (id: {})\tNextTo: {}\tOpposite: {}\n".format(room.description, room.id, room.nextTo, room.opposite)
            toWrite = toWrite + "      Beds:\n"
            for bedId in room.beds:
                bed = dicBeds[bedId]
                toWrite = toWrite + "      - {} (id: {})\tNextTo: {}\tOpposite: {}\n".format(bed.description, bed.id, bed.nextTo, bed.opposite)

    return toWrite

def printUnitsBlocks(toWrite, unitsOrBlocks):
    for ub in unitsOrBlocks:
        nextTo = [ub.nextTo_prev, ub.nextTo_after]
        toWrite = toWrite + "\n   - {} (id: {})\tNextTo: {}\n".format(ub.description, ub.id, nextTo)      

    return toWrite 


###################
# EPISODE SUMMARY #
###################

def printEpisodeSummary(dicPatients, startDateTime):
    file = open(summaryFolder + '\\EpisodeSummary.txt', 'w')
    
    toWrite = "\tSUMMARY OF EPISODES AND EVENTS BY PATIENT:\n\n"
    stringDatetime = startDateTime.strftime("%d-%m-%Y %H:%M:%S")
    toWrite += " - Start date: {}\n\n".format(stringDatetime)
    toWrite += " - There are {} Patients\n\n".format(len(list(dicPatients.keys())))
    toWrite += " PATIENTS:\n"
    for patient in dicPatients.values():
        toWrite += "\n * Patient {}\n".format(patient.id)
        toWrite += "    Episodes:\n"
        for ep in patient.episodes:
            toWrite += "     + {} [{}] : {} - {}\n".format(ep.description, ep.id, ep.start, ep.end)
            toWrite += "\n      Events\n"
            for ev in ep.events:
                toWrite += "       - {} [{}] type: {} : {} - {} -> Bed {}\n".format(ev.description, ev.id, ev.type.name, ev.start, ev.end, ev.location)    

    file.write(toWrite)
    file.close()

    