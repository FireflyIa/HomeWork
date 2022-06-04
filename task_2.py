def userinfo(firstName, secondName, age, city, email, phone):
    return print(f'Имя: {firstName},'
                 f' Фамилия: {secondName},'
                 f' Дата рождения: {age},'
                 f' Город: {city},'
                 f' Email: {email},'
                 f' Тел.: {phone}')


def main():
    print(userinfo(input('Name pls: '),
                   input('Second Name pls: '),
                   input('Date born pls: '),
                   input('Live city pls: '),
                   input('Email pls: '),
                   input('Phone num pls: ')))


if __name__ == '__main__':
    main()
