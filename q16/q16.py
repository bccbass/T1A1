skills = {
    'Python' : 1,
    'Ruby' : 2,
    'Bash' : 4,
    'Git' : 8,
    'HTML' : 16,
    'TDD' : 32,
    'CSS' : 64,
    'JavaScript' : 128,
}

applicant_skills = []
skills_to_learn = []
applicant_score = 0

print('Enter programming languages known. Press enter when complete.')


while True:
    skill = input()
    if skill == '':
        break
    elif skill not in skills:
        print("I don't know that language, please check and try again.")
    else:
        applicant_skills.append(skill)
 

for skill in skills:
    if skill in applicant_skills:
        applicant_score += skills[skill]
    else:
        skills_to_learn.append(skill)
        
print(f'Your overall coding skill score is {applicant_score}. Consider learning any of these languages to boost your score a bit!:')

for skill in skills_to_learn:
    print(f"{skill} will add {skills[skill]} point{'s' if skills[skill] > 1 else ''}.")

print('Thank you for your interest in ACME Corporation!')

    
