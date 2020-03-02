def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


result = is_luhn_valid(4137894711755904)
print ("Correct:",  str(result))
result = is_luhn_valid(6499802450273568)
print ("Correct:",  str(result))
result = is_luhn_valid(8504172191273888)
print ("Correct:" ,str(result))
