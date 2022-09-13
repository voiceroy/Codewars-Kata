def delete_nth(order: list, max_e: int) -> list:
    lst = list()
    for x in order:
        lst.append(x)
        if lst.count(x) > max_e:
            lst.pop()
    return lst
