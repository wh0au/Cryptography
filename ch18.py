def count_repetitions(ciphertext, block_size, counter):

	chunks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]

	number_of_repetitions = len(chunks) - len(set(chunks))

	result = {
		'ciphertext': ciphertext,
		'repetitions': number_of_repetitions,
		'line': counter
	}

	return result;

ciphertext = [bytes.fromhex(line.strip()) for line in open('ch18txt.txt')]

block_size = 16

repetitions = []

line = 1

for cipher in ciphertext:

	repetitions.append(count_repetitions(cipher, block_size, line))

	line += 1


most_repetitions = sorted(repetitions, key=lambda x: x['repetitions'], reverse = True)[0]

print("ciphertext: {}".format(most_repetitions['ciphertext']))
print("Repeating Blocks: {}".format(most_repetitions['repetitions']))
print("Line: {}".format(most_repetitions['line']))