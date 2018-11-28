import commands
entity = []
relation = []
with open ('entity2id.txt', 'r') as file:
  num = file.readline()
  for line in file.readlines():
    line = line.strip('\n')
    line = line.split('\t')
    query = 'wd s {}'.format(line[0])
    output = commands.getstatusoutput(query)
    result = output[1].split('\n')[1][6:].replace(' ', '_')
    entity.append([line[0], line[1], result])

with open ('relation2id.txt', 'r') as file:
  num = file.readline()
  for line in file.readlines():
    line = line.strip('\n')
    line = line.split('\t')
    query = 'wd s {}'.format(line[0])
    output = commands.getstatusoutput(query)
    result = output[1].split('\n')[1][6:].replace(' ', '_')
    relation.append([line[0], line[1], result])

with open('entity_mapping.txt', 'w') as file:
  for line in entity:
    output = '{}\t{}\t{}\n'.format(line[0], line[1], line[2])
    file.write(output)

with open('relation_mapping.txt', 'w') as file:
  for line in relation:
    output = '{}\t{}\t{}\n'.format(line[0], line[1], line[2])
    file.write(output)
#output = commands.getstatusoutput('wd s Q42')
#result = output[1].split('\n')
#print result[0], result[1]
