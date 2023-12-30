def main():
    mass = int(input("What is the Mass: "))
    E = eCompute(mass)
    print(E)
    
def eCompute(mass=0):
    E = mass * (300000000 ** 2)
    return E

main()