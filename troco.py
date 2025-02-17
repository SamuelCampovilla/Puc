c = int(input("Digite o valor da compra "))
p = int(input("Digite o valor do pagamento "))
t = (c-p) * -1
print("Compra: ",c)
print("Pagamento: ",p)
print("Troco: ",t)

print("EM:")
if t>100 or t==100:
    print("R$ 100,00", (t//100), "cédulas")
else:
    print("R$ 100,00 0 cédulas")
d = t%100
if d>50 or d==50:
    print("R$ 50,00", (d//50), "cédulas")
else:
    print("R$ 50,00 0 cédulas")
dd = d%50
if dd>20 or dd==20:
    print("R$ 20,00", (dd//20), "cédulas")
else:
    print("R$ 20,00 0 cédulas")
u = dd%20
if u>10 or u==10:
    print("R$ 10,00", (u//10), "cédulas")
else:
    print("R$ 10,00 0 cédulas")
