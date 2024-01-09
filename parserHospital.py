from classes import *
from alphabets import *


def parseHospital(dicHospUnits, dicServices, huPerService, index):

    # Results
    dicRooms = {}
    dicBeds = {}

    # Control parameters
    parent = False
    children = False
    neighbours = False
    nService = 0   # For the name of the new Services
    currentId = -1
    currentType = -1
    
    listHospUnitsIds = list(dicHospUnits.keys())
    listServicesIds = list(dicServices.keys())

    '''Open hospital.txt'''
    with open(".\\Input\\hospital.txt") as file:
        for line in file:
            
            line = str(line)

            # Read file with input hospital layout 
            if (not parent and not children and not neighbours):
                if (line == "children\n"):
                    children = True
                elif (line == "neighbours\n"):
                    neighbours = True  
                elif (line == "parent\n"):
                    parent = True
                else:
                    line = line.split('\n')
                    line = line[0]
                    words = line.split(",")
                    id = int(words[0])
                    type = int(words[1])
                    
                    currentType = type
                    currentId = id

                    if (type==6):    # Create Service
                        s = Service(id, "Service {}".format(nService), "S{}".format(nService))
                            
                            # Hospitalization Units are created and associated with the Service 
                        hospUnitsServ = []
                        
                        for i in range(0,huPerService):
                            index += 1
                            letter = abcCap[i]
                            u = HospUnit(index, "HospUnit {}{}".format(nService, letter), "HU{}{}".format(nService, letter))
                            u.service = s
                            dicHospUnits[u.id] = u
                            hospUnitsServ.append(u.id)

                        s.hospUnits = hospUnitsServ
                        
                        dicServices[id] = s
                        nService += 1

                    elif (type==1 or type==4 or type==5 or type==3):   # Create Rooms (without name)
                        r = Room(id,"")

                        if (type==1):    # The ER HospUnit and Service are associated with the Room
                            r.description = "er"
                            r.hospUnit = listHospUnitsIds[0]
                            dicHospUnits[listHospUnitsIds[0]].rooms.append(id)
                            dicServices[listServicesIds[0]].rooms.append(r.id)

                        elif (type==5):  # The ICU HospUnit and Service are associated with the Room
                            r.description = "icu"
                            r.hospUnit = listHospUnitsIds[1]
                            dicHospUnits[listHospUnitsIds[1]].rooms.append(id)
                            dicServices[listServicesIds[1]].rooms.append(r.id)
                        
                        elif (type==3): # The Radiology HospUnit and Service are associated with the Room
                            r.description = "rad"
                            r.hospUnit = listHospUnitsIds[2]
                            dicHospUnits[listHospUnitsIds[2]].rooms.append(id)
                            dicServices[listServicesIds[2]].rooms.append(id)
                            
                        dicRooms[id] = r

                    elif (type==2 or type==7):     # Create Beds (no name)    
                        b = Bed(id,"")
                            
                        if (type==2):       # SURGERY
                                # Create Surgery Room for the the Bed  
                            index += 1
                            r = Room(index, "surgery")
                            dicRooms[index] = r
                            r.beds.append(b.id)
                            b.parent = r.id
                                # The Bed and Room are associated with their HospUnit and Service
                            b.hospUnit = listHospUnitsIds[3]
                            dicHospUnits[listHospUnitsIds[3]].beds.append(b.id)
                            r.hospUnit = listHospUnitsIds[3]
                            dicHospUnits[listHospUnitsIds[3]].rooms.append(r.id)
                            dicServices[listServicesIds[3]].rooms.append(r.id)

                            b.type = TypeBed.Surgery

                        dicBeds[id] = b


            # line with the parent
            elif (parent):      
                if (currentType == 7): # Beds. They have as a parent: Room, ER(Room), ICU(Room), RAD(Room)
                    line = line.split('\n')
                    line = line[0]
                    words = line.split(",")
                    idParent = int(words[0])
                    
                    dicBeds[currentId].parent = idParent
                    dicRooms[idParent].beds.append(currentId)

                    typeParent = int(words[1])
                    if typeParent == 1:   # ER   
                        b.type = TypeBed.ER  
                        dicBeds[currentId].hospUnit = listHospUnitsIds[0] 
                    elif typeParent == 5:     # ICU
                        b.type = TypeBed.ICU
                        dicBeds[currentId].hospUnit = listHospUnitsIds[1]
                    elif typeParent == 3:   # RAD
                        b.type = TypeBed.Radiology
                        dicBeds[currentId].hospUnit = listHospUnitsIds[2]
                        dicHospUnits[listHospUnitsIds[2]].beds.append(b.id) 

                elif (currentType == 4):  # Rooms. They have as a parent: Service -> Not their parent
                    line = line.split('\n')
                    line = line[0]
                    words = line.split(",")
                    idParent = int(words[0])

                    dicServices[idParent].rooms.append(currentId)

                parent = False
                

            # With these types of lines we do NOTHING
            elif (children):
                if (line == "children_end\n"):
                    children = False
            elif (neighbours):
                if (line == "neighbours_end\n"):
                    neighbours = False
                

    '''Close hospital.txt'''
    file.close()

    return dicBeds, dicRooms, index



def getLastIndexHospital():

     # Control parameters
    parent = False
    children = False
    neighbours = False

    biggestId = 0

    '''Open hospital.txt'''
    with open(".\\Input\\hospital.txt") as file:
        for line in file:
            line = str(line)

            if (not parent and not children and not neighbours):
                if (line == "children\n"):
                    children = True
                elif (line == "neighbours\n"):
                    neighbours = True  
                elif (line == "parent\n"):
                    parent = True
                
                else:
                    line = line.split('\n')
                    line = line[0]
                    words = line.split(",")
                    id = int(words[0])
                    if biggestId < id:
                        biggestId = id


            # With these types of lines we do NOTHING
            elif (parent):      
                parent = False
            elif (children):
                if (line == "children_end\n"):
                    children = False
            elif (neighbours):
                if (line == "neighbours_end\n"):
                    neighbours = False
    
    '''Close hospital.txt'''
    file.close()
    
    return id
