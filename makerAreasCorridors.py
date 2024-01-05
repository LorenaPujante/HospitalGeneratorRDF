from classes import *
from alphabets import *

def createUnits(nRows, index, planta):
    dicUnits = {}

    for i in range(nRows):
        unitName = abcCap[i]
        modUnits = i//len(abcCap)
        for k in range(modUnits):
            unitName += abcCap[i]

        unit = Unit(index,unitName)
        dicUnits[unit.id] = unit
        planta.units.append(unit)

        index += 1

    # Neighbors
    for key,unit in dicUnits.items():
        prev_key = key-1
        if prev_key in dicUnits:
            unit.nextTo_prev = prev_key
        next_key = key+1
        if next_key in dicUnits:
            unit.nextTo_after = next_key

    return dicUnits, index


def createBlocks(nColumns, index, planta):
    dicBlocks = {}

    for i in range(nColumns):
        block = Block(index,i)
        dicBlocks[block.id] = block
        planta.blocks.append(block)
        
        index += 1

    # Neighbors
    for key,block in dicBlocks.items():
        prev_key = key-1
        if prev_key in dicBlocks:
            block.nextTo_prev = prev_key
        next_key = key+1
        if next_key in dicBlocks:
            block.nextTo_after = next_key

    return dicBlocks, index


def createAreas(grid, nRows, nColumns, index, floor, dicUnits, dicBlocks):
    dicAreas = {}
    gridAreas = []

    keysUnits = list(dicUnits.keys())
    keysBlocks = list(dicBlocks.keys())

    for i in range(nRows):
        unit = dicUnits[keysUnits[i]]
        unitName = unit.description
        row = []

        for j in range(nColumns):
            block = dicBlocks[keysBlocks[j]]

            description = 'a{}{}_{}'.format(j,unitName,floor.description)
            area = Area(index, description, grid[i][j])
            area.unit = unit
            area.block = block
            
            index += 1
            dicAreas[area.id] = area

            row.append(area)
            floor.areas.append(area)            

        gridAreas.append(row)
        
    return dicAreas, gridAreas, index


def createCorridors(gridAreas, nRows, nColumns, index):
    dicCorridors, index = defineCorridors(gridAreas, nRows, nColumns, index)
        
    setExternalNeighbors_Corridor(gridAreas, nRows, nColumns)
    setInternalNeighbor_Corridor(gridAreas, nRows, nColumns)

    return dicCorridors, index


def defineCorridors(gridAreas, nRows, nColumns, index):
    
    dicCorridors = {}
    
    for i in range(nRows):
        for j in range(nColumns):
            area = gridAreas[i][j]

            # 1 Corridor
            if area.type in ['J0','J1','J2',
                            'K0','K1','K2']:
                for k in range(1):
                    description = 'c{}_{}'.format(k,area.description)
                    corridor = Corridor(index, description)
                    index += 1
                    
                    if (area.type.startswith("J")):
                        area.corridorsHoriz.append(corridor)
                    else:
                        area.corridorsVert.append(corridor)

                    dicCorridors[corridor.id] = corridor    

            # 2 Corridors    
            elif area.type in ['A0','A1','A2','A3',
                                'B0','B1','B2','B3',
                                'C0','C1','C2','C3',
                                'D0','D1','D2','D3']:
                for k in range(2):
                    description = 'c{}_{}'.format(k,area.description)
                    corridor = Corridor(index, description)
                    index += 1
                    
                    if k==0:
                        area.corridorsHoriz.append(corridor)
                    else:
                        area.corridorsVert.append(corridor)

                    dicCorridors[corridor.id] = corridor

            # 3 Corridors    
            elif area.type in ['E0','E1','E2','E3','E4','E5','E6','E7',
                                'F0','F1','F2','F3','F4','F5','F6','F7',
                                'G0','G1','G2','G3','G4','G5','G6','G7',
                                'H0','H1','H2','H3','H4','H5','H6','H7',]:
                for k in range(3):
                    description = 'c{}_{}'.format(k,area.description)
                    corridor = Corridor(index, description)
                    index += 1

                    if (area.type.startswith("E") or area.type.startswith("F")):
                        if k<2:
                            area.corridorsHoriz.append(corridor)
                        else:
                            area.corridorsVert.append(corridor)
                    else:
                        if k<2:
                            area.corridorsVert.append(corridor)
                        else:
                            area.corridorsHoriz.append(corridor)

                    dicCorridors[corridor.id] = corridor
                            
            # 4 Corridors
            elif area.type in ['I0','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11']:
                for k in range(4):
                    description = 'c{}_{}'.format(k,area.description)
                    corridor = Corridor(index, description)
                    index += 1

                    if k<2:
                        area.corridorsHoriz.append(corridor)
                    else:
                        area.corridorsVert.append(corridor)

                    dicCorridors[corridor.id] = corridor
    
    return dicCorridors, index


def setExternalNeighbors_Corridor(gridAreas, nRows, nColumns):
    for i in range(nRows):
        for j in range(nColumns):
            area = gridAreas[i][j]
            
            # Corner Top-right:
            if i==0 and j==0:
                if nColumns>1:
                    rightNeighbor_Corridor(area, gridAreas, i, j)
                if nRows>1: 
                    BottomNeighbor_Corridor(area, gridAreas, i, j)
            
            # Corner Top-Right:
            elif i==0 and j==nColumns-1:
                if nColumns>1:
                    leftNeighbor_Coridor(area, gridAreas, i, j)
                if nRows>1: 
                    BottomNeighbor_Corridor(area, gridAreas, i, j)
            
            # Corner Bottom-Left:
            elif i==nRows-1 and j==0:
                if nColumns>1:
                    rightNeighbor_Corridor(area, gridAreas, i, j)
                if nRows>1: 
                    topNeighbor_Corridor(area, gridAreas, i, j)
                
            # Corner Bottom-Right:
            elif i==nRows-1 and j==nColumns-1:
                if nColumns>1:
                    leftNeighbor_Coridor(area, gridAreas, i, j)
                if nRows>1: 
                    topNeighbor_Corridor(area, gridAreas, i, j)
                
            # Top Horizontal:
            elif i==0:
                leftNeighbor_Coridor(area, gridAreas, i, j)
                rightNeighbor_Corridor(area, gridAreas, i, j)
                if len(area.corridorsVert)>0: 
                    BottomNeighbor_Corridor(area, gridAreas, i, j)

            # Bottom Horizontal:
            elif i==nRows-1:
                leftNeighbor_Coridor(area, gridAreas, i, j)
                rightNeighbor_Corridor(area, gridAreas, i, j)
                if len(area.corridorsVert)>0: 
                    topNeighbor_Corridor(area, gridAreas, i, j)
                
            # Vertical Left:
            elif j==0:
                if len(area.corridorsHoriz)>0:
                    rightNeighbor_Corridor(area, gridAreas, i, j)
                topNeighbor_Corridor(area, gridAreas, i, j)
                BottomNeighbor_Corridor(area, gridAreas, i, j)

            # Vertical Right:
            elif j==nColumns-1:
                # External corridors
                if len(area.corridorsHoriz)>0:
                    leftNeighbor_Coridor(area, gridAreas, i, j)
                topNeighbor_Corridor(area, gridAreas, i, j)
                BottomNeighbor_Corridor(area, gridAreas, i, j)

            # Center:
            else:
                leftNeighbor_Coridor(area, gridAreas, i, j)
                rightNeighbor_Corridor(area, gridAreas, i, j)
                if len(area.corridorsVert)>0:
                    if area.type.startsWith('F') or area.type.startsWith('I'):
                        topNeighbor_Corridor(area, gridAreas, i, j)
                    if area.type.startsWith('E') or area.type.startsWith('I'):
                        BottomNeighbor_Corridor(area, gridAreas, i, j)


def setInternalNeighbor_Corridor(gridAreas, nRows, nColumns):
    for i in range(nRows):
        for j in range(nColumns):
            area = gridAreas[i][j]
            type = area.type[0]
            
            if type in ['A','B','C','D']:
                internalNeighbors_ABCD_Corridor(area,type)

            elif type in ['E','F']:
                internalNeighbors_EF_Corridor(area,type)

            elif type in ['G','H']:
                internalNeighbors_GH_Corridor(area,type)

            elif type in ['I']:
                internalNeighbors_I_Corridor(area)

            
def leftNeighbor_Coridor(area, gridAreas, i, j):
    area.corridorsHoriz[0].nextTo[0] = gridAreas[i][j-1].corridorsHoriz[len(gridAreas[i][j-1].corridorsHoriz)-1].id

def rightNeighbor_Corridor(area, gridAreas, i, j):
    area.corridorsHoriz[len(area.corridorsHoriz)-1].nextTo[1] = gridAreas[i][j+1].corridorsHoriz[0].id

def topNeighbor_Corridor(area, gridAreas, i, j):
    area.corridorsVert[0].nextTo[0] = gridAreas[i-1][j].corridorsVert[len(gridAreas[i-1][j].corridorsVert)-1].id

def BottomNeighbor_Corridor(area, gridAreas, i, j):
    area.corridorsVert[len(area.corridorsVert)-1].nextTo[1] = gridAreas[i+1][j].corridorsVert[0].id


def internalNeighbors_ABCD_Corridor(area, type):
    cHoriz = area.corridorsHoriz[0]
    cVert = area.corridorsVert[0]
    
    if (type == 'A'):
        cHoriz.nextTo[4] = cVert.id
        cVert.nextTo[4] = cHoriz.id 

    elif (type == 'B'):
        cHoriz.nextTo[5] = cVert.id
        cVert.nextTo[2] = cHoriz.id

    elif (type == 'C'):
        cHoriz.nextTo[2] = cVert.id
        cVert.nextTo[5] = cHoriz.id

    else:
        cHoriz.nextTo[3] = cVert.id
        cVert.nextTo[3] = cHoriz.id

def internalNeighbors_EF_Corridor(area, type):
    cLeft = area.corridorsHoriz[0]
    cRight = area.corridorsHoriz[1]
    cVert = area.corridorsVert[0]
    
    cLeft.nextTo[1] = cRight.id    
    if (type == 'E'):
        cLeft.nextTo[5] = cVert.id
    else:
        cLeft.nextTo[3] = cVert.id

    cRight.nextTo[0] = cLeft.id
    if (type == 'E'):
        cRight.nextTo[4] = cVert.id
    else:
        cRight.nextTo[2] = cVert.id
   
    if (type == 'E'):
        cVert.nextTo[2] = cLeft.id
        cVert.nextTo[4] = cRight.id
    else:
        cVert.nextTo[3] = cLeft.id
        cVert.nextTo[5] = cRight.id

def internalNeighbors_GH_Corridor(area,type):
    cHoriz = area.corridorsHoriz[0]
    cSup = area.corridorsVert[0]
    cInf = area.corridorsVert[1]
    
    if (type == 'G'):
        cHoriz.nextTo[2] = cSup.id
        cHoriz.nextTo[4] = cInf.id
    else:
        cHoriz.nextTo[3] = cSup.id
        cHoriz.nextTo[5] = cInf.id

    cSup.nextTo[1] = cInf.id
    if (type == 'G'):
        cSup.nextTo[5] = cHoriz.id
    else:
        cSup.nextTo[3] = cHoriz.id
    
    cInf.nextTo[0] = cSup.id
    if (type == 'G'):
        cInf.nextTo[4] = cHoriz.id
    else:
        cInf.nextTo[2] = cHoriz.id
    
def internalNeighbors_I_Corridor(area):
    cLeft = area.corridorsHoriz[0]
    cRight = area.corridorsHoriz[1]
    cSup = area.corridorsVert[0]
    cInf = area.corridorsVert[1]
    
    cLeft.nextTo[1] = cRight.id
    cLeft.nextTo[3] = cSup.id
    cLeft.nextTo[5] = cInf.id

    cRight.nextTo[0] = cLeft.id
    cRight.nextTo[2] = cSup.id
    cRight.nextTo[4] = cInf.id

    cSup.nextTo[1] = cInf.id
    cSup.nextTo[3] = cLeft.id
    cSup.nextTo[5] = cRight.id

    cInf.nextTo[0] = cSup.id
    cInf.nextTo[2] = cLeft.id
    cInf.nextTo[4] = cRight.id














