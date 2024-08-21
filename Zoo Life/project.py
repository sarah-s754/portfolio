import sys

class Animal:
    def __init__(self, symbol, acquisition_count):
        self._symbol = symbol
        self.acquisition_count = acquisition_count

    def __str__(self):
        return f"{self.get_type()} {self.symbol}"

    def get_type(self):
        return type(self).__name__

    @property
    def symbol(self):
        return self._symbol


class Tiger(Animal):
    def __init__(self, acquisition_count):
        super().__init__("🐯", acquisition_count)


class Panda(Animal):
    def __init__(self, acquisition_count):
        super().__init__("🐼", acquisition_count)


class Koala(Animal):
    def __init__(self, acquisition_count):
        super().__init__("🐨", acquisition_count)


class User:
    def __init__(self, capacity=10):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

        self.animals = {}
        self.acquisition_count = {}

    def adopt(self, animal_class):
        if self.total_acquisition_count < self._capacity:
            if animal_class not in self.animals:
                self.animals[animal_class] = []
                self.acquisition_count[animal_class] = 1

            else:
                # Increase counter
                self.acquisition_count[animal_class] += 1

            animal = animal_class(self.acquisition_count[animal_class])
            self.animals[animal_class].append(animal)
            print("Adopted " + str(animal) + " ❤️")

        else:
            print("No room left in your zoo!")

    def release(self, animal_class):
        if animal_class in self.animals and self.animals[animal_class]:
            released = self.animals[animal_class][-1]
            self.animals[animal_class] = self.animals[animal_class][:-1]

            # Decrease counter
            self.acquisition_count[animal_class] -= 1

            print("Released " + str(released) + " 💔")

        else:
            print("No " + str(animal_class('').get_type()) + "s to release!")

    def display_zoo(self):
        if self.animals:
            print("\nMeet the zoo residents...")

            for _, animal_list in self.animals.items():
                for animal in animal_list:
                    print(str(animal) + " 🏠")

        else:
            print("Zoo is empty! 😿")

    @property
    def capacity(self):
        return self._capacity

    @property
    def total_acquisition_count(self):
        return sum(self.acquisition_count.values())


def main():
    print("\n🐾 WELCOME TO ZOO LIFE! 🐾")
    print("Type \"help\" to get started...\n")
    user = User()

    while True:
        handle_action(input("\nAction: "), user)


def handle_action(action, user):
    if action.startswith("adopt") or action.startswith("release"):
        if is_valid_input(action):
            cmd, anml = action.lower().split(" ")
            anml_clss = globals().get(anml.title())

            match cmd:
                case "adopt":
                    user.adopt(anml_clss)
                case "release":
                    user.release(anml_clss)

        else:
            print("Invalid option - please choose from the available animals 🐯🐼🐨 ")

    else:
        match action.lower():
            case "help":
                print("\n❓ AVAILABLE ACTIONS ❓")
                print("adopt - add an animal to your zoo.")
                print("release - release an animal from your zoo.")
                print("check animals - count how many animals are in your zoo.")
                print("pat - give some love to each of the animals in your zoo.")
                print("show zoo - displays all the animals in your zoo.")
                print("leave zoo - exit the program.")
            case "leave zoo" | "exit":
                sys.exit(1)
            case "show zoo":
                user.display_zoo()
            case "check animals":
                print(check_animals(user))
            case "pat":
                print(pat_animals(user))
            case _:
                print("Invalid command - try typing help...")


def is_valid_input(input):
    splt = input.lower().split(" ")

    if len(splt) == 2:
        if globals().get(splt[1].title()):
            return True
        else:
            return False

    else:
        return False


def check_animals(user):
    return str(user.total_acquisition_count) + " animal(s) currently in zoo"


def pat_animals(user):
    txt = ""

    for _ in range(0, user.total_acquisition_count):
        txt += "💖"

    if txt == "":
        return "Zoo is empty! 😿"

    return txt


if __name__ == "__main__":
    main()
