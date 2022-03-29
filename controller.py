from model import Model
from view import View

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def main(self):
        self.view.main()
    
    def onClick(self, name):
        result = self.model.calculate(name)
        self.view.value.set(result)
        
if __name__ == '__main__':
    calc = Controller()
    calc.main()