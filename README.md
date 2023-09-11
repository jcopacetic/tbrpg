# Turn Based RPG Battle

TBRPG is a turnbased text adventure battle system. Currently in development. Experience and leveling system, moves system, dynamic damage system, evolving stats. Have fun!

You are welcome to use this. If you'd like to contribute that'd be great!

coming soon:
- items
- battle tower advancement
- battle win / loss display

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)

## Installation

- Clone this repo
- make sure you have the latest version of python installed
- cd into project folder 
    $ cd where-you-cloned-repo/tbrpg
- run main.py with python 
    $ python main.py

a new player class is created for you that gets assigned a random type. I want to add more stats and stats randomization soon on init soon.

both the Player and Baddy class recieve 4 random moves. They are supposed to be unique moves, currently that is not the case.

# Usage

- command - shows the available commands in main menu
- player - shows information about your player
- exit - will stop the script
- game - starts a battle

There is a Baddy class that it a subclass of Player. I'm currently checking for the subclass to determine the battle logic in the Game class turn method. I want to move that logic to the Player/Baddy classes eventually. 

In the Battle stage there are 2 options:

- run - attempts to run, if attempt fails opponents take turn
- attack - opens moves menu

the moves menu is a list of the available moves. if the moves pp is 0 you can't use it. The move loses 1 pp per successful use. 

Whether you win or lose your first few battles, you will eventually level up. as you level up your attack and hp will grow and you will eventually be able to beat the Baddy. it's literally minutes of fun. The Bad guys need to get stronger too to keep it interesting.

#Configuration

no config options yet

# Contributing

no contributing info yet 

# License 

idk, just have fun with it

# Credits

the internet

# Troubleshooting 

a couple of issues

- sometimes the battle doesn't end on the first turn a player hits 0. They get one more turn. I'm not sure why.
- Player attack is not factored into the damage at the moment.

