import re


def fill_in_0(number):
    result = str(number)
    if len(result) == 1:
        result = '0000000' + result
    if len(result) == 2:
        result = '000000' + result
    if len(result) == 3:
        result = '00000' + result
    if len(result) == 4:
        result = '0000' + result
    if len(result) == 5:
        result = '000' + result
    if len(result) == 6:
        result = '00' + result
    if len(result) == 7:
        result = '0' + result
    return result


def serialNumber(number):
    result = str(number)
    reFilter = re.compile(r'[^0-9]')
    list = reFilter.findall(result)
    # print(list)
    if list:
        assert not list, 'invalid serial number'
    else:
        result = fill_in_0(result)
        return result


print(serialNumber(834783))
print(serialNumber('47839'))
print(serialNumber(834783244839184))


# print(serialNumber('4783926132432*'))


def solid(number):
    string = str(number)
    tf = True
    r = []
    for i in range(len(string)):
        r.append(string[i])
    for i in range(0, len(r)):
        if r[0] != r[i]:
            tf = False
    return tf

print("====================================solid====================================")
print(solid(44444444))
print(solid('44544444'))


def radar(number):
    string = fill_in_0(number)
    forward = string[0:4]
    backward = string[4:]
    backward = ''.join(reversed(backward))
    if forward == backward:
        return True
    else:
        return False

print("====================================radar====================================")
print(radar(1133110))
print(radar('83289439'))


def repeater(number):
    string = fill_in_0(number)
    forward = string[0:4]
    backward = string[4:]
    if forward == backward:
        return True
    else:
        return False

print("================================repeater================================")
print(repeater(20012001))
print(repeater('83289439'))



def radarRepeater(number):
    string = fill_in_0(number)
    forward = string[0:4]
    backward = string[4:]
    if forward == backward:
        return True
    else:
        return False

print("================================radarrepeater================================")
print(radarRepeater('12211221'))
print(radarRepeater('83289439'))


def numismatist(list, kind=None):
    if kind is None:
        result = []
        for digits in list:
            tf = solid(digits)
            if tf is True:
                result.append(digits)
    elif kind == radar:
        result = []
        for digits in list:
            tf = radar(digits)
            tf2 = solid(digits)
            if tf is True and tf2 is False:
                result.append(digits)
    elif kind == repeater:
        result = []
        for digits in list:
            tf = repeater(digits)
            tf2 = solid(digits)
            if tf is True and tf2 is False:
                result.append(digits)
    return result

print("================================numismatist================================")
print(numismatist([33333333, 1133110, '77777777', '12211221']))
print(numismatist([33333333, 1133110, '77777777', '12211221'], radar))
print(numismatist([33333333, 1133110, '77777777', '12211221'], kind=repeater))
