def printHospital(L):
    file = open("hospital.txt", 'w')
    toWrite = ""
    for l in L:
        toWrite += "{},{}\n".format(l.id,l.name.value)
        #print("{},{}".format(l.id,l.name.value))
        if l.children is not None:
            toWrite += "children\n"
            #print("children")
            for child in l.children:
                toWrite += "{},{}\n".format(child.id,child.name.value)
                #print("{},{}".format(child.id,child.name.value))
            toWrite += "children_end\n"
            #print("children_end")
        if l.located_in is not None:
            parent = l.located_in
            toWrite += "parent\n"
            #print("parent")
            toWrite += "{},{}\n".format(parent.id,parent.name.value)
            #print("{},{}".format(parent.id,parent.name.value))
        if l.adjacent is not None:
            toWrite += "neighbours\n"
            #print("neighbours")
            for neighbour in l.adjacent:
                toWrite += "{},{}\n".format(neighbour.id,neighbour.name.value)
                #print("{},{}".format(neighbour.id,neighbour.name.value))
            toWrite += "neighbours_end\n"
            #print("neighbours_end")
    file.write(toWrite)
    file.close()
