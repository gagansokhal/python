def duplicate_encode(word):
    word =word.lower()
    new_lst=["(" if word.count(char)==1 else ")" for char in word ]
    return  "".join(new_lst)   
