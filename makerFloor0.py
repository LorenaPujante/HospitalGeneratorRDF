from classes import *
from alphabets import *
from makerRoomsBeds import setBeds


###############################################################
#  All Functions related to the creation of FLOOR 0 are here  #
###############################################################


################################
# UNIDADES Y SERVICIOS VANILLA #
################################

def createServicesAndHospUnits_Vanilla(index):
    dicServices = {}
    dicHospUnits = {}

    # ER
    s = Service(index, "Emergency Service", "ER")
    dicServices[s.id] = s
    index += 1
    u = HospUnit(index, "Emergency Unit", "ERU")
    u.service = s
    dicHospUnits[u.id] = u
    index += 1
    s.hospUnits.append(u.id)

    # ICU
    s = Service(index, "Intensive Care Unit Service", "ICU")
    dicServices[s.id] = s
    index += 1
    u = HospUnit(index, "Intensive Care Unit", "ICUU")
    u.service = s
    dicHospUnits[u.id] = u
    index += 1
    s.hospUnits.append(u.id)
    
    # RAD
    s = Service(index, "Radiology Service", "RAD")
    dicServices[s.id] = s
    index += 1
    u = HospUnit(index, "Radiology Unit", "RADU")
    u.service = s
    dicHospUnits[u.id] = u
    index += 1
    s.hospUnits.append(u.id)

    # SURG
    s = Service(index, "Surgery Service", "SURG")
    dicServices[s.id] = s
    index += 1
    u = HospUnit(index, "Surgery Unit", "SURGU")
    u.service = s
    dicHospUnits[u.id] = u
    index += 1
    s.hospUnits.append(u.id)

    return dicServices, dicHospUnits, index



#############
#  FLOOR 0  #
#############

def createFloor0(index, dicBuildings, dicHospUnits, dicRooms, dicBeds):
    dicFloors = {}
    floor = Floor(index, "f0")
    index += 1
    dicFloors[floor.id] = floor

    # Assign HUs [ERU, ICUU, RADU, SURGU]
    for hu in dicHospUnits.values():
        if hu.abrev in ["ERU", "ICUU", "RADU", "SURGU"]:
            floor.hospUnits.append(hu)
    
    # Create Units and Blocks  -> 2 Columns (Blocks) y 1 Rows (Unit)
    dicUnits, dicBlocks, index = createUnitsBlocks_f0(floor, index)
        
    # Create Areas   ->  A0 y A1
    dicAreas, index = createAreas_f0(floor, index)

    # Create Corridors    -> An horizontal Corridor per Area
    dicCorridors, index = createCorridors_f0(floor, index)
        
    # Add Rooms
    listRooms = setRooms_f0(floor, dicRooms, dicHospUnits)

    # Set description and Beds neighbors
    setBeds(listRooms, dicBeds)

    # Add Floor to the Building
    idBuild = list(dicBuildings.keys())[0]   # We can do this because there is only one Building
    dicBuildings[idBuild].floors.append(floor)

    return dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, index


def createUnitsBlocks_f0(floor, index):    # 2 Columns (Blocks) y 1 Rows (Unit)
    dicUnits = {}
    unit = Unit(index,abcCap[0])
    dicUnits[unit.id] = unit
    floor.units.append(unit)
    index += 1

    dicBlocks = {}
    for i in range(2):
        block = Block(index, i)
        dicBlocks[block.id] = block
        floor.blocks.append(block)
        index += 1

        # Neighbors
        if i==1:
            block.nextTo_prev = block.id-1
            dicBlocks[block.id-1].nextTo_after = block.id

    return dicUnits, dicBlocks, index

def createAreas_f0(floor, index):     # A0 y A1
    dicAreas = {}
    for i in range(2):
        unit = floor.units[0]
        block = floor.blocks[i]
        description = 'a{}{}_{}'.format(i,unit.description,floor.description)
        area = Area(index, description, "")
        area.unit = unit
        area.block = block
        
        index += 1
        dicAreas[area.id] = area
        floor.areas.append(area)

    return dicAreas, index

def createCorridors_f0(floor, index):   # An horizontal Corridor per Area
    dicCorridors = {}
    for area in floor.areas:
        description = 'c0_{}'.format(area.description)
        corridor = Corridor(index, description)
        
        index += 1
        dicCorridors[corridor.id] = corridor
        area.corridorsHoriz.append(corridor)

        # They are neighbors
    area0 = floor.areas[0]
    area1 = floor.areas[1]
    area0.corridorsHoriz[0].nextTo[1] = area1.corridorsHoriz[0].id
    area1.corridorsHoriz[0].nextTo[0] = area0.corridorsHoriz[0].id

    return dicCorridors, index

def setRooms_f0(floor, dicRooms, dicHospUnits):
    area0 = floor.areas[0]
    area1 = floor.areas[1]
    corr0 = area0.corridorsHoriz[0]
    corr1 = area1.corridorsHoriz[0]
    listRooms = []
    roomEr = None 
    roomIcu = None
    roomsRad = []
    roomsSurg = []
    for hu in dicHospUnits.values():
        if hu.abrev == "ERU":
            roomEr = dicRooms[hu.rooms[0]]
            desc = "rER_{}".format(corr0.description)
            roomEr.description = desc
            
            roomEr.parent = corr0.id
            corr0.rooms.append(roomEr)
            corr0.roomsBorder['leftBottom'] = roomEr
            corr0.roomsBorder['rightBottom'] = roomEr

            listRooms.append(roomEr)
        
        elif hu.abrev == "ICUU":
            roomIcu = dicRooms[hu.rooms[0]]
            desc = "rICU_{}".format(corr0.description)
            roomIcu.description = desc
            
            roomIcu.parent = corr0.id
            corr0.rooms.append(roomIcu)
            corr0.roomsBorder['leftTop'] = roomIcu
            corr0.roomsBorder['rightTop'] = roomIcu

            listRooms.append(roomIcu)

        elif hu.abrev == "RADU":
            for i in range(len(hu.rooms)):
                roomId = hu.rooms[i]
                roomRad = dicRooms[roomId]
                desc = "rRAD{}_{}".format(i,corr1.description)
                roomRad.description = desc
                
                roomRad.parent = corr1.id
                listRooms.append(roomRad)
                roomsRad.append(roomRad)

                if i==0:
                    corr1.roomsBorder['leftBottom'] = roomRad
                elif i==len(hu.rooms)-1:
                    corr1.roomsBorder['rightBottom'] = roomRad
            for r in roomsRad:
                corr1.rooms.append(r)

        elif hu.abrev == "SURGU":
            for i in range(len(hu.rooms)):
                roomId = hu.rooms[i]
                roomSurg = dicRooms[roomId]
                desc = "rSURG{}_{}".format(i,corr1.description)
                roomSurg.description = desc
                
                roomSurg.parent = corr1.id
                listRooms.append(roomSurg)
                roomsSurg.append(roomSurg)

                if i==0:
                    corr1.roomsBorder['leftTop'] = roomSurg
                elif i==len(hu.rooms)-1:
                    corr1.roomsBorder['rightTop'] = roomSurg
            for r in roomsSurg:
                corr1.rooms.append(r)

    # Neighbors
    setNeighborsRooms_p0(roomIcu, roomEr, roomsSurg, roomsRad)
    
    return listRooms


def setNeighborsRooms_p0(roomIcu, roomEr, roomsSurg, roomsRad):
    roomIcu.opposite.append(roomEr.id)
    roomEr.opposite.append(roomIcu.id)

    roomIcu.nextTo.append(roomsSurg[0].id)
    roomsSurg[0].nextTo.append(roomIcu.id)
    roomEr.nextTo.append(roomsRad[0].id)
    roomsRad[0].nextTo.append(roomEr.id)

    for i in range(len(roomsSurg)-1):
        roomsSurg[i].nextTo.append(roomsSurg[i+1].id)
        roomsSurg[i+1].nextTo.append(roomsSurg[i].id)
    for i in range(len(roomsRad)-1):
        roomsRad[i].nextTo.append(roomsRad[i+1].id)
        roomsRad[i+1].nextTo.append(roomsRad[i].id)

    if len(roomsSurg) > len(roomsRad):
        for i in range(len(roomsRad)):
            roomsRad[i].opposite.append(roomsSurg[i].id)
            roomsSurg[i].opposite.append(roomsRad[i].id)
    else:
        for i in range(len(roomsSurg)):
            roomsSurg[i].opposite.append(roomsRad[i].id)
            roomsRad[i].opposite.append(roomsSurg[i].id)