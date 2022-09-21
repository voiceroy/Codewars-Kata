import re


def domain_name(url: str) -> str:
    exp = re.compile(r"(^(http|https):\/\/)?(www.)?([\w\S][^./]*)")
    match = exp.search(url)
    return match
