#BERNARDO DUTRA APERIBENSE OTTONI
class  Consumo():
    def __init__(self):
        self.quantidade_km_rodados = 306
        self.quantidade_comb_gasto = 18

    def calcular_media_combustivel(self):
        media = self.quantidade_km_rodados/self.quantidade_comb_gasto
        return media
carro = Consumo()

print("Média de Combustível de",carro.calcular_media_combustivel(),"KM/L")