from random import seed, randint 
def main():

        
    def create_secret_number():
        """create random number"""
        secret_num = []
        seed()
        
        while len(secret_num) < 4:
            secret_digit = randint((int('0')), int('9'))
            if secret_digit not in secret_num:
                secret_num.append(str(secret_digit))

        return secret_num


    def bull_cow_return(secret_num, player_num):
        """return (cows, bulls) count"""
        cows = len([digit for digit in player_num if digit in secret_num])
        
        bulls = 0
        for i in range(len(player_num)):
            if player_num[i] == secret_num[i]:
                    bulls += 1

        return bulls, cows


    def get_player_num():
        player_num = list()

        while len(player_num) < 4:
            try:
                player_input = input()[0]
                if player_input.isdigit() and \
                    player_input not in player_num:
                    player_num.append(player_input)
            except (ValueError, IndexError):
                continue
        return player_num

    def another_game(state):
            
        if not state:
            play_again = input('Sorry, you ran out of tries! Would you like to play again?\n')
        else:
            play_again = input('Great! Would you like to play again?\n')
     
        if play_again in ['yes', 'y', 'Y', 'YES', 'Yes']:
            return play()
        else:
            return print('OK, Thank you for playing.')   


    def play(tries = 7):
        won = False
        secret_num = create_secret_number()
        print(secret_num)

        for i in range(tries):
            print(f'Try {i+1} of {tries}')

            player_num = get_player_num()
            bulls, cows = bull_cow_return(secret_num, player_num)

            if bulls == 4:
                won = True
                result = f'YOU WON!\n{player_num} is the secrest number {secret_num}.\n'
                break
            else:
                print(f'Cows: {cows}, Bulls: {bulls}')
        
        print(result)
        return won
    
    x = play()   
    another_game(x)

if __name__ == '__main__':
    main()