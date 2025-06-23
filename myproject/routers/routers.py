from rest_framework.routers import DefaultRouter
from viewsets.team_viewsets import TeamViewSet
from viewsets.match_viewsets import MatchViewSet
from viewsets.player_result_viewsets import PlayerResultViewSet
from viewsets.player_viewsets import PlayerViewSet
from viewsets.substitution_viewsets import SubstitutionViewSet
from viewsets.referee_viewsets import RefereeViewSet


router = DefaultRouter()
router.register('team', TeamViewSet, basename="team")
router.register('match', MatchViewSet, basename="match")
router.register('player_result', PlayerResultViewSet, basename="player_result")
router.register('player', PlayerViewSet, basename="player")
router.register('substitution', SubstitutionViewSet, basename="substitution")
router.register('referee', RefereeViewSet, basename='referee')