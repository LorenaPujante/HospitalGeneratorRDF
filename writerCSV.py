import os
from classes import *
from weightsLocsHierarchy import weights
from variablesWriter import nameFiles_Classes, nameFiles_Rels

##################
# INITIALIZATION #
##################

def setFolderOutputCSV(dir):
    global folderOutput_CSV
    folderOutput_CSV = dir
    if (not os.path.exists(folderOutput_CSV)):
        os.makedirs(folderOutput_CSV)
    
    global folderOutput_Classes_CSV
    folderOutput_Classes_CSV = folderOutput_CSV + "\\Classes"
    if (not os.path.exists(folderOutput_Classes_CSV)):
        os.makedirs(folderOutput_Classes_CSV)

    global folderOutput_Relations_CSV
    folderOutput_Relations_CSV = folderOutput_CSV + "\\Relations"
    if (not os.path.exists(folderOutput_Relations_CSV)):
        os.makedirs(folderOutput_Relations_CSV)



''''''''''''''
'''  MAIN  '''
''''''''''''''

def printCSV(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms):
    printClassesCSV(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms)
    printRelsCSV(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients)


def printClassesCSV(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms):
    # Hospital
    printClassesHospitalCSV(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds)

    # Patients
    printPatientsCSV(dicPatients)

    # Microorganisms
    printMicroorganismsCSV(dicMicroorganisms)

    # Episodes y Events
    printClassesEpisodesEventsCSV(dicPatients)


def printRelsCSV(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients):
    # Hospital
    printRelationsHospitalCSV(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds)
    
    # Patients, Episodes y Events
    printRelationEpisodesEventsCSV(dicPatients)

    

''''''''''''''''''
'''  HOSPITAL  '''
''''''''''''''''''

###############
# CSV CLASSES #
###############

# MAIN
def printClassesHospitalCSV(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds):
    
    printServicesCSV(dicServices)
    printHospUnitsCSV(dicHospUnits)
    
    printBuildingsCSV(dicBuildings)
    printFloorsCSV(dicFloors)
    printUnitsCSV(dicUnits)
    printBlocksCSV(dicBlocks)
    printAreasCSV(dicAreas)
    printCorridorsCSV(dicCorridors)
    printRoomsCSV(dicRooms)
    printBedsCSV(dicBeds)


# Services
def printServicesCSV(dicServices):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['service'], '.csv'), 'w')
    toWrite = "id,description,abbreviation\n"
    for id in dicServices:
        toWrite = toWrite + "{},{},{}\n".format(id,dicServices[id].description,dicServices[id].abrev)
    file.write(toWrite)
    file.close()

# Hospitalization Units
def printHospUnitsCSV(dicHospUnits):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['uh'], '.csv'), 'w')
    toWrite = "id,description,abbreviation\n"
    for id, value in dicHospUnits.items():
        toWrite = toWrite + "{},{},{}\n".format(id,value.description,value.abrev)    
    file.write(toWrite)
    file.close()


# Buildings
def printBuildingsCSV(dicBuildings):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['building'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicBuildings.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Floors
def printFloorsCSV(dicFloors):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['floor'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicFloors.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Units
def printUnitsCSV(dicUnits):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['unit'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicUnits.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Blocks
def printBlocksCSV(dicBlocks):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['block'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicBlocks.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Areas
def printAreasCSV(dicAreas):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['area'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicAreas.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Corridors
def printCorridorsCSV(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['corridor'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicCorridors.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Rooms
def printRoomsCSV(dicRooms):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['room'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicRooms.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()

# Beds
def printBedsCSV(dicBeds):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['bed'], '.csv'), 'w')
    toWrite = "id,description\n"
    for id, value in dicBeds.items():
        toWrite = toWrite + "{},{}\n".format(id,value.description)
    file.write(toWrite)
    file.close()



#################
# CSV RELATIONS #
#################

# MAIN
def printRelationsHospitalCSV(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds):
    
    printRel_ServiceHospUnitCSV(dicServices)
    printRel_HospUnitBedCSV(dicBeds)
    
    printRel_BuildingFloorCSV(dicBuildings)
    printRel_FloorAreaCSV(dicFloors)
    printRel_FloorUnidadCSV(dicFloors)
    printRel_FloorBloqueCSV(dicFloors)
    printRel_UnitAreaCSV(dicAreas)
    printRel_BlockAreaCSV(dicAreas)
    printRel_AreaCorridorCSV(dicAreas)
    printRel_CorridorRoomCSV(dicCorridors)
    printRel_RoomBedCSV(dicRooms)

    printRel_BedRoom_NextToOppositeCSV(dicBeds, "{}{}".format(nameFiles_Rels['bed_nt'], '.csv'), "idBed1,idBed2", "nextTo")
    printRel_BedRoom_NextToOppositeCSV(dicBeds, "{}{}".format(nameFiles_Rels['bed_ot'], '.csv'), "idBed1,idBed2", "opposite")
    printRel_BedRoom_NextToOppositeCSV(dicRooms, "{}{}".format(nameFiles_Rels['room_nt'], '.csv'), "idRoom1,idRoom2", "nextTo")
    printRel_BedRoom_NextToOppositeCSV(dicRooms, "{}{}".format(nameFiles_Rels['room_ot'], '.csv'), "idRoom1,idRoom2", "opposite")
    printRel_Corridor_NextToCSV(dicCorridors)
    printRel_UnitBlock_NextToCSV(dicUnits, "{}{}".format(nameFiles_Rels['unit_nt'], '.csv'), "idUnit1,idUnit2")
    printRel_UnitBlock_NextToCSV(dicBlocks, "{}{}".format(nameFiles_Rels['block_nt'], '.csv'), "idBlock1,idBlock2")


# Relation Service - HospUnit
def printRel_ServiceHospUnitCSV(dicServices):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['serv_uh'], '.csv'), 'w')
    toWrite = "idService,idHospUnit,weight\n"
    for s in dicServices.values():
        for uh in s.hospUnits:
            toWrite = toWrite + "{},{},{}\n".format(s.id,uh,weights['hospUnitFromService'])
    file.write(toWrite)
    file.close()
    
# Relation HospUnit - Bed
def printRel_HospUnitBedCSV(dicBeds):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['uh_bed'], '.csv'), 'w')
    toWrite = "idHospUnit,idBed,weight\n"
    for b in dicBeds.values():
        uh = b.hospUnit
        toWrite = toWrite + "{},{},{}\n".format(uh,b.id,weights["looksAfter"])
    file.write(toWrite)
    file.close()


# Relation Building - Floor
def printRel_BuildingFloorCSV(dicBuildings):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['floor_building'], '.csv'), 'w')
    toWrite = "idBuilding,idFloor,weight\n"
    for b in dicBuildings.values():
        for p in b.floors:
            toWrite = toWrite + "{},{},{}\n".format(b.id,p.id,weights["placedIn_FloorBuilding"])
    file.write(toWrite)
    file.close()

# Relation Floor - Area
def printRel_FloorAreaCSV(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['area_floor'], '.csv'), 'w')
    toWrite = "idFloor,idArea,weight\n"
    for p in dicFloors.values():
        for a in p.areas:
            toWrite = toWrite + "{},{},{}\n".format(p.id,a.id,weights["placedIn_AreaFloor"])
    file.write(toWrite)
    file.close()

# Relation Floor - Unit
def printRel_FloorUnidadCSV(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['unit_floor'], '.csv'), 'w')
    toWrite = "idFloor,idUnit,weight\n"
    for p in dicFloors.values():
        for u in p.units:
            toWrite = toWrite + "{},{},{}\n".format(p.id,u.id,weights["placedInFloor_Unit"])
    file.write(toWrite)
    file.close()

# Relation Floor - Block
def printRel_FloorBloqueCSV(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['block_floor'], '.csv'), 'w')
    toWrite = "idFloor,idBlock,weight\n"
    for p in dicFloors.values():
        for b in p.blocks:
            toWrite = toWrite + "{},{},{}\n".format(p.id,b.id,weights["placedInFloor_Block"])
    file.write(toWrite)
    file.close()

# Relation Unit - Area
def printRel_UnitAreaCSV(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['area_unit'], '.csv'), 'w')
    toWrite = "idArea,idUnit,weight\n"
    for a in dicAreas.values():
        toWrite = toWrite + "{},{},{}\n".format(a.id,a.unit.id,weights["placedInUnit"])
    file.write(toWrite)
    file.close()

# Relation Block - Area
def printRel_BlockAreaCSV(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['area_block'], '.csv'), 'w')
    toWrite = "idArea,idBlock,weight\n"
    for a in dicAreas.values():
        toWrite = toWrite + "{},{},{}\n".format(a.id,a.block.id,weights["placedInBlock"])
    file.write(toWrite)
    file.close()

# Relation Area - Corridor
def printRel_AreaCorridorCSV(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['corridor_area'], '.csv'), 'w')
    toWrite = "idArea,idCorridor,weight\n"
    for a in dicAreas.values():
        for p in a.corridorsHoriz:
            toWrite = toWrite + "{},{},{}\n".format(a.id,p.id,weights["placedIn_CorridorArea"])
        for p in a.corridorsVert:
            toWrite = toWrite + "{},{},{}\n".format(a.id,p.id,weights["placedIn_CorridorArea"])
    file.write(toWrite)
    file.close()

# Relation Corridor - Room
def printRel_CorridorRoomCSV(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['room_corridor'], '.csv'), 'w')
    toWrite = "idCorridor,idRoom,weight\n"
    for p in dicCorridors.values():
        for r in p.rooms:
            toWrite = toWrite + "{},{},{}\n".format(p.id,r.id,weights["placedIn_RoomCorridor"])
    file.write(toWrite)
    file.close()

# Relation Room - Bed
def printRel_RoomBedCSV(dicRooms):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['bed_room'], '.csv'), 'w')
    toWrite = "idRoom,idBed,weight\n"
    for r in dicRooms.values():
        for b in r.beds:
            toWrite = toWrite + "{},{},{}\n".format(r.id,b,weights["placedIn_SeatRoom"])
    file.write(toWrite)
    file.close()


# Relations Bed - Bed  //  Room - Room  (nextTo  //  opposite)
def printRel_BedRoom_NextToOppositeCSV(dictionary, nameFile, heading, nextOrOpposite):
    file = open(folderOutput_Relations_CSV + '{}'.format(nameFile), 'w')
    toWrite = "{},weight\n".format(heading)
    
    writtenPairs = {}
    for br in dictionary.values():
        listNeighbors = None
        if nextOrOpposite == "nextTo":
            listNeighbors = br.nextTo
        elif nextOrOpposite == "opposite":
            listNeighbors = br.opposite
        for neighbor in listNeighbors:
            keyPair1 = "{}-{}".format(neighbor,br.id)
            if keyPair1 not in writtenPairs:
                toWrite = toWrite + "{},{}".format(br.id,neighbor)
                if nextOrOpposite == "nextTo":
                    if 'Bed' in heading:
                        toWrite += ",{}\n".format(weights["nextTo_Seat"])
                    elif 'Room' in heading:
                        toWrite += ",{}\n".format(weights["nextTo_Room"])
                elif nextOrOpposite == "opposite":
                    if 'Bed' in heading:
                        toWrite += ",{}\n".format(weights["opposite_Seat"])
                    elif 'Room' in heading:
                        toWrite += ",{}\n".format(weights["opposite_Room"])
                keyPair2 = "{}-{}".format(br.id,neighbor)
                writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()

# Relation Corridor - Corridor (nextTo)
def printRel_Corridor_NextToCSV(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['corridor_nt'], '.csv'), 'w')
    toWrite = "idCorridor1,idCorridor2,weight\n"
    
    writtenPair = {}
    for p in dicCorridors.values():
        for neighbors in p.nextTo.values():
            if (neighbors is not None):
                keyPair1 = "{}-{}".format(neighbors,p.id)
                if keyPair1 not in writtenPair:
                    toWrite = toWrite + "{},{},{}\n".format(p.id,neighbors,weights["nextTo_Corridor"])
                    keyPair2 = "{}-{}".format(p.id,neighbors)
                    writtenPair[keyPair2] = 1
    file.write(toWrite)
    file.close()    

# Relations Unit - Unit // Blcok - Block (nextTo)
def printRel_UnitBlock_NextToCSV(dictionary, nameFile, heading):
    file = open(folderOutput_Relations_CSV + '{}'.format(nameFile), 'w')
    toWrite = "{},weight\n".format(heading)
    
    writtenPairs = {}
    for ub in dictionary.values():
        # Previous neighbor
        if ub.nextTo_prev is not None:
            keyPair1 = "{}-{}".format(ub.nextTo_prev,ub.id)
            if keyPair1 not in writtenPairs:
                toWrite = toWrite + "{},{}".format(ub.id,ub.nextTo_prev)
                if 'Unit' in heading:
                    toWrite += ",{}\n".format(weights["nextTo_Unit"])
                elif 'Block' in heading:
                    toWrite += ",{}\n".format(weights["nextTo_Block"])
                keyPair2 = "{}-{}".format(ub.id,ub.nextTo_prev)
                writtenPairs[keyPair2] = 1
        # Next neighbor
        if ub.nextTo_after is not None:
            keyPair1 = "{}-{}".format(ub.nextTo_after,ub.id)
            if keyPair1 not in writtenPairs:
                toWrite = toWrite + "{},{}".format(ub.id,ub.nextTo_after)
                if 'Unit' in heading:
                    toWrite += ",{}\n".format(weights["nextTo_Unit"])
                elif 'Block' in heading:
                    toWrite += ",{}\n".format(weights["nextTo_Block"])
                keyPair2 = "{}-{}".format(ub.id,ub.nextTo_after)
                writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()    



''''''''''''''''''
'''  PATIENTS  '''
''''''''''''''''''

def printPatientsCSV(dicPatients):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['patient'], '.csv'), 'w')
    toWrite = "id,age,sex\n"
    for p in dicPatients.values():
        toWrite = toWrite + "{},{},{}\n".format(p.id,p.age,p.sex)
    file.write(toWrite)
    file.close()



''''''''''''''''''''''''
'''  MICROORGANISM   '''
''''''''''''''''''''''''

def printMicroorganismsCSV(dicMicroorganisms):
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['microorganism'], '.csv'), 'w')
    toWrite = "id,description\n"
    for m in dicMicroorganisms.values():
        toWrite = toWrite + "{},{}\n".format(m.id,m.description)
    file.write(toWrite)
    file.close()



''''''''''''''''''''''''''''''
'''  EPISODES AND EVENTS   '''
''''''''''''''''''''''''''''''

###############
# CSV CLASSES #
###############

# MAIN
def printClassesEpisodesEventsCSV(dicPatients):
    printEpisodesCSV(dicPatients)

    printEventsCSV(dicPatients, TypeEvent.Hospitalization, "{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['hospitalization'], '.csv'))
    printEventsCSV(dicPatients, TypeEvent.Radiology, "{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['radiology'], '.csv'))
    printEventsCSV(dicPatients, TypeEvent.Surgery, "{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['surgery'], '.csv'))
    printEventsCSV(dicPatients, TypeEvent.Death, "{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['death'], '.csv'))
    printEventsCSV(dicPatients, TypeEvent.TestMicro, "{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['testMicro'], '.csv'))



# Episodes
def printEpisodesCSV(dicPatients):    
    file = open("{}{}{}".format(folderOutput_Classes_CSV, nameFiles_Classes['episode'], '.csv'), 'w')
    toWrite = "id,description,start,end\n"  # Format: %Y-%m-%dT%H:%M:%SZ  ->  2022-01-01T00:00:00Z
    for patient in dicPatients.values():
        for ep in patient.episodes:
            toWrite += "{},{},{},{}\n".format(ep.id,ep.description,ep.start.strftime("%Y-%m-%dT%H:%M:%SZ"),ep.end.strftime("%Y-%m-%dT%H:%M:%SZ"))
    file.write(toWrite)
    file.close()

# Events
def printEventsCSV(dicPatients, type, nameFile):    
    file = open(nameFile, 'w')
    toWrite = "id,description,start,end\n"  # Formato: %Y-%m-%dT%H:%M:%SZ  ->  2022-01-01T00:00:00Z
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.type is type:
                    toWrite += "{},{},{},{}\n".format(ev.id,ev.description,ev.start.strftime("%Y-%m-%dT%H:%M:%SZ"),ev.end.strftime("%Y-%m-%dT%H:%M:%SZ"))
    file.write(toWrite)
    file.close()



#################
# CSV RELATIONS #
#################

# MAIN
def printRelationEpisodesEventsCSV(dicPatients):
    printRel_EpisodePatientCSV(dicPatients)
    printRel_EventEpisodeCSV(dicPatients)
    printRel_EventBedCSV(dicPatients)
    printRel_EventHospUnitCSV(dicPatients)
    printRel_TestMicroorgCSV(dicPatients)


# Relation Episode-Patient
def printRel_EpisodePatientCSV(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['ep_pat'], '.csv'), 'w')
    toWrite = "idEpisode,idPatient\n"
    for patient in dicPatients.values():
        for ep in patient.episodes:
            toWrite += "{},{}\n".format(ep.id, patient.id)
    file.write(toWrite)
    file.close()

# Relation Event-Episode
def printRel_EventEpisodeCSV(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['ev_ep'], '.csv'), 'w')
    toWrite = "idEvent,idEpisode\n"
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                toWrite += "{},{}\n".format(ev.id, ep.id)
    file.write(toWrite)
    file.close() 

# Relation Event-Bed
def printRel_EventBedCSV(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['ev_bed'], '.csv'), 'w')
    toWrite = "idEvent,idBed\n"
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.location is not None:
                    toWrite += "{},{}\n".format(ev.id, ev.location)
    file.write(toWrite)
    file.close()    

# Relation Event-HospUnit
def printRel_EventHospUnitCSV(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['ev_uh'], '.csv'), 'w')
    toWrite = "idEvent,idHospUnit\n"
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.hospUnit is not None:
                    toWrite += "{},{}\n".format(ev.id, ev.hospUnit)
    file.write(toWrite)
    file.close()    

# Relation TestMicro-Microorganism
def printRel_TestMicroorgCSV(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_CSV, nameFiles_Rels['test_micro'], '.csv'), 'w')
    toWrite = "idEvent,idMicroorg,mmr\n"
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.type is TypeEvent.TestMicro:
                    microorg = ev.extra1
                    toWrite += "{},{},{}\n".format(ev.id, microorg.id, ev.extra2)
    file.write(toWrite)
    file.close() 


