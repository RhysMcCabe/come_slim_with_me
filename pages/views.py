from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactUsView(TemplateView):
    template_name = 'contactus.html'

class GamesPageView(TemplateView):
    template_name = 'games_base.html'

class SnakePageView(TemplateView):
    template_name = 'game_snake.html'

class TicTacToePageView(TemplateView):
    template_name = 'game_tictactoe.html'

class FlipMemoryPageView(TemplateView):
    template_name = 'game_flipmemory.html'