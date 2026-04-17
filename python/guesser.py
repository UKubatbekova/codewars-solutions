# https://www.codewars.com/kata/568018a64f35f0c613000054/train/python

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        self.n = n
        if self.lives == 0:
            raise ValueError("Omae wa mo shindeiru")
        elif self.number == n:
            return True
        else:
            self.lives -= 1
            return False