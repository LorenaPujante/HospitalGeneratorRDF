import os
from classes import *
from weightsLocsHierarchy import weights
from variablesWriter import prefixes_nt, nameFiles_Classes, nameFiles_Rels



##################
# INITIALIZATION #
##################

def setFolderOutputRDF(dir):
    global folderOutput_RDF
    folderOutput_RDF = dir
    if (not os.path.exists(folderOutput_RDF)):
        os.makedirs(folderOutput_RDF)
    
    global folderOutput_Classes_RDF
    folderOutput_Classes_RDF = folderOutput_RDF + "\\Classes"
    if (not os.path.exists(folderOutput_Classes_RDF)):
        os.makedirs(folderOutput_Classes_RDF)

    global folderOutput_Relations_RDF
    folderOutput_Relations_RDF = folderOutput_RDF + "\\Relations"
    if (not os.path.exists(folderOutput_Relations_RDF)):
        os.makedirs(folderOutput_Relations_RDF)

    return folderOutput_Classes_RDF, folderOutput_Relations_RDF



''''''''''''''
'''  MAIN  '''
''''''''''''''

def printRDF(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms):
    printClassesRDF(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms)
    printRelsRDF(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients)


def printClassesRDF(dicServicios, dicUnidadesHosp, dicBuildings, dicPlantas, dicUnits, dicBlocks, dicAreas, dicPasillos, dicRooms, dicBeds, dicPatients, dicMicroorganisms):
    # Hospital
    printClasesHospitalRDF(dicServicios, dicUnidadesHosp, dicBuildings, dicPlantas, dicUnits, dicBlocks, dicAreas, dicPasillos, dicRooms, dicBeds)

    # Patients
    printPatientsRDF(dicPatients)

    # Microorganisms
    printMicroorganismsRDF(dicMicroorganisms)

    # Episodes y Events
    printClassesEpisodesEventsRDF(dicPatients)


def printRelsRDF(dicServicios, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients):
    # Hospital
    printRelationsHospitalRDF(dicServicios, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds)

    # Patients, Episodes y Events
    printRelationsEpisodesEventsRDF(dicPatients)



''''''''''''''''''
'''  HOSPITAL  '''
''''''''''''''''''

###########
# CLASSES #
###########

# MAIN
def printClasesHospitalRDF(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds):
    
    printServicesRDF(dicServices)
    printHospUnitsRDF(dicHospUnits)
    
    printBuildingsRDF(dicBuildings)
    printFloorsRDF(dicFloors)
    printUnitsRDF(dicUnits)
    printBlocksRDF(dicBlocks)
    printAreasRDF(dicAreas)
    printCorridorsRDF(dicCorridors)
    printRoomsRDF(dicRooms)
    printBedsRDF(dicBeds)


# Services
def printServicesRDF(dicServices):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['service'], '.nt'), 'w')
    toWrite = getToWriteServicesRDF(dicServices)
    file.write(toWrite)
    file.close()

def getToWriteServicesRDF(dicServices):
    toWrite = ""
    for s in dicServices.values():
        toWrite += "<{}#Service/{}> <{}#type> <{}#Service>.\n".format(prefixes_nt['hospOnt'],s.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Service/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],s.id, prefixes_nt["hospOnt"], s.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Service/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],s.id, prefixes_nt["hospOnt"], s.description,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Service/{}> <{}#abbreviation> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],s.id, prefixes_nt["hospOnt"], s.abrev,prefixes_nt['xmlSchema'])

    return toWrite
    

# Hospitalization Units
def printHospUnitsRDF(dicHospUnits):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['uh'], '.nt'), 'w')
    toWrite = getToWriteHospUnitsRDF(dicHospUnits)
    file.write(toWrite)
    file.close()

def getToWriteHospUnitsRDF(dicHospUnits):
    toWrite = ""
    for uh in dicHospUnits.values():
        toWrite += "<{}#HospitalizationUnit/{}> <{}#type> <{}#HospitalizationUnit>.\n".format(prefixes_nt['hospOnt'],uh.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#HospitalizationUnit/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],uh.id, prefixes_nt["hospOnt"], uh.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#HospitalizationUnit/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],uh.id, prefixes_nt["hospOnt"], uh.description,prefixes_nt['xmlSchema'])
        toWrite += "<{}#HospitalizationUnit/{}> <{}#abbreviation> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],uh.id, prefixes_nt["hospOnt"], uh.abrev,prefixes_nt['xmlSchema'])   

    return toWrite


# Buildings
def printBuildingsRDF(dicBuildings):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['building'], '.nt'), 'w')
    toWrite = getToWriteBuildingsRDF(dicBuildings)
    file.write(toWrite)
    file.close()

def getToWriteBuildingsRDF(dicBuildings):
    toWrite = ""
    for b in dicBuildings.values():
        toWrite += "<{}#Building/{}> <{}#type> <{}#Location>.\n".format(prefixes_nt['hospOnt'],b.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Building/{}> <{}#type> <{}#Building>.\n".format(prefixes_nt['hospOnt'],b.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Building/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], b.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Building/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], b.description,prefixes_nt['xmlSchema'])

    return toWrite


# Floors
def printFloorsRDF(dicFloors):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['floor'], '.nt'), 'w')
    toWrite = getToWriteFloorsRDF(dicFloors)
    file.write(toWrite)
    file.close()

def getToWriteFloorsRDF(dicFloors):
    toWrite = ""
    for f in dicFloors.values():
        toWrite += "<{}#Floor/{}> <{}#type> <{}#Location>.\n".format(prefixes_nt['hospOnt'],f.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Floor/{}> <{}#type> <{}#Floor>.\n".format(prefixes_nt['hospOnt'],f.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Floor/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],f.id, prefixes_nt["hospOnt"], f.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Floor/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],f.id, prefixes_nt["hospOnt"], f.description,prefixes_nt['xmlSchema'])
    
    return toWrite


# Units
def printUnitsRDF(dicUnits):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['unit'], '.nt'), 'w')
    toWrite = getToWriteUnitsRDF(dicUnits)
    file.write(toWrite)
    file.close()

def getToWriteUnitsRDF(dicUnits):
    toWrite = ""
    for u in dicUnits.values():
        toWrite += "<{}#Unit/{}> <{}#type> <{}#Unit>.\n".format(prefixes_nt['hospOnt'],u.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Unit/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],u.id, prefixes_nt["hospOnt"], u.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Unit/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],u.id, prefixes_nt["hospOnt"], u.description,prefixes_nt['xmlSchema'])

    return toWrite


# Blocks
def printBlocksRDF(dicBlocks):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['block'], '.nt'), 'w')
    toWrite = getToWriteBlocksRDF(dicBlocks)
    file.write(toWrite)
    file.close()

def getToWriteBlocksRDF(dicBlocks):
    toWrite = ""
    for b in dicBlocks.values():
        toWrite += "<{}#Block/{}> <{}#type> <{}#Block>.\n".format(prefixes_nt['hospOnt'],b.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Block/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], b.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Block/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], b.description,prefixes_nt['xmlSchema'])

    return toWrite


# Areas
def printAreasRDF(dicAreas):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['area'], '.nt'), 'w')
    toWrite = getToWriteAreasRDF(dicAreas)
    file.write(toWrite)
    file.close()

def getToWriteAreasRDF(dicAreas):
    toWrite = ""
    for a in dicAreas.values():
        toWrite += "<{}#Area/{}> <{}#type> <{}#Location>.\n".format(prefixes_nt['hospOnt'],a.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Area/{}> <{}#type> <{}#Area>.\n".format(prefixes_nt['hospOnt'],a.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Area/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], a.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Area/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],a.id, prefixes_nt["hospOnt"], a.description,prefixes_nt['xmlSchema'])

    return toWrite


# Corridors
def printCorridorsRDF(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['corridor'], '.nt'), 'w')
    toWrite = getToWriteCorridorsRDF(dicCorridors)
    file.write(toWrite)
    file.close()

def getToWriteCorridorsRDF(dicCorridors):
    toWrite = ""
    for c in dicCorridors.values():
        toWrite += "<{}#Corridor/{}> <{}#type> <{}#Location>.\n".format(prefixes_nt['hospOnt'],c.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Corridor/{}> <{}#type> <{}#Corridor>.\n".format(prefixes_nt['hospOnt'],c.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Corridor/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], c.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Corridor/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],c.id, prefixes_nt["hospOnt"], c.description,prefixes_nt['xmlSchema'])

    return toWrite


# Rooms
def printRoomsRDF(dicRooms):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['room'], '.nt'), 'w')
    toWrite = getToWriteRoomsRDF(dicRooms)
    file.write(toWrite)
    file.close()

def getToWriteRoomsRDF(dicRooms):
    toWrite = ""
    for r in dicRooms.values():
        toWrite += "<{}#Room/{}> <{}#type> <{}#Location>.\n".format(prefixes_nt['hospOnt'],r.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Room/{}> <{}#type> <{}#Room>.\n".format(prefixes_nt['hospOnt'],r.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Room/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],r.id, prefixes_nt["hospOnt"], r.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Room/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],r.id, prefixes_nt["hospOnt"], r.description,prefixes_nt['xmlSchema'])

    return toWrite


# Beds
def printBedsRDF(dicBeds):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['bed'], '.nt'), 'w')
    toWrite = getToWriteCamasRDF(dicBeds)
    file.write(toWrite)
    file.close()

def getToWriteCamasRDF(dicBeds):
    toWrite = ""
    for b in dicBeds.values():
        toWrite += "<{}#Bed/{}> <{}#type> <{}#Location>.\n".format(prefixes_nt['hospOnt'],b.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Bed/{}> <{}#type> <{}#Seat>.\n".format(prefixes_nt['hospOnt'],b.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Bed/{}> <{}#type> <{}#Bed>.\n".format(prefixes_nt['hospOnt'],b.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Bed/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], b.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Bed/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],b.id, prefixes_nt["hospOnt"], b.description,prefixes_nt['xmlSchema'])

    return toWrite


#############
# RELATIONS #
#############

# MAIN
def printRelationsHospitalRDF(dicServices, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds):
    
    printRel_ServiceHospUnitRDF(dicServices)
    printRel_HospUnitBedRDF(dicBeds)
    
    printRel_BuildingFloorRDF(dicBuildings)
    printRel_FloorAreaRDF(dicFloors)
    printRel_FloorUnitRDF(dicFloors)
    printRel_FloorBlockRDF(dicFloors)
    printRel_UnitAreaRDF(dicAreas)
    printRel_BlockAreaRDF(dicAreas)
    printRel_AreaCorridorRDF(dicAreas)
    printRel_CorridorRoomRDF(dicCorridors)
    printRel_RoomBedRDF(dicRooms)

    printRel_BedRoom_NextToOppositeRDF(dicBeds, "{}{}".format(nameFiles_Rels['bed_nt'], '.nt'), "idBed1,idBed2", "nextTo")
    printRel_BedRoom_NextToOppositeRDF(dicBeds, "{}{}".format(nameFiles_Rels['bed_ot'], '.nt'), "idBed1,idBed2", "opposite")
    printRel_BedRoom_NextToOppositeRDF(dicRooms, "{}{}".format(nameFiles_Rels['room_nt'], '.nt'), "idRoom1,idRoom2", "nextTo")
    printRel_BedRoom_NextToOppositeRDF(dicRooms, "{}{}".format(nameFiles_Rels['room_ot'], '.nt'), "idRoom1,idRoom2", "opposite")
    printRel_Corridor_NextToRDF(dicCorridors)
    printRel_UnitBlock_NextToRDF(dicUnits, "{}{}".format(nameFiles_Rels['unit_nt'], '.nt'), "idUnit1,idUnit2")
    printRel_UnitBlock_NextToRDF(dicBlocks, "{}{}".format(nameFiles_Rels['block_nt'], '.nt'), "idBlock1,idBlock2")


# Relation Service - HospUnit
def printRel_ServiceHospUnitRDF(dicServices):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['serv_uh'], '.nt'), 'w')
    toWrite = ""
    for s in dicServices.values():
        for uh in s.hospUnits:
            toWrite += "<{}#HospUnitFromService/{}_{}> <{}#type> <{}#HospUnitFromService>.\n".format(prefixes_nt["hospOnt"],uh,s.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#HospUnitFromService/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],uh,s.id, prefixes_nt["hospOnt"], weights['hospUnitFromService'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#HospUnitFromService/{}_{}> <{}#hospUnitFromService1> <{}#HospitalizationUnit/{}>.\n".format(prefixes_nt["hospOnt"],uh,s.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],uh)
            toWrite += "<{}#HospUnitFromService/{}_{}> <{}#hospUnitFromService2> <{}#Service/{}>.\n".format(prefixes_nt["hospOnt"],uh,s.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],s.id)
    file.write(toWrite)
    file.close()
    
    
# Relation HospUnit - Bed
def printRel_HospUnitBedRDF(dicBeds):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['uh_bed'], '.nt'), 'w')
    toWrite = ""
    for b in dicBeds.values():
        hu = b.hospUnit
        toWrite += "<{}#LooksAfter/{}_{}> <{}#type> <{}#LooksAfter>.\n".format(prefixes_nt["hospOnt"],hu,b.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
        toWrite += "<{}#LooksAfter/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],hu,b.id, prefixes_nt["hospOnt"], weights['looksAfter'],prefixes_nt['xmlSchema'])
        toWrite += "<{}#LooksAfter/{}_{}> <{}#looksAfter1> <{}#HospitalizationUnit/{}>.\n".format(prefixes_nt["hospOnt"],hu,b.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],hu)
        toWrite += "<{}#LooksAfter/{}_{}> <{}#looksAfter2> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],hu,b.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],b.id)
    file.write(toWrite)
    file.close()


# Relation Building - Floor
def printRel_BuildingFloorRDF(dicBuildings):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['floor_building'], '.nt'), 'w')
    toWrite = ""
    for b in dicBuildings.values():
        for p in b.floors:
            toWrite += "<{}#PlacedIn/{}_{}> <{}#type> <{}#PlacedIn>.\n".format(prefixes_nt["hospOnt"],p.id,b.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],p.id,b.id, prefixes_nt["hospOnt"], weights['placedIn_FloorBuilding'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn1> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],p.id,b.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],p.id)
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn2> <{}#Building/{}>.\n".format(prefixes_nt["hospOnt"],p.id,b.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],b.id)
    file.write(toWrite)
    file.close()

# Relation Floor - Area
def printRel_FloorAreaRDF(dicFloors):
    fileç = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['area_floor'], '.nt'), 'w')
    toWrite = ""
    for p in dicFloors.values():
        for a in p.areas:
            toWrite += "<{}#PlacedIn/{}_{}> <{}#type> <{}#PlacedIn>.\n".format(prefixes_nt["hospOnt"],a.id,p.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],a.id,p.id, prefixes_nt["hospOnt"], weights['placedIn_AreaFloor'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn1> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],a.id,p.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.id)
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn2> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],a.id,p.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],p.id)
    fileç.write(toWrite)
    fileç.close()

# Relation Floor - Unit
def printRel_FloorUnitRDF(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['unit_floor'], '.nt'), 'w')
    toWrite = ""
    for p in dicFloors.values():
        for u in p.units:
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#type> <{}#PlacedInFloor>.\n".format(prefixes_nt["hospOnt"],u.id,p.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],u.id,p.id, prefixes_nt["hospOnt"], weights['placedInFloor_Unit'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#placedInFloor1> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],u.id,p.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],u.id)
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#placedInFloor2> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],u.id,p.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],p.id)
    file.write(toWrite)
    file.close()

# Relation Floor - Block
def printRel_FloorBlockRDF(dicFloors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['block_floor'], '.nt'), 'w')
    toWrite = ""
    for p in dicFloors.values():
        for b in p.blocks:
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#type> <{}#PlacedInFloor>.\n".format(prefixes_nt["hospOnt"],b.id,p.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],b.id,p.id, prefixes_nt["hospOnt"], weights['placedInFloor_Block'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#placedInFloor1> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],b.id,p.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],b.id)
            toWrite += "<{}#PlacedInFloor/{}_{}> <{}#placedInFloor2> <{}#Floor/{}>.\n".format(prefixes_nt["hospOnt"],b.id,p.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],p.id)
    file.write(toWrite)
    file.close()

# Relation Unit - Area
def printRel_UnitAreaRDF(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['area_unit'], '.nt'), 'w')
    toWrite = ""
    for a in dicAreas.values():
        toWrite += "<{}#PlacedInUnit/{}_{}> <{}#type> <{}#PlacedInUnit>.\n".format(prefixes_nt["hospOnt"],a.id,a.unit.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
        toWrite += "<{}#PlacedInUnit/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],a.id,a.unit.id, prefixes_nt["hospOnt"], weights['placedInUnit'],prefixes_nt['xmlSchema'])
        toWrite += "<{}#PlacedInUnit/{}_{}> <{}#placedInUnit1> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],a.id,a.unit.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.id)
        toWrite += "<{}#PlacedInUnit/{}_{}> <{}#placedInUnit2> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],a.id,a.unit.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.unit.id)
    file.write(toWrite)
    file.close()

# Relation Block - Area
def printRel_BlockAreaRDF(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['area_block'], '.nt'), 'w')
    toWrite = ""
    for a in dicAreas.values():
        toWrite += "<{}#PlacedInBlock/{}_{}> <{}#type> <{}#PlacedInBlock>.\n".format(prefixes_nt["hospOnt"],a.id,a.block.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
        toWrite += "<{}#PlacedInBlock/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],a.id,a.block.id, prefixes_nt["hospOnt"], weights['placedInBlock'],prefixes_nt['xmlSchema'])
        toWrite += "<{}#PlacedInBlock/{}_{}> <{}#placedInBlock1> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],a.id,a.block.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.id)
        toWrite += "<{}#PlacedInBlock/{}_{}> <{}#placedInBlock2> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],a.id,a.block.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.block.id)
    file.write(toWrite)
    file.close()

# Relation Area - Corridor
def printRel_AreaCorridorRDF(dicAreas):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['corridor_area'], '.nt'), 'w')
    toWrite = ""
    for a in dicAreas.values():
        for c in a.corridorsHoriz:
            toWrite += "<{}#PlacedIn/{}_{}> <{}#type> <{}#PlacedIn>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["hospOnt"], weights['placedIn_CorridorArea'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn1> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],c.id)
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn2> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.id)
        for c in a.corridorsVert:
            toWrite += "<{}#PlacedIn/{}_{}> <{}#type> <{}#PlacedIn>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["hospOnt"], weights['placedIn_CorridorArea'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn1> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],c.id)
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn2> <{}#Area/{}>.\n".format(prefixes_nt["hospOnt"],c.id,a.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],a.id)
    file.write(toWrite)
    file.close()

# Relation Corridor - Room
def printRel_CorridorRoomRDF(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['room_corridor'], '.nt'), 'w')
    toWrite = ""
    for c in dicCorridors.values():
        for r in c.rooms:
            toWrite += "<{}#PlacedIn/{}_{}> <{}#type> <{}#PlacedIn>.\n".format(prefixes_nt["hospOnt"],r.id,c.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],r.id,c.id, prefixes_nt["hospOnt"], weights['placedIn_RoomCorridor'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn1> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],r.id,c.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],r.id)
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn2> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],r.id,c.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],c.id)
    file.write(toWrite)
    file.close()

# Relation Room - Bed
def printRel_RoomBedRDF(dicRooms):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['bed_room'], '.nt'), 'w')
    toWrite = ""
    for r in dicRooms.values():
        for b in r.beds:
            toWrite += "<{}#PlacedIn/{}_{}> <{}#type> <{}#PlacedIn>.\n".format(prefixes_nt["hospOnt"],b,r.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],b,r.id, prefixes_nt["hospOnt"], weights['placedIn_SeatRoom'],prefixes_nt['xmlSchema'])
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn1> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],b,r.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],b)
            toWrite += "<{}#PlacedIn/{}_{}> <{}#placedIn2> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],b,r.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],r.id)
    file.write(toWrite)
    file.close()


# Relations Bed - Bed  //  Room - Room  (nextTo  //  opposite)
def printRel_BedRoom_NextToOppositeRDF(dictionary, nameFile, heading, nextOrOpposite):
    file = open(folderOutput_Relations_RDF + '{}'.format(nameFile), 'w')
    toWrite = ""
    
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

                if nextOrOpposite == "nextTo":
                    if 'Bed' in heading:
                        toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                        toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], weights['nextTo_Seat'],prefixes_nt['xmlSchema'])
                        toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],br.id)
                        toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],neighbor)

                    elif 'Room' in heading:
                        toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                        toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], weights['nextTo_Room'],prefixes_nt['xmlSchema'])
                        toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],br.id)
                        toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],neighbor)

                elif nextOrOpposite == "opposite":
                    if 'Bed' in heading:
                        toWrite += "<{}#Opposite/{}_{}> <{}#type> <{}#Opposite>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                        toWrite += "<{}#Opposite/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], weights['opposite_Seat'],prefixes_nt['xmlSchema'])
                        toWrite += "<{}#Opposite/{}_{}> <{}#opposite1> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],br.id)
                        toWrite += "<{}#Opposite/{}_{}> <{}#opposite2> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],neighbor)
                        
                    elif 'Room' in heading:
                        toWrite += "<{}#Opposite/{}_{}> <{}#type> <{}#Opposite>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                        toWrite += "<{}#Opposite/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], weights['opposite_Room'],prefixes_nt['xmlSchema'])
                        toWrite += "<{}#Opposite/{}_{}> <{}#opposite1> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],br.id)
                        toWrite += "<{}#Opposite/{}_{}> <{}#opposite2> <{}#Room/{}>.\n".format(prefixes_nt["hospOnt"],br.id,neighbor, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],neighbor)
                        
                keyPair2 = "{}-{}".format(br.id,neighbor)
                writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()


# Relation Corridor - Corridor (nextTo)
def printRel_Corridor_NextToRDF(dicCorridors):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['corridor_nt'], '.nt'), 'w')
    toWrite = ""
    
    writtenPairs = {}
    for p in dicCorridors.values():
        for neighbors in p.nextTo.values():
            if (neighbors is not None):
                keyPair1 = "{}-{}".format(neighbors,p.id)
                if keyPair1 not in writtenPairs:
                    toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],p.id,neighbors, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                    toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],p.id,neighbors, prefixes_nt["hospOnt"], weights['nextTo_Corridor'],prefixes_nt['xmlSchema'])
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],p.id,neighbors, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],p.id)
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Corridor/{}>.\n".format(prefixes_nt["hospOnt"],p.id,neighbors, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],neighbors)
                    
                    keyPair2 = "{}-{}".format(p.id,neighbors)
                    writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()    

# Relations Unit - Unit // Block - Block (nextTo)
def printRel_UnitBlock_NextToRDF(dictionary, nameFile, heading):
    file = open(folderOutput_Relations_RDF + '{}'.format(nameFile), 'w')
    toWrite = ""
    
    writtenPairs = {}
    for ub in dictionary.values():
        # Previous neighbor
        if ub.nextTo_prev is not None:
            keyPair1 = "{}-{}".format(ub.nextTo_prev,ub.id)
            if keyPair1 not in writtenPairs:
                if 'Unit' in heading:
                    toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                    toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["hospOnt"], weights['nextTo_Unit'],prefixes_nt['xmlSchema'])
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.id)
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.nextTo_prev)
                    
                elif 'Block' in heading:
                    toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                    toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["hospOnt"], weights['nextTo_Block'],prefixes_nt['xmlSchema'])
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.id)
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_prev, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.nextTo_prev)
                    
                keyPair2 = "{}-{}".format(ub.id,ub.nextTo_prev)
                writtenPairs[keyPair2] = 1
        # Next neighbor 
        if ub.nextTo_after is not None:
            keyPair1 = "{}-{}".format(ub.nextTo_after,ub.id)
            if keyPair1 not in writtenPairs:
                if 'Unit' in heading:
                    toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                    toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["hospOnt"], weights['nextTo_Unit'],prefixes_nt['xmlSchema'])
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.id)
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Unit/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.nextTo_after)
                    
                elif 'Block' in heading:
                    toWrite += "<{}#NextTo/{}_{}> <{}#type> <{}#NextTo>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                    toWrite += "<{}#NextTo/{}_{}> <{}#cost> \"{}\"^^<{}#float>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["hospOnt"], weights['nextTo_Block'],prefixes_nt['xmlSchema'])
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo1> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.id)
                    toWrite += "<{}#NextTo/{}_{}> <{}#nextTo2> <{}#Block/{}>.\n".format(prefixes_nt["hospOnt"],ub.id,ub.nextTo_after, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ub.nextTo_after)

                keyPair2 = "{}-{}".format(ub.id,ub.nextTo_after)
                writtenPairs[keyPair2] = 1
    file.write(toWrite)
    file.close()    



''''''''''''''''''
'''  PATIENTS  '''
''''''''''''''''''

def printPatientsRDF(dicPatients):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['patient'], '.nt'), 'w')
    toWrite = getToWritePatientsRDF(dicPatients)
    file.write(toWrite)
    file.close()

def getToWritePatientsRDF(dicPatients):
    toWrite = ""
    for p in dicPatients.values():
        toWrite += "<{}#Patient/{}> <{}#type> <{}#Patient>.\n".format(prefixes_nt['hospOnt'],p.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Patient/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], p.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Patient/{}> <{}#age> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], p.age,prefixes_nt['xmlSchema'])
        if p.sex:
            sex = 'M'
        else:
            sex = 'F'
        toWrite += "<{}#Patient/{}> <{}#sex> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],p.id, prefixes_nt["hospOnt"], sex,prefixes_nt['xmlSchema'])

    return toWrite


''''''''''''''''''''''''
'''  MICROORGANISM   '''
''''''''''''''''''''''''

def printMicroorganismsRDF(dicMicroorganisms):
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['microorganism'], '.nt'), 'w')
    toWrite = getToWriteMicroorganismsRDF(dicMicroorganisms)
    file.write(toWrite)
    file.close()

def getToWriteMicroorganismsRDF(dicMicroorganisms):
    toWrite = ""
    for m in dicMicroorganisms.values():
        toWrite += "<{}#Microorganism/{}> <{}#type> <{}#Microorganism>.\n".format(prefixes_nt['hospOnt'],m.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
        toWrite += "<{}#Microorganism/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],m.id, prefixes_nt["hospOnt"], m.id,prefixes_nt['xmlSchema'])
        toWrite += "<{}#Microorganism/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],m.id, prefixes_nt["hospOnt"], m.description,prefixes_nt['xmlSchema'])
    
    return toWrite



''''''''''''''''''''''''''''''
'''  EPISODES AND EVENTS   '''
''''''''''''''''''''''''''''''

###########
# CLASDES #
###########

# MAIN
def printClassesEpisodesEventsRDF(dicPatients):
    printEpisodesRDF(dicPatients)

    printEventsRDF(dicPatients, TypeEvent.Hospitalization, "{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['hospitalization'], '.nt'))
    printEventsRDF(dicPatients, TypeEvent.Radiology, "{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['radiology'], '.nt'))
    printEventsRDF(dicPatients, TypeEvent.Surgery, "{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['surgery'], '.nt'))
    printEventsRDF(dicPatients, TypeEvent.Death, "{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['death'], '.nt'))
    printEventsRDF(dicPatients, TypeEvent.TestMicro, "{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['testMicro'], '.nt'))


# Episodes
def printEpisodesRDF(dicPatients):    
    file = open("{}{}{}".format(folderOutput_Classes_RDF, nameFiles_Classes['episode'], '.nt'), 'w')
    toWrite = getToWriteEpisodesRDF(dicPatients)
    file.write(toWrite)
    file.close()

def getToWriteEpisodesRDF(dicPatients):
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            toWrite += "<{}#Episode/{}> <{}#type> <{}#Episode>.\n".format(prefixes_nt['hospOnt'],ep.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
            toWrite += "<{}#Episode/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],ep.id, prefixes_nt["hospOnt"], ep.id,prefixes_nt['xmlSchema'])
            toWrite += "<{}#Episode/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],ep.id, prefixes_nt["hospOnt"], ep.description,prefixes_nt['xmlSchema'])
            toWrite += "<{}#Episode/{}> <{}#start> \"{}\"^^<{}#dateTime>.\n".format(prefixes_nt["hospOnt"],ep.id, prefixes_nt["hospOnt"], ep.start.strftime("%Y-%m-%dT%H:%M:%S"),prefixes_nt['xmlSchema'])   # Formato: %Y-%m-%d %H:%M:%S  ->  2022-01-01 00:00:00
            toWrite += "<{}#Episode/{}> <{}#end> \"{}\"^^<{}#dateTime>.\n".format(prefixes_nt["hospOnt"],ep.id, prefixes_nt["hospOnt"], ep.end.strftime("%Y-%m-%dT%H:%M:%S"),prefixes_nt['xmlSchema'])
    
    return toWrite


# Events
def printEventsRDF(dicPatients, type, nameFile):    
    file = open(nameFile, 'w')
    toWrite = getToWriteEventosRDF(dicPatients, type)
    file.write(toWrite)
    file.close()

def getToWriteEventosRDF(dicPatients, type):
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.type is type:
                    toWrite += "<{}#{}/{}> <{}#type> <{}#Event>.\n".format(prefixes_nt['hospOnt'],ev.type.name,ev.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"])
                    toWrite += "<{}#{}/{}> <{}#type> <{}#{}>.\n".format(prefixes_nt['hospOnt'],ev.type.name,ev.id, prefixes_nt['rdf'], prefixes_nt["hospOnt"],ev.type.name)
                    toWrite += "<{}#{}/{}> <{}#id> \"{}\"^^<{}#integer>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], ev.id,prefixes_nt['xmlSchema'])
                    toWrite += "<{}#{}/{}> <{}#description> \"{}\"^^<{}#string>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], ev.description,prefixes_nt['xmlSchema'])
                    toWrite += "<{}#{}/{}> <{}#start> \"{}\"^^<{}#dateTime>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], ev.start.strftime("%Y-%m-%dT%H:%M:%S"),prefixes_nt['xmlSchema'])   # Formato: %Y-%m-%d %H:%M:%S  ->  2022-01-01 00:00:00
                    toWrite += "<{}#{}/{}> <{}#end> \"{}\"^^<{}#dateTime>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], ev.end.strftime("%Y-%m-%dT%H:%M:%S"),prefixes_nt['xmlSchema'])
    
    return toWrite


##############
# RELACIONES #
##############

# MAIN
def printRelationsEpisodesEventsRDF(dicPatients):
    printRel_EpisodePatientRDF(dicPatients)
    printRel_EventEpisodeRDF(dicPatients)
    printRel_EventBedRDF(dicPatients)
    printRel_EventHospUnitRDF(dicPatients)
    printRel_TestMicroorgRDF(dicPatients)


# Relation Episode-Patient
def printRel_EpisodePatientRDF(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['ep_pat'], '.nt'), 'w')
    toWrite = getToWriteRel_EpisodePatientRDF(dicPatients)
    file.write(toWrite)
    file.close()

def getToWriteRel_EpisodePatientRDF(dicPatients):
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            toWrite += "<{}#Episode/{}> <{}#episodeFromPatient> <{}#Patient/{}>.\n".format(prefixes_nt["hospOnt"],ep.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],patient.id)

    return toWrite


# Relation Event-Episode
def printRel_EventEpisodeRDF(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['ev_ep'], '.nt'), 'w')
    toWrite = getToWriteRel_EventEpisodeRDF(dicPatients)
    file.write(toWrite)
    file.close() 

def getToWriteRel_EventEpisodeRDF(dicPatients):
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                toWrite += "<{}#{}/{}> <{}#eventFromEpisode> <{}#Episode/{}>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ep.id)

    return toWrite


# Relation Event-Bed
def printRel_EventBedRDF(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['ev_bed'], '.nt'), 'w')
    toWrite = getToWriteRel_EventBedRDF(dicPatients)
    file.write(toWrite)
    file.close()    

def getToWriteRel_EventBedRDF(dicPatients):
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.location is not None:
                    toWrite += "<{}#{}/{}> <{}#hasLocation> <{}#Bed/{}>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ev.location)
    
    return toWrite


# Relation Event-HospUnit
def printRel_EventHospUnitRDF(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['ev_uh'], '.nt'), 'w')
    toWrite = getToWriteRel_EventHospUnitRDF(dicPatients)
    file.write(toWrite)
    file.close()    

def getToWriteRel_EventHospUnitRDF(dicPatients):
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.hospUnit is not None:
                    toWrite += "<{}#{}/{}> <{}#hasHospUnit> <{}#HospitalizationUnit/{}>.\n".format(prefixes_nt["hospOnt"],ev.type.name,ev.id, prefixes_nt["hospOnt"], prefixes_nt["hospOnt"],ev.hospUnit)
    
    return toWrite


# Relation TestMicro-Microorganism
def printRel_TestMicroorgRDF(dicPatients):
    file = open("{}{}{}".format(folderOutput_Relations_RDF, nameFiles_Rels['test_micro'], '.nt'), 'w')
    toWrite = ""
    for patient in dicPatients.values():
        for ep in patient.episodes:
            for ev in ep.events:
                if ev.type is TypeEvent.TestMicro:
                    microorg = ev.extra1
                    toWrite += "<{}#TestFoundMicroorg/{}_{}> <{}#type> <{}#TestFoundMicroorg>.\n".format(prefixes_nt["hospOnt"],ev.id,microorg.id, prefixes_nt["rdf"], prefixes_nt["hospOnt"])
                    if ev.extra2:
                        mmr = 1
                    else:
                        mmr = 0
                    toWrite += "<{}#TestFoundMicroorg/{}_{}> <{}#mmr> \"{}\"^^<{}#boolean>.\n".format(prefixes_nt["hospOnt"],ev.id,microorg.id, prefixes_nt["hospOnt"], mmr,prefixes_nt['xmlSchema'])
                    toWrite += "<{}#TestFoundMicroorg/{}_{}> <{}#hasFound1> <{}#TestMicro/{}>.\n".format(prefixes_nt["hospOnt"],ev.id,microorg.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],ev.id)
                    toWrite += "<{}#TestFoundMicroorg/{}_{}> <{}#hasFound2> <{}#Microorganism/{}>.\n".format(prefixes_nt["hospOnt"],ev.id,microorg.id, prefixes_nt["hospOnt"], prefixes_nt['hospOnt'],microorg.id)
    file.write(toWrite)
    file.close() 




