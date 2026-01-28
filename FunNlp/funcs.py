def pad_sequence(sentence_list, pad_token):
    #find longest list
    list_len = [len(i) for i in sentence_list]
    longest_list = max(list_len)
    #print(f"longest: {longest_list}")
    new_sentence_list = []

    for i, sentence in enumerate(sentence_list):
        tokensToAdd = longest_list - len(sentence)
        for j in range(tokensToAdd):
            sentence.append(pad_token)
        new_sentence_list.append(sentence)
    return new_sentence_list