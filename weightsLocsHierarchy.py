
weights = {}

weights['hospUnitFromService'] = 0.2    # Change block
weights['looksAfter'] = 0.25

weights['nextTo_Seat'] = 0.25
weights['nextTo_Room'] = 0.625
weights['nextTo_Corridor'] = 0.875
weights['nextTo_Unit'] = 2
weights['nextTo_Block'] = 2

weights['opposite_Seat'] = 0.375
weights['opposite_Room'] = 0.7

weights['placedIn_SeatRoom'] = 0.5
weights['placedIn_RoomCorridor'] = 0.75
weights['placedIn_CorridorArea'] = 1
weights['placedIn_AreaFloor'] = 8
weights['placedIn_FloorBuilding'] = 10

weights['placedInUnit'] = 3     # Change block
weights['placedInBlock'] = 3
weights['placedInFloor_Unit'] = 3 
weights['placedInFloor_Block'] = 3

