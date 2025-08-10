skills = [
    "python-eASy",
    "java-difficult",
    "js-easy",
    "react-Easy",
    "html-EASY",
    "git-moderate"
]

for skill in skills:
    if "easy" in skill.lower():
        print(skill)

skills = [
    "python-eASy   ",
    "java-difficult",
    "   easy-js",
    "react-Easy   ",
    "   EASY-html",
    "git-moderate"
]

for x in skills:
    if "easy" in x.lower():
        print("".join(x.split()))
