class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # Getter
    @property
    def nome(self):
        return self.__nome.title()

    # Setter
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.strip().title()


clienteLucas: Cliente = Cliente("Lucas")
clienteJhen: Cliente = Cliente("jhennifer")
clienteJhen.nome = "  shay shay  "
clienteLucas.nome = "  lusga"

print(f"Os nomes são: {clienteJhen.nome} e {clienteLucas.nome}")
