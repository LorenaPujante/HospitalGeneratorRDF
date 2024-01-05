import os
from classes import *
from weightsLocsHierarchy import weights
from writerRDF import *


##################
# INITIALIZATION #
##################

def setFolderOutputRDFstar(dir):
    global folderOutput_RDF_star
    folderOutput_RDF_star = dir
    if (not os.path.exists(folderOutput_RDF_star)):
        os.makedirs(folderOutput_RDF_star)
    
    global folderOutput_Classes_RDF_star
    folderOutput_Classes_RDF_star = folderOutput_RDF_star + "\\Classes"
    if (not os.path.exists(folderOutput_Classes_RDF_star)):
        os.makedirs(folderOutput_Classes_RDF_star)

    global folderOutput_Relations_RDF_star
    folderOutput_Relations_RDF_star = folderOutput_RDF_star + "\\Relations"
    if (not os.path.exists(folderOutput_Relations_RDF_star)):
        os.makedirs(folderOutput_Relations_RDF_star)

    return folderOutput_Classes_RDF_star, folderOutput_Relations_RDF_star



''''''''''''''
'''  MAIN  '''
''''''''''''''

def printRDF_star(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms):
    printClassesRDF_star(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms)
    printRelsRDF_star(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients)


def printClassesRDF_star(dicServicios, dicUnidadesHosp, dicBuildings, dicPlantas, dicUnits, dicBlocks, dicAreas, dicPasillos, dicRooms, dicBeds, dicPatients, dicMicroorganisms):
    # Hospital
    printClassesHospitalRDF_star(dicServicios, dicUnidadesHosp, dicBuildings, dicPlantas, dicUnits, dicBlocks, dicAreas, dicPasillos, dicRooms, dicBeds)

    # Patients
    printPatientsRDF_star(dicPatients)

    # Microorganisms
    printMicroorganismsRDF_star(dicMicroorganisms)

    # Episodes y Events
    printClassesEpisodesEventsRDF_star(dicPatients)


def printRelsRDF_star(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients):
    # Hospital
    printRelationsHospitalRDF_star(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds)

    # Patients, Episodes y Events
    printRelationsEpisodesEventsRDF_star(dicPatients)



''''''''''''''''''
'''  HOSPITAL  '''
''''''''''''''''''

###########
# CLASSES #
###########

# MAIN
def printClassesHospitalRDF_star(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds):
    
    printServicesRDF_star(dicServices)
    printHospUnitsRDF_star(dicHospUnits)
    
    printBuildingsRDF_star(dicBuildings)
    printFloorsRDF_star(dicFloors)
    printUnitsRDF_star(dicUnits)
    printBlocksRDF_star(dicBlocks)
    printAreasRDF_star(dicAreas)
    printCorridorsRDF_star(dicCorridors)
    printRoomsRDF_star(dicRooms)
    printBedsRDF_star(dicBeds)


# Services
def printServicesRDF_star(dicServices):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['service'], '.nt'), 'w')
    toWrite = getToWriteServicesRDF(dicServices)
    file.write(toWrite)
    file.close()

# Hospitalization Units
def printHospUnitsRDF_star(dicHospUnits):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['uh'], '.nt'), 'w')
    toWrite = getToWriteHospUnitsRDF(dicHospUnits)   
    file.write(toWrite)
    file.close()


# Buildings
def printBuildingsRDF_star(dicBuildings):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['building'], '.nt'), 'w')
    toWrite = getToWriteBuildingsRDF(dicBuildings)
    file.write(toWrite)
    file.close()

# Floors
def printFloorsRDF_star(dicFloors):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['floor'], '.nt'), 'w')
    toWrite = getToWriteFloorsRDF(dicFloors)
    file.write(toWrite)
    file.close()

# Units
def printUnitsRDF_star(dicUnits):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['unit'], '.nt'), 'w')
    toWrite = getToWriteUnitsRDF(dicUnits)
    file.write(toWrite)
    file.close()

# Blocks
def printBlocksRDF_star(dicBlocks):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['block'], '.nt'), 'w')
    toWrite = getToWriteBlocksRDF(dicBlocks)
    file.write(toWrite)
    file.close()

# Areas
def printAreasRDF_star(dicAreas):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['area'], '.nt'), 'w')
    toWrite = getToWriteAreasRDF(dicAreas)
    file.write(toWrite)
    file.close()

# Corridors
def printCorridorsRDF_star(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['corridor'], '.nt'), 'w')
    toWrite = getToWriteCorridorsRDF(dicCorridors)
    file.write(toWrite)
    file.close()

# Rooms
def printRoomsRDF_star(dicRooms):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['room'], '.nt'), 'w')
    toWrite = getToWriteRoomsRDF(dicRooms)
    file.write(toWrite)
    file.close()

# Beds
def printBedsRDF_star(dicBeds):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['bed'], '.nt'), 'w')
    toWrite = getToWriteCamasRDF(dicBeds)
    file.write(toWrite)
    file.close()


#############
# RELATIONS #
#############

# MAIN
def printRelationsHospitalRDF_star(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds):
    
    printRel_ServiceHospUnitsRDF_star(dicServices)
    printRel_HospUnitBedRDF_star(dicBeds)
    
    printRel_BuildingFloorRDF_star(dicBuildings)
    printRel_FloorAreaRDF_star(dicFloors)
    printRel_FloorUnitRDF_star(dicFloors)
    printRel_FloorBlockRDF_star(dicFloors)
    printRel_UnitAreaRDF_star(dicAreas)
    printRel_BloqueAreaRDF_star(dicAreas)
    printRel_AreaCorridorRDF_star(dicAreas)
    printRel_CorridorRoomRDF_star(dicCorridors)
    printRel_RoomBedRDF_star(dicRooms)

    printRel_BedRoom_NextToOppositeRDF_star(dicBeds, "{}{}".format(nameFiles_Rels['bed_nt'], '.ttl'), "idBed1,idBed2", "nextTo")
    printRel_BedRoom_NextToOppositeRDF_star(dicBeds, "{}{}".format(nameFiles_Rels['bed_ot'], '.ttl'), "idBed1,idBed2", "opposite")
    printRel_BedRoom_NextToOppositeRDF_star(dicRooms, "{}{}".format(nameFiles_Rels['room_nt'], '.ttl'), "idRoom1,idRoom2", "nextTo")
    printRel_BedRoom_NextToOppositeRDF_star(dicRooms, "{}{}".format(nameFiles_Rels['room_ot'], '.ttl'), "idRoom1,idRoom2", "opposite")
    printRel_Corridor_NextToRDF_star(dicCorridors)
    printRel_UnitBlock_NextToRDF_star(dicUnits, "{}{}".format(nameFiles_Rels['unit_nt'], '.ttl'), "idUnit1,idUnit2")
    printRel_UnitBlock_NextToRDF_star(dicBlocks, "{}{}".format(nameFiles_Rels['block_nt'], '.ttl'), "idBlock1,idBlock2")


# Relation Service - HospitUnit
def printRel_ServiceHospUnitsRDF_star(dicServices):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['serv_uh'], '.ttl'), 'w')
    toWrite = ""
    for s in dicServices.values():
        for uh in s.hospUnits:
            toWrite += "<{}#HospitalizationUnit/{}> <{}#hospUnitFromService> <{}#Service/{}>.\n".format(prefixes_nt["hospOnt"],uh, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],s.id)
            toWrite += "<< <{}#HospitalizationUnit/{}> <{}#hospUnitFromService> <{}#Service/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],uh, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],s.id, prefixes_nt["hospOnt"], weights["hospUnitFromService"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()
    
    
# Relation HospUnit - Bed
def printRel_HospUnitBedRDF_star(dicBeds):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['uh_bed'], '.ttl'), 'w')
    toWrite = ""
    for b in dicBeds.values():
        uh = b.hospUnit
        toWrite += "<{}#HospitalizationUnit/{}> <{}#looksAfter> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],uh, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],b.id)
        toWrite += "<< <{}#HospitalizationUnit/{}> <{}#looksAfter> <{}#Bed/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],uh, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], weights["looksAfter"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()


# Relation Building - Floor
def printRel_BuildingFloorRDF_star(dicBuildings):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['floor_building'], '.ttl'), 'w')
    toWrite = ""
    for b in dicBuildings.values():
        for p in b.floors:
            toWrite += "<{}#Floor/{}> <{}#placedIn> <{}#Building/{}>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],b.id)
            toWrite += "<< <{}#Floor/{}> <{}#placedIn> <{}#Building/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], weights["placedIn_FloorBuilding"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Floor - Area
def printRel_FloorAreaRDF_star(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['area_floor'], '.ttl'), 'w')
    toWrite = ""
    for p in dicFloors.values():
        for a in p.areas:
            toWrite += "<{}#Area/{}> <{}#placedIn> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],p.id)
            toWrite += "<< <{}#Area/{}> <{}#placedIn> <{}#Floor/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], weights["placedIn_AreaFloor"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Floor - Unit
def printRel_FloorUnitRDF_star(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['unit_floor'], '.ttl'), 'w')
    toWrite = ""
    for p in dicFloors.values():
        for u in p.units:
            toWrite += "<{}#Unit/{}> <{}#placedInFloor> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],u.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],p.id)
            toWrite += "<< <{}#Unit/{}> <{}#placedInFloor> <{}#Floor/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],u.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], weights["placedInFloor_Unit"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Floor - Block
def printRel_FloorBlockRDF_star(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['block_floor'], '.ttl'), 'w')
    toWrite = ""
    for p in dicFloors.values():
        for b in p.blocks:
            toWrite += "<{}#Block/{}> <{}#placedInFloor> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],p.id)
            toWrite += "<< <{}#Block/{}> <{}#placedInFloor> <{}#Floor/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], weights["placedInFloor_Block"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Unit - Area
def printRel_UnitAreaRDF_star(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['area_unit'], '.ttl'), 'w')
    toWrite = ""
    for a in dicAreas.values():
        toWrite += "<{}#Area/{}> <{}#placedInUnit> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.unit.id)
        toWrite += "<< <{}#Area/{}> <{}#placedInUnit> <{}#Unit/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.unit.id, prefixes_nt["hospOnt"], weights["placedInUnit"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Block - Area
def printRel_BloqueAreaRDF_star(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['area_block'], '.ttl'), 'w')
    toWrite = ""
    for a in dicAreas.values():
        toWrite += "<{}#Area/{}> <{}#placedInBlock> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.block.id)
        toWrite += "<< <{}#Area/{}> <{}#placedInBlock> <{}#Block/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.block.id, prefixes_nt["hospOnt"], weights["placedInBlock"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Area - Corridor
def printRel_AreaCorridorRDF_star(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['corridor_area'], '.ttl'), 'w')
    toWrite = ""
    for a in dicAreas.values():
        for c in a.corridorsHoriz:
            toWrite += "<{}#Corridor/{}> <{}#placedIn> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.id)
            toWrite += "<< <{}#Corridor/{}> <{}#placedIn> <{}#Area/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], weights["placedIn_CorridorArea"],prefixes_nt["xmlSchema"])
        for c in a.corridorsVert:
            toWrite += "<{}#Corridor/{}> <{}#placedIn> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.id)
            toWrite += "<< <{}#Corridor/{}> <{}#placedIn> <{}#Area/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], weights["placedIn_CorridorArea"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Corridor - Room
def printRel_CorridorRoomRDF_star(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['room_corridor'], '.ttl'), 'w')
    toWrite = ""
    for c in dicCorridors.values():
        for r in c.rooms:
            toWrite += "<{}#Room/{}> <{}#placedIn> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],r.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],c.id)
            toWrite += "<< <{}#Room/{}> <{}#placedIn> <{}#Corridor/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],r.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], weights["placedIn_RoomCorridor"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()

# Relation Room - Cama
def printRel_RoomBedRDF_star(dicRooms):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['bed_room'], '.ttl'), 'w')
    toWrite = ""
    for r in dicRooms.values():
        for b in r.beds:
            toWrite += "<{}#Bed/{}> <{}#placedIn> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],b, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],r.id)
            toWrite += "<< <{}#Bed/{}> <{}#placedIn> <{}#Room/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],b, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],r.id, prefixes_nt["hospOnt"], weights["placedIn_SeatRoom"],prefixes_nt["xmlSchema"])
    file.write(toWrite)
    file.close()


# Relations Bed - Bed  //  Room - Room  (nextTo  //  opposite)
def printRel_BedRoom_NextToOppositeRDF_star(dictionary, nameFile, heading, nextOrOpposite):
    file = open(folderOutput_Relations_RDF_star + '{}'.format(nameFile), 'w')
    toWrite = ""
    
    writtenPairs = {}
    for br in dictionary.values():
        listNeighbors = None
        if nextOrOpposite == "nextTo":
            listNeighbors = br.nextTo
        elif nextOrOpposite == "opposite":
            listNeighbors = br.opposite
        for neighbor in listNeighbors:
            keyPait1 = "{}-{}".format(neighbor,br.id)
            if keyPait1 not in writtenPairs:

                if nextOrOpposite == "nextTo":
                    if 'Bed' in heading:
                        toWrite += "<{}#Bed/{}> <{}#nextTo> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor)
                        toWrite += "<< <{}#Bed/{}> <{}#nextTo> <{}#Bed/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor, prefixes_nt["hospOnt"], weights["nextTo_Seat"],prefixes_nt["xmlSchema"])

                    elif 'Room' in heading:
                        toWrite += "<{}#Room/{}> <{}#nextTo> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor)
                        toWrite += "<< <{}#Room/{}> <{}#nextTo> <{}#Room/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor, prefixes_nt["hospOnt"], weights["nextTo_Room"],prefixes_nt["xmlSchema"])

                elif nextOrOpposite == "opposite":
                    if 'Bed' in heading:
                        toWrite += "<{}#Bed/{}> <{}#opposite> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor)
                        toWrite += "<< <{}#Bed/{}> <{}#opposite> <{}#Bed/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor, prefixes_nt["hospOnt"], weights["opposite_Seat"],prefixes_nt["xmlSchema"])
                        
                    elif 'Room' in heading:
                        toWrite += "<{}#Room/{}> <{}#opposite> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor)
                        toWrite += "<< <{}#Room/{}> <{}#opposite> <{}#Room/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbor, prefixes_nt["hospOnt"], weights["opposite_Room"],prefixes_nt["xmlSchema"])
                        
                keyPair2 = "{}-{}".format(br.id,neighbor)
                writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()


# Relation Corridor - Corridor (nextTo)
def printRel_Corridor_NextToRDF_star(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['corridor_nt'], '.ttl'), 'w')
    toWrite = ""
    
    writtenPairs = {}
    for p in dicCorridors.values():
        for neighbors in p.nextTo.values():
            if (neighbors is not None):
                keyPair1 = "{}-{}".format(neighbors,p.id)
                if keyPair1 not in writtenPairs:
                    toWrite += "<{}#Corridor/{}> <{}#nextTo> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbors)
                    toWrite += "<< <{}#Corridor/{}> <{}#nextTo> <{}#Corridor/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],neighbors, prefixes_nt["hospOnt"], weights["nextTo_Corridor"],prefixes_nt["xmlSchema"])
           
                    keyPair2 = "{}-{}".format(p.id,neighbors)
                    writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()    

# Relations Unit - Unit // Blcok - Block (nextTo)
def printRel_UnitBlock_NextToRDF_star(dictionary, nameFile, heading):
    file = open(folderOutput_Relations_RDF_star + '{}'.format(nameFile), 'w')
    toWrite = ""
    
    writtenPairs = {}
    for ub in dictionary.values():
        # Previous neighbor
        if ub.nextTo_prev is not None:
            keyPair1 = "{}-{}".format(ub.nextTo_prev,ub.id)
            if keyPair1 not in writtenPairs:
                if 'Unit' in heading:
                    toWrite += "<{}#Unit/{}> <{}#nextTo> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_prev)
                    toWrite += "<< <{}#Unit/{}> <{}#nextTo> <{}#Unit/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_prev, prefixes_nt["hospOnt"], weights["nextTo_Unit"],prefixes_nt["xmlSchema"])
                 
                elif 'Block' in heading:
                    toWrite += "<{}#Block/{}> <{}#nextTo> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_prev)
                    toWrite += "<< <{}#Block/{}> <{}#nextTo> <{}#Block/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_prev, prefixes_nt["hospOnt"], weights["nextTo_Block"],prefixes_nt["xmlSchema"])
                    
                keyPair2 = "{}-{}".format(ub.id,ub.nextTo_prev)
                writtenPairs[keyPair2] = 1
        # Next neighbor
        if ub.nextTo_after is not None:
            keyPair1 = "{}-{}".format(ub.nextTo_after,ub.id)
            if keyPair1 not in writtenPairs:
                if 'Unit' in heading:
                    toWrite += "<{}#Unit/{}> <{}#nextTo> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_after)
                    toWrite += "<< <{}#Unit/{}> <{}#nextTo> <{}#Unit/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_after, prefixes_nt["hospOnt"], weights["nextTo_Unit"],prefixes_nt["xmlSchema"])
                    
                elif 'Block' in heading:
                    toWrite += "<{}#Block/{}> <{}#nextTo> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_after)
                    toWrite += "<< <{}#Block/{}> <{}#nextTo> <{}#Block/{}> >> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ub.nextTo_after, prefixes_nt["hospOnt"], weights["nextTo_Block"],prefixes_nt["xmlSchema"])

                keyPair2 = "{}-{}".format(ub.id,ub.nextTo_after)
                writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()  



''''''''''''''''''
'''  PATIENTS  '''
''''''''''''''''''

def printPatientsRDF_star(dicPatients):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['patient'], '.nt'), 'w')
    toWrite = getToWritePatientsRDF(dicPatients)
    file.write(toWrite)
    file.close()



''''''''''''''''''''''''
'''  MICROORGANISM   '''
''''''''''''''''''''''''

def printMicroorganismsRDF_star(dicMicroorganisms):
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['microorganism'], '.nt'), 'w')
    toWrite = getToWriteMicroorganismsRDF(dicMicroorganisms)
    file.write(toWrite)
    file.close()



''''''''''''''''''''''''''''''
'''  EPISODES AND EVENTS   '''
''''''''''''''''''''''''''''''

###########
# CLASSES #
###########

# MAIN
def printClassesEpisodesEventsRDF_star(dicPatients):
    printEpisodesRDF_star(dicPatients)

    printEventsRDF_star(dicPatients, TypeEvent.Hospitalization, "{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['hospitalization'], '.nt'))
    printEventsRDF_star(dicPatients, TypeEvent.Radiology, "{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['radiology'], '.nt'))
    printEventsRDF_star(dicPatients, TypeEvent.Surgery, "{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['surgery'], '.nt'))
    printEventsRDF_star(dicPatients, TypeEvent.Death, "{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['death'], '.nt'))
    printEventsRDF_star(dicPatients, TypeEvent.TestMicro, "{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['testMicro'], '.nt'))


# Episodes
def printEpisodesRDF_star(dicPatients):    
    file = open("{}{}{}".format(folderOutput_Classes_RDF_star, nameFiles_Classes['episode'], '.nt'), 'w')
    toWrite = getToWriteEpisodesRDF(dicPatients)
    file.write(toWrite)
    file.close()

# Events
def printEventsRDF_star(dicPatients, tipo, nameFile):    
    file = open(nameFile, 'w')
    toWrite = getToWriteEventosRDF(dicPatients, tipo)
    file.write(toWrite)
    file.close()


#############
# RELATIONS #
#############

# MAIN
def printRelationsEpisodesEventsRDF_star(dicPatients):
    printRel_EpisodePatientRDF_star(dicPatients)
    printRel_EventEpisodeRDF_star(dicPatients)
    printRel_EventBedRDF_star(dicPatients)
    printRel_EventHospUnitRDF_star(dicPatients)
    printRel_TestMicroorgRDF_star(dicPatients)


# Relation Episode-Patient
def printRel_EpisodePatientRDF_star(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['ep_pat'], '.ttl'), 'w')
    toWrite = getToWriteRel_EpisodePatientRDF(dicPatients)
    file.write(toWrite)
    file.close()

# Relation Event-Episode
def printRel_EventEpisodeRDF_star(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['ev_ep'], '.ttl'), 'w')
    toWrite = getToWriteRel_EventEpisodeRDF(dicPatients)
    file.write(toWrite)
    file.close() 

# Relation Event-Bed
def printRel_EventBedRDF_star(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['ev_bed'], '.ttl'), 'w')
    toWrite = getToWriteRel_EventBedRDF(dicPatients)
    file.write(toWrite)
    file.close()    

# Relation Event-HospUnit
def printRel_EventHospUnitRDF_star(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['ev_uh'], '.ttl'), 'w')
    toWrite = getToWriteRel_EventHospUnitRDF(dicPatients)
    file.write(toWrite)
    file.close()    

# Relation TestMicro-Microorganism
def printRel_TestMicroorgRDF_star(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF_star, nameFiles_Rels['test_micro'], '.ttl'), 'w')
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.type is TypeEvent.TestMicro:
                    microorg = ev.extra1
                    if ev.extra2:
                        mmr = 1
                    else:
                        mmr = 0
                    toWrite += "<{}#TestMicro/{}> <{}#hasFound> <{}#Microorganism/{}>.\n".format(prefixes_nt["hospOnt"],ev.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],microorg.id)
                    toWrite += "<< <{}#TestMicro/{}> <{}#hasFound> <{}#Microorganism/{}> >> <{}#mmr> \"{}\"^^<{}/boolean>.\n".format(prefixes_nt["hospOnt"],ev.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],microorg.id, prefixes_nt["hospOnt"], mmr,prefixes_nt["xmlSchema"])

    file.write(toWrite)
    file.close() 


