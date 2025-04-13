def encontrar_caminho_hamiltoniano(grafo: dict, direcionado: bool = False) -> list:
    """
    Encontra um caminho Hamiltoniano em um grafo (direcionado ou não)
    
    Args:
        grafo: Dicionário de lista de adjacência {vértice: [vizinhos]}
        direcionado: Se True, considera o grafo como direcionado
        
    Returns:
        Lista com o caminho Hamiltoniano ou None se não existir
    """
    if not grafo:
        return None
        
    vertices = list(grafo.keys())
    n = len(vertices)
    
    def backtrack(caminho_atual: list) -> list:
        if len(caminho_atual) == n:
            return caminho_atual.copy()
            
        ultimo = caminho_atual[-1]
        
        # Verifica vizinhos diretos
        for vizinho in grafo.get(ultimo, []):
            if vizinho not in caminho_atual:
                caminho_atual.append(vizinho)
                if (resultado := backtrack(caminho_atual)):
                    return resultado
                caminho_atual.pop()
                
        # Para grafos não direcionados, verifica conexões inversas
        if not direcionado:
            for v, vizinhos in grafo.items():
                if ultimo in vizinhos and v not in caminho_atual:
                    caminho_atual.append(v)
                    if (resultado := backtrack(caminho_atual)):
                        return resultado
                    caminho_atual.pop()
                    
        return None
    
    # Para grafos direcionados, precisamos verificar todos como iniciais
    for vertice in vertices:
        if (resultado := backtrack([vertice])):
            return resultado
            
    return None