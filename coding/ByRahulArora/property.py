class Student:
    def __init__(self, phy, math, bio):
        self.phy = phy
        self.math = math
        self.bio = bio
        self.percentage = str((self.phy + self.math + self.bio)/3) + "%"

    def calPercentage(self):
        self.percentage = str((self.phy + self.math + self.bio)/3) + "%"


s1 = Student(90, 89, 85)
print(s1.percentage)
s1.phy = 95
print(s1.phy)
print(s1.percentage)  # percentage doesn't update after updating marks so need to calPercentage to update
s1.calPercentage()
print(s1.percentage)


