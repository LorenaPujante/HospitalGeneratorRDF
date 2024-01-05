import traceback
from readInputParams import *

from classes import *
from makerFloorsLayout import generateAreas
from makerAreasCorridors import *
from makerRoomsBeds import *


# Functions
def setNumFloorsToCreate_test(n_floors, n_huPerFloor, n_ord_HU):
    n_ord_floors = n_floors-1     # -(Floor with [ICUU, ERU, RadU, Surgerys])
    b = int(n_ord_HU/n_huPerFloor)
    remain = n_ord_HU%n_huPerFloor
    if (n_ord_floors != b):
        n_floors = b+1
        print("\tEXCEPTION: The number of Floors have been changed to: {}".format(n_floors))
    print("Nº Ord HospUnits ({}) per Ord Floor ({}): {} (remain: {})".format(n_ord_HU, b, n_ord_HU/b, remain))

    return n_floors, remain

def setFloorsToBuilding(building, dicFloors):
    for v in dicFloors.values():
        building.floors.append(v)

def getOrd_HU(dicHospUnits):
    listOrd_HU = []
    for uh in dicHospUnits.values():
        if uh.abrev not in ['ERU', 'ICUU', 'RADU', 'SURGU']:
            listOrd_HU.append(uh)

    return listOrd_HU

def appendDictionarys(dicAux, dicRes):
    for key,value in dicAux.items():
        dicRes[key] = value



############
# BUILDING #
############
def createBuilding(index):
    dicBuildings = {}
    
    building = Building(index, "Main Building")
    index += 1
    dicBuildings[building.id] = building


    return dicBuildings, index



##########
# FLOORS #
##########
def createOrdFloors(n_ord_floors, n_huPerFloor, remainHU, listOrd_HU, index, dicBuildings):
    dicFloors = {}
    
    indHU_init = 0
    indHU_end = indHU_init+n_huPerFloor
    for i in range(n_ord_floors):
        floor = Floor(index,'f{}'.format(i+1))
        
        index += 1
        dicFloors[floor.id] = floor

        # Assign its HospUnits
        if (i == 0):
            indHU_end += remainHU 

        for j in range(indHU_init,indHU_end):
            floor.hospUnits.append(listOrd_HU[j])
        indHU_init = indHU_end
        indHU_end += n_huPerFloor

        # Calculate how many rooms it will have
        countNRoomsOrdFloor(floor)

        # Add Floor to the Building
        idBuild = list(dicBuildings.keys())[0]   # We can do it because there is only a Building
        dicBuildings[idBuild].floors.append(floor)

    return dicFloors, index


def populateOrdFloors(dicFloors, nRows, nColumns, dicBuildings, dicRooms, dicBeds, index):
    dicUnits = {}
    dicBlocks = {}
    dicAreas = {}
    dicCorridors = {}

    for floor in dicFloors.values():
        if (floor.description != "p0"):
            dicUnitsAux, dicBlocksAux, dicAreasAux, dicCorridorsAux, index = populateOrdFloor(floor, nRows, nColumns, dicBuildings, dicRooms, dicBeds, index)

            appendDictionarys(dicUnitsAux, dicUnits)
            appendDictionarys(dicBlocksAux, dicBlocks)
            appendDictionarys(dicAreasAux, dicAreas)
            appendDictionarys(dicCorridorsAux, dicCorridors)

    return dicUnits, dicBlocks, dicAreas, dicCorridors, index

def populateOrdFloor(floor, nRows, nColumns, dicBuildings, dicRooms, dicBeds, index):
    try:
        # Set the layout of the Floor
        print("\tINFO: Floor {} - nRooms: {}".format(floor.description, floor.nRooms))
        print("\tINFO: Searching for a layout for the Floor")
        gridRes, nColumns, nRows = generateAreas(floor.nRooms, nColumns, nRows)
        print("\tINFO: Floor {} has: \n\t - {} Columns \n\t - {} Rows".format(floor.description, nColumns, nRows))

        # Create Units and Blocks
        dicUnits, index = createUnits(nRows,index,floor)
        dicBlocks, index = createBlocks(nColumns,index,floor)
        
        # Create Areas
        dicAreas, gridAreas, index = createAreas(gridRes, nRows, nColumns, index, floor, dicUnits, dicBlocks)    
        
        # Create Corridors
        dicCorridors, index = createCorridors(gridAreas, nRows, nColumns, index)
        
        # Assign Rooms
        listRooms = getRoomsOrdFloor(floor, dicRooms)
        setRooms(nRows, nColumns, gridAreas, listRooms, dicCorridors)
        setExternalNeighbors(nRows, nColumns, gridAreas, dicCorridors)
        
        # Assign Beds
        setBeds(listRooms, dicBeds)
        
        # Update Floor in dicBuildings
        idBuild = list(dicBuildings.keys())[0]   # We can do it because there is only one Building
        i = 0
        found = False
        while i<len(dicBuildings[idBuild].floors)  and  not found:
            if dicBuildings[idBuild].floors[i].id == floor.id:
                found = True
            else:
                i += 1
        if found:
            dicBuildings[idBuild].floors[i] = floor
        else:
            dicBuildings[idBuild].floors.append(floor)
        
    except Exception as e:
        typeException = type(e).__name__
        if typeException in [InsufficientParamsError.__name__, ReadIndexError.__name__, ReadHUPerServiceError.__name__, ReadNumFloorsError.__name__, ReadHUPerFloorError.__name__, ReadNumRowsColumnsError.__name__, ReadOptionChangeFloorsOrHuPerFloorError.__name__, WrongDateTimeFormatError.__name__]:
            print(e.args[0])
        else:
            print(traceback.format_exc())

        exit(1)

    return dicUnits, dicBlocks, dicAreas, dicCorridors, index


def countNRoomsOrdFloor(floor):
    nRoomsFloor = 0
    for uh in floor.hospUnits:
        nRoomsFloor += len(uh.rooms)
    floor.nRooms = nRoomsFloor

def getRoomsOrdFloor(floor, dicRooms):
    listRooms = []
    for uh in floor.hospUnits:
        for id in uh.rooms:
            listRooms.append(dicRooms[id])
    
    return listRooms


