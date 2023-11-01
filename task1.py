import re


def find_smiles(input_string):
    return len(re.findall("X-{I", input_string))
 


# Тесты
assert find_smiles("none") == 0
assert find_smiles("X-{I") == 1
assert find_smiles("X-{IX-{IX-{IX-{I") == 4
assert find_smiles("Hey, my name is X-{I") == 1
assert find_smiles("X wow - w0w { wow I") == 0

# print(find_smiles("none"))
# print(find_smiles("X-{I"))
# print(find_smiles("X-{IX-{IX-{IX-{I"))
# print(find_smiles("Hey, my name is X-{I"))
# print(find_smiles("X wow - wow ) wow"))



# Генератор смайлика
smile_variants = [{
        0: ":",
        1: ";",
        2: "X",
        3: "8",
        4: "="
    }, {
        0: "-",
        1: "<",
        2: "-{",
        3: "<{"
    }, {
        0: "(",
        1: ")",
        2: "O",
        3: "I",
        4: "\\",
        5: "/",
        6: "P",
 }]


var = 223

print(*[smile_variants[idx][int(symb)] for idx, symb in enumerate(str(var))], sep="")