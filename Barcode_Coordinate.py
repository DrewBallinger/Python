def coordinates(Shelving, Box):
    NewCoordinates = [0,0]
    if Shelving == 'A1' or Shelving == 'B1':
        if Shelving =='A1':
            NewCoordinates = [0,6]
        else:
            NewCoordinates = [54,6]
    elif Shelving == 'A2' or Shelving == 'B2':
        if Shelving == 'A2':
            NewCoordinates = [0,30]
        else:
            NewCoordinates = [54,30]
    elif Shelving == 'C1' or Shelving == 'D1':
        if Shelving == 'C1':
            NewCoordinates = [0,54]
        else:
            NewCoordinates = [54,54]
    elif Shelving == 'C2' or Shelving == 'D2':
        if Shelving == 'C2':
            NewCoordinates = [0,78]
        else:
            NewCoordinates = [54,78]

    if (Box > 6) and (Shelving != 'C2' or Shelving != 'D2'):
        Yvalue= NewCoordinates[1] + 24
        NewCoordinates[1] =Yvalue
    
    if (Box == 2 or Box == 8):
        Xvalue = NewCoordinates[0]+6
        NewCoordinates[0] = Xvalue
    elif (Box == 3 or Box == 9):
        Xvalue = NewCoordinates[0]+12
        NewCoordinates[0] = Xvalue
    elif (Box == 4 or Box == 10 ):
        Xvalue = NewCoordinates[0]+18
        NewCoordinates[0] = Xvalue
    elif (Box == 5 or Box == 11):
        Xvalue = NewCoordinates[0] +24
        NewCoordinates[0] = Xvalue
    elif (Box == 6 or Box == 12):
        Xvalue = NewCoordinates[0] + 30
        NewCoordinates[0] = Xvalue


    return NewCoordinates

print(coordinates("A1", 6))

    



