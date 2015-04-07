sto = {
    'google': 123,
    'fb': 188,
    'ti': 259,
    'yahoo': 99
}

print(
    min(
        zip(
            sto.values(),
            sto.keys()
        )
    )
)

print(
    sorted(
        zip(
            sto.values(),
            sto.keys()
        )
    )
)