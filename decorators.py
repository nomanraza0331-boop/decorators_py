def decorator(admission):
    def wrapper():
        print("Welcome to Pune University")
        admission()
        print("Your admissions is confirmed!")
    return wrapper

@decorator
def eng_admission():
    print("FE admission")
eng_admission()

@decorator
def fybsc_admission():
    print("FY BSC Admission")

fybsc_admission()