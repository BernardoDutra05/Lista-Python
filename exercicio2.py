#BERNARDO DUTRA APERIBENSE OTTONI
class  Funcionario():
    def __init__(self):
        self.salario_bruto = 1000
        self.valor_hora_extra = 10
        self.numero_hora_extra = 20

    def calcular_salario_liquido(self):
        salario_com_horas_extras = self.salario_bruto + self.numero_hora_extra * self.valor_hora_extra
        desconto_inss = salario_com_horas_extras - (salario_com_horas_extras * 8) /100
        return desconto_inss




funcionario1 = Funcionario()
print("Salário Líquido R$",funcionario1.calcular_salario_liquido())

