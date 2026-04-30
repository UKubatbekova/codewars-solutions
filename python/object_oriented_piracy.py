# https://www.codewars.com/kata/54fe05c4762e2e3047000add

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        crew_member = self.crew * 1.5
        ships_weigth = self.draft - crew_member
        if ships_weigth > 20:
            return True
        else:
            return False