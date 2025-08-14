mainType=["Color","Digit","Multiplier", "Tolerance"]
def Tolerance(number ,to):
    return (number/100)*to

c=['Red', 'Red', 'Yellow']
data = [
    ["Black", 0, "×1", 0, "250 ppm/°C"],
    ["Brown", 1, "×10", "1", "100 ppm/°C"],
    ["Red", 2, "×100", "2", "50 ppm/°C"],
    ["Orange", 3, "×1k", 0, "15 ppm/°C"],
    ["Yellow", 4, "×10k", 0, "25 ppm/°C"],
    ["Green", 5, "×100k", "0.5", "20 ppm/°C"],
    ["Blue", 6, "×1M", "0.25", "10 ppm/°C"],
    ["Violet", 7, "×10M", "0.1", "5 ppm/°C"],
    ["Gray", 8, "×100M", "0.05", "1 ppm/°C"],
    ["White", 9, "×1G", 0, "—"],  # Usually not used for temp coefficient
    ["Gold", 0, "×0.1", "5", "—"],
    ["Silver", 0, "×0.01", "10", "—"],
    ["No Color", 0, 0, "20", "—"]
]
def getValue(color):
    for i  in data:
        if i[0].lower()==color.lower():
            return i
def CreateWindow (NumberOfBand):
    if NumberOfBand > 0:
        print("it is working")

def Band3(c):
    list=[]
    digit1=float(getValue(c[0])[1])
    digit2 =float( getValue(c[1])[1])
    digit3 = float(getValue(c[2])[1])
    resistance =((digit1*10 )+digit2)* (10**digit3)
    print(digit1,digit2,digit3)
    print(resistance)
    list.append(resistance)
    return list


def Band4(c):
    list = []
    digit1 = float(getValue(c[0])[1])
    digit2 = float(getValue(c[1])[1])
    digit3 = float(getValue(c[2])[1])
    digit4 = float(getValue(c[3])[3])
    resistance = ((digit1 * 10) + digit2) * (10 ** digit3)

    list.append(resistance)
    list .append(Tolerance(resistance,digit4))
    print(digit1, digit2, digit3,digit4)
    print(resistance,Tolerance(resistance,digit4))
    return list


def Band5(c):
    list = []
    digit1 = float(getValue(c[0])[1])
    digit2 = float(getValue(c[1])[1])
    digit3 = float(getValue(c[2])[1])
    digit4 = float(getValue(c[3])[1])
    digit5 = float(getValue(c[4])[3])
    resistance = ((((digit1*10)  + digit2)*10) + digit3)*(10**digit4)

    list.append(resistance)
    list .append(Tolerance(resistance,digit5))
    print(digit1, digit2, digit3,digit4,digit5)
    print(resistance,Tolerance(resistance,digit5))
    return list


def Band6(c):
    list = []
    digit1 = float(getValue(c[0])[1])
    digit2 = float(getValue(c[1])[1])
    digit3 = float(getValue(c[2])[1])
    digit4 = float(getValue(c[3])[1])
    digit5 = float(getValue(c[4])[3])
    digit6=getValue((c[5]))[4]
    resistance = ((((digit1 * 10) + digit2) * 10) + digit3) * (10 ** digit4)

    list.append(resistance)
    list.append(Tolerance(resistance, digit5))
    list .append(digit6)
    print(digit1, digit2, digit3, digit4, digit5,digit6)
    print(resistance, Tolerance(resistance, digit5),digit6)
    return list



