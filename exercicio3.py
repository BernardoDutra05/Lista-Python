#BERNARDO DUTRA APERIBENSE OTTONI
class  Energia():
    def __init__(self):
        self.numeros_quillowats = 1000
        self.valor_quillowatt = 12/100

    def calculcar_conta_de_luz(self):
        valor_conta = self.numeros_quillowats * self.valor_quillowatt
        acrescimo_icms = valor_conta + valor_conta * 18/100
        return acrescimo_icms

conta_de_luz = Energia()
print("Valor da Conta com o ICMS R$",conta_de_luz.calculcar_conta_de_luz())

