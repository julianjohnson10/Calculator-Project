class Model():
    def __init__(self):
        self.value = ''

    def multiply(a,b):
        return a * b


    def calculate(self, name):
        #Check to see if the list is empty.
        #Determine if the button is a number or not.
        is_int = isinstance(name, int)

        #if it IS a number, it will concatenate the current number value to the Entry object
        match is_int:
            case True : self.value += str(name)
            case False : pass

        match name:
            case "C":
                self.value = ''
            case "+":
                pass
            case "/":
                pass

        return self.value
