from flask import jsonify, request
from app import app
from app.models import Player, Game, GameByGame, Totals, UpcomingGame, CurrentSeries
from app.schema import player_schema, players_schema, game_schema, games_schema, gbg_schema, gbg_many_schema, total_schema, totals_schema, upcoming_game_schema, upcoming_games_schema, current_series_many_schema, current_series_schema
from flask_cors import CORS
from app.awards import calculate_potd, calculate_opod, calculate_dpod, calculate_cardio_man, calculate_brick_layer, calculate_traffic_cone
import datetime
from datetime import timedelta
import pytz
from nba_api.stats.static import players

CORS(app, resources=r'/api/*')



# Get ALL Players
@app.route('/api/player', methods=['GET'])
def get_all_players():
      all_players = Player.query.all()
      result = players_schema.dump(all_players)
      return jsonify(result)

# Get a specific player
@app.route('/api/players/<id>', methods=['GET'])
def get_player(id):
      player = Player.query.get(id)

      if player is None:
            return jsonify({"error": "Player not found"}), 404
      return player_schema.jsonify(player)

# Get a player based on search result
@app.route('/api/search', methods=['GET'])
def get_search_result():
      name = request.args.get('name')
      player = Player.query.filter(Player.player == name).first()

      if not player:
            return jsonify({"error": "player not found"}), 404
      return player_schema.jsonify(player)

# Get all games
@app.route('/api/game', methods=['GET'])
def get_all_games():
      all_games = Game.query.all()
      result = games_schema.dump(all_games)
      return jsonify(result)

# Get a specific game
@app.route('/api/games/<id>', methods=['GET'])
def get_game(id):
      game = Game.query.get(id)

      if game is None:
            return jsonify({"error": "Game not found"}), 404
      return game_schema.jsonify(game)

# Get all games for a specific player
@app.route('/api/players/<player_id>/game', methods=['GET'])
def get_all_games_for_player(player_id):
      games = GameByGame.query.filter(GameByGame.player_id == player_id)

      if not games:
            return jsonify({"error": "Game not found"}), 404
      return gbg_many_schema.jsonify(games)

# Get a specific game for a specific player
@app.route('/api/players/<player_id>/games/<date>', methods=['GET'])
def get_game_for_player(player_id, date):
      game = GameByGame.query.filter(GameByGame.player_id == player_id, GameByGame.date_string == date).first()

      if game is None:
            return jsonify({"error": "Game not found"}), 404
      return gbg_schema.jsonify(game)

@app.route('/api/player/total')
def get_all_total_stats():
      all_totals = Totals.query.all()
      result = totals_schema.dump(all_totals)
      return jsonify(result)

# Get total stats for a specific player
@app.route('/api/players/<id>/totals', methods=['GET'])
def get_total_stats_for_player(id):
      totals = Totals.query.filter(Totals.player_id == id).first()

      if not totals:
            return jsonify({"error": "player not found"}), 404
      return total_schema.jsonify(totals)

# Get all upcoming games
@app.route('/api/upcoming_game')
def get_upcoming_games():
      all_upcoming_games = UpcomingGame.query.all()
      result = upcoming_games_schema.dump(all_upcoming_games)
      return jsonify(result)

@app.route('/api/featured_players')
def get_featured_players():
      featured_players = CurrentSeries.query.with_entities(
            CurrentSeries.personid,
            CurrentSeries.name,
            CurrentSeries.playerslug,
            CurrentSeries.jerseynum,
            CurrentSeries.position,
            CurrentSeries.points,
            CurrentSeries.rebounds,
            CurrentSeries.assists
      ).all()

      if not featured_players:
            return jsonify({"error": "No featured players found."}), 404
      return jsonify([row._asdict() for row in featured_players])

@app.route('/api/last_night_performances')
def get_players_for_today():
      edt = pytz.timezone("America/New_York")
      today_edt = datetime.datetime.now(edt).date()

      yesterday = today_edt - timedelta(days=1)

      # Get the string in the exact same format as date_str (mdy)
      yesterday_str = yesterday.strftime("%m%d%Y")

      performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str)

      if not performances:
            return jsonify({"error": "no performances found"}), 404
      return gbg_many_schema.jsonify(performances)

@app.route('/api/potd')
def get_potd():
    edt = pytz.timezone("America/New_York")
    today_edt = datetime.datetime.now(edt).date()

    yesterday = today_edt - timedelta(days=1)

    # Get the string in the exact same format as date_str (mdy)
    yesterday_str = yesterday.strftime("%m%d%Y")

    performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str, GameByGame.actual_minutes > 20)
    best_player, score = calculate_potd(performances)

    if not best_player:
        return jsonify({"error": "no performances for today"}), 404

    player_name = players.find_player_by_id(best_player.player_id)

    result = gbg_schema.dump(best_player)
    result["player_name"] = player_name
    result["score"] = score
    return jsonify(result), 200

@app.route('/api/opod')
def get_opod():
      edt = pytz.timezone("America/New_York")
      today_edt = datetime.datetime.now(edt).date()

      yesterday = today_edt - timedelta(days=1)

      # Get the string in the exact same format as date_str (mdy)
      yesterday_str = yesterday.strftime("%m%d%Y")

      performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str, GameByGame.actual_minutes > 20)
      best_player, score = calculate_opod(performances)

      if not best_player:
            return jsonify({"error": "no performances for today"}), 404

      player_name = players.find_player_by_id(best_player.player_id)

      result = gbg_schema.dump(best_player)
      result["player_name"] = player_name
      result["score"] = score
      return jsonify(result), 200

@app.route('/api/dpod')
def get_dpod():
      edt = pytz.timezone("America/New_York")
      today_edt = datetime.datetime.now(edt).date()

      yesterday = today_edt - timedelta(days=1)

      # Get the string in the exact same format as date_str (mdy)
      yesterday_str = yesterday.strftime("%m%d%Y")

      performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str, GameByGame.actual_minutes > 20)
      best_player, score = calculate_dpod(performances)

      if not best_player:
            return jsonify({"error": "no performances for today"}), 404

      player_name = players.find_player_by_id(best_player.player_id)

      result = gbg_schema.dump(best_player)
      result["player_name"] = player_name
      result["score"] = score
      return jsonify(result), 200

@app.route('/api/cardio_man')
def get_cardio_man():
    edt = pytz.timezone("America/New_York")
    today_edt = datetime.datetime.now(edt).date()

    yesterday = today_edt - timedelta(days=1)

    # Get the string in the exact same format as date_str (mdy)
    yesterday_str = yesterday.strftime("%m%d%Y")

    performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str, GameByGame.actual_minutes > 15)
    worst_player, score = calculate_cardio_man(performances)

    if not worst_player:
        return jsonify({"error": "no performances for today"}), 404

    player_name = players.find_player_by_id(worst_player.player_id)

    result = gbg_schema.dump(worst_player)
    result["player_name"] = player_name
    result["score"] = score
    return jsonify(result), 200

@app.route('/api/brick_layer')
def get_brick_layer():
      edt = pytz.timezone("America/New_York")
      today_edt = datetime.datetime.now(edt).date()

      yesterday = today_edt - timedelta(days=1)

      # Get the string in the exact same format as date_str (mdy)
      yesterday_str = yesterday.strftime("%m%d%Y")

      performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str, GameByGame.actual_minutes > 15)
      worst_player, score = calculate_brick_layer(performances)

      if not worst_player:
            return jsonify({"error": "no performances for today"}), 404

      player_name = players.find_player_by_id(worst_player.player_id)

      result = gbg_schema.dump(worst_player)
      result["player_name"] = player_name
      result["score"] = score
      return jsonify(result), 200

@app.route('/api/traffic_cone')
def get_traffic_cone():
      edt = pytz.timezone("America/New_York")
      today_edt = datetime.datetime.now(edt).date()

      yesterday = today_edt - timedelta(days=1)

      # Get the string in the exact same format as date_str (mdy)
      yesterday_str = yesterday.strftime("%m%d%Y")

      performances = GameByGame.query.filter(GameByGame.date_string == yesterday_str, GameByGame.actual_minutes > 15)
      worst_player, score = calculate_traffic_cone(performances)

      if not worst_player:
            return jsonify({"error": "no performances for today"}), 404

      player_name = players.find_player_by_id(worst_player.player_id)

      result = gbg_schema.dump(worst_player)
      result["player_name"] = player_name
      result["score"] = score
      return jsonify(result), 200