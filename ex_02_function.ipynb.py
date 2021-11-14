def out(a,b,c,d):
    F1=-a 
    F2=b-a
    F3=d
    print (F1,"AB段轴力")
    print (F2,"BC段轴力")
    print (F3,"CD段轴力")
out(10,5,20,15)
def plus(l1,F1,EA):
    z1=F1*l1/EA*1000
    print(z1,"AB段轴向变形")
plus(1,-10,200000)
def plus(l2,F2,EA):
    z2=F2*l2/EA*1000
    print(z2,"BC段轴向变形")
plus(1,-5,200000)
def plus(l3,F3,EA):
    z3=F3*l3/EA*1000
    print(z3,"CD段轴向变形")
plus(1.5,15,200000)
def plus(l1,z1):
    ε1=z1/l1/1000
    print(ε1,"AB段线应变")
plus(1,-0.05)
def plus(l2,z2):
    ε2=z2/l2/1000
    print(ε2,"BC段线应变")
plus(1,-0.025)
def plus(l3,z3):
    ε3=z3/l3/1000
    print(ε3,"CD段线应变")
plus(1.5,0.1125)
def plus(z1,z2,z3):
    z4=z1+z2+z3
    print(z4,"总变形量")
plus(-0.05,-0.025,0.1125)
    
