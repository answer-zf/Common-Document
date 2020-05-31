"""
    
"""


class Skill:
    pass


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    def __iter__(self):
        pass


class SkillIterator:
    def __next__(self):


manager = SkillManager([Skill(), Skill(), Skill()])


# for item in manager.skills:
# for item in manager:
#     print(item)

iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break
