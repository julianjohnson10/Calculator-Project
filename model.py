class Model():
    def __init__(self):
        self.value = ''
        self.operator = ''

    def calculate(self, button_name):
        #Check to see if the list is empty.
        #Determine if the button is a number or not.
        is_int = isinstance(button_name, int)
        
        # self.final_val = self.first_val + self.current_val
    
        #if it IS a number, it will concatenate the current number value to the Entry object
        match is_int:
            case True : self.value += str(button_name)
            case False : pass

        match button_name:
            case 'C':
                self.value = ''
            case '+'|'-'|'/'|'*':
                self.operator = button_name
                self.first_val = self.value
                self.value += str(button_name)
            case "=":
                self.value = str(self._eval())

        if self.value:
            pass

        return self.value
    
    def _eval(self):
        return eval(self.first_val+self.operator+self.value)
