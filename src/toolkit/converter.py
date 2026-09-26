import json
from pathlib import Path

with open(Path(__file__).parent / "convert.json", "r", encoding="utf-8") as file:
    convert_coefs = json.load(file)


def temperature_converter(value: float, unit_from: str, unit_to: str) -> float:
    #Функция перевода температуры реализована через ветвление
    if (unit_from == 'f' and value > (-459.67)) \
    or (unit_from == 'c' and value > (-273.15)) \
    or (unit_from == 'k' and value > 0):
        code_of_convert = unit_from+unit_to
        if code_of_convert in ('cc','ff','kk'):
            return value
        elif code_of_convert == 'cf':
            return value*1.8 + 32
        elif code_of_convert == 'ck':
            return value + 273.15
        elif code_of_convert == 'fc':
            return (value-32)/1.8
        elif code_of_convert == 'fk':
            return (value+459.67)/1.8
        elif code_of_convert == 'kc':
            return value - 273.15
        elif code_of_convert == 'kf':
            return value*1.8 - 459.67
    else:
        return [2, 'Temperature below absolute zero']

def converter_function(value: str, unit_from: str, unit_to: str) -> float:
    #Основная функция конвертера
    supported_units = ('c','f','k','g','kg','km','m','cm','mm')
    groups = [('temperature_units', ('c','f','k')), ('mass_units', ('g','kg')), ('len_units', ('km','m','cm','mm'))]
    unit_from_group = 'ufg' #Создаем непустые переменные для записи групп единиц перевода
    unit_to_group = 'utg' #Изначально с разными значениями

    unit_from = unit_from.lower() #Приводим регистр единиц к единому виду
    unit_to = unit_to.lower()
    try: #Проверяем корректность числового значения value
        value = float(value)
    except ValueError:
        return [2, 'Incorrect value']
    if unit_from in supported_units: unit_from_group = [group[0] for group in groups if unit_from in group[1]][0] #Определяем группы единиц
    if unit_to in supported_units: unit_to_group = [group[0] for group in groups if unit_to in group[1]][0] #Если единица не поддерживается, vvv
    if unit_from_group==unit_to_group: #группа остается со стандартным значением, которое не является группой чтобы выявлять неизвестные единицы
        if unit_to in groups[0][1]:
            return temperature_converter(value, unit_from, unit_to)
        else:
            if not '-' in str(value):
                return value*convert_coefs[unit_from_group][unit_from][unit_to] #Массу и длину переводим с помощью json файла с коэффициентами
            else:
                return [2, 'Negative value of mass or length']
    else:
        if unit_from not in supported_units:
            return [2, 'Incorrect FROM unit']
        if unit_to not in supported_units:
            return [2, 'Incorrect TO unit']
        else:
            return [2, 'Different groups of units']