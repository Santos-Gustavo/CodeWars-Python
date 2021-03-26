''''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
''''

def pig_it(text):
    text = text.split()
    ftext=''
    points=['.','!','?',';',',']
    if text[-1] in points:
        for word in text:
            ftext += ' '+word[1:]+word[0:1]+'ay'
        return ftext[1:-2]
    else:
        for word in text:
            ftext += ' '+word[1:]+word[0:1]+'ay'
        return ftext[1:]
