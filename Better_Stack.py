class Stack(object):
    def __init__(self, stack = []):
        self.stack = stack

    def main(self):
        print(""" 
              The purpose of this program is to demonstrate the stack algorithm.

              First we will define the stack we are starting with. If the stack 
              is empty this program will also handle that situation.
              """)
 

    def create_stack(self, stack):
        while True:
            print("Do you want to add an element to a stack?")
            
            x = input("> ")

            if x == "Yes":
                y = int(input("> "))
                stack.insert[0, y]
                continue
            elif x == "No":
                return False
            else:
                print("I do not recognize that command.")
                continue
        print(stack)

s1 = Stack()
s1.main
s1.create_stack(stack = [])
