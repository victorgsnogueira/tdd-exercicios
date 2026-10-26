# Exercícios Práticos de TDD - LAB V

Implementação dos três exercícios da atividade de TDD em Python, usando unittest para os testes e pytest-cov para a cobertura.

## Estrutura

Cada exercício fica em uma pasta separada, com o código em `src` e os testes em `tests`.

```
exc-1/   Triângulo
exc-2/   Validação de Person (is_valid_to_include)
exc-3/   Calculadora de salário
```

## Requisitos

- Python 3
- pytest e pytest-cov (apenas para gerar a cobertura)

Para instalar em um ambiente virtual, na raiz do projeto:

```
python3 -m venv .venv
source .venv/bin/activate
pip install pytest pytest-cov
```

## Build

Não há etapa de build, o projeto é Python puro e não tem dependências além das de teste.

## Execução dos testes

Entrar na pasta do exercício e rodar:

```
cd exc-1
python3 -m unittest discover -v
```

Ou com o pytest:

```
cd exc-1
python3 -m pytest -v
```

O mesmo vale para `exc-2` e `exc-3`.

## Cobertura

Com o ambiente virtual ativado, dentro da pasta de cada exercício:

```
python3 -m pytest --cov=src --cov-report=term-missing
```

## Evidências

### Exercício 1 - Triângulo

```
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
src/triangulo.py      18      0   100%
------------------------------------------------
TOTAL                 18      0   100%
============================== 15 passed in 0.16s ==============================
```

### Exercício 2 - Person

```
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
src/person.py           8      0   100%
src/person_dao.py      15      0   100%
-------------------------------------------------
TOTAL                  23      0   100%
============================== 16 passed in 0.15s ==============================
```

### Exercício 3 - Calculadora de salário

```
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/calculadora_salario.py      16      0   100%
src/funcionario.py               6      0   100%
----------------------------------------------------------
TOTAL                           22      0   100%
============================== 12 passed in 0.17s ==============================
```
