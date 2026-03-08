# gestor_stock.py

class GestorStock:
    """Classe que representa um gestor de carteira de uma ação específica."""

    def __init__(self, simbolo: str, nome: str, preco_atual=0.0, quantidade=0):
        self.simbolo = simbolo
        self.nome = nome
        self.preco_atual = preco_atual
        self._quantidade = max(0, int(quantidade))
        self._preco_medio_compra = self._preco_atual if self._quantidade > 0 else 0.0
        self._lucro_realizado = 0.0

    @property
    def simbolo(self) -> str:
        return self._simbolo

    @simbolo.setter
    def simbolo(self, valor: str):
        self._simbolo = valor.strip().upper()

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor.strip().title()

    @property
    def preco_atual(self) -> float:
        return self._preco_atual

    @preco_atual.setter
    def preco_atual(self, valor: float):
        self._preco_atual = float(valor) if valor > 0 else 0.0

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
        self._quantidade = int(valor) if valor >= 0 else 0

    @property
    def preco_medio_compra(self) -> float:
        pass

    @preco_medio_compra.setter
    def preco_medio_compra(self, valor: float):
        pass

    @property
    def lucro_realizado(self) -> float:
        pass

    @lucro_realizado.setter
    def lucro_realizado(self, valor: float):
        pass

    def comprar(self, quantidade: int, preco: float) -> bool:
        pass

    def vender(self, quantidade: int, preco: float) -> bool:
        pass

    def valor_total(self) -> float:
        pass

    def lucro_potencial(self) -> float:
        pass

    def receber_dividendo(self, dividendo_por_acao: float) -> float:
        pass