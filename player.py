class Player:

    def __init__(self):
        self.max_health = 15
        self.health = self.max_health
        self.attack_power = 2
        self.defense = 1
        self.health_potion_ammount = 3
        self.health_potion_power = 5
        self.x = 0
        self.y = 0

    # increases the players stats
    def level_up(self):
        self.max_health += 15
        self.health = self.max_health
        self.attack_power += 3
        self.defense += 1
        self.health_potion_ammount += 2
        self.health_potion_power += 4

    def attack(self, boss):
        boss.health -= self.attack_power

    def drink_potion(self):
        
        if self.health_potion_ammount > 0:
            self.health_potion_ammount -= 1

            missing_health = self.max_health - self.health
            recovered_health = self.health_potion_power

            # makes sure that the players health doesn't go above his max health
            if self.health + self.health_potion_power > self.max_health:
                self.health += missing_health
                recovered_health = missing_health
            else:
                self.health += self.health_potion_power

            print("You recovered ", recovered_health, " HP.")
            print(self.health_potion_ammount, " health potions remaining.")
        else:
            print("You ran out of healing potions.")
    
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

    # returns a list that will act as health bar
    def getHealth(self):
        health_color = (255, 0, 0) # RED
        black = (0, 0, 0)

        health = [health_color if i < self.health else black for i in range(64)]

        return health
    
     # player chooses what to do on the terminal
    def playerTurn(self):
        print("[1] Attack \n[2] Heal")
        option = int(input("What will you do?"))

        return option


