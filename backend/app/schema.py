from app import ma
from app.models import Player, Game, GameByGame, Totals, UpcomingGame, CurrentSeries
from marshmallow import fields

class PlayerSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Player
            fields = ('team_id', 'season', 'league_id', 'player', 'nickname', 'player_slug', 'num', 'pos',
                      'height', 'weight', 'birth_date', 'age', 'experience', 'school', 'player_id',
                      'how_acquired')

# Init schema
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

class GameSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Game
            fields = ('id', 'season_id', 'team_id', 'team_abbreviation', 'team_name', 'game_id', 'game_date',
                      'matchup', 'wl', 'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct', 'ftm',
                      'fta', 'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 
                      'plus_minus', 'video_available')
            
game_schema = GameSchema()
games_schema = GameSchema(many=True)


class GameByGameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GameByGame
        load_instance = True


gbg_schema = GameByGameSchema()
gbg_many_schema = GameByGameSchema(many=True)


class TotalsSchema(ma.SQLAlchemyAutoSchema):
    game_by_game = fields.List(fields.Nested(GameByGameSchema))

    class Meta:
        model = Totals
        load_instance = True

total_schema = TotalsSchema()
totals_schema = TotalsSchema(many=True)

class UpcomingGameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
         model = UpcomingGame
         load_instance = True

upcoming_game_schema = UpcomingGameSchema()
upcoming_games_schema = UpcomingGameSchema(many=True)

class CurrentSeriesSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
          model = CurrentSeries
          load_instance = True

current_series_schema = CurrentSeriesSchema()
current_series_many_schema = CurrentSeriesSchema(many=True)