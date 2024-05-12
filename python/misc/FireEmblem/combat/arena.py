'''
This would be best as a C or C++ program
'''
import pandas as pd
import random

# truehit_df = pd.read_csv('truehit.csv')

def GetHitRoll() -> int:
    return 0.5 * (random.randint(0,99) + random.randint(0,99))

def GetCritRoll() -> int:
    return random.randint(0,99)

def CombatRound(PlayerUnit: list, EnemyUnit: list, which_round: int) -> None:
    '''
    Unit: [HP, Hit, Dam, Crit, DblAtk]
    '''
    print(f"Round {which_round} begins")

    # PlayerUnit First Attack
    print("Player unit attacks")
    hit_roll = GetHitRoll()
    if hit_roll < PlayerUnit[1]: # Player unit hits
        crit_roll = GetCritRoll()
        if crit_roll < PlayerUnit[3]: # Player unit crits
            print("Player unit crits!")
            EnemyUnit[0] -= 3.0 * PlayerUnit[2]
        else: 
            print("Player unit hits")
            EnemyUnit[0] -= PlayerUnit[2]
        if EnemyUnit[0] <= 0: 
            print("Enemy unit killed")
            return
    else: 
        print("Player unit misses")
    
    # EnemyUnit First Attack
    print("Enemy unit attacks")
    hit_roll = GetHitRoll()
    if hit_roll < EnemyUnit[1]: # Player unit hits
        crit_roll = GetCritRoll()
        if crit_roll < EnemyUnit[3]: # Player unit crits
            print("Enemy unit crits!")
            PlayerUnit[0] -= 3.0 * EnemyUnit[2]
        else: 
            print("Enemy unit hits")
            PlayerUnit[0] -= EnemyUnit[2]
        if PlayerUnit[0] <= 0: 
            print("Player unit killed")
            return
    else: 
        print("Enemy unit misses")

    # PlayerUnit Possible Second Attack
    if PlayerUnit[4]: # Player unit doubles enemy unit
        print("Player unit doubles")
        hit_roll = GetHitRoll()
        if hit_roll < PlayerUnit[1]: # Player unit hits
            crit_roll = GetCritRoll()
            if crit_roll < PlayerUnit[3]: # Player unit crits
                print("Player unit crits!")
                EnemyUnit[0] -= 3.0 * PlayerUnit[2]
            else: 
                print("Player unit hits")
                EnemyUnit[0] -= PlayerUnit[2]
            if EnemyUnit[0] <= 0: 
                print("Enemy unit killed")
                return
        else: 
            print("Player unit misses")

    # EnemyUnit Possible Second Attack
    if EnemyUnit[4]:
        print("Enemy unit doubles")
        hit_roll = GetHitRoll()
        if hit_roll < EnemyUnit[1]: # Player unit hits
            crit_roll = GetCritRoll()
            if crit_roll < EnemyUnit[3]: # Player unit crits
                print("Enemy unit crits!")
                PlayerUnit[0] -= 3.0 * EnemyUnit[2]
            else: 
                print("Enemy unit hits")
                PlayerUnit[0] -= EnemyUnit[2]
            if PlayerUnit[0] <= 0: 
                print("Player unit killed")
                return
        else: 
            print("Enemy unit misses")
        
    print(f"Round {which_round} is over\n")
    return

def parseCombatants():
    PlayerUnit = [''] * 5
    EnemyUnit = [''] * 5

    with open('combatants.txt', 'r') as cfile:
        lines = [line.rstrip() for line in cfile]
        print(lines)

        # I know this can be refactored to not eval conditional every time
        for i in range(len(PlayerUnit)):
            if i == len(PlayerUnit) - 1:
                if lines[i+1].split('=')[1] == 'True':
                    PlayerUnit[i] = True
                else: 
                    PlayerUnit[i] = False
                if lines[i+8].split('=')[1] == 'True':
                    EnemyUnit[i] = True
                else:
                    EnemyUnit[i] = False
            else:
                PlayerUnit[i] = int(lines[i+1].split('=')[1])
                EnemyUnit[i] = int(lines[i+8].split('=')[1])
    
    PlayerHP = int(lines[1].split('=')[1])
    EnemyHP = int(lines[8].split('=')[1])

    print(f"PlayerUnit: {PlayerUnit}")
    print(f"EnemyUnit: {EnemyUnit}")

    return PlayerUnit, EnemyUnit, PlayerHP, EnemyHP

# Main loop
print("Begining simulation")
print("Parsing combatants")
PlayerUnit, EnemyUnit, PlayerHP, EnemyHP = parseCombatants()
print("Combatants parsed\n")

num_fights = 1000
count = 0
player_wins = 0

while count < num_fights:
    print(f"Fight {count+1} begins!\n")

    num_round = 0
    while PlayerUnit[0] > 0 and EnemyUnit[0] > 0:
        CombatRound(PlayerUnit, EnemyUnit, num_round)
        num_round += 1
    
    print(f"Fight {count+1} is over! PlayerUnit HP: {PlayerUnit[0]}, EnemyUnit HP: {EnemyUnit[0]}")
    
    if PlayerUnit[0] > 0:
        print("Player unit wins!\n")
        player_wins += 1
    elif EnemyUnit[0] > 0:
        print("Enemy unit wins\n")
    count += 1

    # Refill HP
    PlayerUnit[0] = PlayerHP
    EnemyUnit[0] = EnemyHP

win_chance = player_wins / num_fights
print(f"Simulation done: PlayerUnit wins {win_chance * 100} percent of the time")