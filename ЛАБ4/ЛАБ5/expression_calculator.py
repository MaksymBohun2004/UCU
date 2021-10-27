def calculate_expression(expression):
    expression = expression.split("?")
    expression = expression[0]
    expression = expression.split()
    expression.pop(0), expression.pop(0)
    result = 0
    operations = 0
    for i in range(len(expression)):
        if len(expression) == 1:
            try:
                int(expression[0])
                result = int(expression[0])
                operations += 1
                break
            except:
                return "Неправильний вираз!"
        else:
            pass
        if expression[i] == "помножити":
            if expression[i-1] == "0" or expression [i+2] == "0":
                result = result * 0
                operations += 1
            else:
                try:
                    if expression[i + 1] == "на" and int(expression[i - 1]) and  int(expression[i  + 2]):
                        if i > 2:
                            result = result * int(expression[i + 2])
                            operations += 1
                        else:
                            result = result + int(expression[i - 1]) * int(expression[i+2])
                            operations += 1
                except:
                    print('Неправильний вираз!')
        elif expression[i] == "поділити":
            try:
                if expression[i + 1] == "на" and int(expression[i - 1]) and  int(expression[i  + 2]):
                    if i > 2:
                        result = result / int(expression[i + 2])
                        operations += 1
                    else:
                        result = result + int(expression[i - 1]) / int(expression[i+2])
                        operations += 1
            except:
                print('Неправильний вираз!')
        elif expression[i] == "додати" or expression[i] == "плюс":
            try:
                if  int(expression[i - 1]) and  int(expression[i  + 1]):
                    if i > 2:
                        result = result + int(expression[i+1])
                        operations += 1
                    else:
                        result = result + int(expression[i - 1]) + int(expression[i+1])
                        operations += 1
            except:
                print('Неправильний вираз!')
        elif expression[i] == "відняти" or expression[i] == "мінус":
            try:
                if  int(expression[i - 1]) and  int(expression[i  + 1]):
                    if i > 2:
                        result = result - int(expression[i+1])
                        operations += 1
                    else:
                        result = result + int(expression[i - 1]) - int(expression[i+1])
                        operations += 1
            except:
                print('Неправильний вираз!')
    if operations != 0:
        return result
    else:
        return 'Неправильний вираз!'