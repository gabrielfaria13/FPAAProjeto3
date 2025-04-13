import networkx as nx
import matplotlib.pyplot as plt
from main import encontrar_caminho_hamiltoniano
import os

def visualizar_grafo(grafo, direcionado=False):
    try:
        # Criar a pasta assets se não existir
        os.makedirs('assets', exist_ok=True)
        
        G = nx.DiGraph() if direcionado else nx.Graph()
        
        # Adicionar nós e arestas
        for vertice, vizinhos in grafo.items():
            G.add_node(vertice)
            for vizinho in vizinhos:
                G.add_edge(vertice, vizinho)
        
        # Encontrar caminho Hamiltoniano
        caminho = encontrar_caminho_hamiltoniano(grafo, direcionado)
        
        # Configurar layout
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 8))
        
        # Desenhar componentes do grafo
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edges(G, pos, width=1.5, edge_color='gray')
        
        # Destacar caminho se existir
        if caminho:
            arestas_caminho = list(zip(caminho[:-1], caminho[1:]))
            nx.draw_networkx_edges(
                G, pos, edgelist=arestas_caminho,
                width=3, edge_color='red', alpha=0.7
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=caminho,
                node_size=800, node_color='salmon'
            )
        
        plt.title("Visualização do Grafo com Caminho Hamiltoniano", pad=20)
        plt.axis('off')
        
        # Salvar e mostrar
        caminho_imagem = os.path.join('assets', 'grafo.png')
        plt.savefig(caminho_imagem, dpi=300, bbox_inches='tight')
        print(f"Imagem salva em: {caminho_imagem}")
        plt.show()
        
    except Exception as e:
        print(f"Erro durante a visualização: {str(e)}")
        print("Verifique se:")
        print("- Todos os módulos estão instalados (networkx, matplotlib)")
        print("- O grafo de entrada é válido")
        print("- A pasta 'assets' existe ou tem permissões de escrita")

# Exemplo de uso
if __name__ == '__main__':
    # Grafo exemplo
    grafo_exemplo = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    
    visualizar_grafo(grafo_exemplo)