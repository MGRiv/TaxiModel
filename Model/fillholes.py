d = {}

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

def fill():
    for picentry in d.keys():
        for desentry in d[picentry].keys():
            t = 0
            while t < 144:
                test = str(int(t/6) * 100 + int(t%6))
                if test not in d[picentry][desentry].keys():
                    print picentry + "," + desentry + "," + test
                    pre = (int(test) / 100) * 6 + (int(test) % 6) - 1
                    pt = str(int(pre/6) * 100 + int(pre%6))
                    nex = (int(test) / 100) * 6 + (int(test) % 6) + 1
                    nt = str(int(nex/6) * 100 + int(nex%6))
                    p = int((int(d[picentry][desentry][pt][0]) + int(d[picentry][desentry][nt][0])) / 2)
                    r = float(round(float(d[picentry][desentry][pt][1]) + float(d[picentry][desentry][nt][1]),2))
                    d[picentry][desentry][test] = [p,r]
                    print picentry + "," + desentry + "," + test + "," + str(p) + "," + str(r)
                t = t + 1


f = open("dictfullRC.csv","r")
for line in f:
    repar(line)
f.close()
fill()

f = open("dictfullRC2.csv","w")
for lonentry in d.keys():
    for latentry in d[lonentry].keys():
        for timentry in d[lonentry][latentry].keys():
            #print q
            f.write(str(lonentry) + "," + str(latentry) + "," + str(timentry) + "," + str(d[lonentry][latentry][timentry][0]) + "," + str(d[lonentry][latentry][timentry][1]) + "\n")
            #q = q - 1
f.close()
