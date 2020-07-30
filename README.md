# MacGyver-game-2D
MacGyver must escape, you're gonna have to help him!

## python3
This program is coded in python3.  
So, if you have not already installed that language, please start with this.  
More information available [here](https://wiki.python.org/moin/BeginnersGuide/Download "downloading and installing Python")

## first time, create a virtual environment
In order to confine the game in a dedicated environnement, you're encouraged to create a virtual environment.  
You will be able to do that, using command:  
    `python3 -m venv env`  
More information available under [python's documentation](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments "creating virtual environments")

## virtual environment activation
The newly created environment can be activated using:  
    `source env/bin/activate`  
*Please note that it stays available until you close your terminal.*  
**Each time you start a new terminal, you'll have to do this once again.**

## requirements installation
MacGyver-game is based on pygame, more details available [here](https://www.pygame.org "pygame").  
To install the game's requirements, please launch:  
    `python3 -m pip install -r requirements.txt`

## game launch
* To start the game, execute following command:  
    `./game.py`  
* If this doesn't work, you can try:  
    `python3 game.py`  
* Depending on your python installation, sometimes you might use:  
    `python game.py`  
*Please note that **python3** is required. A launch with python2 is not intended.*

## game appearance
Here is what things should look like:  
![screnshot](resources/screenshot.png "game window")

## game flow
Use your keyboard's directional keys to move the hero in the labyrinth.

## game escape
* the window will close after three seconds in case you win or lose
* at any time, you can press `<escape>` or `<alt+F4>`

## pylint linting
As pygame is coded among others in C language, pylint won't load it by default.
This is resulting in errors like: 
> E1101: Module 'pygame' has no 'QUIT' member (no-member)  
>
Please use _--extension-pkg-whitelist=pygame_ option when linting.  
Example: `pylint --extension-pkg-whitelist=pygame game.py`  
Source: [pylint documentation](https://docs.pylint.org/en/1.9/technical_reference/features.html#general-options "general options")

## problems, questions, suggestions
Feel free to send me [an email](mailto:52000851+hacker0uvert@users.noreply.github.com?subject=macgyver-game-2D "reach me out here")