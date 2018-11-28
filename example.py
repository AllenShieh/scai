import commands
import random

def read_triple(triple_file):
	triples = []
	with open(triple_file, 'r') as file:
		file.readline()
		for line in file.readlines():
			line = line.strip('\n').split('\t')
			triples.append(line)
	return triples

def read_mapping(mapping_file):
	mapping = {}
	with open(mapping_file, 'r') as file:
		file.readline()
		for line in file.readlines():
			line = line.strip('\n').split('\t')
			mapping[line[1]] = line[0]
	return mapping

def get_label(name):
	query = 'wd s {}'.format(name)
	query_result = commands.getstatusoutput(query)
	return query_result[1].split('\n')[1][6:].replace(' ', '_')

def main():
	entity = read_mapping('entity2id.txt')
	relation = read_mapping('relation2id.txt')
	triples = read_triple('triple2id.txt')
	result = []
	for i in xrange(10):
		triple = triples[i]
		head = get_label(entity[triple[0]])
		r = get_label(relation[triple[1]])
		tail = get_label(entity[triple[2]])
		result.append([head, r, tail])
	print result

if __name__ == '__main__':
	main()