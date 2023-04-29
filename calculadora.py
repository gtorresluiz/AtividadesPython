while True:

    num1 = float(input("digite o primero numero: "))
    num2 = float(input("digite o segundo numero: "))
    op = str(input("qual operação deseja realizar entre eles? (+, -, *, /)"))
    result = 0
    valid = True

    match op:
        case '+':
            op = 'soma'
            result = num1 + num2
        case '-':
            op = 'subtração'
            result = num1 - num2
        case '/':
            if num2 == 0:
                print("não é possivel dividir por 0")
                valid = False
            else:
                op = 'divisão'
                result = num1 / num2
        case '*':
            op = 'multiplicação'
            result = num1 * num2
        case _:
            print("escolha uma operação válida (+,-,*,/)")  
            valid = False
    
    if valid:
        print("o resultado da %s entre %d e %d resulta em %.3f" %(op, num1, num2, result))
        break 