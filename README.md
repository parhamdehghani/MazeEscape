# MazeEscape
Maze Escape is a popular 1 player game where a bot is trapped in a maze and is expected to find its way out. In this version of the game, 2 bots whose positions are not visible to each other are placed at random points in the maze. the first bot to find its way out of the maze wins the game.

The visibility of the bot is restricted to its 8 adjacent cells where b is the bot. Bots can be facing any of the 4 directions. To make this game more interesting, the orientation of both the bots are randomly chosen at the start of the game and the map visible to them also changes according to the orientation.

It is to be noted that your bot faces the direction in which it chooses to make its next move.

Input Format

The walls are represented by character # ( ascii value 35), empty cells are represented by - (ascii value 45), the maze door which is the indication of the way out is represented by e (ascii value 101)

The input contains 4 lines, the first line being the player id (1 or 2) and followed by 3 lines, each line containing 3 of the above mentioned characters which represents the 8 adjacent cells of the bot. The visible maze given as input always has the bot at the center.

Constraints

5 <= r,c <= 30 where r, c is the number of rows and columns of the maze.

