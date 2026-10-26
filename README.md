# Exercícios Práticos de TDD - LAB V

Implementação dos três exercícios da atividade de TDD em Python, usando unittest para os testes.

## Estrutura

Cada exercício fica em uma pasta separada, com o código em `src` e os testes em `tests`.

```
exc-1/   Triângulo
exc-2/   Validação de Person (is_valid_to_include)
exc-3/   Calculadora de salário
```

## Requisitos

- Python 3

Não é preciso instalar nada. Tanto o unittest quanto o trace, usado para a cobertura, já vêm com o Python.

## Build

Não há etapa de build, o projeto é Python puro e não tem dependências externas.

## Execução dos testes

Entrar na pasta do exercício e rodar:

```
cd exc-1
python3 -m unittest discover -v
```

O mesmo vale para `exc-2` e `exc-3`.

## Cobertura

A cobertura foi gerada com o módulo trace do Python. Dentro da pasta de cada exercício:

```
python3 -m trace --count --summary --missing --ignore-dir=/usr/lib/python3.12 -C cobertura --module unittest discover
```

O comando roda os testes e mostra, no final, a porcentagem de linhas executadas de cada arquivo. Os arquivos `.cover` gerados na pasta `cobertura` mostram linha por linha o que foi executado.

Nos arquivos de teste a cobertura aparece abaixo de 100% só por causa da linha `unittest.main()`, que não é executada quando os testes rodam pelo `discover`.

## Evidências

### Exercício 1 - Triângulo

```
Ran 15 tests in 0.003s

OK
lines   cov%   module   (path)
   20   100%   src.triangulo   (exc-1/src/triangulo.py)
   44    97%   tests.test_triangulo   (exc-1/tests/test_triangulo.py)
```

### Exercício 2 - Person

```
Ran 16 tests in 0.003s

OK
lines   cov%   module   (path)
    8   100%   src.person   (exc-2/src/person.py)
   15   100%   src.person_dao   (exc-2/src/person_dao.py)
   58    98%   tests.test_person_dao   (exc-2/tests/test_person_dao.py)
```

### Exercício 3 - Calculadora de salário

```
Ran 12 tests in 0.002s

OK
lines   cov%   module   (path)
   16   100%   src.calculadora_salario   (exc-3/src/calculadora_salario.py)
    6   100%   src.funcionario   (exc-3/src/funcionario.py)
   35    97%   tests.test_calculadora_salario   (exc-3/tests/test_calculadora_salario.py)
```
