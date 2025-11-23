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