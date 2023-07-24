def circumfrences():
    pi = 3.141526535897
    radius = input("What is the radius of your circle? ")
    radius = float(radius) if '.' in radius else int(radius)
    
    print(2*radius*pi)
    
circumfrences()
