from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def text(title, text):
    return f'<h1>Первый сайт на Django</h1>'\
    f'<h2>{title}</h2>'\
    f'<p>{text}</p>'


def main_page(request):
    title = 'Главная страница сайта'
    body_text = 'Текст главной страницы сайта на Django'
    logger.info(f'Главная страница открыта')
    return HttpResponse(text(title, body_text))

def about_me(request):
    title = 'О себе'
    body_text = 'Инфрмация...<br>'\
    'Ок'
    logger.info(f'Страница "о себе" открыта')
    return HttpResponse(text(title, body_text))
