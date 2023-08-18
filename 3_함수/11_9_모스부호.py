morse_dict = {
 ".-": "A", "-...": "B", "-.-.": "C",
 "-..": "D", ".": "E", "..-.": "F",
 "--.": "G", "....": "H", "..": "I",
 ".---": "J", "-.-": "K", ".-..": "L",
 "--": "M", "-.": "N", "---": "O",
 ".--.": "P", "--.-": "Q", ".-.": "R",
 "...": "S", "-": "T", "..-": "U",
 "...-": "V",  ".--": "W", "-..-": "X",
 "-.--": "Y", "--..": "Z", " ": "",
}
english_dict = {
 "A": ".-", "B": "-...", "C": "-.-.",
 "D": "-..", "E": ".", "F": "..-.",
 "G": "--.", "H": "....", "I": "..",
 "J": ".---", "K": "-.-", "L": ".-..",
 "M": "--", "N": "-.", "O": "---",
 "P": ".--.", "Q": "--.-", "R": ".-.",
 "S": "...", "T": "-", "U": "..-",
 "V": "...-", "W": ".--", "X": "-..-",
 "Y": "-.--", "Z": "--.."," ": ""
}

def morse_to_english(morse_text):
    english_text = ""
    morse_words = morse_text.strip().split(" ")
    for morse_word in morse_words:
        morse_chars = morse_word.split(" ")

        for morse_char in morse_chars:
            if morse_char in morse_dict:
                english_text += morse_dict[morse_char]
            else: #ignore characters that are not in the dictionary
                pass
        english_text += " "
    return english_text

def english_to_morse(english_text):
    morse_text = ""
    for char in english_text:
        if char.upper() in english_dict:
            morse_text += english_dict[char.upper()] + " "
        else:
            # ignore characters that are not in the dictionary
            pass
    return morse_text

morse_text = english_to_morse("i am so tired")
print(morse_text)
english_text = morse_to_english(".--. .-.. . .- ... .   -.. --- -. -  --. ---  ..-. .- ... -")
print(morse_to_english(morse_text))
print(english_text)
