class Pokemon:
    def __init__(self, n, v, a):
        self.nombre = n
        self.vida = v
        self.ataque = a
        self.estado = 'vivo'
    
    def atacar(self):
        return self.ataque

    def recibe_daño(self, d):
        self.vida -= d

    def actualiza_estado(self):
        if vida > 0:
            self.estado = 'Vivo'
        else:
            self.estado = 'Muerto'

if __name__ == "__main__":

    print("Configura el primer Pokemón")
    p1_nombre = input("Nombre del Pokemón: ")
    p1_vida = int(input("Vida del Pokemón: "))
    p1_ataque = int(input("Ataque del Pokemón: "))
    print("")
    print("Configura el segundo Pokemón")
    p2_nombre = input("Nombre del Pokemón: ")
    p2_vida = int(input("Vida del Pokemón: "))
    p2_ataque = int(input("Ataque del Pokemón: "))

    p1 = Pokemon(p1_nombre, p1_vida, p1_ataque)
    p2 = Pokemon(p2_nombre, p2_vida, p2_ataque)

    print("")
    print(f"{p1.nombre}, tiene de vida {p1.vida} y hace un ataque de {p1.ataque}")
    print(f"{p2.nombre}, tiene de vida {p2.vida} y hace un ataque de {p2.ataque}")