d = {}
q = 0

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
    #print q

tracker = 1
while tracker < 13:    
    f = open("dictRC"+ str(tracker) + ".csv","r")
    q = 0
    for line in f:
        repar(line)
        #q = q + 1
    f.close()
    tracker = tracker + 1
        
f = open("dictfullRC.csv","w")
for lonentry in d.keys():
    for latentry in d[lonentry].keys():
        for timentry in d[lonentry][latentry].keys():
            #print q
            f.write(str(lonentry) + "," + str(latentry) + "," + str(timentry) + "," + str(d[lonentry][latentry][timentry][0]) + "," + str(d[lonentry][latentry][timentry][1]) + "\n")
            #q = q - 1
f.close()
