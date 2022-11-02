"""
Emma Naumann
CP1404 Practical 6 - Intermediate Exercises
(with programming_language.py file)

Estimate: 40 minutes (12:22pm) (12:45pm lunch break)
Actual:
"""


from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
# print(python)
# print(ruby)
# print(visual_basic)

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
