from django.urls import path
from .views import HomePageView, ContactUsView, GamesPageView, SnakePageView, TicTacToePageView, FlipMemoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contactus/', ContactUsView.as_view(), name='contactus'),
    path('games/', GamesPageView.as_view(), name='games'),
    path('games/snake', SnakePageView.as_view(), name='snake'),
    path('games/tictactoe', TicTacToePageView.as_view(), name='tictactoe'),
    path('games/flipmemory', FlipMemoryPageView.as_view(), name='flipmemory'),
]
