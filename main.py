#1
def mama(*args):
    k=0
    s=0
    for znach in args:
        s=s+int(znach)
        k=k+1
    print(s/k)
mama(1, 2, 3, 4, 5)

#2
b=[]
def ryadki(*args):
    for i in args:
        r=len(i)
        b.append(r)
    for j in b:
        maxi=b[0]
        if int(j)>maxi:
            maxi=int(j)
    print(maxi)
ryadki("abc", "defg", "hijkl", "moidshf;hg")

#3
b=[]
def ryadki(*args):
    for i in args:
        b.append(i)
    print(' '.join(args))
ryadki("abc", "defg", "hijkl", "mnopqrstuvw")

#4
people=[('nikita', 15), ('ludina', 45), ('gleb', 1)]
def create_dict(*args):
    name_age={}
    if args:
        for name, age in args:
            name_age[name]=age
    return name_age
print(create_dict(people))
