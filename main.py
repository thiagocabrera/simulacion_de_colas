import random

class SimuladorDeUnaCola:
    def __init__(self):
        self.tf = 600
        self.tpll = 0
        self.tps = self.high_value()
        self.t = 0
        self.ns = 0
        self.nt = 0
        self.sto = 0
        self.stpll = 0
        self.stps = 0
        self.ito = 0

    def high_value(self):
        return 99999

    def ta(self):
        return random.randint(1,120)

    def ia(self):
        return random.randint(1,120)

    def start(self):
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
        if self.tpll > self.tf:
            if self.ns == 0:
                self.resultados()
            else:
                self.tpll = self.high_value()
                self.start()
        else:
            self.start()

    def resultados(self):
        pps = (self.stps - self.stpll) / self.nt
        pto = self.sto*100/self.t
        print("RESULTADOS: PPS = %d; PTO = %d" % (pps, pto))

SimuladorDeUnaCola().start()