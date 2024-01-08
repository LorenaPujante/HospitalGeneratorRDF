
#######################
#  LOGICAL HIERARCHY  #
#######################

from enum import Enum


class Service:
    def __init__(self, id, description, abrev):
        self.id = id
        self.description = description
        self.abrev = abrev
        self.hospUnits = []     # IDs are saved
        self.rooms = []

class HospUnit:
    def __init__(self, id, description, abrev):
        self.id = id
        self.description = description
        self.abrev = abrev
        self.rooms = []     # IDs are saved
        self.beds = []      # IDs are saved
        self.service = None    # The object is saved


#######################
#  SPATIAL HIERARCHY  #
#######################

class TypeBed(Enum):
    Service = 0     
    Radiology = 1
    Surgery = 2
    ICU = 3
    ER = 4

class Bed:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.parent = None      # IDs are saved
        self.nextTo = []        # IDs are saved
        self.opposite = []      # IDs are saved
        self.hospUnit = None    # IDs are saved
        self.type = TypeBed.Service

class Room:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.parent = None          # IDs are saved
        self.nextTo = []            # IDs are saved
        self.opposite = []          # IDs are saved
        self.hospUnit = None    # All Rooms have this attribute      # IDs are saved
        self.service = None     # Only Rooms from Services S0-S7 have this attribute
        self.beds = []          # IDs are saved

class Corridor:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.nextTo = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None}    # IDs are saved
        self.rooms = []         # The object is saved
        self.roomsBorder = {'leftTop':None, 'leftBottom':None, 'rightTop':None, 'rightBottom':None, 
                            'topLeft':None, 'topRight':None, 'bottomLeft':None, 'bottomRight':None}   # Se guardan los objetos

class Area:
    def __init__(self, id, description, tipo):
        self.id = id
        self.description = description
        self.type = tipo
        self.corridorsHoriz = []     # The object is saved
        self.corridorsVert = []      # The object is saved
        self.unit = None            
        self.block = None

class Unit:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.nextTo_prev = None     # IDs are saved
        self.nextTo_after = None    # IDs are saved

class Block:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.nextTo_prev = None     # IDs are saved
        self.nextTo_after = None    # IDs are saved

class Floor:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.hospUnits = []      # The objects are saved
        self.nRooms = 0
        self.areas = []
        self.units = []     # The objects are saved
        self.blocks = []    # The objects are saved

class Building:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.floors = []    # The objects are saved


############
# PATIENTS #
############

class Patient:
    def __init__(self, id, age, sex, death):
        self.id = id
        self.age = age
        self.sex = sex
        self.death = death
        self.stepLocations = {}     # IDs are saved
        self.episodes = []      # The objects are saved
        self.seird = [None, None, None, None, None]     # To save in which step each state starts


##########
# EVENTS #
##########

class Episode:
    def __init__(self, id, description, start, end):
        self.id = id
        self.description = description
        self.start = start
        self.end = end
        self.events = []    # The objects are saved

class TypeEvent(Enum):
    Hospitalization = 0     # (It includes UCI y ER)
    Radiology = 1
    Surgery = 2
    Death = 3
    TestMicro = 4

class Event:
    def __init__(self, id, description, start, end, location, hu, type):
        self.id = id
        self.description = description
        self.start = start
        self.end = end
        self.location = location
        self.hospUnit = hu
        self.type = type
            # To save extra info
        self.extra1 = None  # For example, the Microorganism of a TestMicro (object)  
        self.extra2 = None  # For example, if the Microorganism is MDR

class Microorganism:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        
