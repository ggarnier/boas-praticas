---?image=blue.jpg&position=top&size=100% 75%
@title[Boas práticas em desenvolvimento de software]

@snap[north text-white span-100]
@size[2.7em](Boas práticas em desenvolvimento de software)
@snapend

@snap[south text-blue span-100]
@size[1.8em](Guilherme Garnier)
@snapend

---?image=blue.jpg&position=top&size=100% 20%

@snap[north text-white span-100]
@size[1.5em](Por que seguir boas práticas?)
@snapend

@snap[south span-100]
@ul[](false)
- software nunca está pronto. Depois de entregue, precisa de manutenção
- todo software tem bugs :/
- código é lido muito mais vezes do que alterado: legibilidade é importante
- você não sabe quem irá alterar esse código no futuro, qual o contexto da pessoa. Pode ser você mesmo, sem lembrar do contexto em que está agora
@ulend
@snapend

---

## Por que modificar um software?

- correção de bugs
- novas features
- melhorias no design
- otimizações no uso de recursos

---

# Como melhorar a qualidade do código

- clean code
- padrões
- testes

---

# Clean code

![](images/wtfm.jpg)

---

- código ruim pode funcionar, mas dificulta a manutenção
- trabalhar com código ruim é como tentar encontrar um objeto no escuro. Código limpo é como acender a luz antes de procurar
- clean code é o código que deixa claras suas intenções e é fácil de refatorar
- pressa não é motivo para abrir mão da qualidade. Um médico não deixaria de lavar as mãos ou seguir procedimentos de segurança antes de uma cirurgia por pressa

---

## Nomes

Nomes devem revelar uma intenção

```python
def get_them():
    list1 = []
    for x in the_list:
        if x[0] == 4:
            list1.append(x)
    return list1
```

```python
def get_flagged_cells():
    flagged_cells = []
    for cell in game_board:
        if cell[STATUS_VALUE] == FLAGGED:
            flagged_cells.append(cell)
    return flagged_cells
```

---

## Nomes

Nomes devem ser fáceis de pronunciar. Facilita nas discussões do time

```python
class DtaRcrd102:
    def __init__(self):
        self.genymdhms = ...
        self.modymdhms = ...
        self.pszqint = "102"
```

```python
class Customer:
    def __init__(self):
        self.generationTimestamp = ...
        self.modificationTimestamp = ...
        self.recordId = "102"
```

---

## Nomes

Quanto maior o escopo, mais específico deve ser o nome

```python
MAX_ITEMS_PER_PRODUCT = 5

def list_active_items(self):
    product_category = "active"
    result = []
    for product in list_products():
        if product.category == product_category:
            for i in range(0, MAX_ITEMS_PER_PRODUCT):
                result.append(product)
    return result
```

---

## Nomes

Evite nomes muito genéricos que possam confundir dependendo do contexto.

Exemplos:

- Processor
- Data
- Info
- Manager

---

## Nomes

Use padrões na definição dos nomes. Reduz a chance de erros

```python
class UserDB:
    def find_users(self):
        ...

class ProductsDB:
    def list_all(self):
        ...

class Categories:
    def getCategories(self):
        ...
```

```python
class UsersDB:
    def list_all(self):
        ...

class ProductsDB:
    def list_all(self):
        ...

class CategoriesDB:
    def list_all(self):
        ...
```
