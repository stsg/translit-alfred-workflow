#!/usr/local/bin/python3
# encoding: utf-8

import os
import sys
import subprocess

cyrillic_translit = {
    # cyrillic
    'q': 'я',
    'w': 'ш',
    'e': 'е',
    'r': 'р',
    't': 'т',
    'y': 'ы',
    'u': 'у',
    'i': 'и',
    'o': 'о',
    'p': 'п',
    '[': 'ю',
    ']': 'ж',
    'a': 'а',
    's': 'с',
    'd': 'д',
    'f': 'ф',
    'g': 'г',
    'h': 'ч',
    'j': 'й',
    'k': 'к',
    'l': 'л',
    '\\': 'э',
    '`': 'щ',
    'z': 'з',
    'x': 'х',
    'c': 'ц',
    'v': 'в',
    'b': 'б',
    'n': 'н',
    'm': 'м',
    '-': 'ь',
    '=': 'ъ',
    'Q': 'Я',
    'W': 'Ш',
    'E': 'Е',
    'R': 'Р',
    'T': 'Т',
    'Y': 'Ы',
    'U': 'У',
    'I': 'И',
    'O': 'О',
    'P': 'П',
    '{': 'Ю',
    '}': 'Ж',
    'A': 'А',
    'S': 'С',
    'D': 'Д',
    'F': 'Ф',
    'G': 'Г',
    'H': 'Ч',
    'J': 'Й',
    'K': 'К',
    'L': 'Л',
    '"': 'Э',
    '~': 'Щ',
    'Z': 'З',
    'X': 'Х',
    'C': 'Ц',
    'V': 'В',
    'B': 'Б',
    'N': 'Н',
    'M': 'М',
    '_': 'Ь',
    '+': 'Ъ',
    # latin
    'я': 'q',
    'ш': 'w',
    'е': 'e',
    'р': 'r',
    'т': 't',
    'ы': 'y',
    'у': 'u',
    'и': 'i',
    'о': 'o',
    'п': 'p',
    'ю': '[',
    'ж': ']',
    'а': 'a',
    'с': 's',
    'д': 'd',
    'ф': 'f',
    'г': 'g',
    'ч': 'h',
    'й': 'j',
    'к': 'k',
    'л': 'l',
    'э': '\\',
    'щ': '`',
    'з': 'z',
    'х': 'x',
    'ц': 'c',
    'в': 'v',
    'б': 'b',
    'н': 'n',
    'м': 'm',
    'ь': '-',
    'ъ': '=',
    'Я': 'Q',
    'Ш': 'W',
    'Е': 'E',
    'Р': 'R',
    'Т': 'T',
    'Ы': 'Y',
    'У': 'U',
    'И': 'I',
    'О': 'O',
    'П': 'P',
    'Ю': '{',
    'Ж': '}',
    'А': 'A',
    'С': 'S',
    'Д': 'D',
    'Ф': 'F',
    'Г': 'G',
    'Ч': 'H',
    'Й': 'J',
    'К': 'K',
    'Л': 'L',
    'Э': '"',
    'Щ': '~',
    'З': 'Z',
    'Х': 'X',
    'Ц': 'C',
    'В': 'V',
    'Б': 'B',
    'Н': 'N',
    'М': 'M',
    'Ь': '_',
    'Ъ': '+'
}

ru_kl = 'com.apple.keylayout.Russian-Phonetic'
en_kl = 'com.apple.keylayout.US'

issw = os.environ['HOME'] + '/bin/issw'

def translit(line):
    converted_line = ''
    for char in line:
        transchar = ''
        if char in cyrillic_translit:
            transchar = cyrillic_translit[char]
        else:
            transchar = char
        converted_line += transchar
    return converted_line

def toggle_is():
    cu_kl = subprocess.check_output([issw], universal_newlines=True).strip()

    if cu_kl == en_kl:
        subprocess.check_output([issw, ru_kl])
    else:
        subprocess.check_output([issw, en_kl])

def main():
    query = sys.argv[1]
    toggle_is()
    result = translit(query)
    sys.stdout.write(result)


if __name__ == '__main__':
    main()
