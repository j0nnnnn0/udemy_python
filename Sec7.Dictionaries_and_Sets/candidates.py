
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets - application of Subsets and Supersets


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

required_skills = ["python", "github", "linux"]

candidates = {
    "anna" :  {"Java", "linux", "windows","github","python","full stack"},
    "bob" :   {"github", "linux", "python"},
    "carol" : {"linux", "javascript", "html", "python","github"},
    "daniel" :{"pascal", "java", "c++","github"},
    "ekani" : {"html", "css", "github", "python", "linux"},
    "fenna" : {"linux", "pascal","java","c","lisp", "modula-2", "perl", "github"},
}

interviewees = set()
for candidate, skills in candidates.items():
#    if skills.issuperset(required_skills): # superset
    if skills > set(required_skills): # proper superset
        interviewees.add(candidate)
    
print(sorted(interviewees))
# superset ['anna', 'bob', 'carol', 'ekani'] match
# proper subset ['anna', 'carol', 'ekani'] match and more