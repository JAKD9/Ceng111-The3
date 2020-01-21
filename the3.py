def is_Okey(Corpus, input_list, length):
    #function to control the placemnet is correct.
    control = [element[:length] for element in Corpus]
    column = 0
    string = "" 
    column_list = []
    while column < len(Corpus[0]):
        string = ""
        for element in input_list:
            string += element[column]
        column +=1
        column_list.append(string)
    #print("CONTROL LIST")
    #print(control)
    #print("COLUMN LIST")
    #print(column_list)
    for element in column_list:
        if element in control:
            continue
        else:
            return False
    return True

def backtrack_function(Corpus, control_list, answer_list, length):
    #function that will recursively backtrack.
    index = 0
    
    while index < len(control_list):
        answer_list.append(control_list[index])
        #print("ANSWER LIST")
        #print(answer_list)
        if length + 1 == len(Corpus[0]) and is_Okey(Corpus, answer_list, length+1):
            return True
        elif is_Okey(Corpus, answer_list, length+1):
            if backtrack_function(Corpus, control_list[:index] + control_list[index+1:], answer_list, length+1):
                return True
            else:
                answer_list.pop()
                index += 1
        else:
            answer_list.pop()
            index += 1
    return False


def place_words(Corpus):
    #main function.
    Corpus = [x.upper() for x in Corpus]
    #print("INPUT")
    #print(Corpus)
    answer_list = []
    control_list = Corpus[:]
    length = 0
    if backtrack_function(Corpus, control_list, answer_list, length):
        return answer_list
    else: 
        return False


