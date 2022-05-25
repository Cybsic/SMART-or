import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pickle

nv = 100
def getEs(esb,esa,na): 
    x=(na/nv)*(esa-esb)+esb
    return x

def getInt(esa,eda,esb,edb): #this compute the intersection between two intervals
    if eda<esb or edb<esa:
        return [0,0]
    elif esa<esb:
        if eda<edb:
            return [esb,eda]
        else:
            return [esb,edb]
    else:
        if edb<eda:
            return [esa,edb]
        else:
            return [esa,eda]
def getUn(a): #this compute the lenght of the intervals of the union
    b=[]
    nn = a[0][1]-a[0][0]
    b.append(a[0][1])
    for i in range(1,len(a)):
        b.append(a[i][1])
        c=sorted(b)
        if a[i][0] < b[i-1]:
            if a[i][1]>b[i-1]:
                nn = nn + a[i][1] - b[i-1]
        else:
            if a[i][0]>a[i-1][1]:
                nn = nn + a[i][1] - a[i][0]
            else:
                nn = nn + a[i][1] - a[i-1][1]
    return(nn)

ind=[]
def getPi(k,n,a):
    ris = []
    i=1
    ind = []
    for l in range(0,k):
        ind.append(l+1)
    cc = [a[0],a[1]]
    for q in range(0, len(ind)):
        cc = getInt(cc[0], cc[1], a[2 * ind[q]], a[2 * ind[q]+1])
    ris.append(cc)
    cc = [a[0], a[1]]
    while i!=0:
        j=1
        while j!=0 and ind[0]!=n-k:
            if ind[k-1]==n-1:
                for z in range(0,k-1):
                    if ind[k-z-2]!=ind[k-z-1]-1:
                        j=0
                        ind[k-z-2]=ind[k-z-2]+1
                        for q in range(0,z+1):
                            ind[k-z-1+q]=ind[k-z-2+q]+1
                        for q in range(0, len(ind)):
                            cc = getInt(cc[0], cc[1], a[2 * ind[q]], a[2 * ind[q]+1])
                        ris.append(cc)
                        cc = [a[0], a[1]]
                        break
            else:
                ind[k-1]=ind[k-1]+1
                for q in range(0, len(ind)):
                    cc = getInt(cc[0], cc[1], a[2 * ind[q]], a[2 * ind[q]+1])
                ris.append(cc)
                cc = [a[0], a[1]]
        if ind[0]==n-k:
            return(getUn(sorted(ris)))

def getAlfa(p1,p2,i):
    return((p2[0]-p1[0])*(i/nv-p1[1])/(p2[1]-p1[1])+p1[0])

def getSmor(ppp):
    c = []
    for i in range(0,len(ppp)):
        for j in range(0,len(ppp[i])):
            if ppp[i][j][1] == 1:
                c.append(ppp[i][j][0])
    pesi = []
    liv = []
    alt = []
    for i in range(0, nv):
        alt.append(i / nv)
        p = []
        alfa = []
        for j in range(0, num):
            ks = 0
            alfas = []
            for z in range(0,len(ppp[j])):
                if (ppp[j][z][1]>(i/nv) and ks == 0) or (ppp[j][z][1]<=(i/nv) and ks == 1):
                    alfas.append(getAlfa(ppp[j][z-1],ppp[j][z],i))
                    ks = ks + 1
            alfa.append([alfas[0],alfas[1]])
        liv.append(alfa)
        aa = 0.0
        for j in range(0, num):
            if alfa[j][1] > aa:
                aa = alfa[j][1]
        dlt = float(aa-sorted(alfa)[0][0])
        for j in range(0, num):
            ej = []
            beta = []
            beta.append(alfa[j][0])
            beta.append(alfa[j][1])
            k = 0
            while k < num:
                if k != j:
                    beta.append(alfa[k][0])
                    beta.append(alfa[k][1])
                k = k+1
            ej.append(beta[1]-beta[0])
            for z in range(1, num):
                ej.append(getPi(z, num, beta))
            p.append(ej)
        als = sorted(alfa)
        alss = sorted(alfa, key=lambda x: x[1])
        jj = []
        zz = 0
        for g in range(0, len(alfa)):
            for m in range(0, len(als)-1):
                if alfa[g] == als[m] and zz != len(als)-1:
                    zz = zz+1
                    ss = 0
                    for h in range(0, num):
                        if h == num-1:
                            ss = ss+(p[g][h] / (h+1))
                        else:
                            ss = ss+((p[g][h]-p[g][h+1]) / (h+1))
                    ss = ss / dlt
                    jj.append((int(g), float((1+ss) / num)))
                    break
        zz = 0
        for g in range(0, len(alfa)):
            if alfa[g] == als[len(als)-1] and zz == 0:
                mm = 0
                for m in range(0, len(jj)):
                    mm = mm+jj[m][1]
                jj.append((g, 1-mm))
        zz = 0
        for g in range(0, len(alfa)):
            for m in range(1, len(alss)):
                if alfa[g] == alss[m] and zz != len(alss)-1:
                    zz = zz+1
                    ss = 0
                    for h in range(0, num):
                        if h == num-1:
                            ss = ss+(p[g][h] / (h+1))
                        else:
                            ss = ss+((p[g][h]-p[g][h+1]) / (h+1))
                    ss = ss / dlt
                    jj.append((int(g), float((1+ss) / num)))
                    break
        zz = 0
        for g in range(0, len(alfa)):
            if alfa[g] == alss[0] and zz == 0:
                mm = 0
                for m in range(num, len(jj)):
                    mm = mm+jj[m][1]
                jj.append((g, 1-mm))
        pesi.append(jj)
    ess = []
    esd = []

    for i in range(0, len(pesi)):
        x = 0
        y = 0
        for j in range(0, num):
            x = x+liv[i][pesi[i][j][0]][0] * pesi[i][j][1]
            y = y+liv[i][pesi[i][j+num][0]][1] * pesi[i][j+num][1]
        ess.append(x)
        esd.append(y)
    co = 0
    for i in range(0, num):
        co = co + c[i]
    co = co / num
    ess.append(co)
    alt.append(1)
    esd = sorted(esd)
    for i in range(0, len(esd)):
        ess.append(esd[i])
        alt.append(alt[nv-i-1])
    pol = []
    for i in range(0, len(ess)):
        pol.append((ess[i], alt[i]))
    return(ess,alt)

list = [] #in this list we need to insert the lists of vertices of polygonal functions
num = len(list)
results = getSmor(list)
print(results) #it will return a list with the vector of x-coordinates and a list of y-coordinates of the Fuzzy number obtained through the SMART-or
plt.plot(results) #to represent the Fuzzy number
plt.show()
