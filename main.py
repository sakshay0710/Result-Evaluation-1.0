#--------------------------------------------------------------------------------
# Name:        Akshay Dutt Sharma
# Purpose:     To help others in evaluating Marks:
#              "Result Evaluation Program"
#
# Author:      Akshay Dutt Sharma
#
# Created:     08/02/2022
# Copyright:   (c) Akshay 2022
# Class: 9th B
#--------------------------------------------------------------------------------

#Introduction
print('Welcome to Result Evaluation')
print()
school = input("Enter your School name: ")
print()
print("Nice, You're in : ",school)
print()

#Personal Information
name = (input('Enter your Name : '))
grade = (input('Enter your Grade : '))
section = (input('Enter your Section : '))

#Evalution of Half Yearly Examination
print("Let's Evalute Half Yearly Examination Marks")
print()
maximum_half = int(input('Enter Maximum Marks of Half Yearly Examination Per Subject : '))

#Half Marks Input
english = float(input('Enter your English Marks : '))
hindi = float(input('Enter your Hindi : '))
maths = float(input('Enter your Maths Marks : '))
science = float(input('Enter your Science Marks : '))
sst = float(input('Enter your SST Marks : '))
print()

half_total = maximum_half*5

if maximum_half >= english:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_half)
  exit()

if maximum_half >= hindi:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_half)
  exit()

if maximum_half >= maths:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_half)
  exit()

if maximum_half >= science:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_half)
  exit()

if maximum_half >= sst:
  print()
else:
  print("Try Again! You have entered wrong Marks in SST somewhere is more than", maximum_half)
  exit()


if maximum_half >= english and maximum_half >= hindi and maximum_half >= maths and maximum_half >= science and maximum_half >= sst:
  print('Total Marks of Half Yearly Examination : ' , half_total)

print()
half_earned = english+hindi+maths+science+sst

if half_total >= half_earned:
  print('Total Marks achieved in Half Yearly Examination: ', half_earned)
else:
  print('Input your Marks Again! You have entered total marks more than : ', half_total, '',  '[Total Half Yearly Examination]')
  exit()

#Databse Storage Area
print('Database saved for Half Yearly Examination')
print()
print("Now Let's Evalute Marks of Final Examination")

#Evalution of Final Year Examination
maximum_final = int(input('Enter Maximum Marks of Final Yearl Examination Per Subject : '))

eng = float(input('Enter your English of Final Examination : '))
hind = float(input('Enter your Hindi of Final Examination : '))
math = float(input('Enter your Maths Marks of Final Examination : '))
sci = float(input('Enter your Science Marks of Final Examination : '))
social = float(input('Enter your SST Marks of Final Examination : '))

final_total = maximum_final*5

if maximum_final >= eng:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_final)
  exit()

if maximum_final >= hind:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_final)
  exit()

if maximum_final >= math:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_final)
  exit()

if maximum_final >= sci:
  print()
else:
  print("Try Again! You have entered wrong Marks in somewhere which is more than", maximum_final)
  exit()

if maximum_final >= social:
  print()
else:
  print("Try Again! You have entered wrong Marks in SST somewhere is more than", maximum_final)
  exit()



print()
print('Total Marks of Final Yearly Examination :' , final_total)
print()
final_earned = eng+hind+math+sci+social

#Rule Applied - 2
if final_total >= final_earned:
  print('Total Marks achieved in Final Yearly Examination : ', final_earned)
else:
  print('Input your Marks Again! You have enterted total marks more than : ', final_total, '',  '[Total Final Yearly Examination]')
  exit()


#Total Term Marks Evalution
term_max = half_earned + final_earned
total_marks = half_total + final_total
print('Maximum Marks of', grade, ' Grade Examination is : ' , total_marks )
print()

#Important
if(total_marks>=term_max):
    print('Total Marks you got in ', grade, " : ",  term_max)
else:
    print('Try Again! You have entered wrong Marks')
    exit()
  
print()
print('Database saved for Final Yearly Examination')
print()
print('Check your Result Below!')
print()

#Evalution Workspace
annual = term_max

if(annual<=total_marks):
    print('You have earned', annual, 'Marks in your', grade, 'Grade Examination out of', total_marks)
else:
    print('Try Again! You have entered wrong Marks somewhere')
    exit()
    
#Evalution of Percentage
per = (annual/total_marks)*100
if(annual<=total_marks):
    print('Achieved Percentage : ', per,'%', 'in your', grade, 'Grade')
else: 
    print('Try Again! Mistakes in your Marks')
    exit()

#Grade Marking Workspace.
print()
if per >= 91 and per <= 100:
  print('Achived Grade in overall Performance of ', grade,' : A1')
  print('Best of Luck for moving in good Direction.')
elif per >= 81 and per <= 90:
  print('Achived Grade in overall Performance of ', grade,' : A2')
  print('Excellent!')
elif per >= 71 and per <=80:
  print('Achived Grade in overall Performance of ', grade,'B1')
  print('Very Good!')
elif per >= 61 and per <=70:
  print('Achived Grade in overall Performance of ', grade,'B2')
  print('Good')
elif per >= 51 and per >=60:
  print('Achived Grade in overall Performance of ', grade,'C')
  print("Can do better next time. Don't lose your confidence. I am with you.")
elif per >= 41 and per <=50:
  print('Achived Grade in overall Performance of ', grade,'D1')
  print("Don't lose confidence. You can do better next time.")
elif per >= 33 and per <=40:
  print('Achived Grade in overall Performance of ', grade,'D2')
  print('Study Nicely and you can achieve more!')
else:
  print("You really need High Improvement. Study More & Get More Marks. I am upset with your Marks. You are Failed! Sorry")

reaction = (input('Are you feeling Good after getting Marks and Percentage ? : '))
if reaction == "Yes":
  print()
  print('Nice, Move Forward I am with you! Do not lose confidence.')
  print()
  exit()
elif reaction == "No":
  print()
  print('Still Do not lose confidence! Prepare Well')
  print()
  exit()
else:
  print()
  print('Invalid Input')
  print()
  exit()

#Run Again
#Under Construction
    
#--------------------------------------------------------------------------------
# Name:        Akshay Dutt Sharma
# Purpose:     To help others in evaluating Marks:
#              "Result Evaluation Program"
#
# Author:      Akshay Dutt Sharma
#
# Created:     08/02/2022
# Copyright:   (c) Akshay 2022
# Class: 9th B
#--------------------------------------------------------------------------------
