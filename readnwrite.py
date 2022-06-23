txt = "this is the text inside the file\nby Yeison Parra"

file = open('exercises/modulesexe/txtreadnwrite.txt', 'w')
file.write(txt)
file.close()

read_file =open('exercises/modulesexe/txtreadnwrite.txt', 'r')
data = read_file.read()
read_file.close()
print (data)