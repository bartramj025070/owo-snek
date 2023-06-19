# owo-snek
***
*v3.0.2*

*Table of contents*
* [Movement](14)
* [General Controls](21)
* [Difficulties](25)
* [Save & Load](44)

owo-snek is a saveable snake python game, easily able to run. it features:
* Difficulties
* Movement
* Save/Load
***

     Movement
UP_ARROW / W / I = UP<br>
LEFT_ARROW / A / J = LEFT<br>
DOWN_ARROW / S / K = DOWN<br>
RIGHT_ARROW / D / L = RIGHT<br>

      General
Q = SAVE & QUIT GAME

    Difficulties
Score increase is how much speed you get per apple, the higher the difficulty the more score increase.<br>
<br>
Right click on "owo snek.py" and do "Open with Notepad++". Once it is loaded, go to Line 36. It will show all difficulties and<br>
their score increase. Line 36 should be the current difficulty, edit the string (anything inside "").<br>
You MUST keep all capitals the same to the difficulty you want or it will not work!<br>
<br>
To add a difficulty add it like so from line 24:<br>
difficulties = {<br>
	"CUSTOM_DIFF_NAME": SCORE_INCREASE # e.g EASY difficulty has 1 score increase.<br>
}<br>
<br>
The suggested difficulty in game is NORMAL, HARD, or INSANE as the ones after are designed to be unbeatable for<br>
fun.<br>
<br>
Also, in game you can use [ or ] to increase/decrease the score increase in the middle of a game, however this will override your<br>
difficulty to "Custom"<br>
<br>
    Save & Load
Your save data is located in "save.json". Please do not move, rename or rewrite any of that data, for<br>
multiple reasons;<br>
**1.** You may break the save (Not fixable without knowledge of the save data method.)<br>
**2.** If it is moved or renamed the script will not be able to find the save file, it is only searching for<br>
	   "save.json"<br>
**3.** If you do wish to rewrite it, please consult someone who does understand the save data, however<br>
	   your best bet is probably me (Jasper) as I made the game<br>
**4.** Some things may be able to be rewritten easily (Score, Fruit Location, Speed or Direction) but please<br>
	   refrain from doing so, the game is designed to be fun and cheating ruins the game.<br>
<br>
When you press Q in the middle of a game, your data will save, however if you lose a match at any time your<br>
save will be overwritten to the default and be random once more.<br>
<br>
Difficulty does NOT save however it will tell you if your difficulty is different from the one you last played the<br>
save with.<br>
<br>
To load the game simply boot up the game, and it will load automatically!<br>
