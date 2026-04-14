from flask import Flask, render_template, request, redirect, url_for
from oop_arena import Player, Monster

app = Flask(__name__)

# Global Game State (Simple, but limits it to 1 player locally!)
game_state = {
    "player": None,
    "dragon": None,
    "logs": []
}

@app.route("/")
def home():
    # Reset the game state!
    game_state["player"] = Player("Hero")
    game_state["dragon"] = Monster("Dragon", 150)
    game_state["logs"] = ["Welcome to the Monster Battle Arena! Prepare to fight."]
    
    return render_template("arena.html", 
                           player=game_state["player"], 
                           dragon=game_state["dragon"], 
                           logs=game_state["logs"],
                           game_over=False)

@app.route("/play", methods=["POST"])
def play():
    # Ensure they haven't bypassed the start screen somehow
    if not game_state["player"] or not game_state["dragon"]:
        return redirect(url_for("home"))
        
    player = game_state["player"]
    dragon = game_state["dragon"]
    logs = game_state["logs"]
    
    action = request.form.get("action")
    game_over = False
    
    # Player's Turn
    if action == "attack":
        dmg = player.attack()
        log_msg = dragon.take_damage(dmg)
        logs.insert(0, f"⚔️ You attacked! {log_msg}")
    elif action == "heal":
        log_msg = player.heal()
        logs.insert(0, log_msg)
        
    # Dragon's Turn (If it survived)
    if dragon.hp > 0:
        dmg = dragon.attack()
        log_msg = player.take_damage(dmg)
        logs.insert(0, log_msg)
    else:
        logs.insert(0, "🏆 YOU SLAYED THE DRAGON! YOU WIN!")
        game_over = True
        
    if player.hp <= 0:
        logs.insert(0, "💀 THE DRAGON DEFEATED YOU. GAME OVER.")
        game_over = True
        
    # Keep only the last 10 logs so the screen isn't flooded
    game_state["logs"] = logs[:10]
    
    return render_template("arena.html", 
                           player=player, 
                           dragon=dragon, 
                           logs=game_state["logs"],
                           game_over=game_over)

# ALWAYS keep this at the very bottom!
if __name__ == "__main__":
    app.run(port=5000)
