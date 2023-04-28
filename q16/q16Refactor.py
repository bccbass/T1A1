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

print('Enter programming languages known. Press enter when complete: ')

# Collect all skills from User and store in list:
while True:
    skill = input().lower()
    if skill == '':
        break
    else:
        applicant_skills.append(skill)
    
# Loop over skills dictionary to tally score of known languages and append unknowns to skills_to_learn
# Creating skills_to_learn list with keys from skills dictionary helps with cAsE formatting/matching for later logic.
for k, v in skills.items():
    if k.lower() in applicant_skills:
        applicant_score += v
    else:
        skills_to_learn.append(k)
        
print(f'Your overall coding skill score is {applicant_score}. Consider learning any of these languages to boost your score a bit!:')

# loop through skills_to_learn list and access corresponding skills dict items to display.
for skill in skills_to_learn:
    print(f"{skill} will add {skills[skill]} point{'s' if skills[skill] > 1 else ''}.")

print('Thank you for your interest in ACME Corporation!')


# This logic (47-49) could replace lines 39-40 and eliminate need for skills_to_learn list. 
# It loops over skills dictionary, comparing keys to applicant skills to find skills missing. 
# I ultimately opted for the skills_to_learn list approach as it creates a potentially shorter loop iteration (what if the skills dict grows to contain 100 key/value pairs?) as well as having another data point stored for each applicant. 

# for k, v in skills.items():
#     if k.lower() not in applicant_skills:
#         print(f"{k} will add {v} point{'s' if v > 1 else ''}.")
