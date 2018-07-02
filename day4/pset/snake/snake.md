# Snake

## TL;DR

Implement the popular game called Snake from the days of Nokia cell phones!

## Background



### Learning goals


## Your Mission

Let's take a look at `snake.py`, since you're going to tackle a few `TODO`'s in there! Scroll down to line 92 where the class definition of `Snake`begins.

### 0. `def restart(self)`
The first class method you're going to write will be called whenever the game needs to be started or restarted. You'll want to do three things in this method:

1. Set the `length` attribute of the snake. Whenever the game starts the snake begins and it is initially only one unit long, so you can use the syntax you see in the second line of the `def __init__(self):` method to set the `length` attribute of the snake equal to 1.

2. Set the `position` attribute of the snake. Each square that the snake takes up will be defined by a position consisting of an X-coordinate and a Y-coordinate, which can both be saved in a **tuple**. To easily keep track of every square that the snake takes up, we'll save all of its square's positions in a list, which means we'll create a **list of tuples** (i.e. [(x~1~, y~1~), (x~2~, y~2~), (x~3~, y~3~)] would be what this list might look like for a snake of length 3, where x~1~ and y~1~ are the coordinates of the snake's head, x~2~ and y~2~ are the coordinates of its middle and x~3~ and y~3~ are the coordinates of its tail).

   So what should the values of the initial position of the snake be? Well, we conventionally want to start of the snake in the middle of the screen, so we just need to get the coordinates of the middle of the screen! How do we get those though? Scroll up in the file to lines 15-24, where we've defined some constants, and on line 17 you'll see the constants `SCREEN_WIDTH` and `SCREEN_HEIGHT`. You can use these constants to calculate the middle of the screen (halfway through the width and height) and put them in a tuple!

   Hint: Here you only need to set the initial position of the snake, so you need only one tuple to represent it, but in order to ensure that you can add to this list of positions, you'll want to put this tuple in a list!

3. Finally, set the `direction` attribute that the snake should initially move in. We could hardcode this direction (i.e. set the snake to always go up or down), but it might be more fun to have our script pick a random direction each time the game starts. To make this choice, let's use Python's `random` module, which contains a number of potential functions you could select from.

   Hint: Take a look at the [following function](https://docs.python.org/2/library/random.html#random.choice), which takes in a list as an argument and returns a randomly selected element from that list. What elements should you put in the list? Well, if you scroll back up to lines 15-24, where we've defined some constants for you, you should see four directions defined. Try using those with this function!

### 1. `def get_head_position(self)`


### 2. `def point(self,point)`


### 3. `def move(self)`


### 4. `def randomize(self)`


### 5. `def check_eat(snake, apple)`

## Checking Your Work

