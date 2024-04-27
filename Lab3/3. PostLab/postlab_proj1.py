class Student(object):

    def __init__(self, name, number):

        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def getName(self):
        return self.name 

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
         return max(self.scores)

    def __eq__(self,student):
        return self.name == student.name

    def __ge__(self,student):
        return self.name == student.name or self.name>student.name

 
    def __lt__(self,student):
        return self.name<student.name

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
            " ".join(map(str, self.scores))

 
def main():

    """A simple test."""
    student1 = Student("Neal", 5)
    student2 = Student("Lee", 5)
    student3 = Student("Paulo", 3)
    
    # First method test for equality
    print(student1 == student2)  # False
    print(student1 == student3)  # True
    
    # Second method test for less than
    print(student1 < student2)  # True
    print(student1 < student3)  # False
    
    # Third method test for greater than or equal to
    print(student1 >= student2)  # False
    print(student1 >= student3)  # True


if __name__ == "__main__":
    main()
