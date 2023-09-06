with open(r'/home/bhavik/wordy/words/allowed/all_allowed.txt') as file:
    words = file.readlines()

words = [line.replace('\n','') for line in words]

for word in words:
    if len(word) == 4:
        with open(r'/home/bhavik/wordy/words/allowed/allowed_four_letter.txt', 'a') as file:
            file.write(word+'\n')
    elif len(word) == 6:
        with open(r'/home/bhavik/wordy/words/allowed/allowed_six_letter.txt', 'a') as file:
            file.write(word+'\n')
    elif len(word) == 7:
        with open(r'/home/bhavik/wordy/words/allowed/allowed_seven_letter.txt', 'a') as file:
            file.write(word+'\n')
    elif len(word) == 8:
        with open(r'/home/bhavik/wordy/words/allowed/allowed_eight_letter.txt', 'a') as file:
            file.write(word+'\n')

