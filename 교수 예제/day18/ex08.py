class Member:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    name=''
    gender=''
    age=0
    
    def ShowInfo(self):
        print('{}\t{}\t{}'.format(self.name, self.age, self.gender))
        
m01 = Member('원종래', '남성', 30)
m01.ShowInfo()    

