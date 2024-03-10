import unittest
from szukanie_cyklu import force_method, multiplication_method

class TestSzukanieCyklu(unittest.TestCase):
    def test_force_method(self):
        matrix = [[0, 1, 0],[1, 0, 1],[0, 1, 0]]
        matrix1 = [[0, 1, 0],[1, 0, 1],[1, 1, 0]]
        self.assertEqual(force_method(matrix), None)
        self.assertEqual(force_method(matrix1), [1, 2, 0])

    def test_multiplication_method(self):
        matrix = [[0, 1, 0],[1, 0, 1],[0, 1, 0]]
        matrix1 = [[0, 1, 0],[1, 0, 1],[1, 1, 0]]
        self.assertEqual(multiplication_method(matrix), False)
        self.assertEqual(multiplication_method(matrix1), True)

# class TestVertexCover(unittest.TestCase):
    # def test_vertex_cover(self):
        # graph = {(0, 1), (1, 2), (2, 0)}
        # cover = vertex_cover(graph)
        # self.assertEqual(len(cover), 2)
        # self.assertTrue(cover.issubset({0, 1, 2}))
    # def test_vertex_cover_presentation(self):
    #     graph = {(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5)}
    #     cover = vertex_cover(graph)
    #     print(cover)

if __name__ == '__main__':
    unittest.main()