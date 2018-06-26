# Caesar

## tl;dr

Implement a program that runs like the following examples:

```
~/workspace/ $ python caesar.py
What's your message? Never gonna give you up, never gonna let you down
What's the key (as an integer from 1-26)? 1
Cyphertext: Ofwfs hpoob hjwf zpv vq, ofwfs hpoob mfu zpv epxo
```

```
~/workspace/ $ python caesar.py
What's your message? Let's meet at the zoo!
What's the key (as an integer from 1-26)? 2
Cyphertext: Ngv'u oggv cv vjg bqq!
```

## Cryptography

Ever want to send a secret message? Cryptography is the process of converting plaintext (normal English) into cyphertext (encoded text).

The most simple of cyphers are ones where you add a value to each character. For example a + 2 &#10143; c! This is called a Caesar cypher. Of course, to interpret the cyphertext, we would need to know what number is being added, but we'll get back to that later!

## Implementing Caesar

Let's make a program that uses a Caesar cypher to encode text like the below:

```
~/workspace/ $ python caesar.py
What's your message? Let's meet at the zoo!
What's the key (as an integer from 1-26)? 2
Cyphertext: Ngv'u oggv cv vjg bqq!
```

Be sure that your prompts look identical to this!

Note some important details.
1. It seems that spaces and punctuation are not to be affected by this cypher. We'll likely need to have some conditions to check for them!

2. What is z + 2 equal? It looks like we will have to figure out a way to wrap text around. It turns out that modulus operator (%) is quite useful for ensuring that we stay within the alphabet. To do this, we need to think a bit differently about letters.

Let's say **a** is represented by the integer **0**, **b** by **1**, **c** by **2**, ... , and **z** by **25**. This number is called the index! The index of **b** is **1**!

Now, let's use this info. **c** + **24** would be **26**, but as the last character in the alphabet, **z**, is **25**, this is problematic. Enter modulus. What is `(c + 25) % 26`? Well, this would be equivalent to `(2 + 25) % 26`, which is `27 % 26`, which equals **1**, or **a**. Hazzah! We've wrapped around the alphabet.

However, uppercase **A** in ASCII (remember ASCII?) is **65** and lowercase **a** is **97**! 😬

But note this: `B - A` will evaluate to **1**. Why? Because ASCII! `66 - 65 = 1`, which is the index of **B**! After converting letters into this index system we can use the modulus math to make sure things wrap around! Neat-o!

## CS50's Own Zamyla for Help

Ignore the first minute or so, but this should help get you started.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5I7QqTTolHE?start=82" frameborder="0" gesture="media" allowfullscreen></iframe>

## Submission

Be sure to call this caesar.py and save in your google drive folder! 🙃
