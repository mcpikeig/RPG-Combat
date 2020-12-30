import os
from random import randint
import time
#Initialize the Player Value
class Player:
        def __init__(self,name,hp,armor,strength,intelligence,agility,act1,act2,act3):
                self.name=name
                self.hp=hp
                self.armor=armor
                self.strength=strength
                self.intelligence=intelligence
                self.agility=agility
                self.act1=act1
                self.act2=act2
                self.act3=act3

class Enemy:
        def __init__(self,name,hp,armor,strength,intelligence,agility,act1,act2,act3):
                self.name=name
                self.hp=hp
                self.armor=armor
                self.strength=strength
                self.intelligence=intelligence
                self.agility=agility
                self.act1=act1
                self.act2=act2
                self.act3=act3

#The following classes define the base stats for each of the 3 professions
class Fighter(Player):
        def __init__(self):
                super().__init__(
                        name="Fighter",
                        hp=30,
                        armor=3,
                        strength=8,
                        intelligence=3,
                        agility=5,
                        act1="Attack",
                        act2="Defend",
                        act3="War Cry"
                        )


class Rogue(Player):
        def __init__(self):
                super().__init__(
                        name="Rogue",
                        hp=20,
                        armor=2,
                        strength=5,
                        intelligence=3,
                        agility=8,
                        act1="Attack",
                        act2="Flash Bang",
                        act3="Poison"
                        )

class Mage(Player):
        def __init__(self):
                super().__init__(
                        name="Mage",
                        hp=25,
                        armor=1,
                        strength=3,
                        intelligence=8,
                        agility=5,
                        act1="Magic",
                        act2="Shield",
                        act3="Enfeeble"
                        )

#The following classes define the base stats for the enemies
class Slime(Enemy):
        def __init__(self):
                super().__init__(
                        name='Slime',
                        hp=13,
                        armor=5,
                        strength=4,
                        intelligence=5,
                        agility=5,
                        act1="Attack",
                        act2="Heal",
                        act3="Wait"
                        )

class Wolf(Enemy):
        def __init__(self):
                super().__init__(
                        name='Wolf',
                        hp=9,
                        armor=2,
                        strength=6,
                        intelligence=3,
                        agility=10,
                        act1="Claw",
                        act2="Howl",
                        act3="Lick Wounds"
                        )

#Choose your Class!
def profession():
        letter_to_profession = {
                'f': Fighter,
                'r': Rogue,
                'm': Mage
                }
        print("What is your class?\n")
        for letter in letter_to_profession.keys():
                print("- Press {} for {}".format(
                        letter, letter_to_profession[letter].__name__))
        pclass = input(">>>")
        global PlayerStats 
        PlayerStats=letter_to_profession[pclass]()
        os.system('cls')
        print("Player is a {}.".format(
                PlayerStats.name))
        return letter_to_profession[pclass]()

#Choose your Enemy
def monster():
        letter_to_enemy = {
            's': Slime,
            'w': Wolf
        }
        print("What would you like to fight?\n")
        for letter in letter_to_enemy.keys():
                print("- Press {} for {}".format(
                        letter, letter_to_enemy[letter].__name__))
        enemy = input(">>>")
        global EnemyStats
        EnemyStats = letter_to_enemy[enemy]()
        os.system('cls')
        return letter_to_enemy[enemy]()

def fight(): 
        while EnemyStats.hp > 0:
                playerTurn()
                monsterTurn()
                print("{} HP: {} VS {} HP: {}\n".format(
                PlayerStats.name,PlayerStats.hp,EnemyStats.name,EnemyStats.hp))
                if PlayerStats.hp <= 0:
                        break
        if PlayerStats.hp <= 0:
                print("{} is dead!".format(
                        PlayerStats.name))        
        else:
                print("{} is dead!".format(
                        EnemyStats.name))
        

def playerTurn():
        commands()
        hit = toHit()
        if hit == True:
                onHit()

def commands():
        commands = {}
        commands['act1'] = PlayerStats.act1
        commands['act2'] = PlayerStats.act2
        commands['act3'] = PlayerStats.act3
        for x in commands:
            print(commands.setdefault(x))
        print("What will you do?")
        global turnCommand
        turnCommand = input('>>>')
        os.system('cls')
        return turnCommand

def toHit():
    if PlayerStats.agility >= EnemyStats.agility:
        print("Hit!")
        return True
    else:
        print("Miss!")
        return False

def onHit():
    EnemyStats.hp = EnemyStats.hp - PlayerStats.strength

def monsterTurn():
    monsterActions = {}
    monsterActions[1] = EnemyStats.act1
    monsterActions[2] = EnemyStats.act2
    monsterActions[3] = EnemyStats.act3
    action = randint(1,3)
    print("{} decides to:".format(EnemyStats.name))
    time.sleep(2)
    print(monsterActions[action])
    time.sleep(1)
    monsterAction()

def monsterAction():
        print("Hit!")
        PlayerStats.hp = PlayerStats.hp - EnemyStats.strength

def retry():
        print("Play again? Y or N")
        retryinput = input(">>>")
        if retryinput == "Y":
                main()
        else:
                exit()



#Main Game Function; Choose a profession and it shows your stats
def main():
        profession()
        print("HP: {}\nArmor: {}\nStrength: {}\nIntelligence: {}\nAgility: {}".format(
                PlayerStats.hp,PlayerStats.armor,PlayerStats.strength,PlayerStats.intelligence,PlayerStats.agility))
        monster()
        print("You're Fighting:\n{}\nHP: {}".format(
                EnemyStats.name,EnemyStats.hp))
        time.sleep(2)
        fight()

main()
retry()
