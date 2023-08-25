from simulador_prueba_de_escritorio import SimuladorPruebaDeEscritorio
import unittest

class TestModels(unittest.TestCase):

    def test_prueba_de_escritorio(self):
        simulation = SimuladorPruebaDeEscritorio(tf = 150)
        ptlls = [10,5,60,15,30,35,10,20,15]
        ptss = [40,5,15,10,30,45,15,20,10]
        def ta_gen():
            return ptss.pop(0)
        def ia_gen():
            return ptlls.pop(0)
        simulation.ta = ta_gen
        simulation.ia = ia_gen
        simulation.simular()
        self.assertEqual(("%.2f" % simulation.pps), "32.86", "Falló el calculo del PPS!")
        self.assertEqual(("%.2f" % simulation.pto), "11.11", "Falló el cálculo del PTO!")

if __name__ == '__main__':
    unittest.main()