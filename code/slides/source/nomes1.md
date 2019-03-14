## Nomes

Nomes devem revelar uma intenção

<div style="display: flex">
<pre style="flex-grow: 1"><code class="lang-python hljs">
def get_them():
  list1 = []
  for x in the_list:
    if x[0] == 4:
      list1.append(x)
  return list1
</code></pre>

<pre class="fragment" data-fragment-index="1" style="flex-grow: 1"><code class="lang-python hljs">
def get_flagged_cells():
  flagged_cells = []
  for cell in game_board:
    if cell[STATUS_VALUE] == FLAGGED:
      flagged_cells.append(cell)
  return flagged_cells
</code></pre>
</div>
