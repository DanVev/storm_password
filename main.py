import os
from os import path as osp
import colorama
from termcolor import colored
from time import sleep
import json


def printf(text, color='green', sleep_time=0.04):
    for letter in text:
        print(colored(letter, color), end='')
        sleep(sleep_time)


def load_with_response(text, response, delay=1):
    printf(text)
    sleep(delay)
    printf(response)


if __name__ == '__main__':
    colorama.init()
    os.system('cls')
    input()
    cwd = osp.split(osp.realpath(__file__))[0]

    printf("Включение терминала\n")
    printf("Запуск тестовой проверки\n")
    load_with_response('Подключение модулей питания...', 'OK\n')
    load_with_response('Проверка состояния камер видеонаблюдения...', 'OK\n')
    load_with_response('Инициализация систем контроля...', 'OK\n')
    load_with_response('Инициализация ключей доступа...', 'OK\n')
    printf("Проверка пройдена успешно\n")
    load_with_response("Инициализация пользователя...", 'Ошибка\n', 3)
    printf('Требуется ввод мастер ключа.\n')
    while True:
        passwords = json.load(open(osp.join(cwd, 'passwords.json'), 'r'))
        printf('Введите пароль: ')
        typed_password = input()
        if typed_password in passwords:
            printf('Пароль верный.\nИнициализирую систему видеоконтроля\n')
            if passwords[typed_password] != 'exit':
                sleep(2)
                os.startfile(osp.join(cwd, 'videos', str(passwords[typed_password]), 'video.mp4'))
                del passwords[typed_password]
                json.dump(passwords, open(osp.join(cwd, 'passwords.json'), 'w'), sort_keys=True, indent=4)
            break
        else:
            printf('Пароль не верный, попробуйте еще раз.\n')
    input()
