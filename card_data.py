class Card:
    def __init__(self, name, pas, shot, fin, speed, defense, endurance):
        self.name = name
        self.pas = pas
        self.shot = shot
        self.fin = fin
        self.speed = speed
        self.defense = defense
        self.endurance = endurance

    def __str__(self):
        return (f"{self.name}: PASS={self.pas}, SHOT={self.shot}, FIN={self.fin}, "
                f"SPEED={self.speed}, DEF={self.defense}, END={self.endurance}")

    def to_dict(self):
        return {
            'name': self.name,
            'pas': self.pas,
            'shot': self.shot,
            'fin': self.fin,
            'speed': self.speed,
            'defense': self.defense,
            'endurance': self.endurance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['pas'],
            data['shot'],
            data['fin'],
            data['speed'],
            data['defense'],
            data['endurance']
        )

cards = [
    Card("Myth",      60, 70, 80, 65, 50, 45),
    Card("Satellite", 70, 60, 65, 70, 55, 50),
    Card("Swift",     45, 45, 50, 85, 35, 30),
    Card("Titan",     35, 45, 40, 40, 95, 100),
    Card("Nucleus",   60, 60, 60, 60, 75, 70),
    Card("Cobra",     50, 75, 75, 80, 30, 45),
    Card("Mustang",   45, 40, 50, 60, 80, 75),
    Card("Glide",     50, 45, 50, 75, 70, 55),
    Card("Shadow",    30, 30, 35, 50, 95, 100),
    Card("Sprint",    65, 75, 80, 90, 35, 30),
    Card("Blade",     55, 60, 65, 65, 45, 50),
    Card("Jet",       55, 60, 65, 70, 40, 45),
    Card("Needle",    40, 45, 50, 60, 85, 70),
    Card("Hive",      30, 35, 40, 45, 100, 100),
    Card("Highlander",85, 85, 90, 70, 35, 25),
    Card("Invincible",55, 60, 65, 60, 85, 60),
    Card("Damage",    50, 60, 65, 60, 85, 55),
    Card("Stopper",   45, 50, 55, 55, 95, 65),
    Card("Blocker",   40, 30, 40, 40, 100, 95),
    Card("Shield",    40, 30, 40, 45, 100, 90),
    Card("Flint",     55, 60, 65, 65, 45, 45),
    Card("Sparks",    55, 60, 65, 65, 45, 45),
    Card("Bomber",    50, 55, 60, 55, 80, 55),
    Card("Wizard",    40, 40, 40, 45, 85, 100),
]
