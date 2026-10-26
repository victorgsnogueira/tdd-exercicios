import re


class PersonDAO:

    def is_valid_to_include(self, person):
        errors = []

        parts = person.name.split()
        if len(parts) < 2 or not all(part.isalpha() for part in parts):
            errors.append("Nome invalido")

        if person.age < 1 or person.age > 200:
            errors.append("Idade invalida")

        if len(person.emails) == 0:
            errors.append("Pessoa deve ter ao menos um email")

        for email in person.emails:
            if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email.name):
                errors.append("Email invalido")

        return errors
