from rest_framework import serializers


def password_validator(value:str):
    has_digits = False
    for symbol in value:
        if symbol.isdigit():
            has_digits = True

    if len(value) < 8:
        raise serializers.ValidationError("Ваш пароль слишком короткий")
    elif not has_digits:
        raise  serializers.ValidationError("В вашем пароле нет цифр")


def mail_validator(value:str):
    if  not value.endswith(('mail.ru', 'yandex.ru')):
        raise serializers.ValidationError("Допустимо использовать только почту mail.ru и yandex.ru")

def age_validator(value):
    print(value)


