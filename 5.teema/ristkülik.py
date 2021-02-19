class Ristkülik:
    def __init__(self,laius, korgus, symbol):
        self.laius = int(laius)
        self.korgus = int(korgus)
        self.symbol = str(symbol)
    def __str__(self):
        ristkylik = [] # nimekiri symbolite kordamiseks
        for i in range(self.korgus):
            symbolid = self.symbol * self.laius
            read.append(symbolid)
        ristkylik_tekstina =  '\n'.join(read)
        return ristkylik_tekstina
    def __add__(self, teine_ristkülik):
        uus_laius = self.laius + teine_ristkülik.laius
        uus_korgus = self.korgus + teine_ristkülik.korgus
        uus_symbol = self.symbol
        return Riskülik(uus_laius, uus_korgus, uus_symbol)
