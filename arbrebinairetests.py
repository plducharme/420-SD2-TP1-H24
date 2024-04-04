import unittest
import csv

from arbrebinaire import Noeud, DataUtils, EquipeLNH


class TestArbreBinaire(unittest.TestCase):

    def setUp(self):
        self.racine = None
        self.liste_equipes: list[EquipeLNH] = TestArbreBinaire.load_data_test()
        for equipe in self.liste_equipes:
            if self.racine is None:
                self.racine = Noeud(equipe)
            else:
                self.racine.insertion(equipe)

    def test_total_points(self):
        for equipe in self.liste_equipes:
            self.assertEqual(equipe.total_points(), int(equipe.data["PTS"]))

    def test_moyenne_but_par_match(self):
        for equipe in self.liste_equipes:
            self.assertEqual(round(equipe.moyenne_but_par_match(), 2), round(float(equipe.data["MBM"]), 2))

    def test_moyenne_bas_haut(self):
        bas, haut = DataUtils.moyenne_haut_bas(self.liste_equipes)
        total_moyenne = 0
        for equipe in self.liste_equipes:
            total_moyenne += float(equipe.data["MBM"])

        moyenne = total_moyenne / len(self.liste_equipes)

        for equipe in self.liste_equipes:
            if float(equipe.data["MBM"]) < moyenne:
                self.assertIn(equipe, bas)
            else:
                self.assertIn(equipe, haut)

    def test_arbre_binaire(self):
        liste_triee = []
        TestArbreBinaire.tri_arbre(self.racine, liste_triee)
        self.assertEqual(liste_triee, sorted(self.liste_equipes,key=lambda x: int(x.data["PTS"])))

    @staticmethod
    def tri_arbre(racine, liste):
        if racine.gauche:
            TestArbreBinaire.tri_arbre(racine.gauche, liste)
        liste.append(racine._equipe)
        if racine.droite:
            TestArbreBinaire.tri_arbre(racine.droite, liste)


    @staticmethod
    def load_data_test():
        liste_equipes = []
        with open("./data/nhl.csv", 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            lignes = 0
            for ligne in reader:
                if lignes == 0:
                    # Ignorer l'entete
                    lignes += 1
                else:
                    equipe = EquipeLNH(ligne[0], {'MJ': ligne[2], 'V': ligne[3], 'DP': ligne[6], 'BP': ligne[12],
                                                  'PTS': ligne[7], 'MBM': ligne[14]})
                    liste_equipes.append(equipe)
                    lignes += 1
            return liste_equipes


if __name__ == '__main__':
    unittest.main()
