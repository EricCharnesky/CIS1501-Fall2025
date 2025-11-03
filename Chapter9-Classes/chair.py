class Chair:

    # initialize or constructor
    # it's job is to give attributes names and values
    def __init__(self, color, has_arms = False, current_height = 30, minimum_height = 0, max_height = 100):
        self.set_color(color)
        # prefix with _ to 'hide' the value or make it private
        self._height_in_cm = 0
        self._minimum_height_in_cm = minimum_height
        self._maximum_height_in_cm = max_height
        self.change_height(current_height)
        self.set_has_arms(has_arms)


    # um gpt
   # write set and get functions for the attributes of this class
    # class Chair:
    #
    # # initialize or constructor
    # # it's job is to give attributes names and values
    # def __init__(self, color, has_arms, current_height, minimum_height, max_height):
    #     self.set_color(color)
    #     # prefix with _ to 'hide' the value or make it private
    #     self._height_in_cm = 0
    #     self._minimum_height_in_cm = minimum_height
    #     self._maximum_height_in_cm = max_height
    #     self.change_height(current_height)
    #     self._has_arms = has_arms

    def set_has_arms(self, has_arms):
        self._has_arms = has_arms

    def get_has_arms(self):
        return self._has_arms

    def get_minimum_height(self):
        return self._minimum_height_in_cm

    def get_maximum_height(self):
        return self._maximum_height_in_cm

    def get_height_in_cm(self):
        return self._height_in_cm

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    # protects the value of current height - keeps it in bounds
    def change_height(self, change_in_cm):
        if self._height_in_cm + change_in_cm > self._maximum_height_in_cm or \
            self._height_in_cm + change_in_cm < self._minimum_height_in_cm:
            raise ValueError("Invalid height")
        self._height_in_cm += change_in_cm

    # how to represent the instance as a string ( works with print )
    def __str__(self):
        return f'Color: {self._color} - Current Height: {self._height_in_cm}'




if __name__ == "__main__":

    # calls the init method
    erics_chair = Chair("blue")
    # python lets you do bad things
    # erics_chair._height_in_cm = 700
    erics_chair._has_arms = False
    # erics_chair._maximum_height_in_cm = 70
    # erics_chair._minimum_height_in_cm = 70
    erics_chair.change_height(10)

    jubilees_chair = Chair("orange")
    jubilees_chair._has_arms = False
    jubilees_chair._maximum_height_in_cm = 100
    jubilees_chair._minimum_height_in_cm = 30
    changed = False
    while not changed:
        change = int(input("How much do you want to change the height by?"))
        try:
            jubilees_chair.change_height(change)
            changed = True
        except ValueError as exception:
            print(exception)

    # print_chair(erics_chair)
    # print_chair(jubilees_chair)
    print(erics_chair) # uses the __str__ method
    print(jubilees_chair)
