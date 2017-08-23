import backend
import random

def control(w,q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14):
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
        tem = matrixMult1(t,w,d,Rev,Over,TQ,Down)
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
    #print origi
    #print ini
    #print d
    #print Down * 10
    #print tt
    #print Rev
    return [origi,d,Down * 10,Rev]

def optimized(w,q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14):
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
        tem = matrixMult2(t,w,d,Rev,Over,TQ,Down)
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
    #print origi
    #print ini
    #print d
    #print Down * 10
    #print tt
    #print Rev
    return [origi,d,Down * 10,Rev]



def matrixMult1(T,w,cM,Rv,Ov,Tv,Dv):
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
        temp[str(c2)] = temp[str(c2)] + int((float(Idle) * (float(1) - float(w))))
        i = 0
        check = int((float(Idle) * (float(1) - float(w))))
        while i < len(A):
            temp[str(A[i])] = temp[str(A[i])] + int((float(Idle) * (float(w) / float(len(A)))))
            check = check + int((float(Idle) * (float(w) / float(len(A)))))
            i = i + 1
        if Idle > check:
            temp[str(c2)] = temp[str(c2)] + Idle - check
        c2 = c2 + 1
        Dt = Dt + Idle
    return [temp,Rt,Ov,Tv,Dt]

def matrixMult2(T,w,cM,Rv,Ov,Tv,Dv):
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
    if Q == 0:
        Rv = 0
    else:
        Rv = backend.ridevalue(P,D,T) * Q
    return [Tv,Rv]


def run():
    c = 0
    k = 0.01
    a = 1
    con = []
    opt = []
    while c < 200:
        #backend.noise()
        r = control(a*.999,int(k*264),int(k*78),int(k*246),int(k*284),int(k*378),int(k*580),int(k*145),int(k*127),int(k*477),int(k*546),int(k*687),int(k*838),int(k*350),int(k*294),int(k*706))
        con.append(r[3] - (8.65 * 24 * k * 6000) + ((191.78 / 24) * 3.17 * k * 6000))
        m = optimized(a*.998,int(k*260),int(k*52),int(k*238),int(k*272),int(k*370),int(k*625),int(k*49),int(k*69),int(k*530),int(k*617),int(k*732),int(k*972),int(k*313),int(k*246),int(k*655))
        opt.append(m[3] - (8.65 * 24 * k * 6000) + ((191.78 / 24) * 3.17 * k * 6000))
        k = k + 0.01
        c = c + 1
    f = open("modelcostcomparison.csv","w")
    while c > 0:
        f.write(str(c) + "," + str(con[c-1]) + "," + str(opt[c-1]) + "\n")
        c = c - 1


run()
