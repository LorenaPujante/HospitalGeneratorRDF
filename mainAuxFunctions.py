import math
from readInputParams import *


def setRooms_In_HospitalizationUnit(huPerService, dicServices, dicHospUnits, dicRooms, dicBeds):
    servsDelete = []
    for serv in dicServices.values():
        roomsService = serv.rooms
        if serv.abrev not in ['ER','ICU','RAD','SURG'] and len(roomsService) != 0:
            nRooms = len(roomsService)
            
            half = nRooms/huPerService
            halfCeil = math.ceil(half)
            halfFloor = math.floor(half)
            huPerServiceAux = huPerService
            if (half < 1):    
                print("\tEXCEPTION: All the Rooms from Service {} will be in the same Hospitalization Unit ({}) [it will be the only one in the service, with the exception of the Surgery Unit]".format(serv.abrev, dicHospUnits[serv.unidadesHosp[0]].abrev))
                huPerServiceAux = 1
                half = nRooms
                halfFloor = nRooms
                
                # Hospitalization Units that will not be used are eliminated.
                    # An aux list is created with the first UH
                listHUAux = [serv.hospUnits[0]]
                listHUToDelete = []
                for hu in serv.hospUnits:
                    if hu not in listHUAux:
                        listHUToDelete.append(hu)
                serv.hospUnits = listHUAux
                    # They are deleted from the dictionary
                for hu in listHUToDelete:
                    dicHospUnits.pop(hu)

            indInitRoom = 0
            indEndRoom = halfFloor
            for j in range(0,huPerServiceAux):
                    # The first HospUnit will be associated with the Rooms that may be left over 
                if (j==0 and halfCeil!=halfFloor):
                    remain = nRooms%huPerService
                    indEndRoom += remain

                idHospUnit = serv.hospUnits[j]
                # The HospUnit is connected to its Rooms    
                for i in range(indInitRoom,indEndRoom):
                    idRoom = roomsService[i]
                    dicRooms[idRoom].hospUnit = idHospUnit
                    dicHospUnits[idHospUnit].rooms.append(idRoom)

                    # The HospUnit is connected to the Beds of the Room
                    for idBed in dicRooms[idRoom].beds:
                        dicBeds[idBed].hospUnit = idHospUnit
                        par = (idHospUnit, idBed)  

                indInitRoom = indEndRoom
                indEndRoom = indEndRoom + halfFloor

        elif len(roomsService) == 0:    # The Service and its HospUnits are deleted
            servsDelete.append(serv.id)
            for hu in serv.hospUnits:
                dicHospUnits.pop(hu)

    for sId in servsDelete:
        dicServices.pop(sId)        


def setNumFloorsToCreate(n_floor, n_huPerFloor, n_ord_hu, option):
    n_ord_floors = n_floor-1     # -(Floor with [ICUU, ERU, RadU, Surgerys])
    b = int(n_ord_hu/n_huPerFloor)
    remain = n_ord_hu%n_huPerFloor
    if (n_ord_floors != b):
        print("\tEXCEPTION: A configuration with {} Ord Floors, {} Ord HospUnits and {} hospUnits per Floor cannot be created".format(n_ord_floors, n_ord_hu, n_huPerFloor))
        if (n_ord_hu/n_ord_floors >= 1):
            if option is None:
                option = readChangeFloorsOrHUPerFloor(n_floor, n_ord_floors, n_ord_hu, n_huPerFloor, b)
            if option == 1:
                n_floor = b+1
                print("\tEXCEPTION: The number of Floor has been changed to: {}".format(n_floor))
            else:
                n_huPerFloor = int(n_ord_hu/n_ord_floors)
                remain = n_ord_hu%n_huPerFloor
                print("\tEXCEPTION: The number of Ord HospUnits per Ord Floor has been changed to: {}".format(n_huPerFloor))
        else:
            n_floor = b+1
            print("\tEXCEPTION: The number of Floor has been changed to: {}".format(n_floor))
    print("\tINFO: Nº Ord HospUnits ({}) per Ord Floor ({}): {} (remain: {})".format(n_ord_hu, n_floor-1, n_ord_hu/(n_floor-1), remain))

    return n_floor, remain, n_huPerFloor

    
def appendDictionarys(dicAux, dicRes):
    for key,value in dicAux.items():
        dicRes[key] = value    



