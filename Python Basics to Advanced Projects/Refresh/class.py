class Cookie:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


cookie_one = Cookie("green")
cookie_two = Cookie("blue")


print('Cookie one is ', cookie_one.getColor())
print('Cookie two is ', cookie_two.getColor())
