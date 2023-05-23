
#####TASK1######

# def calculateBmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi
#
# def assignDiagnosis(bmi):
#     if bmi < 16.00:
#         return "Starvation"
#     elif bmi < 16.99:
#         return "Emaciation"
#     elif bmi < 18.49:
#         return "Underweight"
#     elif bmi < 24.99:
#         return "Correct weight"
#     elif bmi < 29.99:
#         return "Overweight"
#     elif bmi < 34.99:
#         return "First degree obesity"
#     elif bmi < 39.99:
#         return "Second degree obesity (clinical)"
#     else:
#         return "Third degree obesity (extreme)"
#
# height = float(input("Enter height: "))
# weight = float(input("Enter weight: "))
#
# bmi = calculateBmi(weight, height)
#
# diagnosis = assignDiagnosis(bmi)
#
# print("BMI:", bmi)
# print("Diagnosis:", diagnosis)


####TASK2#####

def exponent(base,exponent):
    result = 1
    for i in range(exponent):
        result*=base
    return result

base = int(input("base"))
exponent = int(input("exponent"))

print("result:",exponent(base,exponent))

