import json,os,sys,urllib.request as U,urllib.error
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(1)
A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
PS="ggggggggeggggggeegiiiigegijkkjigjkmoomkjoqsuusqoy034430yggggggggYbcddcbYbefggfebcfiiiifcdgikkigdceeeeeecehggggheegiiiigeegijjigegghiihggijkkkkjigghiihgggghiihggdeeffeedegghhggeegiiiigefhiiiihfloieeioljkgddgkjegcaacgeacaYYacaYZYWWYZYWWVUUVWWTUSRRSUTQSQOOQSQ"
V=(0,100,320,330,500,900,9000)
N8=(-33,-31,-18,-14,14,18,31,33)
K8=(-17,-16,-15,-1,1,15,16,17)
D4=(-17,-15,15,17)
O4=(-16,-1,1,16)
CR={0:1,7:2,112:4,119:8}
MATE=30000
BU=40000
PST=[[0]*128 for _ in range(7)]
o=0
for t in range(1,7):
    n=8 if t==1 or t==6 else 4
    T=[]
    for r in range(n*8):T.append(4*(A.index(PS[o])-32));o+=1
    if n<8:T+=[v for r in range(n-1,-1,-1) for v in T[r*8:r*8+8]]
    for i in range(8):
        for f in range(8):PST[t][i*16+f]=T[i*8+f]
Z=[[0]+[((i*0x2545F4914F6CDD1D^p*0x9E3779B97F4A7C15)*0x87C37B91114253D5)&0xFFFFFFFFFFFFFFFF for p in range(1,15)] for i in range(128)]
B=[0]*128;OC=set();S=0;C=0;EP=-1;HM=0;KX=0;KG=[0,0];ST=[];KS=[]
TT={};KL=[[0,0] for _ in range(200)];HI=[0]*16384;ND=0;AB=0;GID=-1;NM=0
def atk(i,s):
    d=15-30*s
    for j in (i-d,i-d-2+4*s):
        if not j&0x88 and B[j]==1+8*s:return 1
    for o in N8:
        j=i+o
        if not j&0x88 and B[j]==2+8*s:return 1
    for o in K8:
        j=i+o
        if not j&0x88 and B[j]==6+8*s:return 1
    for o in D4:
        j=i+o
        while not j&0x88 and not B[j]:j+=o
        if not j&0x88 and B[j] in (3+8*s,5+8*s):return 1
    for o in O4:
        j=i+o
        while not j&0x88 and not B[j]:j+=o
        if not j&0x88 and B[j] in (4+8*s,5+8*s):return 1
    return 0
def rep():
    n=len(KS)-1;lo=n-HM
    if lo<0:lo=0
    for i in range(n-2,lo-1,-2):
        if KS[i]==KS[n]:return 1
    return 0
def gen(s):
    M=[]
    for f in OC:
        p=B[f]
        if p>>3!=s:continue
        t=p&7
        if t==1:
            d=16-32*s;q=f+d
            if not q&0x88 and not B[q]:
                if q<8 or q>111:
                    for r in (5,4,3,2):M.append((f,q,r))
                else:
                    M.append((f,q,0))
                    if f>>4==(1,6)[s] and not B[f+2*d]:M.append((f,f+2*d,0))
            for o in (d-1,d+1):
                q=f+o
                if q&0x88:continue
                v=B[q]
                if v:
                    if v>>3!=s:
                        if q<8 or q>111:
                            for r in (5,4,3,2):M.append((f,q,r))
                        else:M.append((f,q,0))
                elif q==EP:M.append((f,q,0))
        else:
            O=N8 if t==2 else K8 if t>4 else D4 if t==3 else O4
            o1=t==2 or t==6
            for o in O:
                q=f+o
                while not q&0x88:
                    v=B[q]
                    if v:
                        if v>>3!=s:M.append((f,q,0))
                        break
                    M.append((f,q,0))
                    if o1:break
                    q+=o
    f=4+112*s
    if B[f]==6+8*s and not atk(f,1-s):
        if C&(2<<(2*s)) and not B[f+1] and not B[f+2] and not atk(f+1,1-s):M.append((f,f+2,0))
        if C&(1<<(2*s)) and not B[f-1] and not B[f-2] and not B[f-3] and not atk(f-1,1-s):M.append((f,f-2,0))
    return M
def mk(m):
    global S,C,EP,HM,KX,KG
    f,t,pr=m;p=B[f];cp=B[t];s=p>>3;e=-1
    if not cp and p&7==1 and f&7!=t&7:e=t-16+32*s;cp=B[e]
    ST.append((p,cp,e,C,EP,HM,KX))
    if e>=0:B[e]=0;OC.discard(e)
    elif cp:OC.discard(t)
    OC.discard(f)
    n=pr+8*s if pr else p
    B[t]=n;B[f]=0;OC.add(t)
    if p&7==6:
        if abs(t-f)==2:
            if t>f:B[f+1]=B[f+3];B[f+3]=0;OC.add(f+1);OC.discard(f+3)
            else:B[f-1]=B[f-4];B[f-4]=0;OC.add(f-1);OC.discard(f-4)
        KG[s]=t;C&=~[3,12][s]
    for q in (f,t):C&=~CR.get(q,0)
    EP=(f+t)//2 if p&7==1 and abs(f-t)==32 else -1
    HM=0 if p&7==1 or cp else HM+1
    KX^=Z[f][p]^Z[t][n]
    if cp:
        if e<0:KX^=Z[t][cp]
        else:KX^=Z[e][cp]
    KS.append(KX);S^=1
    return cp
def um(m):
    global S,C,EP,HM,KX,KG
    f,t,pr=m;p,cp,e,C,EP,HM,KX=ST.pop()
    s=p>>3
    B[f]=p;B[t]=0;OC.add(f)
    if e>=0:B[e]=cp;OC.add(e);OC.discard(t)
    elif cp:B[t]=cp;OC.add(t)
    else:OC.discard(t)
    if p&7==6:
        KG[s]=f
        if abs(t-f)==2:
            if t>f:B[f+3]=B[f+1];B[f+1]=0;OC.add(f+3);OC.discard(f+1)
            else:B[f-4]=B[f-1];B[f-1]=0;OC.add(f-4);OC.discard(f-1)
    KS.pop();S^=1
def ev():
    s=0;b=0
    for i in OC:
        p=B[i];t=p&7
        if p<8:s+=V[t]+PST[t][i];b+=t==3
        else:s-=V[t]+PST[t][i^112];b-=t==3
    if b>1:s+=30
    if b<-1:s-=30
    return s if S==0 else -s
def ok(m,bm,kl):
    if m==bm:return 1<<40
    v=B[m[1]]
    if v:return (1<<30)+9*V[v&7]-V[B[m[0]]&7]
    if m[2]:return 1<<25
    if m==kl[0]:return 1<<20
    if m==kl[1]:return 1<<19
    return HI[m[0]*128+m[1]]
def qs(al,be,ply):
    global ND,AB
    if AB:return al
    ND+=1
    if ND>BU:AB=1;return al
    s=S
    if B[KG[s]]!=6+8*s:return -MATE+ply
    st=ev()
    if st>=be:return st
    if st>al:al=st
    if ply>60:return al
    M=[m for m in gen(s) if B[m[1]] or m[2] or m[1]==EP]
    M.sort(key=lambda m:9*V[(B[m[1]]or 1)&7]-V[B[m[0]]&7],reverse=True)
    for m in M:
        cp=mk(m)
        if cp and cp&7==6:um(m);return MATE-ply
        sc=-qs(-be,-al,ply+1)
        um(m)
        if AB:break
        if sc>al:
            al=sc
            if al>=be:break
    return al
def ab(d,al,be,ply):
    global ND,AB
    if AB:return al
    ND+=1
    if ND>BU:AB=1;return al
    s=S
    if B[KG[s]]!=6+8*s:return -MATE+ply
    if HM>99:return 0
    if HM>3 and rep():return 0
    k=(KX,S,C,EP);e=TT.get(k);bm=None
    if e:
        bm=e[3]
        if e[0]>=d:
            if e[2]==0:return e[1]
            if e[2]>0:
                if e[1]>al:al=e[1]
            elif e[1]<be:be=e[1]
            if al>=be:return e[1]
    if d<1:return qs(al,be,ply)
    ic=atk(KG[s],s^1)
    M=gen(s)
    if ic:
        o=[]
        for m in M:
            cp=mk(m)
            if not (cp and cp&7==6) and not atk(KG[s],s^1):o.append(m)
            um(m)
        M=o
    if not M:return -MATE+ply if ic else 0
    kl=KL[ply]
    M.sort(key=lambda m:ok(m,bm,kl),reverse=True)
    a0=al;b0=be;best=-MATE;bv=None
    for m in M:
        v=B[m[1]];cp=mk(m)
        if cp and cp&7==6:um(m);return MATE-ply
        sc=-ab(d-1,-be,-al,ply+1)
        um(m)
        if AB:break
        if sc>best:
            best=sc;bv=m
            if sc>al:
                al=sc
                if al>=be:
                    if not v and not m[2]:
                        KL[ply]=[m,kl[0]];kl=KL[ply]
                        HI[m[0]*128+m[1]]+=d*d
                    break
    if AB:return al
    TT[k]=(d,best,-1 if best<=a0 else 1 if best>=b0 else 0,bv)
    return best
def pick(ms):
    global ND,AB
    ND=0;AB=0;best=ms[0]
    for d in range(1,60):
        val=-MATE;bm=ms[0]
        for m in ms:
            mk(m)
            sc=-ab(d-1,-MATE,-val,1)
            um(m)
            if AB:break
            if sc>val:val=sc;bm=m
        if AB:break
        best=bm;ms=[bm]+[m for m in ms if m!=bm]
        if val>MATE-500:break
    return best
def load(F):
    global B,OC,S,C,EP,HM,KX,KS,KG
    a=F.split();B=[0]*128;r=7;c=0
    for x in a[0]:
        if x=="/":r-=1;c=0
        elif x>"9":B[r*16+c]=" PNBRQK  pnbrqk".index(x);c+=1
        else:c+=int(x)
    OC={i for i in range(128) if B[i]}
    S=0 if a[1]=="w" else 1
    C=sum({"K":1,"Q":2,"k":4,"q":8}.get(x,0) for x in a[2])
    EP="abcdefgh".index(a[3][0])+(int(a[3][1])-1)*16 if a[3]!="-" else -1
    HM=int(a[4]);KX=0;KG=[0,0]
    for i in OC:
        KX^=Z[i][B[i]]
        if B[i]&7==6:KG[B[i]>>3]=i
    KS=[KX]
def uc(u):
    return ((int(u[1])-1)*16+"abcdefgh".index(u[0]),(int(u[3])-1)*16+"abcdefgh".index(u[2])," nbrq".index(u[4])+1 if len(u)>4 else 0)
def uci(m):
    return "abcdefgh"[m[0]&7]+str((m[0]>>4)+1)+"abcdefgh"[m[1]&7]+str((m[1]>>4)+1)+("nbrq"[m[2]-2]if m[2]else "")
def pick2(g):
    global GID,NM
    if g["game"]!=GID:GID=g["game"];load(g["start_fen"]);NM=0
    for u in g["moves"][NM:]:mk(uc(u))
    NM=len(g["moves"])
    return pick([uc(u) for u in g["legal_moves"]])
def post(p,b):
    r=U.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
    with U.urlopen(r) as x:return json.load(x)
while 1:
    g=post("/game",{})
    if g["status"]=="done":break
    while g["status"]=="your_move":
        try:r=post("/move",{"game":g["game"],"move":uci(pick2(g))})
        except Exception:
            try:r=post("/move",{"game":g["game"],"move":g["legal_moves"][0]})
            except Exception as x:sys.exit(str(x))
        g=r
print("done",g.get("wins"),g.get("draws"),g.get("losses"),file=sys.stderr)