import math
from datetime import datetime

# Pisanie programu plus przypominiane Pythona ok 40min
def main():
    name, personDate = inputData()

    yp = calcWave(personDate, 23)
    ye = calcWave(personDate, 28)
    yi = calcWave(personDate, 33)

    displayPersonInfo(name, personDate, "Hi", [yp, ye, yi])

    return

def calcWave(birthDate, y):
    daysDiff = (datetime.today() - birthDate).days
    return math.sin((2 * math.pi / y) * daysDiff)

def displayPersonInfo(name, birthDate, info, wave):
    nameList = ["Physical", "Emotional", "INTELLECTUAL"]
    print()
    print(info)
    print(name)
    print("Birthday: ", birthDate)
    for index, (wave_val, name) in enumerate(zip(wave, nameList)):
        print(f"{name}: {wave_val}")
        intepreteWaveVal(wave_val, index, birthDate)
        print()
    return

def intepreteWaveVal(val, counter, birthDate):
    if val > 0.5:
        print("GRATULACJE WYSOKIEGO WYNIKU")
    elif val < -0.5:
        print("KAŻDY MIEWA ZLE DNI. PRAWDA?")
        nextDay = calcWave(birthDate, 23 + (counter*5))
        if nextDay > 0.5:
            print("NIE MARTW SIĘ JUTRO BĘDZIE LEPIEJ")

    return

def inputData():
    name = str(input("Name: "))
    year = int(input("Birth year: "))
    month = int(input("Birth month(number): "))
    day = int(input("Birth day: "))
    targetDate = datetime(year, month, day)
    return name, targetDate

if __name__=="__main__":
    main()
