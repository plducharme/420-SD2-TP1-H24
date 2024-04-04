import math
import unittest
from polygone import Triangle, HexagoneRegulier, Vecteur, Point


class TestPolygone(unittest.TestCase):

    @staticmethod
    def setup_triangle() -> Triangle:
        triangle = Triangle()
        v1 = Vecteur(Point(-1, -1), Point(-1, 1))
        v2 = Vecteur(Point(-1, 1), Point(2, -1))
        v3 = Vecteur(Point(2, -1), Point(-1, -1))
        triangle.liste_vecteurs = [v1, v2, v3]
        return triangle


    @staticmethod
    def setup_heaxagone_regulier():
        hexagone = HexagoneRegulier()
        a = 6
        v1 = Vecteur(Point(a, 0), Point(a/2, math.sqrt(3)*a/2))
        v2 = Vecteur(Point(a/2, math.sqrt(3)*a/2), Point(-a/2, math.sqrt(3)*a/2))
        v3 = Vecteur(Point(-a/2, math.sqrt(3)*a/2), Point(-a, 0))
        v4 = Vecteur(Point(-a, 0), Point(-a/2, -math.sqrt(3)*a/2))
        v5 = Vecteur(Point(-a/2, -math.sqrt(3)*a/2), Point(a/2, -math.sqrt(3)*a/2))
        v6 = Vecteur(Point(a/2, -math.sqrt(3)*a/2), Point(a, 0))
        hexagone.liste_vecteurs = [v1, v2, v3, v4, v5, v6]
        return hexagone

    def test_polygone_perimetre(self):
        hexagone = TestPolygone.setup_heaxagone_regulier()
        self.assertEqual(hexagone.perimetre(), 6*6)

    def test_vecteur_longueur(self):
        vecteur = Vecteur(Point(-5, -5), Point(5, 5))
        self.assertEqual(vecteur.longueur(), math.sqrt(10**2 + 10**2))

    def test_polygone_nb_cotes(self):
        hexagone = TestPolygone.setup_heaxagone_regulier()
        self.assertEqual(hexagone.nb_cotes(), 6)

    def test_point_valeur_negative_invalide(self):

        with self.assertRaises(ValueError):
            p = Point(-20, 0)
        with self.assertRaises(ValueError):
            p = Point(0, -20)

    def test_point_valeur_positive_invalide(self):
        with self.assertRaises(ValueError):
            p = Point(20, 0)
        with self.assertRaises(ValueError):
            p = Point(0, 20)


    def test_triangle_aire(self):
        triangle = TestPolygone.setup_triangle()
        self.assertEqual(format(triangle.aire(), ".4f"), format(2*3/2, ".4f"))

    def test_hexagone_regulier_aire(self):
        hexagone = TestPolygone.setup_heaxagone_regulier()
        self.assertEqual(format(hexagone.aire(), ".4f"), format(3*math.sqrt(3)/2*6**2, ".4f"))


if __name__ == '__main__':
    unittest.main()

