from simulador_de_una_cola import SimuladorDeUnaCola

class MockSimuladorDeUnaCola(SimuladorDeUnaCola):
    def __init__(self, ptlls, ptss, tf):
        self.ptll_list = ptlls.copy()
        self.ptls_list = ptss.copy()
        super().__init__(tf)
    
    def ta(self):
        return self.ptls_list.pop(0)
    
    def ia(self):
        return self.ptll_list.pop(0)