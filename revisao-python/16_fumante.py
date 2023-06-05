anos_fumante = int(input("Por quantos Anos você fumou: "))
cigarros_dia = int(input("Em média, quantos cigarros vc fumava por dia: "))
total_cigarros = anos_fumante * 365 * cigarros_dia
perda_vida = (total_cigarros * 10)
dias_perdidos = perda_vida / (60 * 24)
print(f"Você fumou por {anos_fumante} anos \nFumou {cigarros_dia} cigarros por dia \nPerdeu, em média, {perda_vida :.0f} dias de vida.")