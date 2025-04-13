import unittest
from main import encontrar_caminho_hamiltoniano

class TestHamiltoniano(unittest.TestCase):
    def test_grafo_simples(self):
        grafo = {0: [1,2], 1: [0,3], 2: [0,3], 3: [1,2]}
        self.assertEqual(len(encontrar_caminho_hamiltoniano(grafo)), 4)

    def test_grafo_direcionado_valido(self):
        grafo = {0: [1], 1: [2], 2: [3], 3: []}
        self.assertEqual(encontrar_caminho_hamiltoniano(grafo, True), [0,1,2,3])

    def test_grafo_direcionado_invalido(self):
        grafo = {0: [1], 1: [2], 2: [0], 3: []}  # 3 é inalcançável
        self.assertIsNone(encontrar_caminho_hamiltoniano(grafo, True))

    def test_grafo_vazio(self):
        self.assertIsNone(encontrar_caminho_hamiltoniano({}))

    def test_grafo_unitario(self):
        self.assertEqual(encontrar_caminho_hamiltoniano({0: []}), [0])

    def test_grafo_desconexo(self):
        grafo = {0: [1], 1: [0], 2: [3], 3: [2]}
        self.assertIsNone(encontrar_caminho_hamiltoniano(grafo))

if __name__ == '__main__':
    unittest.main()