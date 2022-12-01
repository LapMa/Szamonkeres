
#1.Feladat
"""
nev = input('kérek egy vezetéknevet: ')
nev2 = input('kérek egy kerszetnevet: ')

print(f"Üdv, {nev} {nev2}")
print(f"Üdv, {nev2} {nev}")"""

#2Feladat
"""
szam = int(input("Kéregy egy számot: "))

print("A megelöző szám:", (szam - 1))
print("A megelöző szám:", (szam + 1))"""


#3Feladat
"""
szam = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy számot: "))

print("A két szám összege:",(szam + szam2))
print("A két szám különbsége:", (szam - szam2))
print("A két szám szorzata:" ,(szam * szam2))
print("A két szám hányadosa:" (szam % szam2))"""

#4Feladat
"""
szam = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy számot: "))

c =(2* szam + 3*szam2)
d =(2* szam - 3*szam2)

print("C áltozó:"(c))
print("D változó: "(d))"""

#5Feladat
"""
for szam in range(1,21):
    if szam % 2 == 0:
        print("Páros számok 1-20-ig",szam,end=",")
print()
for szam2 in range(1,21):
    if szam2 % 2 == 1:
        print("Páratlan számok 1-20-ig",szam2,end=",")"""

#6Feledat
"""
mennyi = input("Hányszor: ")
n = int(input("Hány számot szertnél: "))

for j in range(mennyi):
    print(n)
"""

#7Feledat
also = int(input("Alső szám: "))
felso = int(input("Felső szám: "))

list = range(also,felso+1)
sum2 = 0
i = 0
for x in list:
    sum2 = sum2 + x
    i += 1

print(sum2, sum2/i)