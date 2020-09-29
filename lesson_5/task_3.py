"""2) Создать функцию, которая будет скачивать файл из интернета по
ссылке, повесить на неё декоратор, который будет запускать целевую
функцию каждый раз в отдельном потоке. Создать список из 10
ссылок, по которым будет происходить скачивание. Каждый поток
должен сигнализировать, о том, что, он начал работу и по какой
ссылке он работает, так же должен сообщать когда скачивание
закончится."""

import time
from functools import wraps
from random import randint
from threading import Thread

import requests

one_url = 'https://rcnit.com.ua/wp-content/uploads/2016/10/qa.jpg'


def name_of_threads():
    def actual_decorator(func):
        @wraps(func)
        def wrapper():
            thread = Thread(target=func)
            thread.start()

        return wrapper

    return actual_decorator


@name_of_threads()
def ten():
    save_file = requests.get(one_url)
    with open('new_image.jpg', 'wb') as f:
        f.write(save_file.content)


"--------------------------------------------------------------------"
ten_urls = ['https://rcnit.com.ua/wp-content/uploads/2016/10/qa.jpg',
            'https://images.wallpaperscraft.ru/image/mashina_sportkar_neon_157154_1280x720.jpg',
            'https://images.wallpaperscraft.ru/image/mashina_sportkar_neon_156622_300x188.jpg',
            'https://images.wallpaperscraft.ru/image/mashina_sportkar_doroga_156423_300x188.jpg',
            'https://images.wallpaperscraft.ru/image/rollsroyce_vid_speredi_fary_136993_1280x720.jpg',
            'https://rcnit.com.ua/wp-content/uploads/2016/10/qa.jpg',
            'https://images.wallpaperscraft.ru/image/mashina_sportkar_neon_157154_1280x720.jpg',
            'https://images.wallpaperscraft.ru/image/mashina_sportkar_neon_156622_300x188.jpg',
            'https://images.wallpaperscraft.ru/image/mashina_sportkar_doroga_156423_300x188.jpg',
            'https://images.wallpaperscraft.ru/image/rollsroyce_vid_speredi_fary_136993_1280x720.jpg'
            ]


def name_of_threads_():
    def actual_decorator(func):
        @wraps(func)
        def wrapper():
            for url in ten_urls:
                name = randint(0, 100)
                print(f"Thread starting, {url}")
                start = time.time()
                thread = Thread(target=func(url, name), args=(url,))
                thread.start()
                print(f"Thread end. Time: {time.time() - start}")

        return wrapper

    return actual_decorator


@name_of_threads_()
def ten_(url, name):
    save_file = requests.get(url)
    with open(f'new_image{name}.jpg', 'wb') as f:
        f.write(save_file.content)
