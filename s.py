f1 = open("E:/s.txt", "a")
for i in range(1, 6):
    Rno = int(input("Enter Your Roll Number: "))
    Name = input("Enter Your Name: ")
    Mark = int(input("Enter Your Mark: "))
    if(Mark <= 45):
        Status = "FAIL"
    else:
        Status = "PASS"
    print("Status:", Status)
    f1.write(str(Rno) + " " + Name + " " + str(Mark) + " " + Status + "\n")
f1.close()
