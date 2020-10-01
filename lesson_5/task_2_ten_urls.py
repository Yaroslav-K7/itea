import time
from functools import wraps
from random import randint
from threading import Thread

import requests

one_url = 'https://rcnit.com.ua/wp-content/uploads/2016/10/qa.jpg'


def name_of_threads(func):
    @wraps(func)
    def wrapper():
        thread = Thread(target=func)
        thread.start()

    return func


@name_of_threads
def ten():
    save_file = requests.get(one_url)
    with open('new_image.jpg', 'wb') as f:
        f.write(save_file.content)


"--------------------------------------------------------------------"
urls = ['https://rcnit.com.ua/wp-content/uploads/2016/10/qa.jpg',
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


def name_of_threads_(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Thread starting - {args}")
        start = time.time()
        Thread(target=func, args=args, kwargs=kwargs).start()
        print(f"Thread end. Time: {time.time() - start}")

        return func
    return wrapper


@name_of_threads_
def download_and_save(url, name):
    save_file = requests.get(url)
    with open(name, 'wb') as f:
        f.write(save_file.content)


for u in urls:
    download_and_save(u, f'{randint(0, 1000)}.jpg')
