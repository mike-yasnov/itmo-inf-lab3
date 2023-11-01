import re


def encode(text):
    nums = re.findall(r"\b\d+\b", text)
    nums_new = [str(3 * int(x) **2 + 5) for x in nums]

    for (n1, n2) in zip(nums, nums_new):
        text = text.replace(n1, n2)
    return text


assert encode('41 + 22 = 10') == '5048 + 1457 = 305'
assert encode('1 + 2 = 3') == '8 + 17 = 32'
assert encode('10 + 25 = 35') == '305 + 1880 = 3680'
assert encode('13 + 45 = 58') == '512 + 6080 = 10097'
assert encode('44 - 5 = 39') == '80813 - 80 = 4568'