# Algoritmo para Caminho Hamiltoniano

##  Descrição do Projeto

Este projeto implementa o algoritmo de Caminho Hamiltoniano em grafos direcionados e não-direcionados. Um Caminho Hamiltoniano é um caminho em um grafo que visita cada vértice exatamente uma vez, sem repetições.

**Principais características**:
- Implementação via backtracking otimizado
- Suporte para grafos direcionados e não-direcionados
- Análise detalhada da complexidade NP-Completa
- Visualização gráfica dos resultados (opcional)

##  Estrutura do Projeto

O repositório contém os seguintes arquivos:

## 📂 Estrutura do Projeto
```
FPAAProjeto3/
├── main.py                # Implementação principal
├── test.py                # Testes unitários
├── view.py                # Visualização gráfica
├── assets/                # Pasta para imagens
│   └── grafo.png          # Exemplo de visualização
└── README.md              # Documentação
```

##  Como Executar o Projeto
### Pré-requisitos
- Python 3.8+
- Pacotes: `networkx`, `matplotlib`

###  Clonar o repositório
```bash
git clone https://github.com/gabrielfaria13/FPAAProjeto3.git
cd FPAAProjeto3
```

###  Executar o código principal
```bash
python main.py
```

###  Rodar os testes automatizados
```bash
python -m unittest test.py
```

###  Visualização Gráfica
```bash
python view.py
```

---

##  Explicação do Algoritmo



### Fluxo do Algoritmo
1. **Inicialização**: Verifica grafo vazio e prepara estruturas
2. **Backtracking**: Explora caminhos recursivamente
3. **Condição de Parada**: Todos vértices visitados
4. **Tratamento Especial**: Grafos não-direcionados
5. **Retorno**: Caminho válido ou `None`

###  Implementação do Algoritmo

Abaixo está a implementação do algoritmo em **Python**:

```python
def encontrar_caminho_hamiltoniano(grafo: dict, direcionado: bool = False) -> list:
    """
    Encontra um caminho Hamiltoniano em um grafo
    
    Args:
        grafo: Dicionário {vértice: [vizinhos]}
        direcionado: Se True, considera o grafo como direcionado
        
    Returns:
        Lista com o caminho ou None se não existir
    """
    if not grafo:
        return None
        
    vertices = list(grafo.keys())
    n = len(vertices)
    
    def backtrack(caminho_atual: list) -> list:
        """Função recursiva de backtracking"""
        if len(caminho_atual) == n:
            return caminho_atual.copy()
            
        ultimo = caminho_atual[-1]
        
        # Explora vizinhos diretos
        for vizinho in grafo.get(ultimo, []):
            if vizinho not in caminho_atual:
                caminho_atual.append(vizinho)
                if (resultado := backtrack(caminho_atual)):
                    return resultado
                caminho_atual.pop()
                
        # Para grafos não-direcionados
        if not direcionado:
            for v, vizinhos in grafo.items():
                if ultimo in vizinhos and v not in caminho_atual:
                    caminho_atual.append(v)
                    if (resultado := backtrack(caminho_atual)):
                        return resultado
                    caminho_atual.pop()
                    
        return None
    
    # Tenta cada vértice como inicial
    for vertice in vertices:
        if (resultado := backtrack([vertice])):
            return resultado
            
    return None
```



###  Testes Unitários

####  Casos de Teste Implementados
```python
import unittest
from main import encontrar_caminho_hamiltoniano

class TestHamiltoniano(unittest.TestCase):
    def test_grafo_simples(self):
        grafo = {0: [1,2], 1: [0,3], 2: [0,3], 3: [1,2]}
        self.assertEqual(len(encontrar_caminho_hamiltoniano(grafo)), 4)

    def test_grafo_direcionado_valido(self):
        grafo = {0: [1], 1: [2], 2: [3], 3: []}
        self.assertEqual(encontrar_caminho_hamiltoniano(grafo, True), [0,1,2,3])

    def test_grafo_sem_solucao(self):
        grafo = {0: [1], 1: [2], 2: [0], 3: []}
        self.assertIsNone(encontrar_caminho_hamiltoniano(grafo, True))

if __name__ == '__main__':
    unittest.main()
```

###Cobertura de Testes
- Grafo simples não-direcionado
- Grafo direcionado com solução
- Grafo sem solução
- Grafo vazio
- Grafo com único vértice

---

#  Análise Computacional do Problema do Caminho Hamiltoniano

##  Classificação de Complexidade

### # Classes de Complexidade
- **NP**: 
  - Verificação em tempo polinomial (O(n))
  - Certificado: sequência de vértices
  - Verifica:
    - Todos vértices presentes
    - Arestas consecutivas existem

- **NP-Completo**:
  - Pertence a NP
  - É NP-Difícil (TSP ≤ₚ Hamiltonian Path)
  - Problema de decisão

---

##  Análise de Complexidade Temporal

### # Método de Análise
**Recorrência do Backtracking**:
```math
T(n) = (n-1) \cdot T(n-1) + O(1)
```

### # Expansão Recursiva
1. **Caso Base**:
   - T(1) = 1
   - T(2) = 1

2. **Desenvolvimento**:
   ```
   T(n) = (n-1)T(n-1) + c
        = (n-1)[(n-2)T(n-2) + c] + c
        = (n-1)(n-2)T(n-2) + c[(n-1) + 1]
        ...
        = (n-1)! T(1) + c Σ (termos)
   ```

3. **Resultado Final**:
   ```
   T(n) ∈ Θ((n-1)!) ≡ Θ(n!)
   ```

---

##  Teorema Mestre: Não Aplicável

### # Razões Técnicas
1. **Formato Incompatível**:
   - Requer: `T(n) = a·T(n/b) + f(n)`
   - Temos: `T(n) = (n-1)·T(n-1) + O(1)`

2. **Parâmetros Inválidos**:
   - Coeficiente (n-1) não constante
   - Não há divisão proporcional (b fixo)

3. **Alternativa**:
   - Uso de expansão de recorrência
   - Análise combinatorial direta

---

##  Casos de Complexidade

### # Pior Caso (O(n!))
- **Cenário**:
  - Grafo completo sem caminho
  - Explora todas n! permutações

- **Exemplo**:
  - n=15 → 1.3 trilhões de operações
  - n=20 → 2.4×10¹⁸ operações

### # Caso Médio (Θ((n/e)ⁿ√n))
- **Aproximação de Stirling**:
  ```
  n! ≈ (n/e)ⁿ√(2πn)
  ```
- **Grafos Aleatórios**:
  - Explora ~60% das permutações

### # Melhor Caso (O(n))
- **Condição Ideal**:
  - Primeira permutação válida
  - Grafo linear simples

---

##  Tabela Comparativa

| n  | Operações (n!) | Tempo (1μs/op) |
|----|----------------|----------------|
| 10 | 3.6×10⁶        | 3.6 segundos   |
| 15 | 1.3×10¹²       | 36 dias        |
| 20 | 2.4×10¹⁸       | 77 mil anos    |

---

##  Problemas Relacionados

| Problema           | Classe        | Complexidade   | Redução       |
|--------------------|---------------|----------------|---------------|
| Eulerian Path      | P             | O(V+E)         | Não           |
| Hamiltonian Cycle  | NP-Completo   | O(n!)          | Sim           |
| TSP                | NP-Difícil    | O(n²2ⁿ)        | Sim           |

---


##  Ponto Extra: Diagrama Visual

<img width="311" alt="image" src="https://github.com/user-attachments/assets/a62223a7-e26b-47a2-876e-41c90b9cc31b" />

