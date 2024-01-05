from alphabets import nums
from datetime import datetime
import re

##########
# ERRORS #
##########

class InsufficientParamsError(Exception):
    def __init__(self, nParams, line):
        self.message = "\tEXIT: The number of parameters to enter is {}. Parameters must be separated with ;".format(nParams)
        if (line is not None):
            self.message += "\n\t\tline: {}".format(line)
        super().__init__(self.message)

class ReadIndexError(Exception):
    def __init__(self, line):
        self.message = "\tEXIT: You must enter a number that is greater than 0"
        if line is not None:
            self.message += "\n\t\tline: {} - param: 1 (index)".format(line)
        super().__init__(self.message)

class ReadHUPerServiceError(Exception):
    def __init__(self, linea):
        self.message = "\tEXIT: You must enter a number that is greater than 0 and smaller than 10"
        if linea is not None:
            self.message += "\n\t\tline: {} - param: 2 (huPerService)".format(linea)
        super().__init__(self.message)

class ReadNumFloorsError(Exception):
    def __init__(self, line):
        self.message = "\tEXIT: You must enter a number that is greater than or equal to 2 and smaller than 10"
        if line is not None:
            self.message += "\n\t\tline: {} - param: 3 (nFloors)".format(line)
        super().__init__(self.message)

class ReadHUPerFloorError(Exception):
    def __init__(self, line):
        self.message = "\tEXIT: You must enter a number that is greater than 0 and less than or equal to the number of Ord Hospitalization Units"
        if line is not None:
            self.message += "\n\t\tline: {} - param: 4 (huPerFloor)".format(line)
        super().__init__(self.message)

class ReadNumRowsColumnsError(Exception):
    def __init__(self, line, inRow):
        self.message = "\tEXIT: You must enter a number that is greater than 0"
        if line is not None:
            if inRow:
                self.message += "\n\t\tline: {} - param: 5 (nRows)".format(line)
            else:
                self.message += "\n\t\tline: {} - param: 6 (nColumns)".format(line)
        super().__init__(self.message)

class ReadOptionChangeFloorsOrHuPerFloorError(Exception):
    def __init__(self, line):
        self.message = "\tEXIT: The only valid values are: 1 and 2"
        if line is not None:
            self.message += "\n\t\tline: {} - param: 8 (optionFloorUH)".format(line)
        super().__init__(self.message)

class WrongDateTimeFormatError(Exception):
    def __init__(self, line):
        self.message = "\tEXIT: You must enter a date in the format 'dd/mm/yyyy HH:MM:SS' starting from 01/01/1970 00:00:00"
        if (line is not None):
            self.message += "\n\t\tline: {} - param: 7 (startDateTime)".format(line)
        super().__init__(self.message)


######################
# CONSOLE DATA ENTRY #
######################

def readIndex():
    try: 
        # Get last id used in the simulator to start putting ids from it
        index = input("Last index: ") 
        index = int(index)
        if (index<0):
            raise ReadIndexError(None)
        
    except Exception as e:
        print(e.args[0])
        exit(1)

    return index

def readHospitalizationUnitsPerServicio():
    try:
        huPerService = input("Nº Hospitalization Units per Service (default, 2): ")
        if (huPerService == ""):
            huPerService = 2 
        else:
            huPerService = int(huPerService)
            if (huPerService >= 10 or huPerService <= 0):
                raise ReadHUPerServiceError(None)
    except Exception as e:
        print(e.args[0])
        exit(1)

    return huPerService

def readNumFloors():
    try:
        n_floors = input("Nº Floors (default, 2): ")
        if (n_floors == ""):
            n_floors = 2 
        else:
            n_floors = int(n_floors)
            if (n_floors >= 10 or n_floors < 2):
                raise ReadNumFloorsError(None)

    except Exception as e:
        print(e.args[0])
        exit(1)
    
    return n_floors

def readHUPerFloor(nFloors_ord, nHU_ord):
    try:
        n_huPerFloor = input("Nº of Ord Hospitalization Units per Ord Floor (by default, 2) [Ord HU Nº: {}  -  Nº Ord Floors: {}]: ".format(nHU_ord, nFloors_ord))
        if (n_huPerFloor == ""):
            n_huPerFloor = 2 
        else:
            n_huPerFloor = int(n_huPerFloor)
            if (n_huPerFloor < 1  or  n_huPerFloor>nHU_ord):
                raise ReadHUPerFloorError(None)

    except Exception as e:
        print(e.args[0])
        exit(1)

    
    return n_huPerFloor

def readChangeFloorsOrHUPerFloor(n_floors, n_floors_ord, n_hu_ord, n_huPerFloor, b):
    try:
        print("\t\tOPTIONS:"
                +"\n\t\t 1) Change number of Floors to {} (Ord Floors = {}) and set the HospUnits per Floor to {}".format(b+1,b,n_huPerFloor)
                +"\n\t\t 2) Change the number of HospUnits per Floor to {} and set the Floors as {} (Ord Floors = {})".format(2,n_floors,n_floors_ord))
        option = input("Chosen option (1 or 2): ".format())
        if (option not in ["1","2"]):
            raise ReadOptionChangeFloorsOrHuPerFloorError(None)
        else:
            option = int(option)

    except Exception as e:
        print(e.args[0])
        exit(1)
    
    return option

def readNumRowsColumns():
    try:
        nRows = input("Nº Units (rows) per Floor (default, 2): ")
        if (nRows == ""):
            nRows = 2 
        else:
            nRows = int(nRows)
            if (nRows <= 0):
                raise ReadNumRowsColumnsError(None,None)
    
        nColumns = input("No. Blocks (columns) per Floor (default, 2): ")
        if (nColumns == ""):
            nColumns = 2 
        else:
            nColumns = int(nColumns)
            if (nColumns <= 0):
                raise ReadNumRowsColumnsError(None,None)

    except Exception as e:
        print(e.args[0])
        exit(1)

    return nRows, nColumns



###################
# TEXT DATA ENTRY #
###################

# index;huPerService;nFloors;huPerFloor;nRows;nColumns;startDateTime

def readParams():

    nParams = 8
    params = []
    paramsLine = []
    nLine = 1

    try:
        '''Open params.txt'''
        with open(".\\Input\\params.txt") as file:
            for line in file:
                paramsLine = []

                line = str(line)
                line = line.split('\n')
                line = line[0]
                params_txt = line.split(";")
                
                if len(params_txt) != nParams:
                    raise InsufficientParamsError(nParams, nLine)
                
                # index
                index = params_txt[0]
                if index[0] not in nums:
                    raise ReadIndexError(nLine)
                index = int(index)
                if index<0:
                    raise ReadIndexError(nLine)
                paramsLine.append(index)

                # huPerService
                huPerService = params_txt[1]
                if (huPerService == ""):
                    huPerService = 2 
                else:
                    if huPerService[0] not in nums:
                        raise ReadHUPerServiceError(nLine)
                    huPerService = int(huPerService)
                    if (huPerService >= 10 or huPerService <= 0):
                        raise ReadHUPerServiceError(nLine)
                paramsLine.append(huPerService)

                # nFloors
                nFloors = params_txt[2]
                if (nFloors == ""):
                    nFloors = 2 
                else:
                    if nFloors[0] not in nums:
                        raise ReadNumFloorsError(nLine)
                    nFloors = int(nFloors)
                    if (nFloors >= 10 or nFloors < 2):
                        raise ReadNumFloorsError(nLine)
                paramsLine.append(nFloors)

                # huPerFloor
                huPerFloor = params_txt[3]
                if (huPerFloor == ""):
                    huPerFloor = 2 
                else:
                    if huPerFloor[0] not in nums:
                        raise ReadHUPerFloorError(nLine)
                    huPerFloor = int(huPerFloor)
                    if (huPerFloor < 1):
                        raise ReadHUPerFloorError(nLine)
                paramsLine.append(huPerFloor)

                # nRows
                nRows = params_txt[4]
                if (nRows == ""):
                    nRows = 2 
                else:
                    if nRows[0] not in nums:
                        raise ReadNumRowsColumnsError(nLine, True)
                    nRows = int(nRows)
                    if (nRows <= 0):
                        raise ReadNumRowsColumnsError(nLine, True)
                paramsLine.append(nRows)

                # nColumns
                nColumns = params_txt[5]
                if (nColumns == ""):
                    nColumns = 2 
                else:
                    if nColumns[0] not in nums:
                        raise ReadNumRowsColumnsError(nLine, False)
                    nColumns = int(nColumns)
                    if (nColumns <= 0):
                        raise ReadNumRowsColumnsError(nLine, False)
                paramsLine.append(nColumns)

                # startDateTime
                startDateTime = params_txt[6]
                if (startDateTime == ""):
                    startDateTime = "01/01/2022 08:00:00"
                else:
                    regex_DMY_HMS = "^([0-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4}) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
                    x = re.search(regex_DMY_HMS, startDateTime)
                    if x is None:
                        raise WrongDateTimeFormatError(nLine)
                startDateTime = datetime.strptime(startDateTime, '%d/%m/%Y %H:%M:%S')    
                if startDateTime.year < 1970:
                    raise WrongDateTimeFormatError(nLine)                
                paramsLine.append(startDateTime)

                # optionFloorHU -> readChangePlantasOrUhPerPlanta
                optionFloorHU = params_txt[7]
                if (optionFloorHU == ""):
                    optionFloorHU = None 
                else:
                    if (optionFloorHU not in ["1","2"]):
                        raise ReadOptionChangeFloorsOrHuPerFloorError(nLine)
                    optionFloorHU = int(optionFloorHU)
                paramsLine.append(optionFloorHU)


                nLine += 1
                params.append(paramsLine)


    except Exception as e:
        typeException = type(e).__name__
        if typeException in [InsufficientParamsError.__name__, ReadIndexError.__name__, ReadHUPerServiceError.__name__, ReadNumFloorsError.__name__, ReadHUPerFloorError.__name__, ReadNumRowsColumnsError.__name__, ReadOptionChangeFloorsOrHuPerFloorError.__name__, WrongDateTimeFormatError.__name__]:
            print(e.args[0])
        else:
            print(traceback.format_exc())
        
        '''Close params.txt'''
        file.close()

        exit(1)

    '''Close params.txt'''
    file.close()

    return params