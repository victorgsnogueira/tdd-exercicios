class CalculadoraSalario:

    def calcular(self, funcionario):
        salario = funcionario.salario_base
        cargo = funcionario.cargo

        if cargo == "DESENVOLVEDOR":
            if salario >= 3000:
                return salario * 0.80
            return salario * 0.90

        if cargo == "DBA" or cargo == "TESTADOR":
            if salario >= 2000:
                return salario * 0.75
            return salario * 0.85

        if cargo == "GERENTE":
            if salario >= 5000:
                return salario * 0.70
            return salario * 0.80
