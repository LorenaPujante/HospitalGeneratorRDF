from classes import *


    ##############################################
    #  FUNCIONES PRINCICPALES PARA AÑADIR ROOMS  #
    ##############################################
def setRooms(nRows, nColumns, gridAreas, listRooms, dicCorridors):
    indRooms = 0
    for i in range(nRows):
        for j in range(nColumns):
            area = gridAreas[i][j]    

            match area.type:
                case "A0":
                    listRoomsRes, indRooms = setRoomsToListRooms(7, listRooms, indRooms)
                    setRooms_A0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "A1":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_A1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "A2":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_A2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "A3":
                    listRoomsRes, indRooms = setRoomsToListRooms(11, listRooms, indRooms)
                    setRooms_A3(listRooms, area.corridorsHoriz, area.corridorsVert)
                
                case "B0":
                    listRoomsRes, indRooms = setRoomsToListRooms(7, listRooms, indRooms)
                    setRooms_B0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "B1":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_B1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "B2":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_B2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "B3":
                    listRoomsRes, indRooms = setRoomsToListRooms(11, listRooms, indRooms)
                    setRooms_B3(listRooms, area.corridorsHoriz, area.corridorsVert)
                
                case "C0":
                    listRoomsRes, indRooms = setRoomsToListRooms(7, listRooms, indRooms)
                    setRooms_C0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "C1":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_C1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "C2":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_C2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "C3":
                    listRoomsRes, indRooms = setRoomsToListRooms(11, listRooms, indRooms)
                    setRooms_C3(listRooms, area.corridorsHoriz, area.corridorsVert)

                case "D0":
                    listRoomsRes, indRooms = setRoomsToListRooms(7, listRooms, indRooms)
                    setRooms_D0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "D1":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_D1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "D2":
                    listRoomsRes, indRooms = setRoomsToListRooms(9, listRooms, indRooms)
                    setRooms_D2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "D3":
                    listRoomsRes, indRooms = setRoomsToListRooms(11, listRooms, indRooms)
                    setRooms_D3(listRooms, area.corridorsHoriz, area.corridorsVert)
                
                case "E0":
                    listRoomsRes, indRooms = setRoomsToListRooms(10, listRooms, indRooms)
                    setRooms_E0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E1":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_E1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E2":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_E2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E3":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_E3(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E4":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_E4(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E5":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_E5(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E6":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_E6(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "E7":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_E7(listRooms, area.corridorsHoriz, area.corridorsVert)

                case "F0":
                    listRoomsRes, indRooms = setRoomsToListRooms(10, listRooms, indRooms)
                    setRooms_F0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F1":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_F1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F2":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_F2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F3":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_F3(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F4":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_F4(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F5":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_F5(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F6":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_F6(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "F7":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_F7(listRooms, area.corridorsHoriz, area.corridorsVert)

                case "G0":
                    listRoomsRes, indRooms = setRoomsToListRooms(10, listRooms, indRooms)
                    setRooms_G0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G1":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_G1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G2":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_G2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G3":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_G3(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G4":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_G4(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G5":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_G5(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G6":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_G6(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "G7":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_G7(listRooms, area.corridorsHoriz, area.corridorsVert)

                case "H0":
                    listRoomsRes, indRooms = setRoomsToListRooms(10, listRooms, indRooms)
                    setRooms_H0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H1":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_H1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H2":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_H2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H3":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_H3(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H4":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_H4(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H5":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_H5(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H6":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_H6(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "H7":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_H7(listRooms, area.corridorsHoriz, area.corridorsVert)

                case "I0":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_I0(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I1":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_I1(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I2":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_I2(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I3":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_I3(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I4":
                    listRoomsRes, indRooms = setRoomsToListRooms(14, listRooms, indRooms)
                    setRooms_I4(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I5":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_I5(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I6":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_I6(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I7":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_I7(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I8":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_I8(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I9":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_I9(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I10":
                    listRoomsRes, indRooms = setRoomsToListRooms(16, listRooms, indRooms)
                    setRooms_I10(listRooms, area.corridorsHoriz, area.corridorsVert)
                case "I11":
                    listRoomsRes, indRooms = setRoomsToListRooms(20, listRooms, indRooms)
                    setRooms_I11(listRooms, area.corridorsHoriz, area.corridorsVert)

                case "J0":
                    listRoomsRes, indRooms = setRoomsToListRooms(8, listRooms, indRooms)
                    setRooms_J0(listRooms, area.corridorsHoriz)
                case "J1":
                    listRoomsRes, indRooms = setRoomsToListRooms(10, listRooms, indRooms)
                    setRooms_J1(listRooms, area.corridorsHoriz)
                case "J2":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_J2(listRooms, area.corridorsHoriz)

                case "K0":
                    listRoomsRes, indRooms = setRoomsToListRooms(8, listRooms, indRooms)
                    setRooms_K0(listRooms, area.corridorsVert)
                case "K1":
                    listRoomsRes, indRooms = setRoomsToListRooms(10, listRooms, indRooms)
                    setRooms_K1(listRooms, area.corridorsVert)
                case "K2":
                    listRoomsRes, indRooms = setRoomsToListRooms(12, listRooms, indRooms)
                    setRooms_K2(listRooms, area.corridorsVert)
               
def setRoomsToListRooms(nRoomsType, listRooms, indRooms):
    listRoomsResult = []
    for k in range(indRooms,indRooms+nRoomsType):
        listRoomsResult.append(listRooms[k])
    indRooms += nRoomsType

    return listRoomsResult, indRooms            


def setExternalNeighbors(nRows, nColumns, gridAreas, dicCorridors):
    for i in range(nRows):
        for j in range(nColumns):
            area = gridAreas[i][j]    

            match area.type[0]:
                case "A":
                    setNextTo_extern_A(area, dicCorridors)
                case "B":
                    setNextTo_extern_B(area, dicCorridors)
                case "C":
                    setNextTo_extern_C(area, dicCorridors)
                case "D":
                    setNextTo_extern_D(area, dicCorridors)
                case "E":
                    setNextTo_extern_E(area, dicCorridors)
                case "F":
                    setNextTo_extern_F(area, dicCorridors)
                case "G":
                    setNextTo_extern_G(area, dicCorridors)
                case "H":
                    setNextTo_extern_H(area, dicCorridors)
                case "I":
                    setNextTo_extern_I(area, dicCorridors)
                case "J":
                    setNextTo_extern_J(area, dicCorridors)
                case "K":
                    setNextTo_extern_K(area, dicCorridors)
 

 
    ####################
    #  ROOMS POR TIPO  #
    ####################

###################
#  A - B - C - D  #
###################
def insertRooms_ABCD_0(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(4,7):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_ABCD_1(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(4,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_ABCD_2(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_ABCD_3(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)


def setOppositeTo_AC_0(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[5].opposite.append(listRooms[6].id)
    listRooms[6].opposite.append(listRooms[5].id)

def setOppositeTo_BD_0(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)

def setOppositeTo_AC_12(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[5].opposite.append(listRooms[6].id)
    listRooms[6].opposite.append(listRooms[5].id)
    listRooms[7].opposite.append(listRooms[8].id)
    listRooms[8].opposite.append(listRooms[7].id)

def setOppositeTo_BD_12(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)

def setOppositeTo_AC_3(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[7].opposite.append(listRooms[8].id)
    listRooms[8].opposite.append(listRooms[7].id)
    listRooms[9].opposite.append(listRooms[10].id)
    listRooms[10].opposite.append(listRooms[9].id)

def setOppositeTo_BD_3(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[10].id)    


def setNextTo_intern_BC_0(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)

def setNextTo_intern_BC_1(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)

def setNextTo_intern_BC_2(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)

def setNextTo_intern_BC_3(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)


#######
#  A  #
#######
def setRooms_A0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_0(listRooms, corridorsHoriz, corridorsVert)
    
    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[5]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[6]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_AC_0(listRooms)

    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[4].id)

def setRooms_A1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_1(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[7]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[8]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_AC_12(listRooms)

    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)

def setRooms_A2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_2(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[7]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[8]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_AC_12(listRooms)

    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[6].id)

def setRooms_A3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_3(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[9]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[10]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_AC_3(listRooms)

    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)


#######
#  B  #
#######
def setRooms_B0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_0(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_BD_0(listRooms)

    # Internal neighbours
    setNextTo_intern_BC_0(listRooms)

def setRooms_B1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_1(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_BD_12(listRooms)

    # Internal neighbours
    setNextTo_intern_BC_1(listRooms)

def setRooms_B2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_2(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_BD_12(listRooms)

    # Internal neighbours
    setNextTo_intern_BC_2(listRooms)

def setRooms_B3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_3(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_BD_3(listRooms)

    # Internal neighbours
    setNextTo_intern_BC_3(listRooms)


#######
#  C  #
#######
def setRooms_C0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_0(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[5]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[6]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_AC_0(listRooms)

    # Internal neighbours
    setNextTo_intern_BC_0(listRooms)

def setRooms_C1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_1(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[7]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[8]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_AC_12(listRooms)

    # Internal neighbours
    setNextTo_intern_BC_1(listRooms)

def setRooms_C2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_2(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[7]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[8]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_AC_12(listRooms)
    
    # Internal neighbours
    setNextTo_intern_BC_2(listRooms)

def setRooms_C3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_3(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[9]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[10]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_AC_3(listRooms)
    
    # Internal neighbours
    setNextTo_intern_BC_3(listRooms)


#######
#  D  #
#######
def setRooms_D0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_0(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_BD_0(listRooms)

    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[5].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[5].id)

def setRooms_D1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_1(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_BD_12(listRooms)
    
    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[7].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[7].id)

def setRooms_D2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_2(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_BD_12(listRooms)
    
    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[8].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[8].id)

def setRooms_D3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_ABCD_3(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_BD_3(listRooms)
    
    # Internal neighbours
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    listRooms[9].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[9].id)


###########
#  E - F  #
###########

def insertRooms_EF_0(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(4,7):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(7,10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_1(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(4,7):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(7,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_2(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(4,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(9,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_3(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(9,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_4(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(9,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_5(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_6(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(4,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(9,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_EF_7(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)


def setOppositeTo_EF_0(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)

def setOppositeTo_EF_1(listRooms):
    setOppositeTo_EF_0(listRooms)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)

def setOppositeTo_EF_23(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)

def setOppositeTo_EF_46(listRooms):
    setOppositeTo_EF_23(listRooms)
    listRooms[12].opposite.append(listRooms[13].id)
    listRooms[13].opposite.append(listRooms[12].id)

def setOppositeTo_EF_5(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)
    listRooms[12].opposite.append(listRooms[13].id)
    listRooms[13].opposite.append(listRooms[12].id)

def setOppositeTo_EF_7(listRooms):
    setOppositeTo_EF_5(listRooms)
    listRooms[14].opposite.append(listRooms[15].id)
    listRooms[15].opposite.append(listRooms[14].id)


def setNextTo_intern_EF_0(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[6].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[7].id)

def setNextTo_intern_EF_1(listRooms):
    setNextTo_intern_EF_0(listRooms)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)

def setNextTo_intern_EF_2(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[8].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[9].id)

def setNextTo_intern_EF_3(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[8].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[9].id)

def setNextTo_intern_EF_4(listRooms):
    setNextTo_intern_EF_3(listRooms)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id) 

def setNextTo_intern_EF_5(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[10].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[11].id)

def setNextTo_intern_EF_6(listRooms):
    setNextTo_intern_EF_2(listRooms)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_EF_7(listRooms):
    setNextTo_intern_EF_5(listRooms)
    listRooms[12].nextTo.append(listRooms[14].id)
    listRooms[14].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)


#######
#  E  #
#######
def setRooms_E0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_0(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[8]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_EF_0(listRooms)

    # vecinos interiores
    setNextTo_intern_EF_0(listRooms)

def setRooms_E1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_1(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_EF_1(listRooms)

    # vecinos interiores
    setNextTo_intern_EF_1(listRooms)

def setRooms_E2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_2(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_EF_23(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_2(listRooms)

def setRooms_E3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_3(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_EF_23(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_3(listRooms)

def setRooms_E4(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_4(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_EF_46(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_4(listRooms)   

def setRooms_E5(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_5(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_EF_5(listRooms)    

    # Internal neighbours
    setNextTo_intern_EF_5(listRooms)

def setRooms_E6(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_6(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[2]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[3]

    # Opposite
    setOppositeTo_EF_46(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_6(listRooms)

def setRooms_E7(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_7(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[5]

    # Opposite
    setOppositeTo_EF_7(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_7(listRooms)


#######
#  F  #
#######
def setRooms_F0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_0(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[8]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_0(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_0(listRooms)

def setRooms_F1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_1(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_1(listRooms)
    
    # Internal neighbours
    setNextTo_intern_EF_1(listRooms)

def setRooms_F2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_2(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_23(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_2(listRooms)

def setRooms_F3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_3(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_23(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_3(listRooms)

def setRooms_F4(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_4(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_46(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_4(listRooms)

def setRooms_F5(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_5(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_5(listRooms)    

    # Internal neighbours
    setNextTo_intern_EF_5(listRooms)    

def setRooms_F6(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_6(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[4]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[5]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_46(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_6(listRooms)

def setRooms_F7(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_EF_7(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]

    # Opposite
    setOppositeTo_EF_7(listRooms)

    # Internal neighbours
    setNextTo_intern_EF_7(listRooms)


###########
#  G - H  #
###########

def insertRooms_GH_0(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(3):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(3,6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_GH_1(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(3):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(3,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)
    
def insertRooms_GH_2(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(5):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(5,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_GH_3(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(3):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(3,6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_GH_4(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(3):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(3,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_GH_5(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(5):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(5,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_GH_6(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(5):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(5,10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(10,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

def insertRooms_GH_7(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(5):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(5,10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(10,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)


def setOppositeTo_GH_0(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)

def setOppositeTo_GH_13(listRooms):
    setOppositeTo_GH_0(listRooms)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)
    
def setOppositeTo_GH_2(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)

def setOppositeTo_GH_456(listRooms):
    setOppositeTo_GH_13(listRooms)
    listRooms[12].opposite.append(listRooms[13].id)
    listRooms[13].opposite.append(listRooms[12].id)    

def setOppositeTo_GH_7(listRooms):
    setOppositeTo_GH_456(listRooms)
    listRooms[14].opposite.append(listRooms[15].id)
    listRooms[15].opposite.append(listRooms[14].id) 


def setNextTo_intern_GH_0(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[2].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[3].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)

def setNextTo_intern_GH_1(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[2].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[3].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)

def setNextTo_intern_GH_2(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[4].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[5].id)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)

def setNextTo_intern_GH_3(listRooms):
    setNextTo_intern_GH_0(listRooms)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)

def setNextTo_intern_GH_4(listRooms):
    setNextTo_intern_GH_1(listRooms)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_GH_5(listRooms):
    setNextTo_intern_GH_2(listRooms)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_GH_6(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[4].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[5].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_GH_7(listRooms):
    setNextTo_intern_GH_6(listRooms)
    listRooms[12].nextTo.append(listRooms[14].id)
    listRooms[14].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)


#######
#  G  #
#######
def setRooms_G0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_0(listRooms, corridorsHoriz, corridorsVert)            

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5]    
    
    # Opposite
    setOppositeTo_GH_0(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_0(listRooms)

def setRooms_G1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_1(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_13(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_1(listRooms)

def setRooms_G2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_2(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_2(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_2(listRooms)

def setRooms_G3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_3(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_13(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_3(listRooms)

def setRooms_G4(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_4(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_456(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_4(listRooms)

def setRooms_G5(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_5(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_456(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_5(listRooms)

def setRooms_G6(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_6(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[13]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[9]    
 
    # Opposite
    setOppositeTo_GH_456(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_6(listRooms)

def setRooms_G7(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_7(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[15]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[9]    
 
    # Opposite
    setOppositeTo_GH_7(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_7(listRooms)


#######
#  H  #
#######
def setRooms_H0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_0(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5]    
 
    # Opposite
    setOppositeTo_GH_0(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_0(listRooms)

def setRooms_H1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_1(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_13(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_1(listRooms)

def setRooms_H2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_2(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_2(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_2(listRooms)

def setRooms_H3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_3(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5]    
 
    # Opposite
    setOppositeTo_GH_13(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_3(listRooms)

def setRooms_H4(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_4(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_456(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_4(listRooms)

def setRooms_H5(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_5(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7]    
 
    # Opposite
    setOppositeTo_GH_456(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_5(listRooms)

def setRooms_H6(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_6(listRooms, corridorsHoriz, corridorsVert)        

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[9]    
 
    # Opposite
    setOppositeTo_GH_456(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_6(listRooms)

def setRooms_H7(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_GH_7(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[11]
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[9]    
 
    # Opposite
    setOppositeTo_GH_7(listRooms)

    # Internal neighbours
    setNextTo_intern_GH_7(listRooms)


###########
#  J - K  #
###########
def insertRooms_JK_0(listRooms, corridors):
    p = corridors[0]
    for i in range(8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,p.description)
        r.description = desc
        r.parent = p.id
        p.rooms.append(r)    

def insertRooms_JK_1(listRooms, corridors):
    p = corridors[0]
    for i in range(10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,p.description)
        r.description = desc
        r.parent = p.id
        p.rooms.append(r)

def insertRooms_JK_2(listRooms, corridors):
    p = corridors[0]
    for i in range(12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,p.description)
        r.description = desc
        r.parent = p.id
        p.rooms.append(r)         


def setOppositeTo_JK_0(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)

def setOppositeTo_JK_1(listRooms):
    setOppositeTo_JK_0(listRooms)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)
        
def setOppositeTo_JK_2(listRooms):
    setOppositeTo_JK_1(listRooms)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)


def setNextTo_intern_JK_0(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)

def setNextTo_intern_JK_1(listRooms):
    setNextTo_intern_JK_0(listRooms)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)    

def setNextTo_intern_JK_2(listRooms):
    setNextTo_intern_JK_1(listRooms)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)


#######
#  J  #
#######
def setRooms_J0(listRooms, corridorsHoriz):
    insertRooms_JK_0(listRooms, corridorsHoriz)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[0]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[1]
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_JK_0(listRooms)

    # Internal neighbours
    setNextTo_intern_JK_0(listRooms)

def setRooms_J1(listRooms, corridorsHoriz):
    insertRooms_JK_1(listRooms, corridorsHoriz)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[0]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[1]
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[9] 
 
    # Opposite
    setOppositeTo_JK_1(listRooms)
    
    # Internal neighbours
    setNextTo_intern_JK_1(listRooms)

def setRooms_J2(listRooms, corridorsHoriz):
    insertRooms_JK_2(listRooms, corridorsHoriz)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[0]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[1]
    corridorsHoriz[0].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['rightBottom'] = listRooms[11] 
 
    # Opposite
    setOppositeTo_JK_2(listRooms)
    
    # Internal neighbours
    setNextTo_intern_JK_2(listRooms)


#######
#  K  #
#######
def setRooms_K0(listRooms, corridorsVert):
    insertRooms_JK_0(listRooms, corridorsVert)

    # Border rooms
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_JK_0(listRooms)
    
    # Internal neighbours
    setNextTo_intern_JK_0(listRooms)
    
def setRooms_K1(listRooms, corridorsVert):
    insertRooms_JK_1(listRooms, corridorsVert)

    # Border rooms
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[9] 
 
    # Opposite
    setOppositeTo_JK_1(listRooms)
    
    # Internal neighbours
    setNextTo_intern_JK_1(listRooms)
    
def setRooms_K2(listRooms, corridorsVert):
    insertRooms_JK_2(listRooms, corridorsVert)

    # Border rooms
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[0].roomsBorder['bottomLeft'] = listRooms[10]
    corridorsVert[0].roomsBorder['bottomRight'] = listRooms[11] 
 
    # Opposite
    setOppositeTo_JK_2(listRooms)
    
    # Internal neighbours
    setNextTo_intern_JK_2(listRooms)
    

#######
#  I  #
#######

def setRooms_I0(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I0(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[10]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[11] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5] 
 
    # Opposite
    setOppositeTo_I0(listRooms)
    
    # Internal neighbours
    setNextTo_intern_I0(listRooms)

def setRooms_I1(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I1(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5] 
 
    # Opposite
    setOppositeTo_I1(listRooms)

    # Internal neighbours
    setNextTo_intern_I1(listRooms)

def setRooms_I2(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I2(listRooms, corridorsHoriz, corridorsVert)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5] 
 
    # Opposite
    setOppositeTo_I234(listRooms)

    # Internal neighbours
    setNextTo_intern_I2(listRooms)

def setRooms_I3(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I3(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_I234(listRooms)

    # Internal neighbours
    setNextTo_intern_I3(listRooms)

def setRooms_I4(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I4(listRooms, corridorsHoriz, corridorsVert)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[12]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[13] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_I234(listRooms)

    # Internal neighbours
    setNextTo_intern_I4(listRooms)

def setRooms_I5(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I5(listRooms, corridorsHoriz, corridorsVert)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_I579(listRooms)

    # Internal neighbours
    setNextTo_intern_I4(listRooms)    

def setRooms_I6(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I6(listRooms, corridorsHoriz, corridorsVert)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_I6810(listRooms)

    # Internal neighbours
    setNextTo_intern_I6(listRooms)

def setRooms_I7(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I7(listRooms, corridorsHoriz, corridorsVert)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_I579(listRooms)

    # Internal neighbours
    setNextTo_intern_I7(listRooms)

def setRooms_I8(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I8(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[8]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[9]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[6]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[7] 
 
    # Opposite
    setOppositeTo_I6810(listRooms)

    # Internal neighbours
    setNextTo_intern_I8(listRooms)

def setRooms_I9(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I9(listRooms, corridorsHoriz, corridorsVert)    

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[6]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[7]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[4]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[5] 
 
    # Opposite
    setOppositeTo_I579(listRooms)

    # Internal neighbours
    setNextTo_intern_I9(listRooms)

def setRooms_I10(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I10(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[11]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[14]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[15] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[9] 
 
    # Opposite
    setOppositeTo_I6810(listRooms)

    # Internal neighbours
    setNextTo_intern_I10(listRooms)

def setRooms_I11(listRooms, corridorsHoriz, corridorsVert):
    insertRooms_I11(listRooms, corridorsHoriz, corridorsVert)

    # Border rooms
    corridorsHoriz[0].roomsBorder['leftTop'] = listRooms[10]
    corridorsHoriz[0].roomsBorder['leftBottom'] = listRooms[11]
    corridorsHoriz[1].roomsBorder['rightTop'] = listRooms[18]
    corridorsHoriz[1].roomsBorder['rightBottom'] = listRooms[19] 
    corridorsVert[0].roomsBorder['topLeft'] = listRooms[0]
    corridorsVert[0].roomsBorder['topRight'] = listRooms[1]
    corridorsVert[1].roomsBorder['bottomLeft'] = listRooms[8]
    corridorsVert[1].roomsBorder['bottomRight'] = listRooms[9] 
 
    # Opposite
    setOppositeTo_I11(listRooms)

    # Internal neighbours
    setNextTo_intern_I11(listRooms)


def insertRooms_I0(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(9,12):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I1(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,9):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(9,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I2(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I3(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I4(listRooms, corridorsHoriz, corridorsVert):        
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(6,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,14):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I5(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I6(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,13):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(13,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I7(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(6,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I8(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(6,8):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(8,13):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(13,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I9(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(4):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(4,6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(6,11):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(11,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)

def insertRooms_I10(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(6,10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(10,13):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(13,16):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)
        
def insertRooms_I11(listRooms, corridorsHoriz, corridorsVert):
    cV0 = corridorsVert[0] 
    for i in range(6):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV0.description)
        r.description = desc
        r.parent = cV0.id
        cV0.rooms.append(r)

    cV1 = corridorsVert[1]
    for i in range(6,10):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cV1.description)
        r.description = desc
        r.parent = cV1.id
        cV1.rooms.append(r)

    cH0 = corridorsHoriz[0]
    for i in range(10,15):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH0.description)
        r.description = desc
        r.parent = cH0.id
        cH0.rooms.append(r)

    cH1 = corridorsHoriz[1]
    for i in range(15,20):
        r = listRooms[i]
        desc = "r{}_{}".format(i,cH1.description)
        r.description = desc
        r.parent = cH1.id
        cH1.rooms.append(r)      


def setOppositeTo_I0(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)

def setOppositeTo_I1(listRooms):
    setOppositeTo_I0(listRooms)
    listRooms[12].opposite.append(listRooms[13].id)
    listRooms[13].opposite.append(listRooms[12].id)

def setOppositeTo_I234(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)
    listRooms[12].opposite.append(listRooms[13].id)
    listRooms[13].opposite.append(listRooms[12].id)

def setOppositeTo_I579(listRooms):
    setOppositeTo_I234(listRooms)
    listRooms[14].opposite.append(listRooms[15].id)
    listRooms[15].opposite.append(listRooms[14].id)

def setOppositeTo_I6810(listRooms):
    listRooms[0].opposite.append(listRooms[1].id)
    listRooms[1].opposite.append(listRooms[0].id)
    listRooms[2].opposite.append(listRooms[3].id)
    listRooms[3].opposite.append(listRooms[2].id)
    listRooms[4].opposite.append(listRooms[5].id)
    listRooms[5].opposite.append(listRooms[4].id)
    listRooms[6].opposite.append(listRooms[7].id)
    listRooms[7].opposite.append(listRooms[6].id)
    listRooms[8].opposite.append(listRooms[9].id)
    listRooms[9].opposite.append(listRooms[8].id)
    listRooms[10].opposite.append(listRooms[11].id)
    listRooms[11].opposite.append(listRooms[10].id)
    listRooms[14].opposite.append(listRooms[15].id)
    listRooms[15].opposite.append(listRooms[14].id)

def setOppositeTo_I11(listRooms):
    setOppositeTo_I6810(listRooms)
    listRooms[12].opposite.append(listRooms[13].id)
    listRooms[13].opposite.append(listRooms[12].id)
    listRooms[16].opposite.append(listRooms[17].id)
    listRooms[17].opposite.append(listRooms[16].id)
    listRooms[18].opposite.append(listRooms[19].id)
    listRooms[19].opposite.append(listRooms[18].id)


def setNextTo_intern_I0(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[8].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[8].id)

def setNextTo_intern_I1(listRooms):
    setNextTo_intern_I0(listRooms)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_I2(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    listRooms[9].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[9].id)
    listRooms[10].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_I3(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[9].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[9].id)
    listRooms[10].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_I4(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[3].id)
    listRooms[9].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[9].id)
    listRooms[10].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)

def setNextTo_intern_I5(listRooms):
    setNextTo_intern_I3(listRooms)
    listRooms[12].nextTo.append(listRooms[14].id)
    listRooms[14].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[12].id)

def setNextTo_intern_I6(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[4].nextTo.append(listRooms[6].id)
    listRooms[6].nextTo.append(listRooms[4].id)
    listRooms[5].nextTo.append(listRooms[7].id)
    listRooms[7].nextTo.append(listRooms[5].id)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)
    listRooms[11].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[11].id)
    listRooms[12].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)

def setNextTo_intern_I7(listRooms):
    setNextTo_intern_I4(listRooms)
    listRooms[12].nextTo.append(listRooms[14].id)
    listRooms[14].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)

def setNextTo_intern_I8(listRooms):
    setNextTo_intern_common_I81011(listRooms)
    listRooms[8].nextTo.append(listRooms[10].id)
    listRooms[10].nextTo.append(listRooms[8].id)
    listRooms[9].nextTo.append(listRooms[11].id)
    listRooms[11].nextTo.append(listRooms[9].id)
    listRooms[11].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[11].id)
    listRooms[12].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)

def setNextTo_intern_I9(listRooms):
    setNextTo_intern_I2(listRooms)
    listRooms[12].nextTo.append(listRooms[14].id)
    listRooms[14].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)

def setNextTo_intern_I10(listRooms):
    setNextTo_intern_common_I1011(listRooms)
    listRooms[11].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[11].id)
    listRooms[12].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[12].id)
    listRooms[13].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[13].id)

def setNextTo_intern_I11(listRooms):
    setNextTo_intern_common_I1011(listRooms)
    listRooms[10].nextTo.append(listRooms[12].id)
    listRooms[12].nextTo.append(listRooms[10].id)
    listRooms[11].nextTo.append(listRooms[13].id)
    listRooms[13].nextTo.append(listRooms[11].id)
    listRooms[13].nextTo.append(listRooms[14].id)
    listRooms[14].nextTo.append(listRooms[13].id)
    listRooms[14].nextTo.append(listRooms[15].id)
    listRooms[15].nextTo.append(listRooms[14].id)
    listRooms[15].nextTo.append(listRooms[17].id)
    listRooms[17].nextTo.append(listRooms[15].id)
    listRooms[16].nextTo.append(listRooms[18].id)
    listRooms[18].nextTo.append(listRooms[16].id)
    listRooms[17].nextTo.append(listRooms[19].id)
    listRooms[19].nextTo.append(listRooms[17].id)

def setNextTo_intern_common_I81011(listRooms):
    listRooms[0].nextTo.append(listRooms[2].id)
    listRooms[2].nextTo.append(listRooms[0].id)
    listRooms[1].nextTo.append(listRooms[3].id)
    listRooms[3].nextTo.append(listRooms[1].id)
    listRooms[2].nextTo.append(listRooms[4].id)
    listRooms[4].nextTo.append(listRooms[2].id)
    listRooms[3].nextTo.append(listRooms[5].id)
    listRooms[5].nextTo.append(listRooms[3].id)

def setNextTo_intern_common_I1011(listRooms):
    setNextTo_intern_common_I81011(listRooms)
    listRooms[6].nextTo.append(listRooms[8].id)
    listRooms[8].nextTo.append(listRooms[6].id)
    listRooms[7].nextTo.append(listRooms[9].id)
    listRooms[9].nextTo.append(listRooms[7].id)
    


    ########################
    #  VECINOS EXTERIORES  #
    ########################

def setNextTo_extern_A(area, dicCorridors):
    # Horizontal Corridor
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[1] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[1]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['leftTop']
        cH0.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['leftBottom']
        cH0.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[1] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[1]]
            # Top 
        nextRoom = cV0_nextTo.roomsBorder['topLeft']
        cV0.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cV0_nextTo.roomsBorder['topRight']
        cV0.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)

def setNextTo_extern_B(area, dicCorridors):
    # Horizontal Corridor
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[0] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[1] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[1]]
            # Top 
        nextRoom = cV0_nextTo.roomsBorder['topLeft']
        cV0.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cV0_nextTo.roomsBorder['topRight']
        cV0.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)    

def setNextTo_extern_C(area, dicCorridors):
    # Horizontal Corridor
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[1] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[1]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['leftTop']
        cH0.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['leftBottom']
        cH0.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[0] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[0]]
            # Top 
        nextRoom = cV0_nextTo.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cV0_nextTo.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)

def setNextTo_extern_D(area, dicCorridors):
    # Horizontal Corridor
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[0] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id) 

    # Vertical Corridor
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[0] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[0]]
            # Top 
        nextRoom = cV0_nextTo.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cV0_nextTo.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)


def setNextTo_extern_E(area, dicCorridors):
    # Horizontal Corridor - Left
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[0] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id)

    # Horizontal Corridor - Right
    cH1 = area.corridorsHoriz[1]
    if cH1.nextTo[1] != None:
        cH1_nextTo = dicCorridors[cH1.nextTo[1]]
            # Top 
        nextRoom = cH1_nextTo.roomsBorder['leftTop']
        cH1.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH1_nextTo.roomsBorder['leftBottom']
        cH1.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[1] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[1]]
            # Top 
        nextRoom = cV0_nextTo.roomsBorder['topLeft']
        cV0.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cV0_nextTo.roomsBorder['topRight']
        cV0.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)

def setNextTo_extern_F(area, dicCorridors):
    # Horizontal Corridor - Left
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[0] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id)

    # Horizontal Corridor - Right
    cH1 = area.corridorsHoriz[1]
    if cH1.nextTo[1] != None:
        cH1_nextTo = dicCorridors[cH1.nextTo[1]]
            # Top 
        nextRoom = cH1_nextTo.roomsBorder['leftTop']
        cH1.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH1_nextTo.roomsBorder['leftBottom']
        cH1.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[0] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[0]]
            # Top 
        nextRoom = cV0_nextTo.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cV0_nextTo.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)

def setNextTo_extern_G(area, dicCorridors):
    # Horizontal Corridor
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[1] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[1]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['leftTop']
        cH0.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['leftBottom']
        cH0.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor - Top
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[0] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[0]]
            # Left 
        nextRoom = cV0_nextTo.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV0_nextTo.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)

    # Vertical Corridor - Bottom
    cV1 = area.corridorsVert[1]
    if cV1.nextTo[1] != None:
        cV1_nextTo = dicCorridors[cV1.nextTo[1]]
            # Left 
        nextRoom = cV1_nextTo.roomsBorder['topLeft']
        cV1.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV1_nextTo.roomsBorder['topRight']
        cV1.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)

def setNextTo_extern_H(area, dicCorridors):
    # Horizontal Corridor
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[0] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor - Top
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[0] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[0]]
            # Left 
        nextRoom = cV0_nextTo.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV0_nextTo.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)

    # Vertical Corridor - Bottom
    cV1 = area.corridorsVert[1]
    if cV1.nextTo[1] != None:
        cV1_nextTo = dicCorridors[cV1.nextTo[1]]
            # Left 
        nextRoom = cV1_nextTo.roomsBorder['topLeft']
        cV1.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV1_nextTo.roomsBorder['topRight']
        cV1.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)


def setNextTo_extern_I(area, dicCorridors):
    # Horizontal Corridor - Left
    cH0 = area.corridorsHoriz[0]
    if cH0.nextTo[0] != None:
        cH0_nextTo = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id)

    # Horizontal Corridor - Right
    cH1 = area.corridorsHoriz[1]
    if cH1.nextTo[1] != None:
        cH1_nextTo = dicCorridors[cH1.nextTo[1]]
            # Top 
        nextRoom = cH1_nextTo.roomsBorder['leftTop']
        cH1.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH1_nextTo.roomsBorder['leftBottom']
        cH1.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

    # Vertical Corridor - Top
    cV0 = area.corridorsVert[0]
    if cV0.nextTo[0] != None:
        cV0_nextTo = dicCorridors[cV0.nextTo[0]]
            # Left 
        nextRoom = cV0_nextTo.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV0_nextTo.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)

    # Vertical Corridor - Bottom
    cV1 = area.corridorsVert[1]
    if cV1.nextTo[1] != None:
        cV1_nextTo = dicCorridors[cV1.nextTo[1]]
            # Left 
        nextRoom = cV1_nextTo.roomsBorder['topLeft']
        cV1.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV1_nextTo.roomsBorder['topRight']
        cV1.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)


def setNextTo_extern_J(area, dicCorridors):
    
    cH0 = area.corridorsHoriz[0]
    
    # Left
    if cH0.nextTo[0] != None:
        cH0_nextTo_left = dicCorridors[cH0.nextTo[0]]
            # Top 
        nextRoom = cH0_nextTo_left.roomsBorder['rightTop']
        cH0.roomsBorder['leftTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo_left.roomsBorder['rightBottom']
        cH0.roomsBorder['leftBottom'].nextTo.append(nextRoom.id)

    # Right
    if cH0.nextTo[1] != None:
        cH0_nextTo_der = dicCorridors[cH0.nextTo[1]]
            # Top     
        nextRoom = cH0_nextTo_der.roomsBorder['leftTop']
        cH0.roomsBorder['rightTop'].nextTo.append(nextRoom.id)
            # Bottom
        nextRoom = cH0_nextTo_der.roomsBorder['leftBottom']
        cH0.roomsBorder['rightBottom'].nextTo.append(nextRoom.id)

def setNextTo_extern_K(area, dicCorridors):
    
    cV0 = area.corridorsVert[0]

    # Top
    if cV0.nextTo[0] != None:
        cV0_nextTo_Top = dicCorridors[cV0.nextTo[0]]
            # Left 
        nextRoom = cV0_nextTo_Top.roomsBorder['bottomLeft']
        cV0.roomsBorder['topLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV0_nextTo_Top.roomsBorder['bottomRight']
        cV0.roomsBorder['topRight'].nextTo.append(nextRoom.id)    

    # Bottom
    if cV0.nextTo[1] != None:
        cV0_nextTo_Bottom = dicCorridors[cV0.nextTo[1]]
            # Left 
        nextRoom = cV0_nextTo_Bottom.roomsBorder['topLeft']
        cV0.roomsBorder['bottomLeft'].nextTo.append(nextRoom.id)
            # Right
        nextRoom = cV0_nextTo_Bottom.roomsBorder['topRight']
        cV0.roomsBorder['bottomRight'].nextTo.append(nextRoom.id)



    ##################
    # FUNCTIONS BEDS #
    ##################

def setBeds(listRooms, dicBeds):
    for room in listRooms:
        nBeds = len(room.beds)
        if nBeds==1:
            bed = dicBeds[room.beds[0]]
            bed.description = "b{}_{}".format(0,room.description)

        elif nBeds<=3:  
            for i in range(nBeds):
                bed = dicBeds[room.beds[i]]
                bed.description = "b{}_{}".format(i,room.description)

                if i<nBeds-1:
                    bed.nextTo.append(dicBeds[room.beds[i+1]].id)   # If there are 2 or 3 Beds, they are placed next to each other          B0-B1-B2
                    dicBeds[room.beds[i+1]].nextTo.append(bed.id)

        elif nBeds>3:
            for i in range(nBeds):
                bed = dicBeds[room.beds[i]]
                bed.description = "b{}_{}".format(i,room.description)

                if i<nBeds-2:                                           # If there are more than 3 Beds, they are placed like this:     B0-B2-B4 ... B(n-2)
                    bed.nextTo.append(dicBeds[room.beds[i+2]].id)       #                                                               B1-B3-B5 ... B(n-1)       
                    dicBeds[room.beds[i+2]].nextTo.append(bed.id)
                if i<nBeds-1 and i%2==0:
                    bed.opposite.append(dicBeds[room.beds[i+1]].id)
                    dicBeds[room.beds[i+1]].opposite.append(bed.id)



