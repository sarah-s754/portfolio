# ZOO LIFE
#### Video Demo:  https://youtu.be/mdj4lgrlUlw
## Description:
Zoo Life is a command-line game that allows users to manage and interact with animals in a virtual zoo.

Through this program, users can adopt animals into their virtual zoo, view the animals in their zoo as emoji representations of the animals they've adopted, view a count of all the animals they currently have in their zoo, and "pat" their animals to receive a visual display of the animal's appreciation in the form of concatenated heart emojis.

The amount of animals that can be kept in the zoo at any one time is capped at a capacity of 10. If users wish to adopt more animals beyond this point, they must first "release" some of the animals they've already adopted.

The animals available for users to interact with are tigers, pandas, and koalas. However, the program is written to allow the simple addition of new animals if desired.

Happy zookeeping! 🐾

### Details:
The code contains two main classes, *User* and *Animal*. There are also several child classes of the *Animal* class for *Tiger*, *Panda*, and *Koala*. Each child class of the Animal class has their own property "symbol", which is an emoji that is the main way the animals are represented to the user.

The "*capacity*" of the zoo is recorded as a property of the *User* class. The User class also has a property that returns the total number of animals they've currently adopted. It also contains methods to adopt animals, release animals, and display all the animals in the zoo.

The "*acquisition_count*" is incremented up or down whenever animals are adopted or released.

When the program is run, the user is continually prompted to enter "actions". The input actions are handled through the function *handle_action*. This function calls upon the *is_valid_input* function to check whether the entered command is valid in terms of the "*adopt*" and "*release*" commands and the available animals before being compared directly against the rest of the string options for commands. Whenever the user enters an invalid command, they will be directed to type the "*help*" command to see the list of valid options.

The function *check_animals* is used when the user enters the command "*check animals*". This function returns a string description of the number of animals currently in the zoo that can be displayed to the user. Similarly, the function *pat_animals* is called when the user enters the command "pat". This function returns a string of concatenated sparkling heart emojis equal to the number of animals currently present in the zoo.

### Example Usage:
- **adopt** - add an animal to your zoo.
    - e.g. "adopt panda"
- **release** - release an animal from your zoo.
    - e.g. "release tiger"
- **check animals** - count how many animals are in your zoo.
- **pat** - give some love to each of the animals in your zoo.
- **show zoo** - displays all the animals in your zoo.
- **leave zoo** - exit the program.
- **help** - display the list of available commands.
