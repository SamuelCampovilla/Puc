c = int(input("Digite o valor da compra "))
p = int(input("Digite o valor do pagamento "))
t=c-p
print("Compra: ",c)
print("Pagamento: ",p)
if c-p>0:
    print("Troco: ",t)
else:
    print("Troco: ",(t*-1))

print("EM:")        
if t<=100:
    print("R$ 100,00", (t%100), "cédulas")
else:
    print("R$ 100,00 0 cédulas")
