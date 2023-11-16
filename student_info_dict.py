student_info=[{"Name":"madhav","roll no":65,"major":'AI'},
              {"Name":"madhav2","roll no":66,'major':"AI"},
              {"Name":"bro2","roll no":467,'major':"CSE"},
              {"Name":"bro3","roll no":68,'major':"CSE"},
              {"Name":"bro","roll no":69,'major':"AI"}]

roll=int(input("Enter roll no"))
for student in student_info:
    if student["roll no"]==roll:
        print(student)
        break
else:
    print("Sorry your information could not be found")
    print("Please enter your information")
    dic = {'name':'none','roll no':roll,'major':'none'}
    dic['name'] = input("Enter your Name: ")
    dic['roll no'] = roll
    dic['major'] = input("Enter your Major: ")
    print("Your information is saved successfully")
    student_info.append(dic)
    print(student_info)
