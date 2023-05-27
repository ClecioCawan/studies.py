# ------------------CONVERSOR DE MEDIDAS-------------------------------------------------------------------------------------------------------- #
x = float(input(' me diga uma distancia em metros: '))
km = x / 1000
hm = x / 100
dam = x /10
m = x
dm = x * 10
cm = x * 100
mm = x * 1000
print('a medida de {}m corresponde a \n {} km \n {} hm \n {} dam \n {} m \n {} dm \n {} cm \n {} mm'.format(x, km, hm, dam , m , dm , cm, mm))
# ----------------------------------------------FIM--------------------------------------------------------------------------------------------- #