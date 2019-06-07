# Brainvita
Also known as [peg solitaire](https://en.wikipedia.org/wiki/Peg_solitaire) is a classic single player puzzle.


## About :
Little bit about the game. Check out the [wikipedia page](https://en.wikipedia.org/wiki/Peg_solitaire) for more information.
#### Board :
This repository considers the english version of the game. The english version has 33 holes on the board shaped in the form of a cross. All the holes on the board are filled up with balls/pegs(referred to as balls henceforth) at the start except for the one at the very centre.
#### Rules :
A move in this game is when a ball jumps over a ball to land on an empty space. The ball can only move in either of the 4 directions, top, bottom, left and right. The ball that the original ball jumps over is then removed from the board.
#### Objective :
The objective here is to get rid of all the balls on the board except the last one by having a ball jump over it. The game ends when no further move is possible.
If only 1 of the 32 balls remain on the board the game is said to be solved.
It is easy to see that the solution is also the longest game that can be possibly played with 31 moves.



## Reinforcement Learning :
> "Are neural networks really necessary here? is a seriously under asked question." - Some article I read online.

I would not blame someone asking the same question about reinforcement learning here. With that said, the main objective of this exercise is to use RL to navigate possible board states and find a solution without any form of tree search or look ahead.
#### Approach :
Maintain a classic table of states and action. Fill in the Q value for each state-action pair as we explore the state space. Once solved the action corresponding to max value in a given state will be action to take for the solution.

#### Optimistic Initialization :
A technique to ensure exploration till we find the solution. Here the state space is initialized with a value higher than the total reward obtained in all other failure cases.

## Code:
In there repo there is an python file corresponding to the environment, and a notebook for the agent.

### Environment
Then environment maintains the  board, which is a 7x7 matrix, and allows only valid moves on the board. The episode is complete when there are no moves possible. It is also possible to sample a valid move for a given state from the environment.

### Agent
The agent in the notebook is a very simple one, every unique state encountered is assigned action-values for all the possible actions. The agent used optimistic initialization to explore its way to the solution. To reduce the size of the problem rotational symmetry and and mirror images of known states are not recognized as new states, instead the state of the board is changed to match that of a equivalent known state.


## Conclusion
This is a fun little puzzle. This is in no way intended to be the 'correct' solution or approach to the problem.
Feel free to play around and come up with alternate ideas.


