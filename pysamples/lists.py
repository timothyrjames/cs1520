
names = ["Kanye", "Eminem", "Jay-Z"]
print(names)

my_list = list()
my_list.append(5)
my_list.append(3.2)
my_list.append(True)
my_list.append('something')

print(my_list)              # lists can contain mixtures of types

num_list = []               # this is more common than list()

for i in range(10):
  num_list.append(i * 100)

print(num_list)
print(num_list[3:5])        # just like strings, slices can be used
print(num_list[3:])
print(num_list[:3])
print(num_list[-2:])
print(num_list[:-2])

