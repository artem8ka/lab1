import re


def pre_validation(expression: str) -> list:
    #Проверка основных пользовательских ошибок
    if expression == '': return ['error', 2, 'Empty expression']
    if not all((char in '0123456789+-*/.') for char in expression): return ['error', 2, 'Invalid char']
    if expression[-1] in '+-*/': return ['error', 2, 'Missed operand']
    two_binary = ['-*', '+*', '+/','-/', '**', '//', '*/', '/*']
    if any((tb in expression) for tb in two_binary): return ['error', 2, 'Two binary operators in a row']
    first_zero = [z_operator + '0' + z_num for z_operator in '+-*/' for z_num in '0123456789']
    if expression[:2]=='00' or any(oo in expression for oo in first_zero): return ['error', 2, 'Incorrect operand']

def tokenization(expression: str) -> list:
    #Разбиение на токены
    number_expression = r'[+-]?(0|[1-9][0-9]*)([.][0-9]+)?'
    operation_expression = r'[+/*\-]'
    two_numbers_with_space = [fnum + ' ' + snum for fnum in '0123456789' for snum in '0123456789'] #список некорректных вхождений
    while '++' in expression or '+-' in expression \
    or '-+' in expression or '--' in expression or '  ' in expression:
        expression = expression.replace('++','+')
        expression = expression.replace('--','+')
        expression = expression.replace('+-','-')
        expression = expression.replace('-+','-')
        expression = expression.replace('  ', ' ')
    if any(comb in expression for comb in two_numbers_with_space): #Проверка на число, написанное через пробел
        return ['error', 2, 'Missed operator']
    else:
        while ' ' in expression:
            expression = expression.replace(' ', '')
    tokens = []
    first_token = re.match(number_expression,expression) #Первый токен, обязательно число
    if first_token == None:
        return ['error', 2, 'Missed operand']
    else:
        tokens.append(first_token.group())
        expression = expression[len(first_token.group()):]
    while expression: #В этом цикле добавляем токены поочередно, сначала операцию, потом число
        operation = re.match(operation_expression,expression)
        if operation == None:
            return [2, 'Incorrect expression']
        else:
            tokens.append(operation.group())
            expression = expression[len(operation.group()):]
        number = re.match(number_expression,expression)
        if number == None:
            return [2, 'Incorrect expression']
        else:
            tokens.append(number.group())
            expression = expression[len(number.group()):]
    return tokens

def validation(tokens: list) -> list:
    #Проверка деления на ноль
    for index_of_token in range(1,len(tokens)-1,2):
        operation_index = index_of_token
        number_index = index_of_token+1
        if tokens[operation_index]=='/' and float(tokens[number_index])==0:
            return ['error', 2, 'Division by zero']

def calculator_function(calc_argument: str) -> float:
    #Основная функция калькулятора
    if type(pre_validation(calc_argument)) is list: return pre_validation(calc_argument)[1:]
    tokens = tokenization(calc_argument)
    if tokens[0]=='error': return tokens[1:]
    if type(validation(tokens)) is list: return validation(tokens)[1:]
    while '*' in tokens and '/' in tokens: #Приоритет деления и умножения, решаем по порядку только их
        mult = tokens.index('*')
        div = tokens.index('/')
        if mult < div:
            tokens[mult-1:mult+2] = [float(tokens[mult-1])*float(tokens[mult+1])]
        else:
            tokens[div-1:div+2] = [float(tokens[div-1])/float(tokens[div+1])]
    while '*' in tokens:
        mult = tokens.index('*')
        tokens[mult-1:mult+2] = [float(tokens[mult-1])*float(tokens[mult+1])]
    while '/' in tokens:
        div = tokens.index('/')
        tokens[div-1:div+2] = [float(tokens[div-1])/float(tokens[div+1])]
    while len(tokens)>1: #После обработки деления и умножения досчитываем оставшееся выражение с + и - и возвращаем результат
        if tokens[1]=='+':
            tokens[:3]=[float(tokens[0])+float(tokens[2])]
        if len(tokens)>1 and tokens[1]=='-':
            tokens[:3]=[float(tokens[0])-float(tokens[2])]
    result = float(tokens[0])
    return result