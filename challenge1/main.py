def splice(xs: list, start: int, count: int) -> list:
    gap = start + count
    result = []

    if start < 0 or start > len(xs) or gap < 0 or gap > len(xs):
        return result

    for index in range(count):
        result.append(xs[start + index])

    return result
