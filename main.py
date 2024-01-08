
from datetime import datetime
from mainAuxFunctions import *
from readInputParams import *
from parserHospital import *
from parserPatients import parsePatients
from parserSteps import *
from makerFloors import *
from makerFloor0 import *
from writerCSV import *
from writerRDF import *
from writerRDF_star import *
from writerSummary import *
from writerUnion import unionFiles


############
##  MAIN  ##
############

def main(index, huPerService, nFloors, huPerFloor, nRows, nColumns, startDateTime, optionFloorHU):

    # Input of index to start numbering the objects that are created
    #index = readIndex()
    
    # Input of HospitalizationUnits per Service
    #huPerService = readHospitalizationUnitsPerServicio()
    
    # Create vanilla Services and HospUnits
    dicServices, dicHospUnits, index = createServicesAndHospUnits_Vanilla(index)

    # PARSE OF THE INPUT
    dicBeds, dicRooms, index = parseHospital(dicHospUnits, dicServices, huPerService, index)

    
    # The Service Rooms are distributed equally among its HospUnits
    # The Beds in each Room belong to its HospUnit
    setRooms_In_HospitalizationUnit(huPerService, dicServices, dicHospUnits, dicRooms, dicBeds)              


    # Create Building
    dicBuildings, index = createBuilding(index)

    # Request number of plants
    #nFloors = readNumFloors()

    # Filter HUs that are not [ICUU, ERU, RadU, Surgerys]
    list_Ord_HU = getOrd_HU(dicHospUnits)
    n_ord_HU = len(list_Ord_HU)


    # Request number of Hospitalization Units per Floor
    #huPerFloor = readHUPerPlanta(n_plantas-1, n_uH_ord)
    if huPerFloor>n_ord_HU:
        raise ReadHUPerFloorError(None)

    # Calculate the number of Floors to create: 1 [ICUU, ERU, RadU, Surgerys] + (nº Ord HospUnits / n_uhPerPlanta)
        # The first floor will have (huPerFloor + remainHU) HospUnits
    nFloors, remainHU, huPerFloor = setNumFloorsToCreate(nFloors, huPerFloor, n_ord_HU, optionFloorHU)
    n_plantas_ord = nFloors-1


    # Create and populate Plant_0
    dicFloors0, dicUnits0, dicBlocks0, dicAreas0, dicCorridors0, index = createFloor0(index, dicBuildings, dicHospUnits, dicRooms, dicBeds)


    # Create Ordinary Floors and associate their HospUnits with them 
    dicOrdFloors, index = createOrdFloors(nFloors-1, huPerFloor, remainHU, list_Ord_HU, index, dicBuildings)


    # Input of Rows and Columns of Ord Floors
    #nRows, nColumns = readNumRowsColumns()

    # Populate Ord Floors
    dicOrdUnits, dicOrdBlocks, dicOrdAreas, dicOrdCorridors, index = populateOrdFloors(dicOrdFloors, nRows, nColumns, dicBuildings, dicRooms, dicBeds, index)


    # Join the elements of Ord Floors with those of Floor 0
    dicFloors = {}
    appendDictionarys(dicFloors0, dicFloors)
    appendDictionarys(dicOrdFloors, dicFloors)
    dicUnits = {}
    appendDictionarys(dicUnits0, dicUnits)
    appendDictionarys(dicOrdUnits, dicUnits)
    dicBlocks = {}
    appendDictionarys(dicBlocks0, dicBlocks)
    appendDictionarys(dicOrdBlocks, dicBlocks)
    dicAreas = {}
    appendDictionarys(dicAreas0, dicAreas)
    appendDictionarys(dicOrdAreas, dicAreas)
    dicCorridors = {}
    appendDictionarys(dicCorridors0, dicCorridors)
    appendDictionarys(dicOrdCorridors, dicCorridors)

    
    # PATIENTS 
    dicPatients = parsePatients()
    
    # MICROORGANISMS
    # A dummy Microorganism is created, since only one will be detected
    dicMicroorganisms = {}
    microorg = Microorganism(index, "Microorg1") 
    dicMicroorganisms[microorg.id] = microorg
    index += 1

    # STEPS
    lastStep = parseSteps(dicPatients)
    #startDateTime = datetime(2022,1,1,8,0,0)    # 01-01-2022 08:00:00 
    index = createEpisodesAndEventsPerPacient(dicPatients, dicBeds, startDateTime, index)
    #index = createTestMicro_StartInfected(dicPatients, dicMicroorganisms, startDateTime, index)
    index = createTestMicro_DuringInfected(dicPatients, dicMicroorganisms, startDateTime, index)



    keysPatients = list(dicPatients.keys())
    keysPatients.sort()
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("First patient: {}".format(keysPatients[0]))
    print("Last patient: {}".format(keysPatients[len(keysPatients)-1]))

    print("Range Steps: [0, {}] \n".format(lastStep))
    

    
    # PRINT RESUMENES
    setFolderSummary(".\\OutputSummary")
    printSummaryHospital(nFloors, dicFloors, dicBeds)
    printEpisodeSummary(dicPatients, startDateTime)

    
    # PRINT CSV
    setFolderOutputCSV(".\\OutputCSV")
    printCSV(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms)
    

    # PRINT NT
    dirNT = ".\\OutputRDF"
    setFolderOutputRDF(dirNT)
    printRDF(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms)
        # File union
    unionFiles(dirNT, False)


    # PRINT NT-Star
    dirNT_star = ".\\OutputRDF_star"
    setFolderOutputRDFstar(dirNT_star)
    printRDF_star(dicServices, dicHospUnits, dicBuildings, dicFloors, dicUnits, dicBlocks, dicAreas, dicCorridors, dicRooms, dicBeds, dicPatients, dicMicroorganisms)
        # File union
    unionFiles(dirNT_star, True)
    


''' MAIN '''

#print("Last id Hospital: {}".format(getLastIndexHospital()))

# PARAMS
        # The folders where the result files are created are not parameters     
index = 1600
huPerService = 3
nFloors = 5
huPerFloor = 6
nRows = 3
nColumns = 4
startDateTime = datetime(2023,1,1,8,0,0)    # 01-01-2023 08:00:00   # dd/mm/yyyy HH:MM:SS
optionFloorUH = None#1

params = []
paramsLinea = []
paramsLinea.append(index)
paramsLinea.append(huPerService)
paramsLinea.append(nFloors)
paramsLinea.append(huPerFloor)
paramsLinea.append(nRows)
paramsLinea.append(nColumns)
paramsLinea.append(startDateTime)
paramsLinea.append(optionFloorUH)
params.append(paramsLinea)

main(params[0][0], params[0][1], params[0][2], params[0][3], params[0][4], params[0][5], params[0][6], params[0][7])    



