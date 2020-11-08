list = []
index = 0
def MeNeed2Return(list):
    lits = list.copy()
    index1 = 0
    while index1 < len(lits):
        number1 = lits[index1]
        if number1 in lits:
            lits.remove(number1)
            if not number1 in lits:
                lits.insert(index1, number1)
        index1 += 1
    return lits
print(MeNeed2Return(list))
