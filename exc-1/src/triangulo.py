class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def classificar(self):
        self._validar()

        if self.lado_a == self.lado_b == self.lado_c:
            return "equilatero"
        if (self.lado_a == self.lado_b
                or self.lado_a == self.lado_c
                or self.lado_b == self.lado_c):
            return "isosceles"
        return "escaleno"

    def _validar(self):
        a, b, c = self.lado_a, self.lado_b, self.lado_c

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Os lados devem ser maiores que zero")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("A soma de dois lados deve ser maior que o terceiro")
