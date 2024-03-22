def get_bool() -> bool:
    x0 = input('Введите координату x0 ')
    x1 = input('Введите координату x1 ')
    y0 = input('Введите координату y0 ')
    y1 = input('Введите координату y1 ')

    if y0 >= x0:
        if y0 <= x1:
            return True
        elif y1 <= x1:
            return True
        else:
            return False
    elif y1 >= x0:
        if y1 <= x1:
            return True
        elif y0 <= x1:
            return True  
        else:
            return False
    else:
        return False

print(get_bool()) 


