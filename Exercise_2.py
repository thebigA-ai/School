def morse_file_translator(file_name):
    try:
        f = open(file_name, 'r')
        morse = f.read()
        english = ""
        words = []
        max_letter = ""
        max_value = 0
        words = morse.split(" ")

        english_copy = {}
        english_letter_dictionary = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0,
            'G': 0,
            'H': 0,
            'I': 0,
            'J': 0,
            'K': 0,
            'L': 0,
            'M': 0,
            'N': 0,
            'O': 0,
            'P': 0,
            'Q': 0,
            'R': 0,
            'S': 0,
            'T': 0,
            'U': 0,
            'V': 0,
            'W': 0,
            'X': 0,
            'Y': 0,
            'Z': 0,
            " ": 0
        }
        morse_dictionary = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            "/": " "
        }

        for i in words:
            translation = morse_dictionary.get(i, "!")
            english += translation
            english_letter_dictionary[translation] += 1

        print(english)
        f.close()

        while(max(english_letter_dictionary.values()) > 0):
            max_value = max(english_letter_dictionary.values())
            for key, value in english_letter_dictionary.items():
                if (value == max_value):
                    max_letter += key
                    english_letter_dictionary.update({key: 0})
            print(f'{max_letter}: {max_value}')
            max_letter = ""

    except FileNotFoundError:
        print("error in file name")





morse_file_translator("morse.txt")