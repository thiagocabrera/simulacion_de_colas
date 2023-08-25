import random

class SimuladorPruebaDeEscritorio:
    def __init__(self, tf):
        self.tf = tf
        self.tpll = 0
        self.tps = self.high_value()
        self.t = 0
        self.ns = 0
        self.nt = 0
        self.sto = 0
        self.stpll = 0
        self.stps = 0
        self.ito = 0
        self.pto = None
        self.pps = None
        self.ta = random.randint
        self.ia = random.randint

    def high_value(self):
        return 99999

    def simular(self):
        if self.tpll <= self.tps:
            self.llegada()
        else:
            self.salida()
    
    def salida(self):
        self.t = self.tps
        self.stps += self.t
        self.ns -= 1
        if self.ns > 0:
            self.tps = self.t + self.ta()
        else:
            self.tps = self.high_value()
            self.ito = self.t
        self.final()

    def llegada(self):
        self.t = self.tpll
        self.stpll += self.t
        self.tpll = self.t + self.ia()
        self.ns += 1
        self.nt += 1
        if self.ns == 1:
            self.sto += (self.t - self.ito)
            self.tps = self.t + self.ta()
        self.final()

    def final(self):
        if self.t < self.tf:
            self.start()
        else:
            if self.ns == 0:
                self.resultados()
            else:
                self.tpll = self.high_value()
                self.start()


    def resultados(self):
        self.pps = (self.stps - self.stpll) / self.nt
        self.pto = self.sto*100/self.t