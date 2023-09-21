def morse_file_translator(file_name):
    try:
        f = open(file_name, 'r')
        morse = f.read()
        english = ""
        words = []

        words = morse.split(" ")
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
            "/": " ",  # Space between words
        }

        for i in words:
            english += morse_dictionary.get(i, "!")

        for i in english:
            if(i=="!"):
                print("Error in Morse Code")
                break
        else:
            print()
        f.close()

    except FileNotFoundError:
        print("error in file name")

