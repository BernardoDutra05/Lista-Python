#BERNARDO DUTRA APERIBENSE OTTONI
class  Funcionario():
    def __init__(self):
        self.salario_atual = 1000
        self.aumento_salario = 20

    def calcular_salario(self):
        #calcula o novo salário
      valor_do_aumento = (self.salario_atual * self.aumento_salario) / 100
      salario_aumentado = self.salario_atual + valor_do_aumento
      return  salario_aumentado

    def valor_aumento(self):
        #calcula o valor do aumento
       aumento = self.salario_atual * self.aumento_salario / 100
       return aumento



funcionario1 = Funcionario()
funcionario1.salario_atual
print("Novo Salário R$" ,funcionario1.calcular_salario())
print("Aumento de R$",funcionario1.valor_aumento())