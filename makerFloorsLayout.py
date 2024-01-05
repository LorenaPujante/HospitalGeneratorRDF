import random

##########
# ERRORS #
##########
class SmallNumberRoomsError(Exception):
    def __init__(self, nRooms):
        self.nRooms = nRooms
        self.message = "\tEXIT: The number of rooms in the Floor ({}) must be greater than or equal to 7".format(nRooms)
        super().__init__(self.message)

class SolutionNotFoundError(Exception):
    def __init__(self):
        self.message = "\tEXIT: A suitable configuration for the Floor cannot be found"
        super().__init__(self.message)



#########################
# INITIALIZATION PIECES #
#########################

def initializePieces():
    global listPieces 
    listPieces =  {}

    letters = ['A','B','C','D','E','F','G','H','I','J','K']
    for letter in letters:
        
        indEnd = -1
        if (letter in ['A','B','C','D']):
            indEnd = 4
        elif (letter in ['E','F','G','H']):
            indEnd = 8
        elif (letter == 'I'):
            indEnd = 12
        else:   #elif (letter in ['J','K']):
            indEnd = 3

        for i in range(0,indEnd):
            name = '{}{}'.format(letter, i)
            listPieces[name] = setNRooms(name)

    return listPieces
        

def setNRooms(nr):
    letter = nr[0]
    num = int(nr[1])
    num2 = -1
    if (len(nr)>2):
        num2 = int(nr[2])
        
    letters1 = ['A','B','C','D']
    letters2 = ['E','F','G','H']
    letters4 = ['J','K']
    if (letter in letters1):
        if (num == 0):   
            return 7
        elif (num == 1):
            return 9
        elif (num == 2):
            return 9
        else:   #elif (num == 3):
            return 11   

    elif (letter in letters2):
        if (num == 0):   
            return 10
        elif (num == 1):
            return 12
        elif (num == 2):
            return 12
        elif (num == 3):
            return 12
        elif (num == 4):
            return 14
        elif (num == 5):
            return 14
        elif (num == 6):
            return 14
        else:   #elif (num == 7):
            return 16

    elif (letter == 'I'):
        if (num == 0):   
            return 12
        elif (num == 1): 
            if (num2 == -1):
                return 14
            elif (num2 == 0):               # 10
                return 16
            else:   #elif (num2 == 1):      # 11
                return 20
        elif (num == 2):
            return 14
        elif (num == 3):
            return 14
        elif (num == 4):
            return 14
        elif (num == 5):
            return 16
        elif (num == 6):
            return 16
        elif (num == 7):
            return 16
        elif (num == 8):
            return 16
        else:   #elif (num == 9):
            return 16

    elif (letter in letters4):
        if (num == 0):   
            return 8
        elif (num == 1):
            return 10
        else:   #elif (num == 2):
            return 12
        
    return 0



#################
# MAIN FUNCTION #
#################

def generateAreas(nRooms, nCols, nRows):
    
    initializePieces()

    if (nRooms < 7):
        raise SmallNumberRoomsError(nRooms)

    # Base cases
    if (nRooms <= 20):
        gridRes, nColumns, nRows = baseCases(nRooms, nCols, nRows) 
        if (nColumns < 0):
            raise SolutionNotFoundError()
        else:    
            return gridRes, nColumns, nRows    
    
    # Backtracking
    if (nCols==1 or nRows==1):
        nColumns = nCols
        if (nRows > 1):
            nColumns = nRows
        gridRes, nColumns, nRows = generateAreas_OneRow(nRooms,nColumns)
        if (nColumns < 0):
            raise SolutionNotFoundError()
        else:    
            return gridRes, nColumns, nRows 

    elif (nCols==2 or nRows==2):
        nColumns = nCols
        if (nRows > 2):
            nColumns = nRows
        gridRes, nColumns, nRows = generateAreas_twoRows(nRooms,nColumns,1)
        if (nColumns < 0):
            raise SolutionNotFoundError()
        else:    
            return gridRes, nColumns, nRows 
    else:
        gridRes, nColumns, nRows = generateAreas_grid(nRooms, nRows, nCols)
        if (nColumns < 0):
            raise SolutionNotFoundError()
        else:    
            return gridRes, nColumns, nRows 



##############
# BASE CASES #
##############

def baseCases(nRooms, nCols, nRows):
    match nRooms:
        case 7:
            return [['A0']], 1, 1
        case 8:
            return [['J0']], 1, 1
        case 9:
            return [['A1']], 1, 1
        case 10:
            option = random.randint(0,1)
            if (option == 0):
                return [['J1']], 1, 1
            return [['E0']], 1, 1   
        case 11:
            return [['A3']], 1, 1
        case 12:
            option = random.randint(0,3)
            if (option == 0):
                return [['J2']], 1, 1
            elif (option == 1):
                return [['E1']], 1, 1
            elif (option == 2):
                return [['E3']], 1, 1
            else:            
                return [['I0']], 1, 1
        case 13:        
            return -1, -1, -1   # ERROR
        case 14:
            if (nCols>1 or nRows>1):            
                return [['A0','B0']], 2, 1
            else:
                option = random.randint(0,3)
                if (option == 0):
                    return [['E4']], 1, 1
                elif (option == 1):
                    return [['E6']], 1, 1
                elif (option == 2):
                    return [['I1']], 1, 1        
                else:
                    return [['I3']], 1, 1
        case 15:
            return [['A0','J0']], 1, 1
        case 16:
            if (nCols>1 or nRows>1):
                option = random.randint(0,1)
                if (option == 0):
                    return [['J0','J0']], 2, 1
                else:
                    return [['A0','B1']], 2, 1  
            else:
                option = random.randint(0,3)
                if (option == 0):
                    return [['E7']], 1, 1
                elif (option == 1):
                    return [['I5']], 1, 1
                elif (option == 2):
                    return [['I9']], 1, 1        
                return [['I10']], 1, 1
        case 17:
            option = random.randint(0,1)
            if (option == 0):
                return [['A2','JO']], 2, 1
            else:
                return [['A0','J1']], 2, 1 
        case 18:
            option = random.randint(0,4)
            if (option == 0):
                return [['A0','B3']], 2, 1
            elif (option == 1):
                return [['J0','J1']], 2, 1
            elif (option == 2):
                return [['A1','B1']], 2, 1
            elif (option == 3):
                return [['A2','B2']], 2, 1
            else:
                return [['A1','B2']], 2, 1            
        case 19:
            option = random.randint(0,3)
            if (option == 0):
                return [['A1','J1']], 2, 1
            elif (option == 1):
                return [['A0','E1']], 2, 1
            elif (option == 2):
                return [['A0','E2']], 2, 1
            else: 
                return [['A3','J0']], 2, 1
        case 20:
            if (nCols>1 or nRows>1):
                option = random.randint(0,5)
                if (option == 0):
                    return [['J1','J1']], 2, 1
                elif (option == 1):
                    return [['J0','E1']], 2, 1
                elif (option == 2):
                    return [['J0','E2']], 2, 1
                elif (option == 3):
                    return [['J0','E3']], 2, 1
                elif (option == 4):
                    return [['A1','B3']], 2, 1        
                else:
                    return [['A2','B3']], 2, 1
            else:
                return [['I11']], 1, 1
    
    return -1,-1,-1



#########
# 1 ROW #
#########

def generateAreas_OneRow(nRooms, nColumns):

    print(" Trying: ONE ROW - {} Columns".format(nColumns))

    # Number of rooms in the cases: smallest and largest
    nRooms_Small = listPieces['A0']  +  (nColumns-2) * listPieces['J0']  +  listPieces['B0']
    nRooms_Big = nColumns * listPieces['I11']
    
    # Some of the base cases are the solution    
    solSmall = ['A0']
    for i in range(0,nColumns-2):
        solSmall.append('J0')
    solSmall.append('B0')
    if (nRooms_Small == nRooms): 
        return [solSmall], nColumns, 1
    if (nRooms_Big == nRooms):
        s = []
        for i in range(0,nColumns):
            s.append('I11') 
        return [s], nColumns, 1    

    # Cases where it is not possible to create a suitable layout
    
        # There are LESS rooms than are needed for the number of columns 
    if (nRooms_Small > nRooms):
        print("\tWARNING: nRooms SMALLER than required for {} columns ({})".format(nColumns, nRooms_Small))
        # We test with smaller numbers of columns (RECURSION)
        if (nColumns > 3):
            return generateAreas_OneRow(nRooms, nColumns-1)
        else:
            return -2,-2,-2

        # There are MORE rooms than can be reached with the number of columns
    if (nRooms_Big < nRooms):
        print("\tWARNING: nRooms BIGGER than achievable with {} columns ({})".format(nColumns, nRooms_Big))
        # We test with bigger numbers of columns (RECURSION)
        return generateAreas_OneRow(nRooms, nColumns+1)


    # Backtracking from the SMALL solution
    return backtracking_oneRow(nRooms, nColumns, solSmall, nRooms_Small)


def backtracking_oneRow(nRooms, nColumns, initialSolution, initialCost):
    
    # Combination of pieces
    pos1 = ['A0','J0','A1','G0','A3','G3','G1','E6','I9','I11']
    posLast = ['B0','J0','B1','H0','B3','H3','H1','E6','I9','I11']
    ordinary8 = ['J0']                          #0
    ordinary10 = ['J1','E0']                    #1
    ordinary12 = ['J2','E1','E2','E3','I0']     #2
    ordinary14 = ['E4','E5','E6','I1','I2','I3']    #3
    ordinary16 = ['E7','I5','I6','I9']          #4
    ordinary20 = ['I11']                        #5
    posOrdinary = [ordinary8, ordinary10, ordinary12, ordinary14, ordinary16, ordinary20]

    # To PRUNE
    costPrune = []      # Matrix that stores the maximum cost that can be reached from the first cell you are in (this one included)
    cost = 0
    maxCost = nColumns * listPieces['I11']
    for j in range(nColumns):
        cost += listPieces['I11']
        costPrune.append(maxCost-cost)

    # Variable initialization
    solution = initialSolution
    
    currPos = []  # pos1, ordinary, posLast
    for i in range(0,nColumns):
        currPos.append(-1)
    
    level = 0
    cost = initialCost
    end = False

    while (not end and level>=0):
        # Generate
        cost = bck_1R_genete(level, currPos, cost, solution, nColumns, pos1, posLast, posOrdinary)     
        # isSolution
        if (cost==nRooms):
            end = True
        else:
            # Prune
            continuing = True

            costToLevel = bck_1R_calculateCost_toLevel(level, solution)

            # Calculate maximum cost that can be obtained
            maxCost = costToLevel + costPrune[level]
            if (maxCost < nRooms):
                continuing = False

            # Criterion
            if (continuing and level<nColumns-1  and  cost<nRooms):
                level += 1
            else:
                # While NO moreSiblings 
                while (level>=0  and  not bck_1R_moreSiblings(level, currPos, nColumns, len(pos1), len(posLast), len(posOrdinary))):
                    # Go back
                    level, cost, solution = bck_1R_goBack(level, currPos, cost, solution, nColumns)

    if end:
        return [solution], nColumns, 1

    return -1,-1,-1

def bck_1R_genete(level, p, cost, solution, nColumns, pos1, posLast, posOrdinary):
    if (level == 0):
        cost -= listPieces[solution[0]] # Subtract the cost of the letter that was in the position
        p[0] += 1    # Go to the next piece of the candidates
        solution[0] = pos1[p[0]]
        cost += listPieces[solution[0]]    # Add the cost of the new piece
    elif (level == nColumns-1):     
        cost -= listPieces[solution[level]]
        p[level] += 1
        solution[level] = posLast[p[level]]
        cost += listPieces[solution[level]]
    else:
        cost -= listPieces[solution[level]]
        p[level] += 1
        if (p[level] == 0  or p[level]== 5):
            solution[level] = posOrdinary[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenPosOrdPAct = len(posOrdinary[p[level]])
            indPieza = random.randint(0,lenPosOrdPAct-1)
            solution[level] = posOrdinary[p[level]][indPieza]    
        cost += listPieces[solution[level]]

    return cost  

def bck_1R_moreSiblings(level, p, nColumns, lenPos1, lenPosLast, lenPosOrdinary):   
    if (level == 0):
        return p[0] < lenPos1-1
    elif (level == nColumns-1):
        return p[nColumns-1] < lenPosLast-1
    else:
        return p[level] < lenPosOrdinary-1

def bck_1R_goBack(level, p, cost, solution, nColumns):
    if (level == 0):
        level = -1
    elif (level == nColumns-1):
        cost -= listPieces[solution[level]]   # Substrct the cost of the current piece
        solution[level] = 'B0'      # The default piece is added (position 0 of its list)
        p[level] = -1
        cost += listPieces['B0']   # Add the cost of the default piece
        level -= 1
    else:
        cost -= listPieces[solution[level]]
        solution[level] = 'J0'
        p[level] = -1
        cost += listPieces['J0']
        level -= 1

    return level, cost, solution

def bck_1R_calculateCost_toLevel(nivel, solucion):

    coste = 0
    for j in range(nivel+1):
        coste += listPieces[solucion[j]]
    
    return coste



#############
# TWO FILAS #
#############

def generateAreas_twoRows(nRooms, nColumns, level):

    print(" Trying: TWO ROWS - {} Columns".format(nColumns))

    # Generate the smallest and largest cases (within a constrained geometry)
        
        # SMALLEST case
    solRow1_small = ['A0']
    solRow2_small = ['C0']
    for i in range(0,nColumns-2):
        solRow1_small.append('J0')
        solRow2_small.append('J0')
    solRow1_small.append('B0')
    solRow2_small.append('D0')
    solucion_small = [solRow1_small,solRow2_small]
    
    cost_small = 0
    for i in range(2):
        for j in range(nColumns):
            piece = solucion_small[i][j]
            cost_small += listPieces[piece]

            # The cost is equal to nRooms   
    if (cost_small == nRooms): 
        return solucion_small, nColumns, 2
    

        # BIGGEST case
    solRow1_big = []
    solRow2_big = []
    cost_big = 0
    for i in range(nColumns):
        solRow1_big.append('I11')
        solRow2_big.append('I11')
    cost_big += nColumns*2*listPieces['I11']
    solucion_big = [solRow1_big,solRow2_big]

            # The cost is equal to nRooms    
    if (cost_big == nRooms): 
        return solucion_big, nColumns, 2


    # Cases where it is not possible to create a suitable layot

        # There are LESS rooms than are needed for the number of columns 
    if (cost_small > nRooms):
        print("\tWARNING: nRooms SMALLER than required for {} columns ({})".format(nColumns, cost_small))
        # We test with smaller numbers of columns (RECURSION)
        if (nColumns>=3):
            s0,s1,s2 = generateAreas_twoRows(nRooms, nColumns-1, 2) # First, with 2-row layouts
            if (level == 1  and  s0 == -2):                         # Second, with 1-row layouts                          
                return generateAreas_OneRow(nRooms, nColumns)       # Only the first call can call to generate a solution with a row (due to the recursion of the function)
            else:
                return s0, s1, s2
        elif (nColumns == 2):
            return generateAreas_OneRow(nRooms, nColumns)
        else:
            return -2,-2,-2

        # There are MORE rooms than are needed for the number of columns 
    if (cost_big < nRooms):
        print("\tWARNING: nRooms BIGGER than achievable with {} columns ({})".format(nColumns, cost_big))
        # We test with bigger numbers of columns (RECURSION)
        return generateAreas_twoRows(nRooms, nColumns+1, 1)


    # Backtracking from the SMALL solution
    return backtracking_twoRows(nRooms, nColumns, solucion_small, cost_small)
    

def backtracking_twoRows(nRooms, nColumns, initialSolution, initialCost):

    # Combination of Pieces

    cornerA_7 = ['A0']                              #0
    cornerA_9 = ['A1','A2']                         #1
    cornerA_11 = ['A3']                             #2
    cornerA_12 = ['E1','E2','E3','G1','G2','G3']    #3
    cornerA_14 = ['E4','E5','E6','G4','G5','G6','I1','I2','I3','I4']    #4
    cornerA_16 = ['E7','G7','I5','I6','I7','I8','I9','I10']             #5
    cornerA_20 = ['I11']                            #6
    cornerA = [cornerA_7, cornerA_9, cornerA_11, cornerA_12, cornerA_14, cornerA_16, cornerA_20]

    cornerB_7 = ['B0']                              #0
    cornerB_9 = ['B1','B2']                         #1
    cornerB_11 = ['B3']                             #2
    cornerB_12 = ['E1','E2','E3','H1','H2','H3']    #3
    cornerB_14 = ['E4','E5','E6','H4','H5','H6','I1','I2','I3','I4']    #4
    cornerB_16 = ['E7','H7','I5','I6','I7','I8','I9','I10']             #5
    cornerB_20 = ['I11']                            #6
    cornerB = [cornerB_7, cornerB_9, cornerB_11, cornerB_12, cornerB_14, cornerB_16, cornerB_20]

    cornerC_7 = ['C0']                              #0
    cornerC_9 = ['C1','C2']                         #1
    cornerC_11 = ['C3']                             #2
    cornerC_12 = ['F1','F2','F3','G1','G2','G3']    #3
    cornerC_14 = ['F4','F5','F6','G4','G5','G6','I1','I2','I3','I4']    #4
    cornerC_16 = ['F7','G7','I5','I6','I7','I8','I9','I10']             #5
    cornerC_20 = ['I11']                            #6
    cornerC = [cornerC_7, cornerC_9, cornerC_11, cornerC_12, cornerC_14, cornerC_16, cornerC_20]

    cornerD_7 = ['D0']                              #0
    cornerD_9 = ['D1','D2']                         #1
    cornerD_11 = ['D3']                             #2
    cornerD_12 = ['F1','F2','F3','H1','H2','H3']    #3
    cornerD_14 = ['F4','F5','F6','H4','H5','H6','I1','I2','I3','I4']    #4
    cornerD_16 = ['F7','H7','I5','I6','I7','I8','I9','I10']             #5
    cornerD_20 = ['I11']                            #6
    cornerD = [cornerD_7, cornerD_9, cornerD_11, cornerD_12, cornerD_14, cornerD_16, cornerD_20]
    
    top_Flat_8 = ['J0']                             #0
    top_Flat_10 = ['J1']                            #1
    top_10 = ['E0']                                 #2
    top_Flat_12 = ['J2']                            #3
    top_12 = ['E1','E2','E3','I0']                  #4
    top_14 = ['E4','E5','E6','I1','I2','I3','I4']   #5
    top_16 = ['E7','I5','I6','I7','I8','I9','I10']  #6
    top_20 = ['I11']                                #7
    top = [top_Flat_8, top_Flat_10, top_10, top_Flat_12, top_12, top_14, top_16, top_20]

    bottom_Flat_8 = ['J0']                              #0
    bottom_Flat_10 = ['J1']                             #1
    bottom_10 = ['F0']                                  #2
    bottom_Flat_12 = ['J2']                             #3
    bottom_12 = ['F1','F2','F3','I0']                   #4
    bottom_14 = ['F4','F5','F6','I1','I2','I3','I4']    #5
    bottom_16 = ['F7','I5','I6','I7','I8','I9','I10']   #6
    bottom_20 = ['I11']                                 #7  
    bottom = [bottom_Flat_8, bottom_Flat_10, bottom_10, bottom_Flat_12, bottom_12, bottom_14, bottom_16, bottom_20]

    firstInd_Flat = 0
    firstInd_NoFlat = 2
    lastInd_Flat = 3
    lastInd_NoFlat = 7
    bottomModified = []
    for i in range(nColumns):
        bottomModified.append(False)

    # To PRUNE
    costFrune = []      # Matrix that stores the maximum cost that can be reached from the first position you are in (this one included)
    nAreas = nColumns * 2
    cost = 0
    maxCost = nAreas * listPieces['I11']
    for i in range(2):
        aux = []
        for j in range(nColumns):
            cost += listPieces['I11']
            aux.append(maxCost-cost)
        costFrune.append(aux)

    # Initialization of variables
    solution_1 = initialSolution[0]
    solution_2 = initialSolution[1]
    
    currPos = []  # cornerA, cornerB, cornerC, cornerD, top*, bottom*          # Everything in grid order (not what it says here)
    for i in range(nColumns*2):
        currPos.append(-1)
    
    level = 0
    cost = initialCost
    end = False     

    while (not end  and  level>=0):
        # Generate
        cost = bck_2R_generate(level, currPos, cost, nRooms, nColumns, solution_1, solution_2, 
                                    cornerA, cornerB, cornerC, cornerD, top, bottom, 
                                    firstInd_Flat, firstInd_NoFlat, bottomModified)     
        # isSolution
        if (cost==nRooms):
            end = True
        else:
            # Prune
            continuing = True

            indRow = int(level/nColumns)
            indCol = level%nColumns
            
            costToLevel = bck_2F_calculateCost_toLevel(level, solution_1, solution_2, nColumns)

            # Calculate maximum cost that can be obtained
            maxCost = costToLevel + costFrune[indRow][indCol]
            if (maxCost < nRooms):
                continuing = False

            # Criterion
            if (continuing and level<nColumns*2-1  and  cost<nRooms):
                level += 1
            else:
                # While NO moreSiblings
                while (level>=0  and  not bck_2R_moreSiblings(level, currPos, solution_2, nColumns, len(cornerA), len(bottom), lastInd_Flat, lastInd_NoFlat)):
                    # Go back
                    level, cost, solution_1, solution_2 = bck_2R_goBack(level, currPos, cost, nColumns, solution_1, solution_2, bottomModified, firstInd_Flat, firstInd_NoFlat)
                    
    if end:
        solution = [solution_1, solution_2]
        return solution, nColumns, 2
    
    return -1,-1,-1

def bck_2R_generate(level, p, cost, nRooms, nColumns, solution_1, solution_2, 
                        cornerA, cornerB, cornerC, cornerD, top, bottom, 
                        firstInd_Flat, firstInd_NoFlat, bottomModified):
    
    # Corner A
    if (level == 0):
        cost -= listPieces[solution_1[level]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution_1[level] = cornerA[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerA[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution_1[level] = cornerA[p[level]][indPiece]
        cost += listPieces[solution_1[level]]   

    # Corner B
    elif (level == nColumns-1):
        cost -= listPieces[solution_1[level]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution_1[level] = cornerB[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerB[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution_1[level] = cornerB[p[level]][indPiece]
        cost += listPieces[solution_1[level]]

    # Corner C
    elif (level == nColumns):
        ind = level%nColumns
        cost -= listPieces[solution_2[ind]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution_2[ind] = cornerC[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerC[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution_2[ind] = cornerC[p[level]][indPiece]
        cost += listPieces[solution_2[ind]]

    # Corner D
    elif (level == nColumns*2-1):
        ind = level%nColumns
        cost -= listPieces[solution_2[ind]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution_2[ind] = cornerD[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerD[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution_2[ind] = cornerD[p[level]][indPiece]
        cost += listPieces[solution_2[ind]]
    

    # Top will switch between 'Flat' and 'No Flat' pieces, causing Bottom to do so as well.
    # If Top is 'Flat', Bottom can only have 'Flat' pieces, and the same with 'No Flat'
        # Problem: when Bottom changed his piece because of Top, the first thing done in Generate is p[level]++ -> This causes the entire tree from it to be lost
            # Solution: an array that indicates whether Top has modified Bottom or not
        
    # Top
    elif (level < nColumns):
        
        cost -= listPieces[solution_1[level]]  # Start by removing its own cost

        p[level] += 1
        isCurrFlat = bck_2R_isFlat(top[p[level]][0])
        isBottomFlat = bck_2R_isFlat(solution_2[level])
        # If the type of piece to be used now does not match the one below, the smallest piece that matches the type above is placed below
        if (isCurrFlat != isBottomFlat):
            if isCurrFlat:
                p[level+nColumns] = firstInd_Flat
            else:
                p[level+nColumns] = firstInd_NoFlat
            
            cost -= listPieces[solution_2[level]]  # The cost of the bottom piece that was there is subtracted
            solution_2[level] = bottom[p[level+nColumns]][0]    # The bottom piece is changed
            cost += listPieces[solution_2[level]]  # The cost of the new piece below is added

            bottomModified[level] = True     # We mark that the Bottom piece has been changed

        # Get a random piece for Top (or not)
        if (p[level] in [0,1,2,3,7]):
            solution_1[level] = top[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenTopPAct = len(top[p[level]])
            indPiece = random.randint(0,lenTopPAct-1)
            solution_1[level] = top[p[level]][indPiece]
        
        cost += listPieces[solution_1[level]]  # Add the new cost of the piece
        
    # Bottom
    else:
        ind = level%nColumns
        
        cost -= listPieces[solution_2[ind]]    # It is just needed to substract the cost of the current position
        # The index of the list to search in is only changed if Bottom was NOT modified by Top
        # If it was modified -> The index is maintained and the modification flag is removed
        if (bottomModified[ind]):
            bottomModified[ind] = False
        else:
            p[level] += 1

        # Actually, the list we will access for Bottom depends on the type of Top piece
        isTopFlat = bck_2R_isFlat(solution_1[ind])
        isCurrFlat = bck_2R_isFlat(bottom[p[level]][0])
        while (p[level]<len(bottom)-1  and  isCurrFlat != isTopFlat):
            p[level] += 1
            isCurrFlat = bck_2R_isFlat(bottom[p[level]][0])
        # If there are no more pieces of the same category as the Top one to explore -> DO NOT CONTINUE WITH THIS BRANCH OF BACKTRACKING
        if (p[level]==len(bottom)-1  and  isCurrFlat != isTopFlat):
            cost = nRooms + 1  # It will not be a Solution nor will it pass Criterion   
            p[level] = -5   # To indicate to goBack that there is no piece for this Level
        else:
            # Get a random piece (or not) from the selected list
            if (p[level] in [0,1,2,3,7]):
                solution_2[ind] = bottom[p[level]][0]
            else:
                lenBottomCurrPiece = len(bottom[p[level]])
                indPiece = random.randint(0,lenBottomCurrPiece-1)
                solution_2[ind] = bottom[p[level]][indPiece]

            cost += listPieces[solution_2[ind]]    # Just add the new cost of the piece

    return cost

def bck_2R_moreSiblings(level, p, solution_2, nColumns, lenCorners, lenOrdinaries, lastInd_Flat, lastInd_NoFlat):   
    # Corners
    if (level in [0, nColumns-1, nColumns, nColumns*2-1]):
        return p[level] < lenCorners-1
    # Top
    elif (level < nColumns):
        return p[level] < lenOrdinaries-1
    # Bottom
    else:
        if (p[level] == -5):
            return False
        else:
            ind = level%nColumns
            if (bck_2R_isFlat(solution_2[ind])):
                    return p[level] < lastInd_Flat
            else:
                return p[level] < lastInd_NoFlat    

def bck_2R_goBack(level, p, cost, nColumns, solution_1, solution_2, bottomModified, firstInd_Flat, firstInd_NoFlat):
    # Corner A
    if (level == 0):
        level = -1

    # Corner B
    elif (level == nColumns-1):
        cost -= listPieces[solution_1[level]]   # Substract the cost of the current piece
        solution_1[level] = 'B0'      # Set the default piece 
        p[level] = -1
        cost += listPieces['B0']   # Add the cost of the default piece
        level -= 1

    # Corner C
    elif (level == nColumns):
        ind = level%nColumns 
        cost -= listPieces[solution_2[ind]]
        solution_2[ind] = 'C0'
        p[level] = -1
        cost += listPieces['C0']
        level -= 1

    # Corner D
    elif (level == nColumns*2-1):
        ind = level%nColumns 
        cost -= listPieces[solution_2[ind]]
        solution_2[ind] = 'D0'
        p[level] = -1
        cost += listPieces['D0']
        level -= 1

    # Top
    elif (level < nColumns):
        # Normal procedure
        cost -= listPieces[solution_1[level]]   
        solution_1[level] = 'J0'      
        p[level] = -1
        cost += listPieces['J0']   
        level -= 1

        # If the Bottom piece is not J0 -> It is changed to J0
        if (solution_2[level] != 'J0'):
            cost -= listPieces[solution_2[level]]
            solution_2[level] = 'J0'      
            p[level+nColumns] = firstInd_Flat
            cost += listPieces['J0']
            bottomModified[level] = True   

    # Bottom
    else:
        ind = level%nColumns 
        cost -= listPieces[solution_2[ind]]

        # It must be taken into account that p[level]==-5 (No part was found to generate) and that is why cost==nRooms+1 was set
        if (p[level] == -5):
            # It is needed to take into account whether Top is Flat or not.
            if (bck_2R_isFlat(solution_1[ind])):
                solution_2[ind] = 'J0'
                p[level] = firstInd_Flat
                cost = bck_2R_calculateCost(solution_1, solution_2)
            else:
                solution_2[ind] = 'F0'
                p[level] = firstInd_NoFlat
                cost = bck_2R_calculateCost(solution_1, solution_2)
        # Normal procedure
        else:
            if (bck_2R_isFlat(solution_1[ind])):
                solution_2[ind] = 'J0'
                p[level] = firstInd_Flat
                cost += listPieces['J0']
            else:
                solution_2[ind] = 'F0'
                p[level] = firstInd_NoFlat
                cost += listPieces['F0']

        bottomModified[ind] = True
        level -= 1        

    return level, cost, solution_1, solution_2

def bck_2R_isFlat(piece):
    return piece.startswith('J')     

def bck_2R_calculateCost(solution_1, solution_2):
    cost = 0
    for i in solution_1:
        cost += listPieces[i]
    for j in solution_2:
        cost += listPieces[j]
    
    return cost

def bck_2F_calculateCost_toLevel(level, solution_1, solution_2, nColumns):
    indRow = int(level/nColumns)
    indColumn = level%nColumns

    cost = 0

    if (indRow == 0):
        # Top
        for j in range(indColumn+1):
            cost += listPieces[solution_1[j]]
    else:
        # Top
        for j in range(nColumns):
            cost += listPieces[solution_1[j]]
        # Bottom       
        for j in range(indColumn+1):
            cost += listPieces[solution_2[j]]

    return cost



##########
# X ROWS #
##########

def generateAreas_grid(nRooms, nRowsParam, nColumnsParam):

    nCols, nRows = nColumnsParam, nRowsParam

    print(" Trying: {} Rows - {} Columns".format(nRows, nCols))

    # Generate the smallest and largest cases (within a constrained geometry)   
        # SMALLEST case
    solRow1_small = ['A0']
    solRowLast_small = ['C0']
    for i in range(nCols-2):
        solRow1_small.append('J0')
        solRowLast_small.append('J0')
    solRow1_small.append('B0')
    solRowLast_small.append('D0')
    solution_small = [solRow1_small]
    for i in range(nRows-2):
        solRow = ['G0']
        for j in range(nCols-2):
            solRow.append('J0')
        solRow.append('H0')
        solution_small.append(solRow) 
    solution_small.append(solRowLast_small)
    
    cost_small = 0
    for i in range(nRows):
        for j in range(nCols):
            piece = solution_small[i][j]
            cost_small += listPieces[piece]

            # Cost equal to nRooms    
    if (cost_small == nRooms):
        return solution_small, nCols, nRows 
    

        # BIGGEST case
    solution_big = []
    for i in range(nRows):
        solRow = []
        for j in range(nCols):
            solRow.append('I11')
        solution_big.append(solRow)
    cost_big = nRows * nCols * listPieces['I11']
    
            # Cost equal to nRooms  
    if (cost_big == nRooms): 
        return solution_big, nCols, nRows 

    # Cases where it is not possible to create a suitable layout

        # There are LESS rooms than are needed for the number of columns 
    if (cost_small > nRooms):
        print("\tWARNING: nRooms SMALLER than required for {} columns and {} rows ({})".format(nCols, nRows, cost_small))
        # We test with smaller numbers of columns (RECURSION)
        if (nCols>3):
            s0,s1,s2 = generateAreas_grid(nRooms, nRows, nCols-1)   # First, with layouts with fewer columns
            if (s0 in [-2]):         # Second, with layouts with less rows
                if (nRows > 3):                          
                    return generateAreas_grid(nRooms, nRows-1, nCols)       
                else:
                    return generateAreas_twoRows(nRooms, nCols, 1)
            else:
                return s0, s1, s2
        elif (nColumnsParam == 3):
            return generateAreas_twoRows(nRooms, nRows, 1) 
        else:
            return -2,-2,-2

        # There are MORE rooms than are needed for the number of columns 
    if (cost_big < nRooms):
        print("\tWARNING: nRooms BIGGER than achievable with {} columns and {} rows ({})".format(nCols, nRows, cost_big))
        # We test with bigger numbers of columns or rows (RECURSION)
            # The option is chosen by heuristics (which number is closest to nRooms without going over)
        coste_colExtra = cost_big + (nRows * listPieces['I11'])
        coste_rowExtra = cost_big + (nColumnsParam * listPieces['I11'])
        dif_colExtra = nRooms - coste_colExtra
        dif_rowExtra = nRooms - coste_rowExtra
        if (dif_colExtra < 0  and  dif_rowExtra < 0):
            return -3,-3,-3
        elif (dif_rowExtra < 0):
            return generateAreas_grid(nRooms, nRows, nCols+1)
        elif (dif_colExtra < 0):
            return generateAreas_grid(nRooms, nRows+1, nCols)
        else:
            if (dif_colExtra < dif_rowExtra):
                return generateAreas_grid(nRooms, nRows, nCols+1)
            else:
                return generateAreas_grid(nRooms, nRows+1, nCols)

    # Backtracking from the SMALL solution
    return backtracking_grid(nRooms, nRows, nCols, solution_small, cost_small)


def backtracking_grid(nRooms, nRows, nColumns, initialSolution, initialCost):
    
    # Combination of Pieces

    cornerA_7 = ['A0']                              #0
    cornerA_9 = ['A1','A2']                         #1
    cornerA_11 = ['A3']                             #2
    cornerA_12 = ['E1','E2','E3','G1','G2','G3']    #3
    cornerA_14 = ['E4','E5','E6','G4','G5','G6','I1','I2','I3','I4']    #4
    cornerA_16 = ['E7','G7','I5','I6','I7','I8','I9','I10']             #5
    cornerA_20 = ['I11']                            #6
    cornerA = [cornerA_7, cornerA_9, cornerA_11, cornerA_12, cornerA_14, cornerA_16, cornerA_20]

    cornerB_7 = ['B0']                              #0
    cornerB_9 = ['B1','B2']                         #1
    cornerB_11 = ['B3']                             #2
    cornerB_12 = ['E1','E2','E3','H1','H2','H3']    #3
    cornerB_14 = ['E4','E5','E6','H4','H5','H6','I1','I2','I3','I4']    #4
    cornerB_16 = ['E7','H7','I5','I6','I7','I8','I9','I10']             #5
    cornerB_20 = ['I11']                            #6
    cornerB = [cornerB_7, cornerB_9, cornerB_11, cornerB_12, cornerB_14, cornerB_16, cornerB_20]

    cornerC_7 = ['C0']                              #0
    cornerC_9 = ['C1','C2']                         #1
    cornerC_11 = ['C3']                             #2
    cornerC_12 = ['F1','F2','F3','G1','G2','G3']    #3
    cornerC_14 = ['F4','F5','F6','G4','G5','G6','I1','I2','I3','I4']    #4
    cornerC_16 = ['F7','G7','I5','I6','I7','I8','I9','I10']             #5
    cornerC_20 = ['I11']                            #6
    cornerC = [cornerC_7, cornerC_9, cornerC_11, cornerC_12, cornerC_14, cornerC_16, cornerC_20]

    cornerD_7 = ['D0']                              #0
    cornerD_9 = ['D1','D2']                         #1
    cornerD_11 = ['D3']                             #2
    cornerD_12 = ['F1','F2','F3','H1','H2','H3']    #3
    cornerD_14 = ['F4','F5','F6','H4','H5','H6','I1','I2','I3','I4']    #4
    cornerD_16 = ['F7','H7','I5','I6','I7','I8','I9','I10']             #5
    cornerD_20 = ['I11']                            #6
    cornerD = [cornerD_7, cornerD_9, cornerD_11, cornerD_12, cornerD_14, cornerD_16, cornerD_20]
    
    top_Flat_8 = ['J0']                             #0
    top_Flat_10 = ['J1']                            #1
    top_10 = ['E0']                                 #2
    top_Flat_12 = ['J2']                            #3
    top_12 = ['E1','E2','E3','I0']                  #4
    top_14 = ['E4','E5','E6','I1','I2','I3','I4']   #5
    top_16 = ['E7','I5','I6','I7','I8','I9','I10']  #6
    top_20 = ['I11']                                #7
    top = [top_Flat_8, top_Flat_10, top_10, top_Flat_12, top_12, top_14, top_16, top_20]

    bottom_Flat_8 = ['J0']                              #0
    bottom_Flat_10 = ['J1']                             #1
    bottom_10 = ['F0']                                  #2
    bottom_Flat_12 = ['J2']                             #3
    bottom_12 = ['F1','F2','F3','I0']                   #4
    bottom_14 = ['F4','F5','F6','I1','I2','I3','I4']    #5
    bottom_16 = ['F7','I5','I6','I7','I8','I9','I10']   #6
    bottom_20 = ['I11']                                 #7  
    bottom = [bottom_Flat_8, bottom_Flat_10, bottom_10, bottom_Flat_12, bottom_12, bottom_14, bottom_16, bottom_20]

        # Left and Right will only have 'T' and '+', no '-'
    left_10 = ['G0']                                #0
    left_12 = ['G1', 'G2', 'G3', 'I0']              #1
    left_14 = ['G4','G5','G6','I1','I2','I3','I4']  #2
    left_16 = ['G7','I5','I6','I7','I8','I9','I10'] #3
    left_20 = ['I11']                               #4
    left = [left_10, left_12, left_14, left_16, left_20] 

    right_10 = ['H0']                                #0
    right_12 = ['H1', 'H2', 'H3', 'I0']              #1
    right_14 = ['H4','H5','H6','I1','I2','I3','I4']  #2
    right_16 = ['H7','I5','I6','I7','I8','I9','I10'] #3
    right_20 = ['I11']                               #4
    right = [right_10, right_12, right_14, right_16, right_20] 

    middle_2Flat_8 = ['J0']                         #0
    middle_2Flat_10 = ['J1']                        #1
    middle_TopFlat_10 = ['E0']                      #2
    middle_BotFlat_10 = ['F0']                      #3
    middle_2Flat_12 = ['J2']                        #4
    middle_TopFlat_12 = ['E1','E2','E3']            #5
    middle_BotFlat_12 = ['F1','F2','F3']            #6
    middle_12 = ['I0']                              #7
    middle_TopFlat_14 = ['E4','E5','E6']            #8
    middle_BotFlat_14 = ['F4','F5','F6']            #9
    middle_14 = ['I1','I2','I3','I4']               #10
    middle_TopFlat_16 = ['E7']                      #11
    middle_BotFlat_16 = ['F7']                      #12
    middle_16 = ['I5','I6','I7','I8','I9','I10']    #13
    middle_20 = ['I11']                             #14  
    middle = [middle_2Flat_8, 
                middle_2Flat_10, middle_TopFlat_10, middle_BotFlat_10, 
                middle_2Flat_12, middle_TopFlat_12, middle_BotFlat_12, middle_12, 
                middle_TopFlat_14, middle_BotFlat_14, middle_14, 
                middle_TopFlat_16, middle_BotFlat_16, middle_16, 
                middle_20]

    firstInd_Bottom_Flat = 0
    firstInd_Bottom_NoFlat = 2
    lastInd_Bottom_Flat = 3
    lastInd_Bottom_NoFlat = 7
    
    firstInd_Middle_TopFlat = 0     # Index of the first piece that is Flat on Top (regardless of whether it is flat on the Bottom or not)
    lastInd_Middle_TopFlat = 11     # Same but the last
    firstInd_Middle_NoTopFlat = 3   # Index of the first piece that is NOT Flat on top (regardless of whether it is flat on the Bottom or not)
    lastInd_Middle_NoFlat = 14      # Last piece that is NOT Flat because a G

    bottomModified = []
    for i in range(nRows):
        row = []
        for j in range(nColumns):
            row.append(False)
        bottomModified.append(row)

    indexLeftColumn = []
    for i in range(1,nRows-1):
        indexLeftColumn.append(i*nColumns)
    indexRightColumn = []
    for i in range(1,nRows-1):
        indexRightColumn.append(i*nColumns+nColumns-1)

    # To PRUNE
    costPrune = []      # Matrix that stores the maximum cost that can be reached from the first position you are in (this one included)
    nAreas = nColumns * nRows
    cost = 0
    maxCost = nAreas * listPieces['I11']
    for i in range(nRows):
        aux = []
        for j in range(nColumns):
            cost += listPieces['I11']
            aux.append(maxCost-cost)
        costPrune.append(aux)

    # Initialization of variables
    solution = initialSolution
    
    currPos = []  # cornerA, cornerB, cornerC, cornerD, top*, bottom*, left*, right*, middle*      # Todo en orden de la cuadrícula (no en el que aquí pone)
    for i in range(nRows*nColumns):
        currPos.append(-1)
    
    level = 0
    cost = initialCost
    end = False     

    while (not end  and  level>=0):
        # Generate
        cost = bck_gr_generar(level, currPos, cost, nRooms, nRows, nColumns, solution, 
                                    cornerA, cornerB, cornerC, cornerD, top, bottom, left, right, middle,
                                    indexLeftColumn, indexRightColumn, 
                                    firstInd_Bottom_Flat, firstInd_Bottom_NoFlat, firstInd_Middle_TopFlat, firstInd_Middle_NoTopFlat, 
                                    bottomModified)

        # isSolution
        if (cost==nRooms):
            end = True
        else:
            # Prune
            continuing = True

            indRow = int(level/nColumns)
            indCol = level%nColumns
            
            costTolevel = bck_gr_calculateCost_toLevel(level, solution, nColumns)

            # Calculate maximum cost that can be obtained
            maxCost = costTolevel + costPrune[indRow][indCol]
            if (maxCost < nRooms):
                continuing = False
            
            # Criterion  
            if (continuing and level<nColumns*nRows-1  and  cost<nRooms):
                level += 1
            else:
                # While NO moreSiblings
                while (level>=0  and  not bck_gr_moreSiblings(level, currPos, solution, nRows, nColumns, 
                                                                len(cornerA), len(bottom), len(left), 
                                                                indexLeftColumn, indexRightColumn,
                                                                lastInd_Bottom_Flat, lastInd_Bottom_NoFlat, lastInd_Middle_TopFlat, lastInd_Middle_NoFlat)):
                    # goBack
                    level, cost, solution = bck_gr_goBack(level, currPos, cost, nRows, nColumns, solution,
                                                                indexLeftColumn, indexRightColumn, 
                                                                firstInd_Bottom_Flat, firstInd_Bottom_NoFlat, firstInd_Middle_TopFlat, firstInd_Middle_NoTopFlat,
                                                                bottomModified)
                    
    if end:
        return solution, nColumns, nRows
    
    return -1,-1,-1

def bck_gr_generar(level, p, cost, nRooms, nRows, nColumns, solution,        
                        cornerA, cornerB, cornerC, cornerD, top, bottom, left, right, middle,
                        indicesLeftColumn, indicesRightColumn, 
                        firstInd_Bottom_Flat, firstInd_Bottom_NoFlat, firstInd_Middle_TopFlat, firstInd_Middle_NoTopFlat, 
                        bottomModified):
    
    # Corner A
    if (level == 0):    # solution[0][0]  ==  solution[0][nivel]
        cost -= listPieces[solution[0][0]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution[0][0] = cornerA[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerA[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution[0][0] = cornerA[p[level]][indPiece]
        cost += listPieces[solution[0][0]]   

    # Corner B
    elif (level == nColumns-1):     # solution[0][nColumns-1]  ==  solution[0][level] 
        cost -= listPieces[solution[0][level]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution[0][level] = cornerB[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerB[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution[0][level] = cornerB[p[level]][indPiece]
        cost += listPieces[solution[0][level]]

    # Corner C
    elif (level == (nRows-1)*nColumns):    # solution[nRows-1][0]
        cost -= listPieces[solution[nRows-1][0]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution[nRows-1][0] = cornerC[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerC[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution[nRows-1][0] = cornerC[p[level]][indPiece]
        cost += listPieces[solution[nRows-1][0]]

    # Corner D
    elif (level == (nRows*nColumns)-1):    # solution[nRows-1][nColumns-1]
        cost -= listPieces[solution[nRows-1][nColumns-1]]
        p[level] += 1
        if (p[level] in [0,2,6]):
            solution[nRows-1][nColumns-1] = cornerD[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenCornerCurrPiece = len(cornerD[p[level]])
            indPiece = random.randint(0,lenCornerCurrPiece-1)
            solution[nRows-1][nColumns-1] = cornerD[p[level]][indPiece]
        cost += listPieces[solution[nRows-1][nColumns-1]]
    

    # Left
    elif (level in indicesLeftColumn):  # solution[level/nColumns][0]  ==  solution[indRow][0]
        indRow = int(level/nColumns)
        cost -= listPieces[solution[indRow][0]]
        p[level] += 1
        if (p[level] in [0,4]):
            solution[indRow][0] = left[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenLeftPAct = len(left[p[level]])
            indPiece = random.randint(0,lenLeftPAct-1)
            solution[indRow][0] = left[p[level]][indPiece]
        cost += listPieces[solution[indRow][0]]    

    # Right
    elif (level in indicesRightColumn):     # solution[level/nColumns][nColumns-1]  ==  solucion[indRow][nColumns-1]
        indRow = int(level/nColumns)
        cost -= listPieces[solution[indRow][nColumns-1]]
        p[level] += 1
        if (p[level] in [0,4]):
            solution[indRow][nColumns-1] = right[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenRightPAct = len(right[p[level]])
            indPiece = random.randint(0,lenRightPAct-1)
            solution[indRow][nColumns-1] = right[p[level]][indPiece]
        cost += listPieces[solution[indRow][nColumns-1]]   


    # Top will change between 'Flat' and 'Non-Flat' pieces, causing the Bottom Row piece to do so as well.
    # If Top is 'Flat', the Bottom Row can only have 'Flat' pieces on Top, and the same with 'No Flat'
        # Problem: when Bottom changed his piece because of Top, the first thing done in Generate is p[level]++ -> This causes the entire tree from him to be lost
            # Solution: an array that indicates whether Top has modified the piece in the Bottom Row or not.

    # Top
    elif (level < nColumns):        # solution[0][level]
        cost -= listPieces[solution[0][level]]  # Substract the cost of the piece

        p[level] += 1
        isCurrFlat = bck_gr_isTopBotFlat(top[p[level]][0])
        isUnderRowFlat = bck_gr_isMiddleFlat(solution[1][level])    # Piece located just below: solution[1][level]
        # If the type of the current piece does not match the type of the piece below, the smallest piece that matches the type above is placed at the bottom
            # Do NOT match when:
                # - TOP is Flat         -   MIDDLE is NOT Flat on top (0, 3)
                # - TOP is NOT Flat     -   MIDDLE is Flat on top (1, 2)   
        if ((isCurrFlat  and  isUnderRowFlat in [0,3]) or (not isCurrFlat  and  isUnderRowFlat in [1,2])):
            if isCurrFlat:
                p[level+nColumns] = firstInd_Middle_TopFlat     # The bottom piece has to be FLAT on top
            else:
                p[level+nColumns] = firstInd_Middle_NoTopFlat     # The bottom piece has to be NO FLAT on Top
            
            cost -= listPieces[solution[1][level]]  # Subtract the cost of the piece below 
            solution[1][level] = middle[p[level+nColumns]][0]    # Change the bottom piece
            cost += listPieces[solution[1][level]]  # Add the cost of the new piece below    

            bottomModified[1][level] = True     # Indicate that the piece below has been modified

        # Get a random (or not) piece for Top 
        if (p[level] in [0,1,2,3,7]):
            solution[0][level] = top[p[level]][0]
        else:   # Obtain a random piece from the list of pieces that have the same cost
            lenTopPAct = len(top[p[level]])
            indPiece = random.randint(0,lenTopPAct-1)
            solution[0][level] = top[p[level]][indPiece]
        
        cost += listPieces[solution[0][level]]  # Add the cost of the new piece
        
    # Bottom
    elif (level > (nRows-1)*nColumns  and  level < (nRows*nColumns)-1):       # solution[nRows-1][level%nColumns]  ==  solution[nRows-1][indCol]
        indCol = level%nColumns
        cost -= listPieces[solution[nRows-1][indCol]]    # Just have to subtract the cost of its piece
        
        # Only change the index of the list to search in if Bottom was NOT modified by the Top Row piece
        # If it was modified -> The index is maintained and the modification flag is removed
        if (bottomModified[nRows-1][indCol]):
            bottomModified[nRows-1][indCol] = False
        else:
            p[level] += 1

        # The list we will access for Bottom depends on the type of piece we have in the Top Row
        isCurrFlat = bck_gr_isTopBotFlat(bottom[p[level]][0])
        isOverRowFlat = bck_gr_isMiddleFlat(solution[nRows-2][indCol])    # Piece just above: solution[nRows-2][indCol]
        while (p[level]<len(bottom)-1  and  ((isCurrFlat  and  isOverRowFlat in [0,2]) or (not isCurrFlat  and  isOverRowFlat in [1,3]))):
            p[level] += 1
            isCurrFlat = bck_gr_isTopBotFlat(bottom[p[level]][0])
        # If there are no more pieces of the same category as the one in the Row Above to explore -> DO NOT CONTINUE WITH THIS BRANCH OF THE BACKTRACKING
        if (p[level]==len(bottom)-1  and  isCurrFlat != isOverRowFlat):
            cost = nRooms + 1  # It will not be a Solution nor will it pass Criterion  
            p[level] = -5   # To indicate to goBack that there is no piece for this Level
        else:
            # Get the random piece (or not) from the selected list
            if (p[level] in [0,1,2,3,7]):
                solution[nRows-1][indCol] = bottom[p[level]][0]
            else:
                lenBottomPAct = len(bottom[p[level]])
                indPiece = random.randint(0,lenBottomPAct-1)
                solution[nRows-1][indCol] = bottom[p[level]][indPiece]

            cost += listPieces[solution[nRows-1][indCol]]    # Just add the cost of its piece
    

    # Middle
    else:                           # solution[level/nColumns][level%nColumns] == solution[indRow][indCol]
        indRow = int(level/nColumns)
        indCol = level%nColumns
        cost -= listPieces[solution[indRow][indCol]]  # Empieza quitando su propio coste

        # The index of the list to search in is only changed if the piece was NOT modified by the one in the Row Above
        # If it was modified -> The index is maintained and the modification flag is removed
        if (bottomModified[indRow][indCol]):
            bottomModified[indRow][indCol] = False
        else:
            p[level] += 1

        # The list we will access depends on the type of piece we have in the Top Row
        isCurrFlat = bck_gr_isMiddleFlat(middle[p[level]][0])
        isOverRowFlat = bck_gr_isMiddleFlat(solution[indRow-1][indCol])    # Piece located just above: solution[indRow-1][indCol]
        matchFlat = isOverRowFlat in [1,3] and isCurrFlat in [1,2]
        matchNoFlat = isOverRowFlat in [0,2] and isCurrFlat in [0,3]
        doMatch = matchFlat or matchNoFlat
        while(p[level]<len(middle)-1 and not doMatch):
            p[level] += 1
            isCurrFlat = bck_gr_isMiddleFlat(middle[p[level]][0])

            matchFlat = isOverRowFlat in [1,3] and isCurrFlat in [1,2]
            matchNoFlat = isOverRowFlat in [0,2] and isCurrFlat in [0,3]
            doMatch = matchFlat or matchNoFlat 
        # If there are no more pieces of the same category as the one in the Row Above to explore -> DO NOT CONTINUE WITH THIS BRANCH OF THE BACKTRACKING
        if (p[level]==len(middle)-1  and  not doMatch):
            cost = nRooms + 1  # It will not be a Solution nor will it pass Criterion   
            p[level] = -5   # To indicate to goBack that there is no piece for this Level 
        else:
            # Get a random piece (or not) from the selected list
            if (p[level] in [0,1,2,3,4,7,11,12,14]):
                solution[indRow][indCol] = middle[p[level]][0]
            else:
                lenMiddlePAct = len(middle[p[level]])
                indPiece = random.randint(0,lenMiddlePAct-1)
                solution[indRow][indCol] = middle[p[level]][indPiece]
    
            cost += listPieces[solution[indRow][indCol]]  # Add the new cost of its piece

            # Change (or not) the bottom piece
            isCurrFlat = bck_gr_isMiddleFlat(middle[p[level]][0])
            isUnderRowFlat = bck_gr_isMiddleFlat(solution[indRow+1][indCol])    # Piece located just below: solution[indRow+1][indCol]
            # If the current piece type does not match that of the piece below, the smallest piece that matches the type above is placed at the bottom
                # Do NOT match when:
                    # - Above is Flat below         -   Below is NOT Flat above (0, 3)
                    # - Above is NOT Flat below     -   MIDDLE is Flat on top (1, 2)   
            if ((isCurrFlat in [1,3]  and  isUnderRowFlat in [0,3]) or (isCurrFlat in [0,2]  and  isUnderRowFlat in [1,2])):
                if (isCurrFlat in [1,3]):       # Top Flat   ->  The bottom one has to be FLAT on top
                    if (indRow == nRows-2):     # Below is Bottom
                        p[level+nColumns] = firstInd_Bottom_Flat
                    else:
                        p[level+nColumns] = firstInd_Middle_TopFlat   
                else:   # Above Not Flat    ->  The bottom one has to be NO FLAT on top
                    if (indRow == nRows-2):    # Below is Bottom
                        p[level+nColumns] = firstInd_Bottom_NoFlat
                    else:
                        p[level+nColumns] = firstInd_Middle_NoTopFlat
                
                cost -= listPieces[solution[indRow+1][indCol]]  # Subtract the cost of the part below
                # Change the bottom piece
                if (indRow == nRows-2):    # Below is Bottom
                    solution[indRow+1][indCol] = bottom[p[level+nColumns]][0]
                else: 
                    solution[indRow+1][indCol] = middle[p[level+nColumns]][0]
                cost += listPieces[solution[indRow+1][indCol]]  # Add the cost of the new bottom piece    

                bottomModified[indRow+1][indCol] = True     # Indicate that the piece below has been modified

    return cost

def bck_gr_moreSiblings(level, p, solution, nRows, nColumns,        
                        lenCorners, lenTopBottom, lenLeftRight,
                        indicesLeftColumn, indicesRightColumn,
                        lastInd_Bottom_Flat, lastInd_Bottom_NoFlat, lastInd_Middle_TopFlat, lastInd_Middle_NoFlat):   
    # Corners
    if (level in [0, nColumns-1, (nRows-1)*nColumns, (nRows*nColumns)-1]):
        return p[level] < lenCorners-1
    # Left
    elif (level in indicesLeftColumn):
        return p[level] < lenLeftRight-1
    # Right
    elif (level in indicesRightColumn):
        return p[level] < lenLeftRight-1
    # Top
    elif (level < nColumns):
        return p[level] < lenTopBottom-1
    # Bottom
    elif (level > (nRows-1)*nColumns  and  level < (nRows*nColumns)-1):
        if (p[level] == -5):
            return False
        else:
            indCol = level%nColumns
            if (bck_gr_isTopBotFlat(solution[nRows-1][indCol])):
                    return p[level] < lastInd_Bottom_Flat
            else:
                return p[level] < lastInd_Bottom_NoFlat    
    # Middle
    else:
        if (p[level] == -5):
            return False
        else:
            indRow = int(level/nColumns)
            indCol = level%nColumns
            flat = bck_gr_isMiddleFlat(solution[indRow][indCol])
            if (flat == 2  or flat == 1):     # Flat above (regardless of whether it is flat below)
                return p[level] < lastInd_Middle_TopFlat
            else:   # Not Flat on top
                return p[level] < lastInd_Middle_NoFlat

def bck_gr_goBack(level, p, cost, nRows, nColumns, solution, 
                    indicesLeftColumn, indicesRightColumn,
                    firstInd_Bottom_Flat, firstInd_Bottom_NoFlat, firstInd_Middle_TopFlat, firstInd_Middle_NoTopFlat,
                    bottomModified):
    # Corner A
    if (level == 0):
        level = -1

    # Corner B
    elif (level == nColumns-1):
        cost -= listPieces[solution[0][level]]   # Subtract the cost of the current piece
        solution[0][level] = 'B0'      # Add the default part to its position (position 0 of its list)
        p[level] = -1
        cost += listPieces['B0']   # Add the cost of the default part
        level -= 1

    # Corner C
    elif (level == (nRows-1)*nColumns):
        cost -= listPieces[solution[nRows-1][0]]
        solution[nRows-1][0] = 'C0'
        p[level] = -1
        cost += listPieces['C0']
        level -= 1

    # Corner D
    elif (level == (nRows*nColumns)-1):
        cost -= listPieces[solution[nRows-1][nColumns-1]]
        solution[nRows-1][nColumns-1] = 'D0'
        p[level] = -1
        cost += listPieces['D0']
        level -= 1

    # Left
    elif (level in indicesLeftColumn):
        indRow = int(level/nColumns)
        cost -= listPieces[solution[indRow][0]]
        solution[indRow][0] = 'G0'
        p[level] = -1
        cost += listPieces['G0']
        level -= 1

    # Right
    elif (level in indicesRightColumn):
        indRow = int(level/nColumns)
        cost -= listPieces[solution[indRow][nColumns-1]]
        solution[indRow][nColumns-1] = 'H0'
        p[level] = -1
        cost += listPieces['H0']
        level -= 1    


    # Top
    elif (level < nColumns):
        # Normal procedure
        cost -= listPieces[solution[0][level]]   
        solution[0][level] = 'J0'      
        p[level] = -1
        cost += listPieces['J0']   
        level -= 1

        # If the Bottom piece is Not J0 -> It is changed to J0
        if (solution[1][level] != 'J0'):
            cost -= listPieces[solution[1][level]]
            solution[1][level] = 'J0'      
            p[level+nColumns] = firstInd_Middle_TopFlat
            cost += listPieces['J0']
            bottomModified[1][level] = True

    # Bottom
    elif (level > (nRows-1)*nColumns  and  level < (nRows*nColumns)-1):
        indCol = level%nColumns 
        cost -= listPieces[solution[nRows-1][indCol]]

        # It must be taken into account that p[level]==-5 (No piece was found to generate) and that is why cost==nRooms+1 was set
        if (p[level] == -5):
            # Take into account whether or not the piece on top is flat on bottom
            if (bck_gr_isMiddleFlat(solution[nRows-2][indCol]) in [1,3]):  # Above is Flat
                solution[nRows-1][indCol] = 'J0'
                p[level] = firstInd_Bottom_Flat
                cost = bck_gr_calculateCost(solution, nRows, nColumns)
            else:
                solution[nRows-1][indCol] = 'F0'
                p[level] = firstInd_Bottom_NoFlat
                cost = bck_gr_calculateCost(solution, nRows, nColumns)
        # Normal procedure  ->  Take into account whether or not the piece on top is flat on bottom
        else:
            if (bck_gr_isMiddleFlat(solution[nRows-2][indCol]) in [1,3]):  # Above is Flat
                solution[nRows-1][indCol] = 'J0'
                p[level] = firstInd_Bottom_Flat
                cost += listPieces['J0']
            else:
                solution[nRows-1][indCol] = 'F0'
                p[level] = firstInd_Bottom_NoFlat
                cost += listPieces['F0']

        bottomModified[nRows-1][indCol] = True
        level -= 1        

    # Middle
    else:
        indRow = int(level/nColumns)
        indCol = level%nColumns
        cost -= listPieces[solution[indRow][indCol]]

        # It must be taken into account that p[level]==-5 (No piece was found to generate) and that is why cost==nRooms+1 was set
        if (p[level] == -5):
            # Take into account whether or not the piece on top is flat on bottom
            if (bck_gr_isMiddleFlat(solution[indRow-1][indCol]) in [1,3]):  # Above is Flat
                solution[indRow][indCol] = 'J0'
                p[level] = firstInd_Middle_TopFlat
                cost = bck_gr_calculateCost(solution, nRows, nColumns)
            else:
                solution[nRows-1][indCol] = 'F0'
                p[level] = firstInd_Middle_NoTopFlat
                cost = bck_gr_calculateCost(solution, nRows, nColumns)
        # Normal procedure  ->  Take into account whether or not the piece on top is flat on bottom
        else:
            if (bck_gr_isMiddleFlat(solution[indRow-1][indCol]) in [1,3]):  # Above is Flat
                solution[indRow][indCol] = 'J0'
                p[level] = firstInd_Middle_TopFlat
                cost += listPieces['J0']
            else:
                solution[indRow][indCol] = 'F0'
                p[level] = firstInd_Middle_NoTopFlat
                cost += listPieces['F0']
        
        bottomModified[indRow][indCol] = True
               
        # As in TOP, it is checked if the piece below is J0
        if (solution[indRow+1][indCol] != 'J0'):
            cost -= listPieces[solution[indRow+1][indCol]]
            solution[indRow+1][indCol] = 'J0'      
            if (indRow == nRows-2):    # Check if the next Row is Bottom
                p[level+nColumns] = firstInd_Bottom_Flat
            else:
                p[level+nColumns] = firstInd_Middle_TopFlat
            cost += listPieces['J0']
            
            bottomModified[indRow+1][indCol] = True

        level -= 1 
        
    return level, cost, solution

def bck_gr_isTopBotFlat(piece):        
    return piece.startswith('J')

def bck_gr_isMiddleFlat(piece):        
    if (piece.startswith('J')):
        return 1
    elif (piece.startswith('E')):   # Flat on top
        return 2
    elif (piece.startswith('F')):   # Flat on bottom
        return 3
    else:
        return 0

def bck_gr_calculateCost(solution, nRows, nColumns):        
    cost = 0
    for i in range(nRows):
        for j in range(nColumns):
            cost += listPieces[solution[i][j]]
    
    return cost

def bck_gr_calculateCost_toLevel(level, solution, nColumns):        
    indRow = int(level/nColumns)
    indColumn = level%nColumns

    cost = 0
    # Top Rows
    for i in range(indRow):
        for j in range(nColumns):
            cost += listPieces[solution[i][j]]
    # Level row      
    for j in range(indColumn+1):
        cost += listPieces[solution[indRow][j]]

    return cost
