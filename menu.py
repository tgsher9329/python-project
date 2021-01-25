class Menu:
    def __init__(self, prompt_text, choices):
        self.prompt_text = prompt_text
        self.choices = choices

    def getChoice(self):
        choice = -1
        choice_string = self.choices_to_string()
        while choice == -1:
            try:
                choice = int(input(choice_string))
                if choice <= 0 or choice > len(self.choices):
                    raise ValueError
            except ValueError:
                self.print_menu_error()
        return choice

    def choices_to_string(self):
        choice_string = ""
        num = 1
        for choice in self.choices:
            choice_string += "%d: %s\n" % (num, choice)
            num += 1
        choice_string += self.prompt_text
        return choice_string

    def print_menu_error():
        print("That was not a valid choice. Try again.\n\n\n")