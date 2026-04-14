import random

def player_attack():
    base = random.randint(15, 30)
    
    # Critical hit chance
    if random.random() < 0.2:
        print("💥 CRITICAL HIT!")
        return base * 2
    return base

def dragon_attack(phase):
    if phase == 1:
        return random.randint(10, 25)
    else:
        # Phase 2 stronger
        dmg = random.randint(20, 40)
        
        # Fire breath chance
        if random.random() < 0.3:
            print("🔥 DRAGON USES FIRE BREATH!")
            dmg += 20
        
        return dmg


def play_game():
    player_hp = 100
    potions = 3
    dragon_hp = 150
    
    phase = 1
    
    print("\n⚔️ BATTLE STARTS! You vs Dragon 🐉\n")
    
    while player_hp > 0 and dragon_hp > 0:
        
        # Phase change
        if dragon_hp <= 75 and phase == 1:
            phase = 2
            print("\n🐉 THE DRAGON ENTERS PHASE 2! IT GETS ANGRY 🔥\n")
        
        print(f"❤️ HP: {player_hp} | 🐉 Dragon: {dragon_hp} | 🧪 Potions: {potions}")
        
        choice = input("Choose action: [1] Attack [2] Heal: ")
        
        # Player turn
        if choice == "1":
            damage = player_attack()
            dragon_hp -= damage
            print(f"⚔️ You dealt {damage} damage!")
        
        elif choice == "2":
            if potions > 0:
                player_hp += 30
                if player_hp > 100:
                    player_hp = 100
                potions -= 1
                print(f"🧪 Healed! HP: {player_hp}")
            else:
                print("💀 No potions left!")
        
        else:
            print("❌ Invalid move!")
        
        # Dragon turn
        if dragon_hp > 0:
            dmg = dragon_attack(phase)
            player_hp -= dmg
            print(f"🔥 Dragon hits for {dmg}!")
    
    # Result
    print("\n--- FINAL RESULT ---")
    if player_hp > 0:
        print("🏆 YOU SLAYED THE DRAGON!")
    else:
        print("💀 YOU WERE DESTROYED...")


# Replay system
while True:
    play_game()
    
    again = input("\nPlay again? (yes/no): ").lower().strip()
    
    if again not in ["yes", "y"]:
        print("👋 Thanks for playing!")
        break