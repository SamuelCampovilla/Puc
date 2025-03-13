numbers = []

def main():
    for num in range(6):
        num = float(input("Digite um numero: "))
        numbers.append(float(num))
main()

a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[3]
e = numbers[4]
f = numbers[5]
def check():
    while True:
        if ((a*e)-(b*d)) == 0:
            print ("Insira valores novamente")
            main()
        else:
            return
        break
check()

def expression():
    x = ((c*e) - (b*f))/((a*e)-(b*d))
    y = ((a*f)-(c*d))/((a*e)-(b*d))
    print (f"X: {x:.2f}, Y: {y:.2f}")

expression()

print (numbers)
