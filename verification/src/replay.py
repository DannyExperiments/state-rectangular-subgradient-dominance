from fractions import Fraction as F
from itertools import product
import random

n=3
gamma=F(1,2)
mu=[F(1,3)]*3
V=[F(1,2),F(1,2),F(3,4)]
c=[v-F(5,16) for v in V]
rng=random.Random(870)

def solve(A,b):
    U=[list(a)+[x] for a,x in zip(A,b)]
    for i in range(n):
        j=next(j for j in range(i,n) if U[j][i])
        U[i],U[j]=U[j],U[i]
        z=U[i][i]
        U[i]=[x/z for x in U[i]]
        for j in range(n):
            if j!=i:
                z=U[j][i]
                U[j]=[x-z*y for x,y in zip(U[j],U[i])]
    return [row[-1] for row in U]

def transitions(P,pi):
    return [[pi[s]*P[s][0][t]+(1-pi[s])*P[s][1][t] for t in range(n)] for s in range(n)]

def ev(P,pi):
    T=transitions(P,pi)
    return solve([[F(s==t)-gamma*T[s][t] for t in range(n)] for s in range(n)],c)

def occ(P,pi):
    T=transitions(P,pi)
    return solve([[F(s==t)-gamma*T[t][s] for t in range(n)] for s in range(n)],
                 [(1-gamma)*m for m in mu])

def row(q):
    p=F(rng.randrange(int(4*(1-q))+1),4)
    return [p,1-p-q,q]

pi=[F(1,2)]*3
vary_occ=0
for trial in range(300):
    P=[]
    for _ in range(3):
        rows=[]
        for _ in range(n):
            q=F(rng.randrange(5),4)
            rows.append([row(q),row(1-q)])
        P.append(rows)
    ds=[occ(M,pi) for M in P]
    assert all(ev(M,pi)==V for M in P)
    vary_occ += len(set(map(tuple,ds)))>1
    ws=[F(1,6),F(2,6),F(3,6)]
    d=[sum(w*di[s] for w,di in zip(ws,ds)) for s in range(n)]
    B=[[[sum(w*di[s]*M[s][a][t]/d[s] for w,di,M in zip(ws,ds,P))
          for t in range(n)] for a in range(2)] for s in range(n)]
    assert occ(B,pi)==d and ev(B,pi)==V
    def q(M,s,a):return c[s]+gamma*sum(x*y for x,y in zip(M[s][a],V))
    for s,a in product(range(n),range(2)):
        assert d[s]*q(B,s,a)==sum(w*di[s]*q(M,s,a) for w,di,M in zip(ws,ds,P))
    J=sum(x*y for x,y in zip(mu,V))
    gap=sum(d[s]*(V[s]-min(q(B,s,a) for a in range(2)))/(1-gamma) for s in range(n))
    D=1/((1-gamma)*min(mu))
    for candidate in product((F(0),F(1)),repeat=n):
        assert J-sum(x*y for x,y in zip(mu,ev(B,candidate)))<=D*gap
assert vary_occ
print('300 exact mixtures and 2400 fixed-model comparisons checked.')

# Independent arithmetic for the worked 3D example.
first = ((1, 0, 0), (0, 0, 1))
second = ((0, 0, 1), (0, 1, 0))
first_model = [first] * 3
second_model = [second] * 3
d1 = occ(first_model, pi)
d2 = occ(second_model, pi)
assert d1 == [F(5, 12), F(1, 6), F(5, 12)]
assert d2 == [F(1, 6), F(5, 12), F(5, 12)]
assert all(ev(model, pi) == V for model in product((first, second), repeat=3))
for i in range(13):
    lam = F(i, 12)
    mixed = [lam * u + (1 - lam) * v for u, v in zip(d1, d2)]
    local = [lam * u / d for u, d in zip(d1, mixed)]
    model = [
        [[alpha * u + (1 - alpha) * v for u, v in zip(row1, row2)]
         for row1, row2 in zip(first, second)]
        for alpha in local
    ]
    assert ev(model, pi) == V
    assert occ(model, pi) == mixed
    for s, a in product(range(n), range(2)):
        assert mixed[s] * q(model, s, a) == (
            lam * d1[s] * q(first_model, s, a) +
            (1 - lam) * d2[s] * q(second_model, s, a)
        )
    if lam == F(1, 2):
        assert mixed == [F(7, 24), F(7, 24), F(5, 12)]
        assert local == [F(5, 7), F(2, 7), F(1, 2)]
print("Eight active row selections and 13 worked mixtures checked exactly.")
