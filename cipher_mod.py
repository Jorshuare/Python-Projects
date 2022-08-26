class Cipher:
    def __init__(self):
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                     's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def cip(self, text, shift, method):
        self.text = text
        self.shift = shift
        self.method = method

        self.final_text = ''
        for char in self.text:
            if char in self.alphabets:
                place = self.alphabets.index(char)

                if self.method == 'decode':
                    new_place = place - shift
                else:
                    new_place = place + shift
                self.final_text += self.alphabets[new_place]

            else:
                self.final_text += char
        print(f'The {self.method}d message is: {self.final_text}')

        # print(text, shift, method)


c = Cipher()
game_on = True
while game_on:
    c_text = input('What\'s your message: ').lower()
    c_method = input('Press "encode" to encrypt and "decode" to decrypt: ').lower()
    c_shift = int(input('enter your shift number: '))
    c_shift = c_shift % 26
    c.cip(c_text, c_shift, c_method)

    asking = True
    while asking:
        ask = input('Type "yes" if you wish to continue or "no" if you wish to stop: ').lower()
        if ask == 'yes':
            game_on = True
            asking = False

        elif ask == 'no':
            game_on = False
            asking = False

        else:
            print('invalid answer')
            asking = True
