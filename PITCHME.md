# Boas práticas em desenvolvimento de software

## Guilherme Garnier

---

# Por que seguir boas práticas?

- software nunca está pronto. Depois de entregue, precisa de manutenção
- todo software tem bugs :/
- código é lido muito mais vezes do que alterado: legibilidade é importante
- você não sabe quem irá alterar esse código no futuro, qual o contexto da pessoa. Pode ser você mesmo, sem lembrar do contexto em que está agora

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
