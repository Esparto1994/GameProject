import re
text = open('wiki.txt', encoding='utf-8-sig')
text = text.read()
text = re.sub('  ',' ',text)
text = re.sub('\\n\\n',' ',text)
#print(set(text))
sentences = re.split(' *[\.\?!][\'"\)\]]* *', text) #CLASS2
row_tok_sents = []
tok_sents = [] #CLASS3
let_dict = {'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'jo',
            'ж': 'zh',
            'з': 'z',
            'и': 'i',
            'й': 'i',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'kh',
            'ц': 'c',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ъ': '″',
            'ы': 'y',
            'ь': '′',
            'э': 'e',
            'ю': 'ju',
            'я': 'ya'}

for sent in sentences:
    row_tok_sents.append(sent.split())
for toksent in row_tok_sents:
    i = 1
    inxtoksent = []
    for word in toksent:
        transword = ''
        for letter in word:
            if letter.lower() in let_dict:
                transword += let_dict[letter.lower()]
            else:
                transword += letter
        inxtoksent.append([i, word, transword])
        i += 1
    tok_sents.append(inxtoksent) #CLASS3
t = 0
for q in tok_sents:
    if t < 100:
        print(q)
        t += len(q)
    else:
        break






