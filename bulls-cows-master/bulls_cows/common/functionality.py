from bulls_cows.models import Player


def test_cooke(request):
    """
    Return the result of the last test cookie.
    returns cookie_state = bool
    """
   
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        cookie_state = True
    else:
        cookie_state = False
    
    return cookie_state


def current_player_get_or_create(request):
    """
    Get the cureent player, based on cookie var 'player_id'.
    If not found, make new player and set the cookie variable.
    retuns Player object.
    """
    
    #get the player token from cookies
    player_token = request.session.get('player_token')

    #if the token exists search the player from DB, else
    # If no player token is present in cookies - create player and set token in session 
    if player_token:
        current_player = Player.objects.get(player_id=player_token)
    else:
        current_player = Player.objects.create()
        request.session['player_token'] = str(current_player.player_id)
   
    return current_player
