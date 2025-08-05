import time
cipher = {
    '@': 'a', ')': 'b', 'x': 'c', 'b': 'd', '(': 'e', 'v': 'f',
    'z': 'g', '#': 'h', '^': 'i', '<': 'j', '-': 'k', '_': 'l',
    '%': 'm', '>': 'n', '&': 'o', 'f': 'p', 'Q': 'q', '*': 'r',
    '$': 's', ' ': 't', '/': 'u', 'u': 'v', 't': '~', '?': 'x',
    'd': 'y', 'k': 'z', '=': ' ', '+': '?', 'h': '!', ',': ',',
    '.': '.','j': '_'
}

while True:
    lines = []
    print("Enter CIPHER here \n (Type 'END'  in a new line after typing or pasting the text to reveal the output): ")
    while True:
        line = input()
        if line.upper().strip() == 'END':
            message='\n'.join(lines)
            break
        lines.append(line)
    confirm = input(f"\n Is this correct? (y(yes)/n(no)): ").lower().strip()
    if confirm == 'y':
        pass
        break
    elif confirm == 'n':
        print("\nAlright, try again.\n")
    else:
        print("Please type 'y' or 'n'.")

for box in "███████████████████████████████████████████████████████████████████🎉" :
    print(box, end='', flush=True)
    time.sleep(0.02)

print("\n")

for box in ''.join(cipher.get(c, c) for c in message):
    print(box, end='', flush=True)
    time.sleep(0.09)
