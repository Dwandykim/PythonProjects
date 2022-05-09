"""from codeacademy"""
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  def set_numberOfStudents(self, number):
    self.numberOfStudents = number
  def __repr__(self):
    return(f"A {self.level} school named {self.name} with {self.numberOfStudents} students")
    
JB = School("JB", "secondary", 15)

print(JB.get_name())
print(JB.get_level())
JB.set_numberOfStudents(20)
print(JB.get_numberOfStudents())
print(JB)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name,"Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def get_pickupPolicy(self):
    return self.pickupPolicy
  def __repr__(self):
    parentrep = super().__repr__()
    return parentrep + ". " + f"The pickup policy is {self.pickupPolicy}"

Laces = PrimarySchool("Laces", 40, "Pickup Allowed")
print(Laces.get_pickupPolicy())
print(Laces)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name,"HighSchool", numberOfStudents)
    self.sportsTeams = sportsTeams
  def get_sportsTeams(self):
    return self.sportsTeams
  def __repr__(self):
    parentrep = super().__repr__()
    return parentrep + ". " + f"Sports teamms in this school include {self.sportsTeams}"


Uni = HighSchool("Uni", 60, ["swim", "football", "basketball"])
print(Uni.get_sportsTeams())
print(Uni)