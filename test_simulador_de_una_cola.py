from mock_simulador_de_una_cola import MockSimuladorDeUnaCola

simulation = MockSimuladorDeUnaCola(
    ptlls = [10,5,60,15,30,35,10,20,15],
    ptss = [40,5,15,10,30,45,15,20,10],
    tf = 150)
simulation.start()
if ("%.2f" % simulation.pps) == "32.86" and ("%.2f" % simulation.pto) == "11.11":
    print("Test superado!")
else:
    print(simulation.pps, simulation.pto)