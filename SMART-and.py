import matplotlib.pyplot as plt


es=[]
co=[]
ed=[]

for i in range(0, 2):
    a=float(input('Insert left extremes  '))
    es.append(a)
for i in range(0,2):
    a=float(input('Insert cores '))
    co.append(a)
for i in range(0,2):
    a=float(input('Insert right extremes '))
    ed.append(a)
for i in range(0,2):
    if es[i]>co[i] or co[i]>ed[i]:
        print('Attention: Wrong values')
        exit()
nv=int(input('How many levels do you want to compute? '))
nv=nv-1
a=[]
b=[]
ris=[]
def getEs(esb,esa,na):
    x=(na/nv)*(esa-esb)+esb
    return float(x)
def getInt(esa,eda,esb,edb):
    if eda<esb or edb<esa:
        return 0
    elif esa<esb:
        if eda<edb:
            return eda-esb
        else:
            return edb-esb
    else:
        if edb<eda:
            return edb-esa
        else:
            return eda-esa
def getDis(esa,eda,esb,edb):
    return eda-esa-getInt(esa,eda,esb,edb)

ris=[]
aus=[]

for i in range(0,nv):
    alfa=[]
    for k in range(0,2):
        alfa.append(getEs(es[k],co[k],i))
        alfa.append(getEs(co[k],ed[k],i))
    dd=sorted([alfa[1], alfa[3]])
    ss=sorted([alfa[2], alfa[0]])
    delta = float(dd[1])-float(ss[0])
    if getInt(alfa[0],alfa[1],alfa[2],alfa[3])!=0:
        if ss[1]==alfa[0]:
            gj=0.5*getDis(alfa[0],alfa[1],alfa[2],alfa[3])+getInt(alfa[0],alfa[1],alfa[2],alfa[3])
            gj=gj/(gj+getInt(alfa[0],alfa[1],alfa[2],alfa[3])+0.5*getDis(alfa[2],alfa[3],alfa[0],alfa[1]))
            ris.append((alfa[0]*(1+gj)+alfa[2]*(1-gj)) / 2)
            aus.append((alfa[0] * (1+gj)+alfa[2] * (1-gj)) / 2)
        else:
            gj = 0.5 * getDis(alfa[2], alfa[3], alfa[0], alfa[1])+getInt(alfa[0], alfa[1], alfa[2], alfa[3])
            gj=gj / (gj+getInt(alfa[0], alfa[1], alfa[2], alfa[3])+0.5 * getDis(alfa[0], alfa[1], alfa[2], alfa[3]))
            ris.append((alfa[2] * (1+gj)+alfa[0] * (1-gj)) / 2)
            aus.append((alfa[2] * (1+gj)+alfa[0] * (1-gj)) / 2)
        if dd[0]==alfa[1]:
            gj = 0.5 * getDis(alfa[0], alfa[1], alfa[2], alfa[3])+getInt(alfa[0], alfa[1], alfa[2], alfa[3])
            gj=gj / (gj+getInt(alfa[0], alfa[1], alfa[2], alfa[3])+0.5 * getDis(alfa[2], alfa[3], alfa[0], alfa[1]))
            ris.append((alfa[1] * (1+gj)+alfa[3] * (1-gj)) / 2)
            aus.append((alfa[1] * (1+gj)+alfa[3] * (1-gj)) / 2)
        else:
            gj = 0.5 * getDis(alfa[2], alfa[3], alfa[0], alfa[1])+getInt(alfa[0], alfa[1], alfa[2], alfa[3])
            gj=gj / (gj+getInt(alfa[0], alfa[1], alfa[2], alfa[3])+0.5 * getDis(alfa[0], alfa[1], alfa[2], alfa[3]))
            ris.append((alfa[3] * (1+gj)+alfa[1] * (1-gj)) / 2)
            aus.append((alfa[3] * (1+gj)+alfa[1] * (1-gj)) / 2)
    else:
        if ss[0]==alfa[0]:
            ej=(getInt(alfa[0],alfa[1],alfa[2],alfa[3])*0.5+getDis(alfa[0],alfa[1],alfa[2],alfa[3]))/delta
            aus.append((alfa[0]*(1+ej)+alfa[2]*(1-ej)) / 2)
        else:
            ej=(getInt(alfa[0], alfa[1], alfa[2], alfa[3]) * 0.5+(getDis(alfa[2], alfa[3], alfa[0], alfa[1])))/delta
            aus.append((alfa[2] * (1+ej)+alfa[0] * (1-ej)) / 2)
        if dd[1]==alfa[1]:
            ej = ((getInt(alfa[0], alfa[1], alfa[2], alfa[3]) * 0.5+getDis(alfa[0], alfa[1], alfa[2], alfa[3]))) /delta
            aus.append((alfa[1] * (1+ej)+alfa[3] * (1-ej)) / 2)
        else:
            ej = ((getInt(alfa[0], alfa[1], alfa[2], alfa[3])) * 0.5+(getDis(alfa[2], alfa[3], alfa[0], alfa[1]))) /delta
            aus.append((alfa[3] * (1+ej)+alfa[1] * (1-ej)) / 2)
        dm=(ris[2*i-1]-ris[2*i-2])/(aus[2*i-1]-aus[2*i-2])
        ris.append(ris[2*i-2]+dm*(aus[2*i]-aus[2*i-2]))
        ris.append(ris[2*i-1]-dm*(aus[2*i+1]-aus[2*i-1]))
ris.append((co[0]+co[1])/2)
liv=[]
for i in range(0,nv):
    liv.append(i/nv)
liv.append(1)
for i in range(0,nv):
    liv.append((nv-i-1)/nv)
ris=sorted(ris)
plt.plot(ris,liv)
plt.show()
