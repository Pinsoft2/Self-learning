<<<<<<< HEAD
#Q1
filenames = ['document', 'report', 'presentation']

for i,j in enumerate(filenames):
    print(f"{i}-{j.capitalize()}.txt")

#Q2

ips = ['100.122.133.105', '100.122.133.111']
index=input("Enter the index of the IP you want: ")
=======
#Q1
filenames = ['document', 'report', 'presentation']

for i,j in enumerate(filenames):
    print(f"{i}-{j.capitalize()}.txt")

#Q2

ips = ['100.122.133.105', '100.122.133.111']
index=input("Enter the index of the IP you want: ")
>>>>>>> 6e4bf84439071a9e5da8dfa05fa0d27d65a1666a
print(f"You chose {ips[int(index)]}")