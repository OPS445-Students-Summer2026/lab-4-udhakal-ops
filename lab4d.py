def middle_number(num):
    text = str(num)

    if len(text) % 2 == 0:
        middle = len(text) // 2
        return text[middle - 1:middle + 1]
    else:
        middle = len(text) // 2
        return text[middle:middle + 2]
