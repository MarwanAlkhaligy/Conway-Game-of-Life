# Conway-Game-of-Life
The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## Game of Life's Rules:-

- Death. If a cell is alive (state = 1)
  - > Overpopulation: four or more alive neighbors, it dies.
  - > Loneliness: one or fewer alive neighbors, it dies.
- Birth. If a cell is dead (state = 0) it will come to life (state becomes 1) if it has exactly three alive
- Stasis. In all other cases, the cell state does not change. To be thorough, let’s describe those scenarios.
   - > Staying Alive: If a cell is alive and has exactly two or three live neighbors, it stays alive.
   - > Staying Dead: If a cell is dead and has anything other than three live neighbors, it stays dead.

##  Variations of Traditional CA:

 - Implemented functionality to make Mouse Left Click draw on the grid (Activate a cell)
 - Changed the cells so that it becomes non-rectangular when it is activated or not
 - Made the cell color a random color each time it is activated (State = 1)

## Requirements :-

- Pygame : pip install pygame
- Numpy  : pip install numpy

## References and Documentation :-

- [Nature of code](https://natureofcode.com/book/chapter-7-cellular-automata/)
- [MathWorld](https://mathworld.wolfram.com/)
- [Pygame documentation](https://www.pygame.org/docs/)
- [Python documentation](https://docs.python.org/3/)

