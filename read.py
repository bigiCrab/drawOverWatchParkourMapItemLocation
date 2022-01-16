import re


def readMap(filePath):
    fp = filePath

    f = open(fp, 'r', encoding="utf-8")
    lines = f.read()
    # print(lines)
    # print(type(lines))
    f.close()

    return lines


def printLocations(fileLines, targetLocations: str):
    arr = re.findall(r"Global\."+targetLocations +
                     "\[\d\] = .*?;", fileLines, re.DOTALL)
    targetStr = "\n".join(arr)
    print(targetStr)
    if len(arr) > 0:
        return targetStr

    targetMatch = re.search(r"Global\."+targetLocations +
                            " = .*?;", fileLines, re.DOTALL)
    if targetMatch is None:
        print("# cant find "+targetLocations+"!!")
        return
    targetStr = re.sub(r"Array\(", '[', targetMatch.group())
    targetStr = re.sub(r"\);", '];', targetStr)
    print(targetStr)
    return targetStr


def getAllLocs(filePath="map/1CFV4.ow"):

    lines = readMap(filePath)

    targetLocNames = ["ZoneLocations", "HeroLocations",
                      "UnlockLocations", "EasterEggLocations"]
    # targetLocNames = ["ZoneLocations", "HeroLocations", "UnlockLocations"]
    # targetLocNames = ["ZoneLocations", "HeroLocations", "UnlockLocations","PortalLocations"]

    result = ''
    for targetLocName in targetLocNames:
        result += printLocations(lines, targetLocName)
    return result
