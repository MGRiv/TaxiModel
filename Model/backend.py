import random
d = {}

Area = [[1, 2, 3, 4],
     [0, 2, 3, 4, 5, 6, 7],
     [0, 1, 3, 4, 5, 6],
     [0, 1, 2, 4, 5, 6, 7, 9],
     [0, 1, 2, 3, 5, 6, 7, 8],
     [1, 2, 3, 4, 6, 7, 8, 9, 11],
     [1, 2, 3, 4, 5, 7, 8, 9, 10, 11],
     [1, 3, 4, 5, 6, 8, 9, 10],
     [4, 5, 6, 7, 9, 10, 11],
     [3, 5, 6, 7, 8, 10, 11],
     [6, 7, 8, 9, 11, 12, 13, 14],
     [5, 6, 8, 9, 10, 12, 13, 14],
     [10, 11, 13, 14],
     [10, 11, 12, 14],
     [10, 11, 12, 13]]

DTimes = [[10,10,20,20,20,20,20,30,30,30,40,40,40,40,40],
          [10,10,20,10,20,20,20,30,30,30,40,40,50,40],
          [10,10,20,20,20,30,40,30,40,40,50,40,40],
          [10,10,10,20,20,30,20,40,30,40,40,50],
          [10,20,10,10,20,20,40,30,40,40,50],
          [10,10,10,20,20,30,20,30,20,30],
          [10,10,20,20,30,30,40,40,40],
          [10,10,30,20,30,30,40,30],
          [10,10,20,30,30,30,30],
          [10,30,20,30,30,30],
          [10,10,20,20,20],
          [10,20,10,30],
          [10,10,10],
          [10,10],
          [10]]



#loads the data from a csv
def load():
    f = open("dictfullRC2.csv","r")
    for line in f:
        repar(line)
    f.close()

#lin is a line from a csv file
def repar(lin):
    t = lin.split(',')
    lat = str(t[1])
    lon = str(t[0])
    tim = str(t[2])
    if lon in d.keys():
        if lat in d[lon].keys():
            if tim in d[lon][lat].keys():
                d[lon][lat][tim][0] = int(d[lon][lat][tim][0]) + int(t[3])
                d[lon][lat][tim][1] = float(d[lon][lat][tim][1]) + float(t[4])
            else:
                d[lon][lat][tim] = [int(t[3]),float(t[4])]
        else:
            dt = {tim:[int(t[3]),float(t[4])]}
            d[lon][lat] = dt
    else:
        dt = {tim:[int(t[3]),float(t[4])]}
        dlat = {lat:dt}
        d[lon] = dlat

load()

##############################################################################################

#Q is the current concentration of cabs in an area
#A is the area
#T is the time interval
#O is the extra passengers from the last interval
#Returns a dictionary containing the quantity of cabs entering transit going to each area
def transitquants(Q,O,A,T):
    tot = 0
    c = 0
    r = {}
    while c < 15:
        time = str(int(T/6) * 100 + int(T%6))
        r[str(c)] = float(d[str(A)][str(c)][time][0]) + float(O)
        c = c + 1
    for entry in r.keys():
        r[entry] = int(round(float(r[entry]) / float(365)))
        tot = tot + r[entry]
    if tot > Q and tot != 0:
        for entry in r.keys():
            r[entry] = int(float(Q) * float(r[entry]) / float(tot))
        r[str(15)] = tot - Q
    else:
        r[str(15)] = 0
    return r

#A is an area
#Returns a list of adjacent areas
def adjacent(A):
    return Area[A]

#P is the pickup area
#D is the destination area
#T is the time interval
# Returns the value of the ride at the given time
def ridevalue(P,D,T):
    time = str(int(T/6) * 100 + int(T%6))
    return float(round(float(d[str(P)][str(D)][time][1]) / float(d[str(P)][str(D)][time][0]),2))


#P is the pickup area
#D is the destination area
# Returns the index of the time interval for the transit queue
def timetodes(P,D):
    if D > P:
        return DTimes[P][(D - P)]
    return DTimes[D][(P - D)]

#W is the willingness factor
#I is the number of idle cabs
#A is the area
#T is the time interval
# Returns a dictionary containing the quantity of idle cabs transtioning to each area
def opidlequants(W,I,A,T):
    temp = {}
    temp[str(A)] = int((float(I) * (float(1) - float(W))))
    ad = adjacent(A)
    tot = 0.0
    i = 0
    check = int((float(I) * (float(1) - float(W))))
    tes = (T + 1)%144
    time = str(int(tes/6) * 100 + int(tes%6))
    while i < len(ad):
        tot = tot + float(d[str(A)][str(ad[i])][time][0])
        i = i + 1
    i = 0
    while i < len(ad):
        temp[str(ad[i])] = int(float(I) * float(W) * float(d[str(A)][str(ad[i])][time][0]) / tot)
        check = check + int(float(I) * float(W) * float(d[str(A)][str(ad[i])][time][0]) / tot)
        i = i + 1
    if I > check:
        temp[str(A)] = temp[str(A)] + I - check
    return temp

def noise():
    for lon in d.keys():
        for lat in d[lon].keys():
            for tim in d[lon][lat].keys():
                scal = float((random.random() * .2) + .9)
                d[lon][lat][tim][0] = int(float(d[lon][lat][tim][0]) * scal)
                d[lon][lat][tim][1] = round(float(d[lon][lat][tim][1]) * scal,2)
