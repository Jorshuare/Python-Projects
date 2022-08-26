alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(text, shift, method):
    final_text = ''
    for char in text:
        if char in alphabets:
            place = alphabets.index(char)

            if method == 'decode':
                new_place = place - shift
            else:
                print(f'You are encoding {text}')
                new_place = place + shift
            final_text += alphabets[new_place]

        else:
            final_text += char
    print(f'The {method}d message is {final_text}')


game_on = True
while game_on:
    c_text = input('what yor message: ')
    c_method = input('press "encode" to encrypt and "decode" to decrypt: ').lower()
    c_shift = int(input('enter your shift number: '))
    c_shift = c_shift % 26
    cipher(c_text, c_shift, c_method)

    asking = True
    while asking:
        ask = input('Type "yes" if you wish to continue or "no" if you wish to stop').lower()
        if ask == 'yes':
            game_on = True
            asking = False

        elif ask == 'no':
            game_on = False
            asking = False

        else:
            print('invalid answer')
            asking = True
