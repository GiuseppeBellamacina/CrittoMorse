import random

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 'è': '...-..-', 'à': '.--.-', 'é': '..-..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', '*': '-..--',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

signs = ['.', '-', '*', '/', '+', '!', '?', '&', ':', ';', '=', '_', '"', '$', '@']

def text_to_morse(text):
    morse = ''
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + ' '
        elif char in morse_code:
            morse += morse_code[char] + ' '
        else:
            morse += char + ' '
    return morse.strip()

def morse_to_text(morse):
    text = ''
    morse_words = morse.split(' / ')
    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        for morse_char in morse_chars:
            for key, value in morse_code.items():
                if value == morse_char:
                    text += key
                    break
            else:
                text += morse_char
        text += ' '
    return text.strip()

def morse_to_code(morse):
    code = ''
    for morse_char in morse:
        if morse_char == '.':
            code += '0'
        elif morse_char == '-':
            code += str(random.randint(1, 9))
        else:
            code += morse_char
    return code

def code_to_morse(code):
    morse = ''
    for code_char in code:
        if code_char == '0':
            morse += '.'
        elif code_char in '123456789':
            morse += '-'
        else:
            morse += code_char
    return morse

def inv(string):
    return string[::-1]

def old_encrypt(text):
    return inv(morse_to_code(text_to_morse(text)))

def old_decrypt(code):
    return morse_to_text(code_to_morse(inv(code)))

def keygen(text):
    key = ''
    count = 0
    for char in text:
        if char.isalnum():
            count += 1
        else:
            key += str(count)
            if char == ' ':
                key += chr(random.randint(ord('a'), ord('z')))
            else:
                key += random.choice(signs)
            count = 0
    return key + str(count)

def clear(text):
    return ''.join([char for char in text if char.isalnum()])    

def encrypt2(text):
    encrypted = old_encrypt(text)
    key = keygen(encrypted)
    return clear(encrypted), key

def decrypt2(encrypted, key):
    to_decrypt = ''
    for k in key:
        if k in '0123456789':
            to_decrypt += encrypted[:int(k)]
            encrypted = encrypted[int(k):]
        elif k in signs:
            to_decrypt += '/'
        else:
            to_decrypt += ' '
    return old_decrypt(to_decrypt)

def encrypt_file(file_path, encrypted_file_path):
    key_file_path = encrypted_file_path.split('.')[0] + '.key'
    with open(file_path, 'r', encoding='utf-8') as file:
        total = len(file.readlines())
        count = 0
        file.seek(0)
        for line in file:
            text = line
            encrypted, key = encrypt2(text)
            with open(encrypted_file_path, 'a', encoding='utf-8') as encrypted_file:
                encrypted_file.write(encrypted + '\n')
            with open(key_file_path, 'a', encoding='utf-8') as key_file:
                key_file.write(key + '\n')
            count += 1
            if count % 100 == 0:
                print(f'{count}/{total} lines encrypted')

def decrypt_file(encrypted_file_path, key_file_path, decrypted_file_path):
    total = 0
    count = 0
    with open(encrypted_file_path, 'r', encoding='utf-8') as encrypted_file:
        encrypted_lines = encrypted_file.readlines()
        total = len(encrypted_lines)
    with open(key_file_path, 'r', encoding='utf-8') as key_file:
        key_lines = key_file.readlines()
    for i in range(len(encrypted_lines)):
        encrypted = encrypted_lines[i].strip()
        key = key_lines[i].strip()
        decrypted = decrypt2(encrypted, key)
        with open(decrypted_file_path, 'a', encoding='utf-8') as decrypted_file:
            decrypted_file.write(decrypted + '\n')
        count += 1
        if count % 100 == 0:
            print(f'{count}/{total} lines decrypted')

def main():
    file = 'test.txt'
    encrypted_file = 'test_encrypted.txt'
    key_file = 'test_encrypted.key'
    decrypted_file = 'test_decrypted.txt'
    encrypt_file(file, encrypted_file)
    decrypt_file(encrypted_file, key_file, decrypted_file)
    
if __name__ == '__main__':
    main()