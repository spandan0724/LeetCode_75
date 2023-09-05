def merge_two_words(word1, word2):
    len1, len2 = len(word1), len(word2)
    merged = []
    i, j = 0, 0
    while i<len1 and j<len2:
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    return ''.join(merged)

merge_two_words(word1 = "hello", word2 = "pelloqoutehbjnxhhkd")    


