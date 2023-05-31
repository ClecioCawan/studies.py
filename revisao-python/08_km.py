distancia = float(input("Digite uma distância em metros: "))

km = distancia/1000
hm = distancia/100
dam = distancia/10
m = distancia
dm = distancia*10
cm = distancia*100
mm = distancia*1000
print(f"A distância de {distancia :.0f}m correponde a: \n{km :.5f}km\n{hm :.5f}hm\n{dam :.5f}dam\n{m}m\n{dm}dm\n{cm}cm\n{mm}mm")