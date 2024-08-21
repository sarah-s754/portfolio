# PLANT LIFE
#### Video Demo: https://youtu.be/rkrwV5xciic
## Description:
*Plant Life* is a web-based application using Python, Flask and JavaScript in which users can create and cultivate a virtual garden.

This virtual garden takes the form of a game or mindfulness activity that encourages users to enjoy the benefits of gardening without the requirement for a physical garden or the demoralisation of being unable to keep real plants alive.

Enjoy! 🌱

## Functionality:
- **User authentication** - required registration, storage of hashed password, log-in to access garden functionality and log-out options.
- **Plant status** - plants each have a status that transitions from 'healthy' to 'dry' every two minutes.
- **Point system** - the user gains points by watering any plants listed as 'dry'. These points can then be used to purchase new plants.
- **Gardening log** - records of the types, times and dates of any plants sown are displayed in a table.

## Files:
### 'app.py'
Contains the main code of the program. This includes the setup of the Flask application. This facilitates the timing of the application and the transitions between the various web pages. As part of this timing, plants are initially purchased with a 'healthy' status that's updated that's based on its 'last_watered' time.

This time is initially set to the purchase time and is updated each time the 'water' button is used on the index.html page. The plant's status is updated to 'dry' each time the current time is greater than two minutes after the 'last_watered' time.

The initial concept was to have the plants require watering once per day, but this time requirement was reduced to make the application more interactive. To accommodate the shortened watering time, it was decided not to punish the user for failing to water the plants. This supports the vision of allowing users to enjoy cultivating a virtual garden without experiencing punishment for being productive in other areas of life or being demoralised by losing achievements.

### 'helpers.py'
Contains the functions apology and login_required that support the application.

### 'static/'
Directory containing the tab icon, plant images and the stylesheet.

#### 'style.css'
Stylesheet defining the appearance of the navigation bar, green-coloured heading, and padding of list items.

### 'templates/'
The directory containing the html files for each of the pages on the website.

#### 'layout.html'
Base HTML file of which all other HTML files are an extension. This file contains the navigation bar and the footer.

#### 'apology.html'
Displays an image and apology message detailing errors that may have gone wrong in the code.

#### 'register.html'
Allows the user to create an account by specifying a unique username and password. The usernames and hashed passwords are recorded in the 'users' table in the 'plantlife.db' database.

#### 'login.html'
Allows the user to log in using a previously registered username and password. The user is directed to an apology page if an invalid username or password is entered. Validity is determined by comparison against the 'users' table in the 'plantlife.db' database.

#### 'profile.html'
Allows the user to change their password from the one they initially registered with. The password can be changed as many times as desired. If the new password isn't identically entered twice, the user is directed to an apology page.

#### 'info.html'
Displays an introductory message and basic instructions for how to use the web application. This information page is available both before and after the user has logged in.

#### 'index.html'
This page displays the user's virtual garden in the form of a table showing each plant's image, name, associated points, and status. When a plant's status is 'dry' a button appears on the right side of the table to allow the user to gain points by changing the plant's status to 'healthy'.

This page is auto-refreshed every 30 seconds using JavaScript to make sure the plant's status is always accurately reflected. The user's total points and the points available to purchase more plants are also displayed.

#### 'guide.html'
Displays a field guide of all the plants available in the application and lists the points required for the user to purchase each one. The available plants are recorded in the 'plants' table in the 'plantlife.db' database.

#### 'sow.html'
Allow the user to purchase desired quantities of any of the available plants. The plant options are visible in a dropdown that displays a preview image of the selected plant.

Users will be directed to the apology page if they attempt to purchase an invalid quantity or if the selected option exceeds the user's points.

#### 'log.html'
Displays a table detailing the user's purchase history. The table contains the name of the purchased plant, the points spent, and the date of the purchase.

### 'plantfile.db'
Database used for storing the user, plant and garden information used in the application.
The SQL code used to create the tables in the database is shown below:

- >CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash TEXT NOT NULL,
    points NUMERIC NOT NULL DEFAULT 100
);

- >CREATE TABLE plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price NUMERIC NOT NULL,
    image_filename TEXT
);

- >CREATE TABLE garden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    plant_name TEXT NOT NULL,
    price NUMERIC NOT NULL,
    status TEXT NOT NULL DEFAULT 'healthy',
    last_watered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    plant_image_filename TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (plant_name) REFERENCES plants (name),
    FOREIGN KEY (plant_image_filename) REFERENCES plants (image_filename)
);

- >CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    plant_name TEXT NOT NULL,
    quantity INTEGER,
    price NUMERIC NOT NULL,
    transacted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (plant_name) REFERENCES plants (name)
);
