





import json ,os ,sys ,urllib .request as U 

E =os .environ ["MAKEFUN_ENV_URL"]

def post (path ,body ):
    r =U .Request (E +path ,data =json .dumps (body ).encode (),
    headers ={"content-type":"application/json"})
    return json .load (U .urlopen (r ))

VAL =[0 ,100 ,320 ,330 ,500 ,900 ,30000 ]

PST_P =[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,10 ,10 ,-20 ,-20 ,10 ,10 ,5 ,5 ,-5 ,-10 ,0 ,0 ,-10 ,-5 ,5 ,
0 ,0 ,0 ,20 ,20 ,0 ,0 ,0 ,5 ,5 ,10 ,25 ,25 ,10 ,5 ,5 ,10 ,10 ,20 ,30 ,30 ,20 ,10 ,10 ,
50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
PST_N =[-50 ,-40 ,-30 ,-30 ,-30 ,-30 ,-40 ,-50 ,-40 ,-20 ,0 ,5 ,5 ,0 ,-20 ,-40 ,
-30 ,5 ,10 ,15 ,15 ,10 ,5 ,-30 ,-30 ,0 ,15 ,20 ,20 ,15 ,0 ,-30 ,
-30 ,5 ,15 ,20 ,20 ,15 ,5 ,-30 ,-30 ,0 ,10 ,15 ,15 ,10 ,0 ,-30 ,
-40 ,-20 ,0 ,0 ,0 ,0 ,-20 ,-40 ,-50 ,-40 ,-30 ,-30 ,-30 ,-30 ,-40 ,-50 ]
PST_B =[-20 ,-10 ,-10 ,-10 ,-10 ,-10 ,-10 ,-20 ,-10 ,5 ,0 ,0 ,0 ,0 ,5 ,-10 ,
-10 ,10 ,10 ,10 ,10 ,10 ,10 ,-10 ,-10 ,0 ,10 ,10 ,10 ,10 ,0 ,-10 ,
-10 ,5 ,5 ,10 ,10 ,5 ,5 ,-10 ,-10 ,0 ,5 ,10 ,10 ,5 ,0 ,-10 ,
-10 ,0 ,0 ,0 ,0 ,0 ,0 ,-10 ,-20 ,-10 ,-10 ,-10 ,-10 ,-10 ,-10 ,-20 ]
PST_R =[0 ,0 ,0 ,5 ,5 ,0 ,0 ,0 ,5 ,10 ,10 ,10 ,10 ,10 ,10 ,5 ,-5 ,0 ,0 ,0 ,0 ,0 ,0 ,-5 ,
-5 ,0 ,0 ,0 ,0 ,0 ,0 ,-5 ,-5 ,0 ,0 ,0 ,0 ,0 ,0 ,-5 ,-5 ,0 ,0 ,0 ,0 ,0 ,0 ,-5 ,
-5 ,0 ,0 ,0 ,0 ,0 ,0 ,-5 ,0 ,0 ,0 ,5 ,5 ,0 ,0 ,0 ]
PST_Q =[-20 ,-10 ,-10 ,-5 ,-5 ,-10 ,-10 ,-20 ,-10 ,0 ,5 ,0 ,0 ,0 ,0 ,-10 ,
-10 ,5 ,5 ,5 ,5 ,5 ,0 ,-10 ,0 ,0 ,5 ,5 ,5 ,5 ,0 ,-5 ,
-5 ,0 ,5 ,5 ,5 ,5 ,0 ,-5 ,-10 ,0 ,5 ,5 ,5 ,5 ,0 ,-10 ,
-10 ,0 ,0 ,0 ,0 ,0 ,0 ,-10 ,-20 ,-10 ,-10 ,-5 ,-5 ,-10 ,-10 ,-20 ]
PST_K =[20 ,30 ,10 ,0 ,0 ,10 ,30 ,20 ,20 ,20 ,0 ,0 ,0 ,0 ,20 ,20 ,-10 ,-20 ,-20 ,-20 ,-20 ,-20 ,-20 ,-10 ,
-20 ,-30 ,-30 ,-40 ,-40 ,-30 ,-30 ,-20 ,-30 ,-40 ,-40 ,-50 ,-50 ,-40 ,-40 ,-30 ,
-30 ,-40 ,-40 ,-50 ,-50 ,-40 ,-40 ,-30 ,-30 ,-40 ,-40 ,-50 ,-50 ,-40 ,-40 ,-30 ,
-30 ,-40 ,-40 ,-50 ,-50 ,-40 ,-40 ,-30 ]
PST =[None ,PST_P ,PST_N ,PST_B ,PST_R ,PST_Q ,PST_K ]
MIR =[(7 -i //8 )*8 +i %8 for i in range (64 )]
N_OFF =(-17 ,-15 ,-10 ,-6 ,6 ,10 ,15 ,17 )
B_OFF =(-9 ,-7 ,7 ,9 )
R_OFF =(-8 ,-1 ,1 ,8 )
K_OFF =(-9 ,-8 ,-7 ,-1 ,1 ,7 ,8 ,9 )
CODE ="pnbrqk"


CRB =set ()


def RD (fen ):
    global CRB 
    parts =fen .split ()
    CRB =set ()if len (parts )<3 or parts [2 ]=="-"else set (parts [2 ])
    b =[0 ]*64 
    for i ,row in enumerate (parts [0 ].split ("/")):
        f =0 
        for c in row :
            if c .isdigit ():
                f +=int (c )
            else :
                v =CODE .index (c .lower ())+1 
                b [(7 -i )*8 +f ]=v if c .isupper ()else -v 
                f +=1 
    return b 


def NR (prev ,q ,mx =1 ):
    return 0 <=q <64 and abs (q %8 -prev %8 )<=mx and abs (q //8 -prev //8 )<=mx 


def KOK (s ,q ):
    if not (0 <=q <64 ):
        return False 
    df =abs (q %8 -s %8 )
    dr =abs (q //8 -s //8 )
    return (df ==1 and dr ==2 )or (df ==2 and dr ==1 )


def GM (b ,side ):
    white =side >0 
    out =[]
    push =out .append 
    for s in range (64 ):
        p =b [s ]
        if p ==0 or (p >0 )!=white :
            continue 
        t =p if p >0 else -p 
        if t ==1 :
            d =8 if white else -8 
            one =s +d 
            if 0 <=one <64 and b [one ]==0 :
                if one >55 or one <8 :
                    push ((s ,one ,5 ));push ((s ,one ,4 ));push ((s ,one ,3 ));push ((s ,one ,2 ))
                else :
                    push ((s ,one ,0 ))
                    if (8 <=s <=15 )if white else (48 <=s <=55 ):
                        two =one +d 
                        if 0 <=two <64 and b [two ]==0 :
                            push ((s ,two ,0 ))
            for c in (d -1 ,d +1 ):
                q =s +c 
                if NR (s ,q )and b [q ]!=0 and (b [q ]>0 )!=white :
                    if q >55 or q <8 :
                        push ((s ,q ,5 ));push ((s ,q ,4 ));push ((s ,q ,3 ));push ((s ,q ,2 ))
                    else :
                        push ((s ,q ,0 ))
        elif t ==2 :
            for o in N_OFF :
                q =s +o 
                if KOK (s ,q )and (b [q ]==0 or (b [q ]>0 )!=white ):
                    push ((s ,q ,0 ))
        elif t in (3 ,4 ,5 ):
            offs =B_OFF if t ==3 else (R_OFF if t ==4 else K_OFF )
            for o in offs :
                q =s 
                while True :
                    prev =q 
                    q +=o 
                    if not NR (prev ,q ):
                        break 
                    if b [q ]==0 :
                        push ((s ,q ,0 ))
                    else :
                        if (b [q ]>0 )!=white :
                            push ((s ,q ,0 ))
                        break 
        else :
            for o in K_OFF :
                q =s +o 
                if NR (s ,q )and (b [q ]==0 or (b [q ]>0 )!=white ):
                    push ((s ,q ,0 ))

            if s ==(4 if white else 60 ):
                if "K"in CRB if white else "k"in CRB :
                    if b [s +3 ]==(4 if white else -4 )and not (b [s +1 ]or b [s +2 ]):
                        push ((s ,s +2 ,0 ))
                if "Q"in CRB if white else "q"in CRB :
                    if b [s -4 ]==(4 if white else -4 )and not (b [s -1 ]or b [s -2 ]or b [s -3 ]):
                        push ((s ,s -2 ,0 ))
    return out 


def IC (b ,side ):
    """Is `side`'s king attacked? Rays out of the king, never a full scan."""
    white =side >0 
    k =b .index (6 if white else -6 )
    e =-1 if white else 1 


    for o in (7 ,9 )if white else (-7 ,-9 ):
        q =k +o 
        if NR (k ,q )and b [q ]==e :
            return True 
    for o in N_OFF :
        q =k +o 
        if KOK (k ,q )and b [q ]==2 *e :
            return True 
    for o in K_OFF :
        q =k +o 
        if NR (k ,q )and b [q ]==6 *e :
            return True 
    for offs ,pieces in ((R_OFF ,(4 *e ,5 *e )),(B_OFF ,(3 *e ,5 *e ))):
        for o in offs :
            q =k 
            while True :
                prev =q 
                q +=o 
                if not NR (prev ,q ):
                    break 
                p =b [q ]
                if p :
                    if p in pieces :
                        return True 
                    break 
    return False 


H =0 


def do (b ,m ):
    global H 
    s ,q ,pr =m 
    p =b [s ]
    cap =b [q ]
    np_ =(pr if p >0 else -pr )if pr else p 
    H ^=ZK [s ][p +6 ]^ZK [q ][cap +6 ]^ZK [q ][np_ +6 ]^ZST 
    b [q ]=np_ 
    b [s ]=0 
    if p ==6 or p ==-6 :
        if q -s ==2 :
            r =q +1 
            b [q -1 ]=b [r ]
            b [r ]=0 
        elif s -q ==2 :
            r =q -2 
            b [q +1 ]=b [r ]
            b [r ]=0 
    return p ,cap 


def UN (b ,m ,p ,cap ):
    global H 
    s ,q ,pr =m 
    np_ =(pr if p >0 else -pr )if pr else p 
    H ^=ZK [s ][p +6 ]^ZK [q ][cap +6 ]^ZK [q ][np_ +6 ]^ZST 
    if p ==6 or p ==-6 :
        if q -s ==2 :
            r =q +1 
            b [r ]=b [q -1 ]
            b [q -1 ]=0 
        elif s -q ==2 :
            r =q -2 
            b [r ]=b [q +1 ]
            b [q +1 ]=0 
    b [s ]=p 
    b [q ]=cap 


def LG (b ,side ):
    out =[]
    for m in GM (b ,side ):
        p ,c =do (b ,m )
        if not IC (b ,side ):
            out .append (m )
        UN (b ,m ,p ,c )
    return out 


def ev (b ):
    s =0 
    wb =bb =0 
    for i in range (64 ):
        p =b [i ]
        if p :
            if p >0 :
                s +=VAL [p ]+PST [p ][i ]
                if p ==3 :
                    wb +=1 
            else :
                t =-p 
                s -=VAL [t ]+PST [t ][MIR [i ]]
                if t ==3 :
                    bb +=1 
    if wb >1 :
        s +=30 
    if bb >1 :
        s -=30 
    return s 


ND =0 
CP =130000 
MT =30000 


ZK =[[((sq *13 +c *7 +1 )*2654435761 )&0xFFFFFFFF for c in range (13 )]
for sq in range (64 )]
ZST =0x9E3779B9 
KL =[[None ,None ]for _ in range (64 )]
HS ={}



def KO (b ,ply =None ):
    def k (m ):
        v =b [m [1 ]]
        if v :
            return -1000000 -VAL [v if v >0 else -v ]
        if m [2 ]:
            return -900000 
        if ply is not None :
            km =KL [ply ]
            if m ==km [0 ]:
                return -800000 
            if m ==km [1 ]:
                return -700000 
        return -HS .get (m [:2 ],0 )
    return k 


def qs (b ,side ,a ,be ):
    """Quiescence, with the check extension the house engines use: in check we
    may not stand pat and must look at every LG reply, not just captures."""
    global ND 
    ND +=1 
    chk =IC (b ,side )
    if not chk :
        st =ev (b )if side >0 else -ev (b )
        if st >=be :
            return be 
        if st >a :
            a =st 
    if ND >=CP :
        return a 
    n =0 
    for m in sorted (GM (b ,side ),key =KO (b )):
        cap =b [m [1 ]]
        if not chk and cap ==0 and not m [2 ]:
            continue 
        p ,c =do (b ,m )
        if IC (b ,side ):
            UN (b ,m ,p ,c )
            continue 
        n +=1 
        sc =-qs (b ,-side ,-be ,-a )
        UN (b ,m ,p ,c )
        if sc >=be :
            return be 
        if sc >a :
            a =sc 
    if n ==0 and chk :
        return -MT 
    return a 


def ab (b ,side ,d ,a ,be ,ply =0 ):
    global ND 
    if ND >=CP :
        return ev (b )if side >0 else -ev (b )
    ND +=1 
    if d <=0 :
        return qs (b ,side ,a ,be )
    z =H 
    if z in SN :
        return 0 
    if d >=3 and not IC (b ,side ):


        if -ab (b ,-side ,d -3 ,-be ,-be +1 ,ply +1 )>=be :
            SN .discard (z )
            return be 
    best =-MT -1 
    n =0 
    bm =None 
    SN .add (z )
    ms =sorted (GM (b ,side ),key =KO (b ,ply ))
    tm =TT .get (z )
    if tm is not None and tm in ms :
        ms .remove (tm )
        ms .insert (0 ,tm )
    for m in ms :
        p ,c =do (b ,m )
        if IC (b ,side ):
            UN (b ,m ,p ,c )
            continue 
        n +=1 
        sc =-ab (b ,-side ,d -1 ,-be ,-a ,ply +1 )
        UN (b ,m ,p ,c )
        if sc >best :
            best =sc 
            bm =m 
        if best >a :
            a =best 
        if a >=be :
            km =KL [ply ]
            if not b [m [1 ]]and not m [2 ]:
                if km [0 ]!=m :
                    KL [ply ]=[m ,km [0 ]]
                HS [m [:2 ]]=HS .get (m [:2 ],0 )+d *d 
            break 
    if bm is not None :
        TT [z ]=bm 
    SN .discard (z )
    if n ==0 :
        if IC (b ,side ):
            return -MT +ply 
        return 0 
    return best 


def uci (m ):
    return ("abcdefgh"[m [0 ]%8 ]+str (m [0 ]//8 +1 )+"abcdefgh"[m [1 ]%8 ]
    +str (m [1 ]//8 +1 )+("nbrq"[m [2 ]-2 ]if m [2 ]else ""))


SN =set ()
TT ={}


def PIK (fen ,legal_moves ):
    global ND ,H 
    SN .clear ()
    TT .clear ()
    b =RD (fen )
    side =1 if fen .split ()[1 ]=="w"else -1 
    H =ZST if side >0 else 0 
    for i in range (64 ):
        if b [i ]:
            H ^=ZK [i ][b [i ]+6 ]
    allow =set (legal_moves )
    root =sorted ([m for m in LG (b ,side )if uci (m )in allow ],key =KO (b ))
    if not root :
        return legal_moves [0 ]
    bm =root [0 ]
    ND =0 
    for d in (2 ,3 ,4 ,5 ,6 ):
        SN .clear ()
        SN .add (H )
        cur ,cm ,a =-MT -1 ,None ,-MT -1 
        for m in root :
            p ,c =do (b ,m )
            sc =-ab (b ,-side ,d -1 ,-MT -1 ,-a ,1 )
            UN (b ,m ,p ,c )
            if sc >cur :
                cur ,cm =sc ,m 
            if sc >a :
                a =sc 
            if ND >=CP :
                break 



        if ND >=CP :
            break 
        if cm :
            bm =cm 
    return uci (bm )


while True :
    g =post ("/game",{})
    if g ["status"]=="done":
        break 
    while g ["status"]=="your_move":
        g =post ("/move",{"game":g ["game"],"move":PIK (g ["fen"],g ["legal_moves"])})
    print (f"game {g ['game']}: {g ['outcome']}",file =sys .stderr )
print (f"done: {g .get ('wins')}/{g .get ('draws')}/{g .get ('losses')}",file =sys .stderr )
