import json


def load_candidates():
    with open('candidates.json', 'rt', encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for i in get_all():
        if i['pk'] == pk:
            return i


def get_by_skill(skill_name):
    l = []
    for i in get_all():
        if skill_name.lower() in i['skills'].lower():
            l.append(i)
    return l





