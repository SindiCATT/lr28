#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add():
    name = input("Фамилия и имя? ")
    zod = input("Знак Зодиака? ")
    birth = input("Дата рождения? ")

    # Создать словарь:
    people = {
        'name': name,
        'zod': zod,
        'birth': birth,
    }

    # Добавить словарь в список:
    peoples.append(people)
    # Отсортировать список в случае необходимости.
    if len(peoples) > 1:
        peoples.sort(key=lambda item: item.get('birth', ''))
