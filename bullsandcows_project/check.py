
from random import randint
class Check:
    def validate_number(self, numbers: list):
        try:
            numbers_list = [int(number) for number in numbers]
            if len(numbers_list) < 4:
                return f"Chisel doljno bit 4"
            for number in numbers_list:
                if number < 1 or number > 9:
                    return f"Vvedite chislo ot 1 do 9"
        except ValueError as e:
            return f"vvedite chislo"
        return numbers_list
    
    def guess_numbers(self, secret_numbers: list, numbers: list):
        i = 0
        j = 0
        numbers_list = [int(number) for number in numbers]
        for secret_number, number in zip(secret_numbers, numbers_list):
            if number == secret_number:
                i += 1
            elif number in secret_numbers and number != secret_number:
                j += 1
        if secret_numbers == numbers_list:
            return f"You got win"
        return f"bulls: {i}; cows: {j}"
    
    def generate_numbers(self, random_num):
        secret_numbers = []
        for _ in range(random_num):
            secret_numbers.append(randint(1,9))
        return secret_numbers
