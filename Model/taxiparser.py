import math
q = 0
d = {}

Areas = [[[40.718,-74.017], [40.726,-74.011], [40.718,-74.000], [40.710,-73.992], [40.699,-74.020]],
         [[40.726,-74.011], [40.725,-73.995], [40.718,-74.000]],
         [[40.718,-74.000], [40.725,-73.995], [40.719,-73.974], [40.711,-73.977], [40.710,-73.992]],
         [[40.725,-73.995], [40.734,-73.990], [40.727,-73.972], [40.719,-73.974]],
         [[40.726,-74.011], [40.743,-74.009], [40.739,-74.000], [40.734,-73.990], [40.725,-73.995]],
         [[40.734,-73.990], [40.747,-73.981], [40.743,-73.972], [40.727,-73.972]],
         [[40.739,-74.000], [40.751,-73.991], [40.747,-73.981], [40.734,-73.990]],
         [[40.743,-74.009], [40.757,-74.005], [40.751,-73.991], [40.739,-74.000]],
         [[40.757,-74.005], [40.772,-73.995], [40.765,-73.978], [40.751,-73.991]],
         [[40.751,-73.991], [40.765,-73.978], [40.757,-73.960], [40.743,-73.972], [40.747,-73.981]],
         [[40.772,-73.995], [40.811,-73.967], [40.808,-73.956], [40.801,-73.958], [40.768,-73.982], [40.765,-73.978]],
         [[40.765,-73.978], [40.768,-73.982], [40.801,-73.958], [40.797,-73.949], [40.788,-73.956], [40.783,-73.944], [40.775,-73.943], [40.757,-73.960]],
         [[40.811,-73.967], [40.834,-73.950], [40.828,-73.935], [40.817,-73.934], [40.797,-73.949], [40.801,-73.958], [40.808,-73.956]],
         [[40.788,-73.956], [40.797,-73.949], [40.817,-73.934], [40.796,-73.929], [40.783,-73.944]],
         [[40.834,-73.950], [40.878,-73.926], [40.872,-73.910], [40.835,-73.935], [40.828,-73.935]]]
Manhattan = [[40.711,-73.977], [40.796,-73.929], [40.835,-73.935], [40.872,-73.910], [40.878,-73.926], [40.754,-74.008], [40.718,-74.017], [40.699,-74.020]]

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def inManhattan(lon,lat):
    i = -1
    t = 0
    while i < len(Manhattan) - 1:
        t = t + inPolygon([[lat,lon],[0.0,0.0]],[Manhattan[i],Manhattan[i+1]])
        i = i + 1
    if t % 2 == 1:
        return True
    #print t
    return False

def inPolygon(lin1,lin2):
    xdiff = (lin1[0][0] - lin1[1][0], lin2[0][0] - lin2[1][0])
    ydiff = (lin1[0][1] - lin1[1][1], lin2[0][1] - lin2[1][1])
    #if (xdiff[0] == 0 and xdiff[1] == 0 and ydiff[0] == ydiff[1]) or ((ydiff[0] / xdiff[0]) == (ydiff[1] / xdiff[1])):
    #    return 0
    x = (lin1[0][0] * lin1[1][1] - lin1[0][1] * lin1[1][0]) * xdiff[1] - xdiff[0] * (lin2[0][0] * lin2[1][1] - lin2[0][1] * lin2[1][0])
    y = (lin1[0][0] * lin1[1][1] - lin1[0][1] * lin1[1][0]) * ydiff[1] - ydiff[0] * (lin2[0][0] * lin2[1][1] - lin2[0][1] * lin2[1][0])
    denom = xdiff[0] * ydiff[1] - ydiff[0] * xdiff[1]
    if denom == 0:
        return 0
    xd = x/denom
    yd = y/denom
    #print str(abs(xd - lin2[0][0]) + abs(xd - lin2[1][0])) + " = " + str(abs(xdiff[1]))
    #print str(abs(yd - lin2[0][1]) + abs(yd - lin2[1][1])) + " = " + str(abs(ydiff[1])) + "\n"
    if (abs(xd - lin2[0][0]) + abs(xd - lin2[1][0]) - abs(xdiff[1]) == 0 and abs(yd - lin2[0][1]) + abs(yd - lin2[1][1]) - abs(ydiff[1]) == 0 and math.sqrt((xd**2) + (yd**2)) <= math.sqrt(lin1[0][0]**2 + lin1[0][1]**2)):
        #print "Equal! \n"
        return 1
    return 0

def inArea(lon,lat):
    # 0 = Financial/Tribeca/South Chinatown, 1 = SOHO, 2 = LES, 3 = East Village, 4 = Greenwich Village
    # 5 = Kips Bay, 6 = East of Chelsea, 7 = Chelsea, 8 = Hell's Kitchen and West Midtown, 9 = East Midtown
    # 10 = Upper West Side, 11 = Central Park and Upper East Side, 12 = Harlem, 13 = Spanish Harlem
    # 14 = The Heights and Inwood
    k = 0
    r = 14
    while k < len(Areas):
        i = -1
        t = 0
        while i < len(Areas[k]) - 1:
            t = t + inPolygon([[lat,lon],[0.0,0.0]],[Areas[k][i],Areas[k][i+1]])
            i += 1
        if t % 2 == 1:
            r = k
            return r
        k = k + 1
    return r

    
def par(lin):
    t = lin.split(',')
    if isFloat(t[5]) and isFloat(t[6]) and float(t[5]) != 0.0 and float(t[6]) != 0.0 and inManhattan(float(t[5]),float(t[6])) and isFloat(t[9]) and isFloat(t[10]) and float(t[9]) != 0.0 and float(t[10]) != 0.0 and inManhattan(float(t[9]),float(t[10])):
        #print str(round(float(t[6]),3)) + " " + str(round(float(t[5]),3)) + " " + str(round(float(t[10]),3)) + " " + str(round(float(t[9]),3))
        piczone = inArea(float(t[5]),float(t[6]))
        deszone = inArea(float(t[9]),float(t[10]))
        tem = t[1].split(':')
        tim = str(int(tem[0].split(' ')[1]) * 100 + int(tem[1][0:1]))
        if piczone in d.keys():
            if deszone in d[piczone].keys():
                if tim in d[piczone][deszone].keys():
                    d[piczone][deszone][tim][0] = int(d[piczone][deszone][tim][0]) + 1
                    d[piczone][deszone][tim][1] = float(d[piczone][deszone][tim][1]) + float(t[18])
                else:
                    d[piczone][deszone][tim] = [1,float(t[18])]
            else:
                dt = {tim:[1,float(t[18])]}
                d[piczone][deszone] = dt
        else:
            dt = {tim:[1,float(t[18])]}
            dlat = {deszone:dt}
            d[piczone] = dlat


#while q < 12:
month = ["2016-01","2016-02","2016-03","2016-04","2016-05","2016-06",
         "2015-08","2015-09","2015-10","2015-11","2015-12","2015-07",]
f = open("yellow_tripdata_"+ month[0] + ".csv","r")
for line in f:
    par(line)
f.close()
q = q + 1
    
f = open("dictRC1.csv","w")
for lonentry in d.keys():
    for latentry in d[lonentry].keys():
        for timentry in d[lonentry][latentry].keys():
            #print q
            f.write(str(lonentry) + "," + str(latentry) + "," + str(timentry) + "," + str(d[lonentry][latentry][timentry][0]) + "," + str(d[lonentry][latentry][timentry][1]) + "\n")
            #q = q - 1
f.close()

