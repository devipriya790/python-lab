f1 = open("E://s.txt", "r")

print("-" * 50)
print("{:<10} {:<15} {:<10} {:<10}".format("Roll No", "Name", "Mark", "Status"))
print("-" * 50)

for rec in f1:
    data = rec.strip().split()

    Rno = data[0]
    Name = data[1]
    Mark = data[2]
    Status = data[3]

    print("{:<10} {:<15} {:<10} {:<10}".format(Rno, Name, Mark, Status))

print("-" * 50)

f1.close()
