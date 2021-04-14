class Boss:
    
    def __init__(self, new_name, hp, power, pos_x, pos_y):
        self.name = new_name
        self.health = hp
        self.attack_power = power
        self.x = pos_x
        self.y = pos_y

    # attacks the player taking the players defense into consideration
    def attack(self, player):
        damage = abs(player.defense - self.attack_power)
        player.health -= damage
    
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

    # returns a list that will act as health bar
    def getHealth(self):
        health_color = (148, 0, 211) #PURPLE/VIOLET
        black = (0, 0, 0)

        health = [health_color if i < self.health else black for i in range(64)]

        return health



