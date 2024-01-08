from classes import Patient

def parsePatients():
    
    dicPatients = {}

    with open(".\\Input\\patients.csv") as file:
        for lineString in file:
            
            lineString = str(lineString)
            line = lineString.split(';')
            
            id = int(line[0])
            age = int(line[1])
            sexLetter = line[2]
            if (sexLetter == 'M'):
                sex = False
            else:
                sex = True                
            death = line[len(line)-4].rstrip()
            if death=='False':
                death = False
            elif death=='True':
                death = True
            patient = Patient(id,age,sex,death)
            dicPatients[id] = patient

    file.close()

    return dicPatients
