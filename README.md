# Breakthrough
Breakthrough game, AI agents playing.

# How To Play
 1. Make sure you have `python 3` installed.
 2. Run `python game.py` and follow the instructions.

# Unit Testing
Simply run the `testTransition.py` file:

```python testTransition.py```

# Progress
* Finished implementing `Board` Class methods

    * `get_moves(position)`
    * `is_valid(source, destination)`
    * `get_sym(position)`
    * `get_direction(position)`
    * Integrated `display_state()`
    * Integrated `terminal_state()`
    * Add `self.turn` to the `Board` and check before moving 
      any piece to ensure the integrity of the game
    * Implement `move_generator(player)` method that will provide
      all the moves for a particular player

* Test coverage for finished methods
    
    - [x] `get_moves(position)`
    - [x] `is_valid(source, destination)`
    - [x] `all_moves(player)`
    - [x] `move(position, direction)`
    - [ ] `get_sym(position)`
    - [ ] `get_direction(position)`
    - [ ] `display_state()`
    - [ ] `terminal_state()`

# ToDo 
- [ ] Finish implementing the `Agent` class
- [ ] Decide whether to implement a function or class for `Game`
- [ ] Finish `minimax` tree
- [ ] Implement `conquerer` and 2 more utility functions

