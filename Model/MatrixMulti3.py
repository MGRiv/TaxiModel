import backend
import random

def model(w,q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14):
    d = {'0':q0,'1':q1,'2':q2,'3':q3,'4':q4,'5':q5,'6':q6,'7':q7,'8':q8,'9':q9,'10':q10,'11':q11,'12':q12,'13':q13,'14':q14}
    TQ = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    Over = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0}
    Rev = 0
    Down = 0
    origi = d
    ini = 0
    fir = 0
    while fir < 15:
        ini = ini + d[str(fir)]
        fir = fir + 1
    t = 0
    while t < 144:
        tem = matrixMult(t,w,d,Rev,Over,TQ,Down)
        d = tem[0]
        Rev = Rev + tem[1]
        Over = tem[2]
        TQ = tem[3]
        Down = Down + tem[4]
        reent = TQ.pop(0)
        c = 0
        TQ.append([])
        while c < 15:
            d[str(c)] = d[str(c)] + reent[c]
            TQ[4].append(0)
            c = c + 1
        t = t + 1
    while len(TQ) > 0:
        reent = TQ.pop(0)
        c = 0
        while c < 15:
            d[str(c)] = d[str(c)] + reent[c]
            c = c + 1
    c = 0
    tt = 0
    while c < 15:
        tt = tt + d[str(c)]
        c = c + 1
    print origi
    print ini
    print d
    print Down * 10
    print tt
    print Rev
    return [origi,d,Down * 10,Rev]

def matrixMult(T,w,cM,Rv,Ov,Tv,Dv):
    #print cM
    temp = {}
    k = 0
    Dt = 0
    while k < 15:
        temp[str(k)] = 0
        k = k + 1
    c2 = 0
    Rt = 0
    while c2 < 15:
        ov = Ov[str(c2)]
        r = backend.transitquants(cM[str(c2)],ov,c2,T)
        tot = 0
        for key in r.keys():
            if int(key) != 15:
                tot = tot + r[key]
                tm = entertotransit(r[key],c2,int(key),T,Rv,Tv)
                Tv = tm[0]
                Rt = Rt + float(tm[1])
            else:
                Ov[str(c2)] = r[key]
        Idle = cM[str(c2)] - tot
        A = backend.adjacent(c2)
        idl = backend.opidlequants(w,Idle,c2,T)
        for key in idl.keys():
            temp[key] = temp[key] + idl[key]
        c2 = c2 + 1
        Dt = Dt + Idle
    return [temp,Rt,Ov,Tv,Dt]

def entertotransit(Q,P,D,T,Rv,Tv):
    i = (backend.timetodes(P,D) / 10) - 1
    Tv[i][D] = Tv[i][D] + Q
    Rv = backend.ridevalue(P,D,T) * Q
    return [Tv,Rv]

def run(n):
    times = 0
    Mod = {}
    Jtrc = 0
    while times < n:
        ars = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        rn = {}
        full = 6000
        while len(ars) > 0:
            qars = random.randint(0,full)
            full = full - qars
            iars = random.randint(0,len(ars) - 1)
            rn[ars.pop(iars)] = qars
        dat = model(0.998,rn[0],rn[1],rn[2],rn[3],rn[4],rn[5],rn[6],rn[7],rn[8],rn[9],rn[10],rn[11],rn[12],rn[13],rn[14])
        Mod[str(Jtrc)] = dat
        Jtrc = Jtrc + 1
        times = times + 1
    f = open("directsteadystatetrend.csv","w")
    for keys in Mod.keys():
        f.write(keys + "," + str(Mod[keys]) + "\n")

def run2():
    times = 0.0
    Mod = {}
    Jtrc = 0
    while times <= 1:
        dat = model(times,260,52,238,272,370,625,49,69,530,617,732,972,313,246,655)
        #[origi,d,Down * 10,Rev]
        rat = float(float(dat[3]) / ((1440.0 * 6000.0) -  float(dat[2]) ))
        Mod[str(times)] = [rat,dat[3]]
        Jtrc = Jtrc + 1
        times = times + .001
    f = open("directrevratiowithwilling.csv","w")
    for keys in Mod.keys():
        f.write(keys + "," + str(Mod[keys][0]) + "\n")
    f = open("directrevwithwilling.csv","w")
    for keys in Mod.keys():
        f.write(keys + "," + str(Mod[keys][1]) + "\n")

def run3():
    k = 0.0
    Mod = {}
    Jtrc = 0
    while k <= 2:
        dat = model(.998,int(k*260),int(k*52),int(k*238),int(k*272),int(k*370),int(k*625),int(k*49),int(k*69),int(k*530),int(k*617),int(k*732),int(k*972),int(k*313),int(k*246),int(k*655))
        Mod[str(k)] = dat
        Jtrc = Jtrc + 1
        k = k + .001
    f = open("directmaximumconcentration.csv","w")
    for keys in Mod.keys():
        f.write(keys + "," + str(Mod[keys]) + "\n")

def run4():
    times = 0.0
    Mod = {}
    Jtrc = 0
    while times <= 1:
        dat = model(times,260,52,238,272,370,625,49,69,530,617,732,972,313,246,655)
        Mod[str(times)] = dat
        Jtrc = Jtrc + 1
        times = times + .001
    f = open("NEWdirectvarywillingness.csv","w")
    for keys in Mod.keys():
        f.write(keys + "," + str(Mod[keys]) + "\n")
        
model(.998,260,52,238,272,370,625,49,69,530,617,732,972,313,246,655)
#run(5000)
#run2()
#run3()
#run4()
