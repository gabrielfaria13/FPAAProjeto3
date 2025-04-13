import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # Configura o backend
import matplotlib.pyplot as plt
import os
from main import encontrar_caminho_hamiltoniano

def visualizar_grafo(grafo, direcionado=False):
    """Gera visualização do grafo com caminho Hamiltoniano destacado"""
    try:
        os.makedirs('assets', exist_ok=True)
        
        G = nx.DiGraph() if direcionado else nx.Graph()
        
        # Adiciona nós e arestas
        for vertice, vizinhos in grafo.items():
            G.add_node(vertice, label=str(vertice))
            for vizinho in vizinhos:
                G.add_edge(vertice, vizinho)
        
        caminho = encontrar_caminho_hamiltoniano(grafo, direcionado)
        pos = nx.spring_layout(G, seed=42)  # Seed para layout consistente
        
        plt.figure(figsize=(12, 8))
        
        # Desenha o grafo completo
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, alpha=0.5)
        
        # Destaca o caminho se existir
        if caminho:
            arestas = list(zip(caminho[:-1], caminho[1:]))
            nx.draw_networkx_edges(
                G, pos, edgelist=arestas,
                edge_color='red', width=3, alpha=0.8
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=caminho,
                node_color='salmon', node_size=800
            )
            plt.title(f"Caminho Hamiltoniano: {' → '.join(map(str, caminho))}", pad=20)
        else:
            plt.title("Nenhum Caminho Hamiltoniano Encontrado", pad=20)
        
        plt.axis('off')
        caminho_imagem = os.path.join('assets', 'grafo.png')
        plt.savefig(caminho_imagem, dpi=120, bbox_inches='tight')
        plt.close()
        return caminho_imagem
        
    except Exception as e:
        print(f"Erro na visualização: {e}")
        return None

if __name__ == '__main__':
    # Exemplo de uso
    grafo_teste = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 3],
        3: [1, 2, 4],
        4: [1, 3]
    }
    
    imagem_salva = visualizar_grafo(grafo_teste)
    
    if imagem_salva:
        print(f"Imagem gerada com sucesso em: {imagem_salva}")
        # Mostra a imagem na tela
        img = plt.imread(imagem_salva)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    else:
        print("Falha ao gerar visualização")