from flask import Flask, render_template, request, redirect, url_for, jsonify
from oop_arena import Player, Monster

app = Flask(__name__)

game_state = {
    "player": None,
    "dragon": None,
    "logs": []
}

@app.route("/")
def home():
    game_state["player"] = Player("Hero")
    game_state["dragon"] = Monster("Dragon", 150)
    game_state["logs"] = ["Welcome to the Monster Battle Arena! Prepare to fight."]
    
    return render_template("arena.html", 
                           player=game_state["player"], 
                           dragon=game_state["dragon"], 
                           logs=game_state["logs"],
                           game_over=False)

@app.route("/api/play", methods=["POST"])
def api_play():
    if not game_state["player"] or not game_state["dragon"]:
        return jsonify({"error": "Game not initialized"}), 400
        
    player = game_state["player"]
    dragon = game_state["dragon"]
    
    data = request.get_json()
    action = data.get("action")
    game_over = False
    new_logs = []
    
    if action == "attack":
        dmg = player.attack()
        log_msg = dragon.take_damage(dmg)
        new_logs.append(f"⚔️ You attacked! {log_msg}")
    elif action == "heal":
        log_msg = player.heal()
        new_logs.append(log_msg)
        
    if dragon.hp > 0:
        dmg = dragon.attack()
        log_msg = player.take_damage(dmg)
        new_logs.append(log_msg)
    else:
        new_logs.append("🏆 YOU SLAYED THE DRAGON! YOU WIN!")
        game_over = True
        
    if player.hp <= 0:
        new_logs.append("💀 THE DRAGON DEFEATED YOU. GAME OVER.")
        game_over = True
        
    game_state["logs"] = new_logs + game_state["logs"]
    game_state["logs"] = game_state["logs"][:20]
    
    return jsonify({
        "player_hp": player.hp,
        "player_potions": player.potions,
        "dragon_hp": dragon.hp,
        "game_over": game_over,
        "new_logs": new_logs
    })

if __name__ == "__main__":
    app.run(port=5000)
