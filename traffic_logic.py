def get_signal(count):
    if count < 5:
        return "GREEN (SHORT)"
    elif count < 15:
        return "GREEN (NORMAL)"
    else:
        return "GREEN (EXTENDED)"
