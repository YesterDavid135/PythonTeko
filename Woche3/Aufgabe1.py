expressions = [
    "17 / 5",
    "17 // 5",
    "-17 // 5",
    "17 % 5",
    "2 ** 10",
    "6 / 3",
    '"3" * 3',
    '"5" + "3"',
    "int(3.9)",
    "round(2.5)",
    'float("2.5") + 1',
    "10 > 3 > 1",
    'bool("")',
    'int("7") + 0.5',
]

for expr in expressions:
    result = eval(expr)
    print(f"{expr:<18} => {repr(result):<8} ({type(result).__name__})")

round(2.5)