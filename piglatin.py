def pyg_latin():
    pyg = 'ay'

    original = raw_input('Enter a word: ')

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = (word + first + pyg)
        final_word = new_word[1:len(new_word)]
        print final_word
    else:
        print 'empty'
