import math
from datetime import datetime

def main() -> None:
    t = 0
    name, personDate = inputData()
    daysDiff = (datetime.today() - personDate).days

    yp = calcWave(daysDiff, 23)
    ye = calcWave(daysDiff, 28)
    yi = calcWave(daysDiff, 33)

    displayPersonInfo(name, personDate, "Hi", [yp, ye, yi])

    return

def calcWave(t, y):
    return math.sin((2 * math.pi / y) * t)

def displayPersonInfo(name: str, birth, info: str, wave) -> None:
    print("\n", info)
    print(name)
    print("Birthday: ", birth)

    print(wave)
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
