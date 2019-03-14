## Nomes

Quanto maior o escopo, mais específico deve ser o nome

<div style="display: flex">
<pre style="flex-grow: 1"><code class="lang-python hljs">
class DtaRcrd102:
  def __init__(self):
    self.genymdhms = ...
    self.modymdhms = ...
    self.pszqint = "102"
</code></pre>

<pre class="fragment" data-fragment-index="1" style="flex-grow: 1"><code class="lang-python hljs">
class Customer:
  def __init__(self):
    self.generationTimestamp = ...
    self.modificationTimestamp = ...
    self.recordId = "102"
</code></pre>
</div>

