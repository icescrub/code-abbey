data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def BMI(bmi):
    if bmi < 18.5:
        print("under")
    elif 18.5 <= bmi < 25.0:
        print("normal")
    elif 25.0 <= bmi < 30.0:
        print("over")
    else:
        print("obese")

def f(data):
    for line in data:
        x = list(map(float, line.split()))
        bmi = x[0]/(x[1]**2)
        BMI(bmi)
