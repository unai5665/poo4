import random

def intDiv(a:int, b:int)->int:
    try:
        return a // b
    except:
        print("realizamos tareas de control de cierre")

#Si es el flujo principal
if __name__ == "__main__":
    '''
    for i in range(30):
        a = random.randint(0,9)
        b = random.randint(0,9)
        print("a:", a, "b:", b, intDiv(random.randint(0,9), 5))
    '''   