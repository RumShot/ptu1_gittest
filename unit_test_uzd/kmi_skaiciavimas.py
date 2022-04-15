def kmi(svoris, ugis):
    if svoris <= 20:
        raise ValueError("svoris per mazas")
    if svoris >= 240:
        raise ValueError("svoris per didelis")
    if ugis <= 0.4:
        raise ValueError("ugis per mazas")
    if ugis >= 3.4:
        raise ValueError("ugis per didelis")
    return svoris/ (ugis **2)

# print(kmi(78, 1.82))
# print(kmi(50, 1.56))
# print(kmi(100, 1.90))