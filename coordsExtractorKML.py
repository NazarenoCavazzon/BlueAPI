def getFilesInFolder(path):
    from os import walk
    f = []
    names = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        names = filenames
        break
    return names

def checkKMLInFolder(path):
    import os
    count = []
    files = getFilesInFolder(path)
    for file in files:
        file = str(file)
        name, extension = os.path.splitext(path+file)
        if extension == ".kml":
            count.append(file)
    for kml in count:
        if kml[:2] == "~$":
            count.remove(kml)
    return count

def printArray(array):
    array_numbers = 0
    for i, j in enumerate(array):
        print(str(i+1)+'_ '+str(j.split(".")[0]))
        array_numbers += 1
    return array_numbers

def clear(): 
    import os
    return os.system("cls")

def main():
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    import os
    almostList = []
    finalList = []
    cacheList = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
    path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    kmls = checkKMLInFolder(path)
    lines = "="*80
    counter = 0
    clear()
    print(lines)
    print("Detectamos",len(kmls),"kmls en la carpeta, seleccione el que quiere usar")
    print(lines)
    printArray(kmls)
    print(lines)
    kmlSeleccion = input("Opcion: ")
    while str(kmlSeleccion) not in numbers[0:len(kmls)+1]:
        clear()
        print(lines)
        print("Ingrese una opcion valida")
        print(lines)
        printArray(kmls)
        print(lines)
        kmlSeleccion = input("Opcion: ")

    kmlSeleccion = int(kmlSeleccion)
    excelSeleccionado = kmls[kmlSeleccion-1]
    with open(excelSeleccionado, "r") as f:
        soup = bs(f,'lxml')
        coordinates = soup.find("coordinates")
        for element in coordinates:
            elementList = element.split(",")
        for element in elementList:
            elementClean = element.split("-")
            try: 
                almostList.append(elementClean[1])
            except:
                pass
        for element in almostList:
            if counter == 0:            
                cacheList.append(float("-"+element))
                counter += 1
            elif counter == 1:
                cacheList.append(float("-"+element))
                finalList.append([cacheList[1], cacheList[0]])
                cacheList = []
                counter = 0
    clear()
    print(finalList)
    input("copia tranqui capo")
    main()

if __name__ == '__main__':
    main()