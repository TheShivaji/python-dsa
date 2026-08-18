def count_word_frequency(sentence):
    sen = sentence.split(" ")

    frequency = {}
    couter = 0
    for word in sen:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


sentence = "hello world hello"
print(count_word_frequency(sentence))
