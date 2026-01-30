student_id = input("Enter student id: ")
email = input("Enter email: ")
password = input("Enter password: ")
referral = input("Enter referral: ")
valid = True
if len(student_id) !=7:
    valid = False
elif( (student_id[0] != "C" ) and (student_id[1] != "S") and (student_id[2] != "E" )):
    valid = False
elif student_id[3]!= "-" :
    valid = False
elif(student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit())  :
    valid = False
elif "@" not in email or "." not in email :
    valid = False
elif email[0]== "@" :
    valid = False
elif not email.endswith(".edu"):
    valid = False

elif len(password) < 8 :
    valid = False
elif not password[0].isupper() :
    valid = False
elif not (password[0].isdigit() or password[1].isdigit() or password[2].isdigit() or password[3].isdigit() or password[4].isdigit() or password[5].isdigit()or password[6].isdigit() or password[7].isdigit()) :
      valid = False
elif len(referral) !=6 :
    valid = False
elif( (referral[0]!= "R" ) and (referral[1] != "E") and (referral[2] != "F" )):
    valid = False
elif(referral[3].isdigit() and referral[4].isdigit()) :
    valid = False
elif referral[5]!="@" :
    valid = False

if valid == True :
    print("APPROVED")
else :
    print("REJECTED")


