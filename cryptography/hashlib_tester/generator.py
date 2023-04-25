import random
import string

lengths = [1, 10, 100, 1000, 10000]

for length in lengths:
    generated_strings = set()
    while len(generated_strings) < 2000:
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
        if random_string not in generated_strings:
            generated_strings.add(random_string)

    with open(f'{length}_char_strings.txt', 'w') as f:
        for string in generated_strings:
            f.write(f'{string}\n')
