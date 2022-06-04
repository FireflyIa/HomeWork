import langid


def title_word():
    f = True
    while f:
        word = str(input('Enter word by english: \n'))
        try:
            lg = list(langid.classify(word))
            if lg[0] != 'en' \
                    or word.isdigit()\
                    or word.istitle():
                print('Error, english and lowercase pls!')
                print('-'*20)
                continue
            f = False
            print(f'Great, You words Title:   {word.title()}')
        except Exception:
            print('Error, english and lowercase pls!')
            print('-' * 20)
            continue


def main():
    title_word()


if __name__ == '__main__':
    main()

# Код из видео не работает
# def titl_word(word):
#     return word[0].upper() + word[1:].lower
#
#
# s = input().split()
# for i, word in enumerate(s):
#     if not word.isascii() or not word.isalpha() or not word.islower():
#         print('error!')
#     else:
#         s[i] = titl_word(word)
# print(' '.join(s))


