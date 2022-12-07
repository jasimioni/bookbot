def count_by_word(text):
    cnt_by_word = {}
    for word in text.lower().split():
        if not word in cnt_by_word:
            cnt_by_word[word] = 1
        else:
            cnt_by_word[word] += 1
    return cnt_by_word

def count_by_char(text):
    cnt_by_char = {}
    for char in text.lower():
        if not char in cnt_by_char:
            cnt_by_char[char] = 1
        else:
            cnt_by_char[char] += 1
    return cnt_by_char

def read_file(file):
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()
    return file_contents   

text = read_file('books/frankenstein.txt')
cnt_by_char = count_by_char(text)

print(f'We have {len(text.split())} words')
for char in sorted(cnt_by_char.items(), key=lambda x:x[1], reverse=True):
    if char[0].isalpha():
        print(f'{char[0]} appears {char[1]} times')






