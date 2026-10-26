import unittest

from src.person import Person, Email
from src.person_dao import PersonDAO


class TestPersonDAO(unittest.TestCase):

    def setUp(self):
        self.dao = PersonDAO()

    def test_pessoa_valida(self):
        person = Person("Joao Silva", 30, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), [])

    def test_nome_com_uma_parte(self):
        person = Person("Joao", 30, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Nome invalido"])

    def test_nome_com_numero(self):
        person = Person("Joao Silva2", 30, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Nome invalido"])

    def test_nome_vazio(self):
        person = Person("", 30, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Nome invalido"])

    def test_idade_zero(self):
        person = Person("Joao Silva", 0, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Idade invalida"])

    def test_idade_negativa(self):
        person = Person("Joao Silva", -1, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Idade invalida"])

    def test_idade_201(self):
        person = Person("Joao Silva", 201, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Idade invalida"])

    def test_idade_1(self):
        person = Person("Joao Silva", 1, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), [])

    def test_idade_200(self):
        person = Person("Joao Silva", 200, [Email("joao@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), [])

    def test_sem_email(self):
        person = Person("Joao Silva", 30, [])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Pessoa deve ter ao menos um email"])

    def test_email_sem_arroba(self):
        person = Person("Joao Silva", 30, [Email("joaogmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Email invalido"])

    def test_email_sem_ponto(self):
        person = Person("Joao Silva", 30, [Email("joao@gmailcom")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Email invalido"])

    def test_email_sem_usuario(self):
        person = Person("Joao Silva", 30, [Email("@gmail.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Email invalido"])

    def test_email_sem_dominio(self):
        person = Person("Joao Silva", 30, [Email("joao@.com")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Email invalido"])

    def test_email_sem_final(self):
        person = Person("Joao Silva", 30, [Email("joao@gmail.")])
        self.assertEqual(self.dao.is_valid_to_include(person), ["Email invalido"])

    def test_varios_erros(self):
        person = Person("Joao", 0, [])
        self.assertEqual(
            self.dao.is_valid_to_include(person),
            ["Nome invalido", "Idade invalida", "Pessoa deve ter ao menos um email"],
        )


if __name__ == "__main__":
    unittest.main()
