def decode(message_file):
    with open(message_file, 'r') as file:
        content = file.readlines()

    num_word_map = {}

    for line in content:
        num, word = line.strip().split(" ")
        num = int(num)
        num_word_map[num] = word

    temp = 1
    current = 1
    decoded_message = ""

    for _ in range(len(num_word_map)):
        if current in num_word_map:
            decoded_message += num_word_map[current] + " "
        temp += 1
        current += temp

    return decoded_message.strip()

file_content = decode("coding_qual_input.txt")
print(file_content)
