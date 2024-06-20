<<<<<<< HEAD
# #q1,2
# doc = open("essay.txt",'r')
# content=doc.read()
# print(content.capitalize())
# print(len(content))
# doc.close()

# #q3
# doc2 = open("members.txt",'r')
# originallist = doc2.read()
# doc2.close()
# doc2 = open("members.txt",'w')
# newmember = input("Add a new member: ")
# doc2.write(f"{originallist}{newmember}")
# doc2.close()

#q4
# filenames = ['1.txt','2.txt','3.txt']
# for i in filenames:
#     file = open(i,'w')
#     file.write("Hello")
#     file.close()

#q5
filenames2 = ['a.txt','b.txt','c.txt']
for i in filenames2:
    file = open(i,'r')
    doc = file.read()
    print(doc)
=======
# #q1,2
# doc = open("essay.txt",'r')
# content=doc.read()
# print(content.capitalize())
# print(len(content))
# doc.close()

# #q3
# doc2 = open("members.txt",'r')
# originallist = doc2.read()
# doc2.close()
# doc2 = open("members.txt",'w')
# newmember = input("Add a new member: ")
# doc2.write(f"{originallist}{newmember}")
# doc2.close()

#q4
# filenames = ['1.txt','2.txt','3.txt']
# for i in filenames:
#     file = open(i,'w')
#     file.write("Hello")
#     file.close()

#q5
filenames2 = ['a.txt','b.txt','c.txt']
for i in filenames2:
    file = open(i,'r')
    doc = file.read()
    print(doc)
>>>>>>> 6e4bf84439071a9e5da8dfa05fa0d27d65a1666a
    file.close()