def likes(names: list) -> str:
    if names:
        length = len(names)
        if length == 1:
            return f"{names[0]} likes this"
        elif length == 2:
            return f"{names[0]} and {names[1]} like this"
        elif length == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        elif length >= 4:
            return f"{names[0]}, {names[1]} and {length-2} others like this"
        else:
            pass
    else:
        return "no one likes this"
