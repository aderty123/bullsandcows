from django.forms import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.views import View

from bulls_cows.common.play_master import *
from bulls_cows.models import ScoreCard, ScoreBoard, Player
from bulls_cows.forms.profile import PlayerForm
from bulls_cows.forms.number_form import NumberForm

from bulls_cows.common.functionality import test_cooke, current_player_get_or_create


# from bulls_cows.common import player_session

# This view handles the user selection and play logic.
# There are two forms - player name and player number input.

class Play(View):

    def get(self, request):

        cookie_state = test_cooke(request)
        request.session.set_test_cookie()

        current_player = current_player_get_or_create(request)

        form_player_name = PlayerForm(instance=current_player)
        form_number_input = NumberForm()

        context = {
            'id': current_player.player_name,
            'cookie_state': cookie_state,
            'form_player_name': form_player_name,
            'form_number_input': form_number_input
        }

        if request.session.get('number_bulls_cows'):
            context['num_bull_cow'] = request.session.get('number_bulls_cows')
            bull_cow_message(request)

        game_won(request)
        game_over(request)
        debug_show_secret_number(request)


        return render(request, 'play.html', context) 

    def post(self, request):
        #set next test cookie
        request.session.set_test_cookie()

        #Get current player
        player_token = request.session.get('player_token')
        current_player = Player.objects.get(player_id=player_token)

        #Determine form bein posted and act
        if 'player_name' in request.POST:      
            form = PlayerForm(request.POST, instance=current_player)
            if form.is_valid():
                form.save()
                messages.add_message(self.request, messages.INFO, f'Changed player name. Hello, {request.POST["player_name"]}')
                return HttpResponseRedirect(request.path_info)                 

        elif 'digits_input' in request.POST:
            form = NumberForm(request.POST)
            if form.is_valid():
                play_round(request)

                return HttpResponseRedirect(request.path_info)
            else:
                messages.add_message(self.request, messages.INFO, 'Please input correct number')
                return HttpResponseRedirect(request.path_info)
