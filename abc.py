def happyNewYear(b):
    o=[]
    t=0
    b=b.split(" ")
    for i in b:
        if len(i)>t:
            t=len(i)
    o.append("**"+"*"*t+"**")
    for j in b:
        q=t-len(j)
        o.append("* "+j+" "*q+" *")
    o.append("**"+"*"*t+"**")
    return o
    
a="Happy New Year and CodeFight On in 2016!"
e=happyNewYear(a)
for i in e:
    print i
