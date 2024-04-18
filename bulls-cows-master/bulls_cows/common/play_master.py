# Here is the business end of the Bull-Cow logic
from random import randint

from django.contrib import messages

# class PlayMaster:
#     def __init__(self):
#         pass
#         # self.secret_num = SecretNumber.create_secret_number()


def create_secret_number():
    """
    create random 4 dig number in a list
    """
    secret_num = []

    while len(secret_num) < 4:
        secret_digit = randint(0, 9)
        if secret_digit not in secret_num:
            secret_num.append(secret_digit)
    result = ''.join(str(x) for x in secret_num)
    return result


def bull_cow_return(secret_num, player_num):
    """return (cows, bulls) count"""
    
    cows = len([digit for digit in player_num if digit in secret_num])
    bulls = 0

    for i in range(len(player_num)):
        if player_num[i] == secret_num[i]:
            bulls += 1
    
    won = False
    if bulls == 4:
        won = True

    return bulls, cows, won


def play_round(request):
    """
    play a round with the secret and user number
    returns [(player_number, bulls, cows)]
    """

    if not request.session.get('session_round'):
        request.session['secret_number'] = create_secret_number()

        request.session['session_round'] = 1
        request.session['number_bulls_cows'] = list()
        
        bulls, cows, won = bull_cow_return(request.session['secret_number'], request.POST.get('digits_input'))
        request.session['number_bulls_cows'].append(
            (request.POST.get('digits_input'), bulls, cows))
       
    else:
        request.session['session_round'] += 1

        bulls, cows, won = bull_cow_return(request.session['secret_number'], request.POST.get('digits_input'))
        
        request.session['number_bulls_cows'].append(
            (request.POST.get('digits_input'), bulls, cows))
    
    request.session['won'] = won
    return request.session['number_bulls_cows']


def clean_session(request):
    try:
        del request.session['secret_number']
        del request.session['session_round']
        del request.session['number_bulls_cows']
        return "cleaned round data"
    except KeyError:
        return "something went wrong"


def bull_cow_message(request):
    nbc = request.session.get('number_bulls_cows')[-1]
    messages.add_message(request, messages.INFO, f'Bulls: {nbc[1]}, Cows: {nbc[2]}')


def game_won(request):
    if request.session.get('won'):
        msg = f"You've won!!!\nThe secret number was {request.session.get('secret_number')}"
        messages.add_message(request, messages.INFO, msg)
        clean_session(request)


def game_over(request):
    if request.session.get('session_round') == 7:
        sn = request.session.get('secret_number')
        msg = f"The secret number was {sn}"
        messages.add_message(request, messages.INFO, msg)
        clean_session(request)


def debug_show_secret_number(request):
    msg = f"The secret number is **** {request.session.get('secret_number')}"
    messages.add_message(request, messages.INFO, msg)

