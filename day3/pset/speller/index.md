# Speller

## TL;DR

Implement a program that spell-checks a file, per the below.

## Background

### Learning goals

Let's build ourselves a very simple spellchecker and actually use it to check the spelling of a number of texts! We're going to do so using Python to implement our spellchecked, but first we're going to take a look at **classes**, **methods** and **file input/output**.

### Classes

In the real world, there are often entities that we want to represent that aren't fully covered by simple data types like integers and strings or by data structures like lists and dictionaries. Turns out, it's really useful to have a way to represent more complex entities, especially if you have many of them! For example, in the case of products like Facebook or Google, when people use their services, there is a lot of information associated with each person, and it's not enough to just keep track of their name and/or email address. This is where classes come in. Classes in Python allow us to create new data structures and you can think of them kind of like super variables in the sense that it's up to you what kind of information you can store for each class and what kind of capabilities each class will have.

According to the Python [documentation](https://docs.python.org/3/tutorial/classes.html), Python classes allow us to package data and functionality together and "Creating a new class creates a new *type* of object, allowing new *instances* of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state."

So we can see that a `class` is essentially a fundamental building block in Python. Consider the example below, in which we look at a potential implementation of a class for a customer at a bank:

```
class Customer():

def __init__(self, name, balance=0.0)
	self.name = name
	self.balance = balance

def withdraw(self, amount):
	if amount > self.balance:
		print("Insufficient funds.")
	self.balance -= amount
	return self.balance

def deposit(self, amount):
	self.balance += amount
	return self.balance
```

Here, we have defined the customer class, which is a blueprint for any future instances of customers we may want to create. Using the above blueprint, we can create one or more specific customers like so:

```
maria = Customer("Maria Zlatkova", 3000.0)
```

Here, we created a new specific instance of the customer class and we placed it in the variable called `maria` and from now on, we will refer to this specific instance of the customer as `maria`.  Maria can also withdraw or deposit money from her bank account:

```
maria.deposit(1500)
maria.withdraw(2000)
print(maria.balance)
```


## Your Mission

We're going to create a program that can spellcheck bodies of text when given a dictionary against which to reference the correct spelling of worlds.

You're going to tackle a few `TODO`'s in `speller.py`.

### 0. 



### 1. 



## Checking Your Work

