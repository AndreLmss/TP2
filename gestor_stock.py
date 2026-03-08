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
        return self._preco_medio_compra

    @preco_medio_compra.setter
    def preco_medio_compra(self, valor: float):
        self._preco_medio_compra = float(valor)

    @property
    def lucro_realizado(self) -> float:
        return self._lucro_realizado

    @lucro_realizado.setter
    def lucro_realizado(self, valor: float):
        self._lucro_realizado = float(valor)

    def comprar(self, quantidade: int, preco: float) -> bool:
        if quantidade <= 0 or preco <= 0:
            return False
        total_atual = self._quantidade * self._preco_medio_compra
        total_novo = quantidade * preco
        nova_quantidade = self._quantidade + quantidade
        self._preco_medio_compra = (total_atual + total_novo) / nova_quantidade
        self._quantidade = nova_quantidade
        self.preco_atual = preco
        return True

    def vender(self, quantidade: int, preco: float) -> bool:
        if quantidade <= 0 or preco <= 0:
            return False
        if quantidade > self._quantidade:
            return False
        margem = (preco - self._preco_medio_compra) * quantidade
        self._lucro_realizado += margem
        self._quantidade -= quantidade
        self.preco_atual = preco
        return True

    def valor_total(self) -> float:
        return self._quantidade * self._preco_atual

    def lucro_potencial(self) -> float:
        return (self._preco_atual - self._preco_medio_compra) * self._quantidade

    def receber_dividendo(self, dividendo_por_acao: float) -> float:
        if dividendo_por_acao <= 0:
            return 0.0
        total = dividendo_por_acao * self._quantidade
        self._lucro_realizado += total
        return total