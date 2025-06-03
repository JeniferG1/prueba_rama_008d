decil = 0
promedio = 0
Arancel = 2200000
Matrícula = 95000
desc_aran = 0
desc_matr = 0

decil =  int(input("Ingrese el decil "))
promedio = float(input("Ingrese su promedio "))

if decil == 1  or decil == 2:
    if promedio > 6.5:
        desc_aran = 0.25
    elif promedio > 5.5 and promeido <= 6.5:
        desc_aran = 0.13
elif decil == 3  or decil == 4:
    if promedio > 6.5:
        desc_aran = 0.18
    elif promedio > 5.5 and promeido <= 6.5:
        desc_aran = 0.12

pago_arancel =  round(Arancel * desc_aran,0)

if decil == 1 or decil == 2 or decil == 3:
   desc_matr = 0.12
   if promedio >= 6:
       desc_matr = desc_matr + 0.05

pago_matricula = round(Matrícula*desc_matr,0)
