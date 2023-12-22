print("Nama : MUH.DAFFA NASHWAN RASYA")
print("Nim  : 231031096")
print("Prodi: Sistem Informasi")
print("Tanggal Lahir : 27-10-2005")

#Operator Penugasan
print()
a = 96
print("Nilai a =", a)
a = 96
a+=2
print("Nilai a+=2 akan menjadi", a)
a = 96
a-=2
print("Nilai a-=2 akan menjadi", a)
a = 96
a*=2
print("Nilai a*=2 akan menjadi", a)
a = 96
a/=2
print("Nilai a/=2 akan menjadi", a)
a = 96
a%=2
print("Nilai a%=2 akan menjadi", a)
a = 96
a**=2
print("Nilai a**=2 akan menjadi", a)
a = 96
a//=2
print("Nilai a//=2 akan menjadi", a)
a = 96
a&=2
print("Nilai a&=2 akan menjadi", a)
a = 96
a|=2
print("Nilai a|=2 akan menjadi", a)
a = 96
a^=2
print("Nilai a^=2 akan menjadi", a)
a = 96
a>>=2
print("Nilai a>>=2 akan menjadi", a)
a = 96
a<<=2
print("Nilai a<<=2 akan menjadi", a)

#OR
print()
b = True
print("Nilai b =",b)

b|=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b =",b)

b|=False
print("Nilai b|=False akan menjadi",b)

#AND
print()
b=True
print("Nilai b =",b)

b&=False
print("Nilai b&=False akan menjadi",b)

b=False
print("Nilai b =",b)

b&=False
print("Nilai b&=False akan menjadi",b)

#XOR
print()
b=True
print("Nilai b =",b)

b^=False
print("Nilai b^=False akan menjadi",b)

b=False
print("Nilai b =",b)

b^=False
print("Nilai b^=False akan menjadi",b)

#Shifthing
print()
c=0b0100
print("Nilai c =",format(c, "04b"))

c>>=1
print("Nilai c >>=1 akan menjadi",format(c, "04b"))
c=0b0100
c<<=1
print("Nilai c <<=1 akan menjadi",format(c, "04b"))

#Operasi Komparasi/Perbandingan
print()
a=6 #isi dengan ujung NIM
b=11 #Ubah dengan hasil jumlah ujung NIM dengan 5
print("================== Besar dari 9")
hasil = a>11
print(a,"> 11 adalah",hasil)
hasil = b>11
print(b,"> 11 adalah",hasil)

print("================== Kecil dari 9")
hasil = a<11
print(a,"< 11 adalah",hasil)
hasil = b<11
print(b,"< 11 adalah",hasil)

print("================== Besar atau sama dari 9")
hasil = a>=11
print(a,">= 11 adalah",hasil)
hasil = b>=11
print(b,">= 11 adalah",hasil)

print("================== Kecil atau sama dari 9")
hasil = a<=11
print(a,"<= 11 adalah",hasil)
hasil = b<=11
print(b,"<= 11 adalah",hasil)

print("================== Sama dengan 9")
hasil = a==11
print(a,"== 11 adalah",hasil)
hasil = b==11
print(b,"== 11 adalah",hasil)

print("================== Tidak sama dengan 9")
hasil = a!=11
print(a,"!= 11 adalah",hasil)
hasil = b!=11
print(b,"!= 11 adalah",hasil)

#Operasi Logika
print()
print("=============NOT=============")
a=True
c = not a
print("a adalah",a)
print("------c = not a-------NOT")
print("c adalah",c)

print("=============OR=============")
a=True
b=True
c=a or b
print(a, "OR",b,"menjadi",c)

a=True
b=False
c=a or b
print(a, "OR",b,"menjadi",c)

a=False
b=True
c=a or b
print(a, "OR",b,"menjadi",c)

a=False
b=False
c=a or b
print(a, "OR",b,"menjadi",c)

print("=============AND=============")
a=True
b=True
c=a and b
print(a, "AND",b,"menjadi",c)

a=True
b=False
c=a and b
print(a, "AND",b,"menjadi",c)

a=False
b=True
c=a and b
print(a, "AND",b,"menjadi",c)

a=False
b=False
c=a and b
print(a, "AND",b,"menjadi",c)

print("=============XOR=============")
a=True
b=True
c=a ^ b
print(a, "^",b,"menjadi",c)

a=True
b=False
c=a ^ b
print(a, "^",b,"menjadi",c)

a=False
b=True
c=a ^ b
print(a, "^",b,"menjadi",c)

a=False
b=False
c=a ^ b
print(a, "^",b,"menjadi",c)

#TUGAS
#Buat kode untuk masing masing operator berikut
#Jawaban
print()
print("=============NAND=============")
a=True
b=True
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

a=True
b=False
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

a=False
b=True
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

a=False
b=False
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

print("=============NOR==============")
a=True
b=True
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

a=True
b=False
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

a=False
b=True
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

a=False
b=False
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

print("=============NXOR=============")
a=True
b=True
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

a=True
b=False
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

a=False
b=True
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

a=False
b=False
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

#Operator Membership
print()
print("======================= IN")
nama_lengkap = "Bachruddin Jusuf Habibie"
test = "a"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

test = "rud"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

test = "bac"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

print()
print("=======================NOT IN")
nama_lengkap = "Bachruddin Jusuf Habibie"
test = "a"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

test = "rud"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

test = "bac"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

#Tugas
#Dengan cara yang sama buat operator in dan not in , ubah nama â†- lengkap menjadi nama masing - masing dengan uji test
test1 = "DA"
test2 = "MD"
test3 = "MDN"
test4 = "d"
test5 = "f"
test6 = "n"

#Jawaban
print()
print("======================= IN")
nama_lengkap = "MUH.DAFFA NASHWAN RASYA"
test1 = "DA"
cek = test1 in nama_lengkap
print(test1," terdapat di ",nama_lengkap," adalah ",str(cek))

test2 = "MD"
cek = test2 in nama_lengkap
print(test2," terdapat di ",nama_lengkap," adalah ",str(cek))

test3 = "MDN"
cek = test3 in nama_lengkap
print(test3," terdapat di ",nama_lengkap," adalah ",str(cek))

test4 = "d"
cek = test4 in nama_lengkap
print(test4," terdapat di ",nama_lengkap," adalah ",str(cek))

test5 = "f"
cek = test5 in nama_lengkap
print(test5," terdapat di ",nama_lengkap," adalah ",str(cek))

test6 = "n"
cek = test6 in nama_lengkap
print(test6," terdapat di ",nama_lengkap," adalah ",str(cek))


print()
print("======================= NOT IN")
nama_lengkap = "MUH.DAFFA NASHWAN RASYA"
test1 = "DA"
cek = test1 not in nama_lengkap
print(test1," terdapat di ",nama_lengkap," adalah ",str(cek))

test2 = "MD"
cek = test2 not in nama_lengkap
print(test2," terdapat di ",nama_lengkap," adalah ",str(cek))

test3 = "MDN"
cek = test3 not in nama_lengkap
print(test3," terdapat di ",nama_lengkap," adalah ",str(cek))

test4 = "d"
cek = test4 not in nama_lengkap
print(test4," terdapat di ",nama_lengkap," adalah ",str(cek))

test5 = "f"
cek = test5 not in nama_lengkap
print(test5," terdapat di ",nama_lengkap," adalah ",str(cek))

test6 = "n"
cek = test6 not in nama_lengkap
print(test6," terdapat di ",nama_lengkap," adalah ",str(cek))


#Operator Bitwise
print()
a=27 # ubah menjadi tanggal lahir 
a +=60
b=10 # ubah menjadi bulan lahir
b+= 90
print("=============================OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(|)")
hasil=a|b
print("Nilai",a,"|",b,"dalam biner =", format(hasil,"08b"))

print("=============================AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(&)")
hasil=a&b
print("Nilai",a,"&",b,"dalam biner =", format(hasil,"08b"))

print("=============================XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(^)")
hasil=a^b
print("Nilai",a,"^",b,"dalam biner =", format(hasil,"08b"))

print("=============================NOT")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print( "----------------------------(~a)")
hasil= ~a
print("Nilai ~",a,"dalam biner  =", format(hasil,"08b"))

print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~b)")
hasil= ~b
print("Nilai ~",b,"dalam biner  =", format(hasil,"08b"))

print("=============================>>")
print("Nilai",a,"dalam biner     =", format(a,"08b"))
print( "----------------------------(>>2)")
hasil= a >> 2
print("Nilai",a,">>2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------(>>2)")
hasil= b >> 2
print("Nilai",b,">>2 dalam biner =", format(hasil,"08b"))

print("=============================<<")
print("Nilai",a,"dalam biner     =", format(a,"08b"))
print( "----------------------------(<<2)")
hasil= a << 2
print("Nilai",a,"<<2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------(<<2)")
hasil= b << 2
print("Nilai",b,"<<2 dalam biner =", format(hasil,"08b"))

#Tugas
#print("=============================NOT AND")
#print("=============================NOT OR")
#print("=============================NOT XOR")
#print("=============================NOT (>>2)")
#print("=============================NOT (<<2)")

#jawaban
print()
a=27 # ubah menjadi tanggal lahir 
a +=60
b=10 # ubah menjadi bulan lahir
b+= 90

print("=============================NOT AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~&)")
hasil=~(a&b)
print("Nilai",a,"~&",b,"dalam biner =", format(hasil,"08b"))

print("=============================NOT OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~|)")
hasil=~(a|b)
print("Nilai",a,"~|",b,"dalam biner =", format(hasil,"08b"))

print("=============================NOT XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~^)")
hasil=~(a^b)
print("Nilai",a,"~^",b,"dalam biner =", format(hasil,"08b"))

print( "----------------------------NOT (>>2)")
hasil= ~(a >> 2)
print("Nilai",a,"~>>2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------NOT (>>2)")
hasil= ~(b >> 2)
print("Nilai",b,"~>>2 dalam biner =", format(hasil,"08b"))

print( "----------------------------NOT (<<2)")
hasil= ~(a << 2)
print("Nilai",a,"~<<2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------NOT (<<2)")
hasil= ~(b << 2)
print("Nilai",b,"~<<2 dalam biner =", format(hasil,"08b"))