import docx
file = input("file name") #path of word file that wants to be changed
word1 = input("what word you want to replace") #Word that wants to be replaced 
word2 = input("replacing word") #word that you want to replace with
def replace_word(file,word1,word2): #function that performs word swap
    doc = docx.Document(file) #loads the file
    for p in doc.paragraphs: #Searches through all the paragraphs and swaps the chosen words
        if word1 in p.text:
            text = p.text.replace(word1,word2)
            p.text = text

    doc.save(file) #Saves the file
replace_word(file,word1,word2)