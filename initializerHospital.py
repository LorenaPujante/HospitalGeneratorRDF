from enum import Enum

class TypeLocation(Enum):
    ER = 1
    Surgery = 2
    Radiology = 3
    Room = 4
    ICU = 5
    Service = 6
    Bed = 7


class Location:
    def __init__(self, id, type_local, father_location=None, infected=False, neighbor_location=None, children=None):
        self.id = id
        self.name = type_local
        self.infected = infected
        self.located_in = father_location
        self.adjacent = neighbor_location
        self.children = children


    def to_string(self):
        return str(self.id)  + ';' + str(self.infected) # + str(self.name.name)

    def print_location(self):
        print(self.to_string())

    def is_temporal_location(self):
        return self.name in [TypeLocation.Surgery, TypeLocation.Radiology]

    def is_room_bed(self):
        return self.name is TypeLocation.Bed and self.located_in.name is TypeLocation.Room

    def is_room_infected(self):
        return self.located_in.infected

    def is_located_in(self, location):
        return self.located_in is not None and self.located_in.name is location

    def is_location(self, localization):
        return self.name is not None and self.name is localization

    def get_service(self):
        if self.located_in and self.located_in.name is TypeLocation.Room:
            return self.located_in.located_in
        else:
            return None



# Initialize a new hospitals with given number of beds and rooms 
def initialize_hospital(er_nbeds, uci_nbeds, s0_nrooms, s1_nrooms, s2_nrooms, s3_nrooms, s4_nrooms, s5_nrooms, s6_nrooms, s7_nrooms, room_nbeds):
    er = Location(0, TypeLocation.ER)
    uci = Location(1, TypeLocation.ICU)
    s0 = Location(2, TypeLocation.Service)
    s1 = Location(3, TypeLocation.Service)
    s2 = Location(4, TypeLocation.Service)
    s3 = Location(5, TypeLocation.Service)
    s4 = Location(6, TypeLocation.Service)
    s5 = Location(7, TypeLocation.Service)
    s6 = Location(8, TypeLocation.Service)
    s7 = Location(9, TypeLocation.Service)
    sx1 = Location(10, TypeLocation.Surgery)
    sx2 = Location(11, TypeLocation.Surgery)
    sx3 = Location(12, TypeLocation.Surgery)
    rx1 = Location(13, TypeLocation.Radiology)
    rx2 = Location(14, TypeLocation.Radiology)
    rx3 = Location(15, TypeLocation.Radiology)
    rx4 = Location(16, TypeLocation.Radiology)

    beds_er, index = create_beds(er_nbeds, 17, er)
    beds_uci, index = create_beds(uci_nbeds, index, uci)

    rooms_s0, beds_s0, index = create_rooms(s0_nrooms, room_nbeds, index, s0)
    rooms_s1, beds_s1, index = create_rooms(s1_nrooms, room_nbeds, index, s1)
    rooms_s2, beds_s2, index = create_rooms(s2_nrooms, room_nbeds, index, s2)
    rooms_s3, beds_s3, index = create_rooms(s3_nrooms, room_nbeds, index, s3)
    rooms_s4, beds_s4, index = create_rooms(s4_nrooms, room_nbeds, index, s4)
    rooms_s5, beds_s5, index = create_rooms(s5_nrooms, room_nbeds, index, s5)
    rooms_s6, beds_s6, index = create_rooms(s6_nrooms, room_nbeds, index, s6)
    rooms_s7, beds_s7, index = create_rooms(s7_nrooms, room_nbeds, index, s7)

    L = [er, uci, s0, s1, s2, s3, s4, s5, s6, s7, sx1, sx2, sx3, rx1, rx2, rx3, rx4] + beds_er + beds_uci + rooms_s0 + beds_s0 + rooms_s1 + beds_s1 + rooms_s2 + beds_s2 + rooms_s3 + beds_s3 + rooms_s4 + beds_s4 + rooms_s5 + beds_s5 + rooms_s6 + beds_s6 + rooms_s7 + beds_s7
  
    
    return L

# creates nbeds and assigns it to located_in
def create_beds(nbeds, index, located_in):
  beds = []
  for i in range(nbeds):
    beds.append(Location(index, TypeLocation.Bed, located_in))
    index = index+1

  # we indicate who are the neighbors of this bed
  for b in beds:
    b.adjacent = [bed for bed in beds if bed is not b]
  
  # we assign to the room/service its beds 
  located_in.children = beds
  return beds, index

# creates nrooms with its room_nbeds
def create_rooms(nrooms, room_nbeds, index, located_in):
  rooms = []
  beds = []
  for i in range(nrooms):
    r = Location(index, TypeLocation.Room, located_in)
    rooms.append(r)
    index = index+1
    bs, index = create_beds(room_nbeds, index, r)
    beds.extend(bs)

  located_in.children = rooms  
  return rooms, beds, index


def printVerboseHospital(L):
  s = ""
  for x in L:
    s = s + '\n' + '{} - {}'.format(x.id, x.name)
    if (x.located_in != None):
      s = s + '\n' + '\t0. Located in: {} - {}'.format(x.located_in.id, x.located_in.name)
    if (x.adjacent != None):
      s = s + '\n' + "\t1. Neighbors: "
      for y in x.adjacent:
        s = s + '\n' + '\t\t{} - {}'.format(y.id, y.name)
    if (x.children != None):
      s = s + '\n' + "\t2. Children: "
      for y in x.children:
        s = s + '\n' + '\t\t{} - {}'.format(y.id, y.name) 

  return s


def printHospital(L):
  s = ""
  for x in L:
    s = s + '{},{}\n'.format(x.id, x.name.value)
    if (x.located_in != None):
      s = s + 'parent\n{},{}\n'.format(x.located_in.id, x.located_in.name.value)
    if (x.adjacent != None):
      s = s + "neighbors\n"
      for y in x.adjacent:
        s = s + '{},{}\n'.format(y.id, y.name.value)
      s = s + "neighbors_end\n"
    if (x.children != None):
      s = s + "children\n"
      for y in x.children:
        s = s + '{},{}\n'.format(y.id, y.name.value)
      s = s + "children_end\n"

  return s


def printInfichero(namefile):
  file = open(namefile, 'w')
  file.write(s)
  file.close()    


############
### MAIN ###
############


L = initialize_hospital(2, 1, 4, 1, 4, 1, 4, 1, 4, 5, 3)
# self, id, type_local, located_in=None, infected=False, adjacent=None, children=None

s = printHospital(L)
printInfichero('hospital.txt')  