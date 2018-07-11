# Quidditch

### tl;dr

Create a program that calculates the score of a quidditch match.

### Background

You want to calculate the final score for a team that has just participated in an exciting quidditch match using a program called `quidditch.py`. If you don't know about [quidditch](https://en.wikipedia.org/wiki/Quidditch)... Recall that each "goal" in quidditch is worth **10** points, and that catching the snitch is worth **150** points.

### Your Mission

Building on the code below, implement a function that takes two variables as input — an int indicating the number of times the team got the Quaffle through the other team's hoops, and a bool indicating whether or not they caught the snitch -- and returns that team's final score (what would the return type be?).

### Distribution Code

Copy this code to start your implementation!

```
def main():
    goal_num = int(input("Number of times your chasers got the quaffle through a hoop: "))
    snitch_caught = int(input("Did your team's seeker catch the snitch? Enter 1 if true, 0 otherwise: "))
    score = final_score(goal_num, snitch_caught)
    print("Your team's final score is: " + str(score))

# TODO: define final_score()

if __name__ == "__main__":
    main()
```
