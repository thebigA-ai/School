def serialize(file_name):
    f = open(file_name, 'r')
    ascii = f.read()
    f.close()
    print(ascii)
    lines = ascii.splitlines()
    current_letter = ""
    count = 0
    serialize_txt = ""

    for line in lines:
        for char in line:
            if char == current_letter:
                count += 1
            else:
                if count > 0:
                    serialize_txt += str(count) + current_letter
                current_letter = char
                count = 1
        serialize_txt += str(count) + current_letter
        current_letter = ""
        count = 0
        serialize_txt += "\n"
    print(serialize_txt)

    f = open("serialize.txt", 'w')
    f.write(serialize_txt)
    f.close()


def deserialize(file_name):
    f = open(file_name, 'r')
    ser_ascii = f.read()
    f.close()
    lines = ser_ascii.splitlines()
    deserialize_txt = ""
    count = ""
    deserialize_txt = ""
    for line in lines:
        for i in line:
            if (ord(i) >= 48 and ord(i) <= 57):
                count += i
            else:
                deserialize_txt += int(count) * i
                count = ""
        deserialize_txt += "\n"
    print(deserialize_txt)

    f = open("deserialize.txt", 'w')
    f.write(deserialize_txt)
    f.close()


def rotation_270(text):
    lines = text.splitlines()
    rotated_txt = ""

    while (lines[0] != ""):
        for i in range(len(lines)):
            line = lines[i]
            rotated_txt += line[-1]
            lines[i] = line[:-1]
        rotated_txt += "\n"

    return rotated_txt


def rotation_0(text):
    return text


def rotation_90(text):
    text = rotation_270(rotation_270(rotation_270(text)))
    return text


def rotation_180(text):
    text = rotation_270(rotation_270(text))

    return text


def rotation_360(text):
    lines = text.splitlines()
    flipped_text = ""

    for line in lines:
        flipped_text += line[::-1] + "\n"

    return flipped_text


def rotation(file_name, degrees):
    f = open(file_name, 'r')
    text = f.read()
    f.close()

    if degrees == "0":
        text = rotation_0(text)
    elif degrees == "90":
        text = rotation_90(text)
    elif degrees == "180":
        text = rotation_180(text)
    elif degrees == "270":
        text = rotation_270(text)
    elif degrees == "360":
        text = rotation_360(text)

    f = open(file_name, 'w')
    f.write(text)
    f.close()


def conversion(file_name, key):
    f = open(file_name, 'r')
    text = f.read()
    f.close()
    converted_text = ""
    conversion_dict = {
        "(": "^",
        "^": "$",
        "$": ";",
        ";": "!",
        "*": "|",
        "|": "o",
        "\n": "\n"
    }

    for i in range(key):
        for char in text:
            converted_text += conversion_dict.get(char, "X")

    f = open(file_name, 'w')
    f.write(converted_text)
    f.close()


try:
    request = ""
    while (request not in ["serialize", "deserialize"]):
        request = input("what action do yo want to do? (serialize/deserialize) ")
    file_name = input("what is the file name? ")
    twisting = input("do you want to rotate the file? (yes/no)")
    if (twisting in ["yes", "YES", "Yes"]):
        degrees = input("how many degrees do you want to rotate the file? (0/90/180/270/360) ")
        if degrees in ["0", "90", "180", "270", "360"]:
            rotation(file_name, degrees)

    conversion = input("do you want to convert the file? (yes/no)")
    if (conversion in ["yes", "YES", "Yes"]):
        key = input("what is the convertion key? (0/1/2) ")
        if key in ["0", "1", "2"]:
            conversion(file_name, key)

except FileNotFoundError:
    print("error in file name")
