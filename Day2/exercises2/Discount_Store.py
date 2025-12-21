valor_compra = float(input("Informe o valor da compra: "))

vip_input = input("O cliente é VIP? (sim/não): ").lower()

cliente_vip = vip_input == 'sim'

if valor_compra > 100 or cliente_vip:
    print("Desconto aplicado!")
else:
    print("Sem desconto!")