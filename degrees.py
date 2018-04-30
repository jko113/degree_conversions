def c_to_f():

    while True:
        c = input("Temperature in Celsius? ")
        try:
            c = int(c)
        except:
            print("Not a valid integer. Try again")
            continue
        break

    def to_Fahr(cel):
        return cel * 1.8 + 32

    fahr_result = to_Fahr(c)
    print ("%.1f degrees in Fahrenheit is %.1f degrees Fahrenheit." % (c, fahr_result) )

def f_to_c():

    while True:
        f = input("Temperature in Fahrenheit? ")
        try:
            f = int(f)
        except:
            print("Not a valid integer. Try again")
            continue
        break

    def to_Cel(fahr):
        return (fahr - 32) * (5/9)

    cel_result = to_Cel(f) 
    print ("%.1f degrees in Fahrenheit is %.1f degrees Celsius." % (f, cel_result) )