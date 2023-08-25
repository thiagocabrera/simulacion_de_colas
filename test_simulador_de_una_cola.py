from mock_simulador_de_una_cola import MockSimuladorDeUnaCola
import unittest

class TestModels(unittest.TestCase):

    def test_upper(self):
        simulation = MockSimuladorDeUnaCola(
        ptlls = [10,5,60,15,30,35,10,20,15],
        ptss = [40,5,15,10,30,45,15,20,10],
        tf = 150)
        simulation.start()
        self.assertEqual(("%.2f" % simulation.pps), "32.86", "Falló el calculo del PPS!")
        self.assertEqual(("%.2f" % simulation.pto), "11.11", "Falló el cálculo del PTO!")

if __name__ == '__main__':
    unittest.main()