
from writerRDF import setFolderOutputRDF
from variablesWriter import nameFiles_Classes, nameFiles_Rels


##############
# FILE UNION #
##############

def getInfiles_Classes(folderClasses):
    infiles = ["{}{}{}".format(folderClasses, nameFiles_Classes['patient'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['episode'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['death'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['hospitalization'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['radiology'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['surgery'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['testMicro'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['microorganism'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['uh'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['service'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['bed'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['room'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['corridor'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['area'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['unit'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['block'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['floor'], '.nt'),
             "{}{}{}".format(folderClasses, nameFiles_Classes['building'], '.nt')]
    
    return infiles

def getInfiles_Relations(folderRelations, star):
    if star:
        extension = '.ttl'
    else:
        extension = '.nt'

    infiles = ["{}{}{}".format(folderRelations, nameFiles_Rels['ep_pat'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['ev_ep'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['test_micro'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['ev_bed'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['ev_uh'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['serv_uh'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['uh_bed'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['bed_room'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['room_corridor'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['corridor_area'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['area_block'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['area_unit'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['area_floor'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['block_floor'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['unit_floor'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['floor_building'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['bed_nt'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['bed_ot'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['room_nt'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['room_ot'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['corridor_nt'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['block_nt'], extension),
             "{}{}{}".format(folderRelations, nameFiles_Rels['unit_nt'], extension)]  
    
    return infiles



def unionRDF_Files_classes(folderClasses):
    
    infiles = getInfiles_Classes(folderClasses)

    outfileName = folderClasses + "\\Classes_complete.nt"
    with open(outfileName, "w") as outfile:
        for infileName in infiles:
            with open(infileName, "r") as infile:
                outfile.write(infile.read())
                outfile.write('\n')
                infile.close()

    outfile.close()
    print(" - {} : Completed".format(outfileName))


def unionRDF_Files_Relations(folderRelations, star):

    infiles = getInfiles_Relations(folderRelations, star)

    if star:
        extension = '.ttl'
    else:
        extension = '.nt'
    outfileName = folderRelations + "\\Relations_complete" + extension
    with open(outfileName, "w") as outfile:
        for infileName in infiles:
            with open(infileName, "r") as infile:
                outfile.write(infile.read())
                outfile.write('\n')
                infile.close()

    outfile.close()
    print(" - {} : Completed".format(outfileName))


def unionRDF_Files_Full(dir, folderClasses, folderRelations, star):
    infiles_Classes = getInfiles_Classes(folderClasses)
    infiles_Rels = getInfiles_Relations(folderRelations, star)

    if star:
        extension = '.nt'
    else:
        extension = '.ttl'
    outfileName = dir + "\\data_complete" + extension
    with open(outfileName, "w") as outfile:
        for infileName in infiles_Classes:
            with open(infileName, "r") as infile:
                outfile.write(infile.read())
                outfile.write('\n')
                infile.close()

        for infileName in infiles_Rels:
            with open(infileName, "r") as infile:
                outfile.write(infile.read())
                outfile.write('\n')
                infile.close()

    outfile.close()
    print(" - {} : Completed".format(outfileName))


########
# MAIN #
########

def unionFiles(folder, star):
    folderClasses, folderRelations = setFolderOutputRDF(folder)
    unionRDF_Files_classes(folderClasses)
    unionRDF_Files_Relations(folderRelations, star)
    
    unionRDF_Files_Full(folder, folderClasses, folderRelations, star)

