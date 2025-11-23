class GameLogger:
    _instance = None

    def __new__(cls):
        
        if cls._instance is None:
            cls._instance = super(GameLogger, cls).__new__(cls)
            cls._instance.history = []
        return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")
        self.history.append(message)

    def show_history(self):
        print("\n--- Histórico Completo ---")
        for event in self.history:
            print(event)

logger1 = GameLogger()
logger1.log("Jogo começou.")

logger2 = GameLogger()
logger2.log("O herói entrou na caverna.")

print(f"\nLogger1 é igual ao Logger2? {logger1 is logger2}") 
logger1.show_history()

class Weapon:
    def __init__(self, name, damage, element):
        self.name = name
        self.damage = damage
        self.element = element

    def __str__(self):
        return f"[{self.name}] Dano: {self.damage} | Elemento: {self.element}"

class WeaponBuilder:
    def __init__(self):
        self._name = "Arma Básica"
        self._damage = 1
        self._element = "Normal"

    def set_name(self, name):
        self._name = name
        return self

    def set_damage(self, damage):
        self._damage = damage
        return self

    def set_element(self, element):
        self._element = element
        return self

    def build(self):
        return Weapon(self._name, self._damage, self._element)

faca = WeaponBuilder().set_name("Faca de Cozinha").build()
print(faca)

martelo_do_trovao = (WeaponBuilder()
                     .set_name("Mjolnir")
                     .set_damage(999)
                     .set_element("Raio")
                     .build())

print(martelo_do_trovao)