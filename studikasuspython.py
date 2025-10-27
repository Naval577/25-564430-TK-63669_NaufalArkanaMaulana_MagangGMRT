import math

l1 = int (input ("berapa panjang tulang femur anda(dalam cm): "))
l2 = int (input ("berapa panjang tulang tibia anda(dalam cm): "))
d1 = int (input ("berapa derajat tulang femur dimiringkan: "))
d2 = int (input ("berapa derajat tulang tibia dimiringkan: "))

d1 = math.radians(d1)
d2 = math.radians(d2)

x = l1*math.cos(d1) + l2*math.cos(d1+d2)
y = l1*math.sin(d1) + l2*math.sin(d1+d2)
        
print ("Hasil perhitungan: ")
print (f"x = {x: .4f}")
print (f"x = {y: .4f}")
print ("koordinat lengang", f"x({x: .4f}, {y: .4f})")
