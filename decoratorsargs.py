def decArgs(admission):
    def wrapper(*args,**kwargs):
        print("University of Pune")
        print(f"This is {len(args)}")
        print(f"This is keyword Args {len(kwargs)}")
        admission(*args,**kwargs)
        print("Thank you!")
    return wrapper
'''
@decArgs
def FE_admission(sname,marks,round):  
    print(f"The student name={sname}")
    print(f"Total CET marks={marks} ")
    print(f"This is {round}nd round")

FE_admission("Kaif",220,round=2)
'''

@decArgs
def MCA_admissions(merit_no,college_assigned,category,marks):
    print(f"The MErti No ={merit_no}")
    print(f"College = {college_assigned}")
    print(f"Category={category}")
    print(f"Total Marks={sum(marks)}")

MCA_admissions(1001,"SES COE",marks=[75,85,49],category="General")



