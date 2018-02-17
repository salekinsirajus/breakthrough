# Breakthrough
Breakthrough game, playing with an AI agent

# Progress
* Finished implementing `Board` Class methods

    * `get_moves(position)`
    * `is_valid(source, destination)`
    * `get_sym(position)`
    * `get_direction(position)`
    * Integrated `display_state()`
    * Integrated `terminal_state()`

* Test coverage for finished methods
    
    - [x] `get_moves(position)`
    - [x] `is_valid(source, destination)`
    - [ ] `get_sym(position)`
    - [ ] `get_direction(position)`
    - [ ] `display_state()`
    - [ ] `terminal_state()`
# ToDo 
    - Add `self.turn` to the `Board` and check before moving 
      any piece to ensure the integrity of the game
    - Implement `move_generator(player)` method that will provide
      all the moves for a particular player

# Unit Testing
Simply run the `testTransition.py` file:
>```python testTransition.py```
