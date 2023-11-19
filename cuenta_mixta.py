from cuenta_ahorro import cuenta_ahorro
from cuenta_corriente import cuenta_corriente


class Cuenta_mixta(cuenta_ahorro, cuenta_corriente):
    def _init_(self, numero, nombrePropietario, saldo, interes, TieneChequera, limite: float = None, bono: float = None):
        cuenta_ahorro._init_(self, numero, nombrePropietario, saldo, interes)
        cuenta_corriente._init_(self, numero, nombrePropietario, saldo, TieneChequera)
        self._limite = limite
        self._bono = bono

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, nuevo_limite):
        self._limite = nuevo_limite

    @property
    def bono(self):
        return self._limite

    @bono.setter
    def bono(self, nuevo_bono):
        self._bono = nuevo_bono

    def fijar_limite(self, limite):
        self.limite = 10000

    def fijar_bono(self, bono):
        self.bono = 5000

    def credito(self, cantidad):
        if self.saldo <= self.limite:
            self.saldo += cantidad
        else:
            print("El saldo de la cuenta a llegado a su tope")

    def bono(self, bono):
        if self.saldo <= self.limite:
            self.saldo += bono
        else:
            print("El saldo de la cuenta a llegado a su tope")

if  "name"=="main_":
    cuenta_pru = cuenta_corriente("85736", "daniela", 2354.00, True)
    print(cuenta_pru)
    cuenta_pru.mostrar_saldo()
    cuenta_pru.credito(800.00)
    cuenta_pru.mostrar_saldo()
    cuenta_pru.debito(356.00)
    cuenta_pru.mostrar_saldo()
    cuenta_pru.pagar_cheque(680.00)
    cuenta_pru.mostrar_saldo()
