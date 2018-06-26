# Vigenére

## tl;dr

Implement a program that runs like the following examples:

```
~/workspace/ $ python vigenere.py
What's your message? HELLO
What's the key (as an key word)? ABC
Cyphertext: HFNLP
```

```
~/workspace/ $ python vigenere.py
What's your message? Hello, world!
What's the key (as an integer from 1-26)? ABC
Cyphertext: Hfnlp, yosnd!
```

## Cryptography

Ever want to send a secret message? Cryptography is the process of converting plaintext (normal English) into cyphertext (encoded text).

The most simple of cyphers are ones where you add a value to each character. For example a + 2 &#10143; c! This is called a Caesar cypher. Of course, to interpret the cyphertext, we would need to know what number is being added, but we'll get back to that later!

## Implementing Vigenére

Let's make a program that uses a Vigenére cypher to encode text like the below:

```
~/workspace/ $ python vigenere.py
What's your message? HELLO
What's the key (as an key word)? ABC
Cyphertext: HFNLP
```

Be sure that your prompts look identical to this!

## Hints

1. It seems that spaces and punctuation are not to be affected by this cypher. We'll likely need to have some conditions to check for them!

2. What is z + 2 equal? It looks like we will have to figure out a way to wrap text around. It turns out that modulus operator (%) is quite useful for ensuring that we stay within the alphabet. To do this, we need to think a bit differently about letters.

3. Let's say **a** is represented by the integer **0**, **b** by **1**, **c** by **2**, ... , and **z** by **25**. This number is called the index! The index of **b** is **1**!

4. Now, let's use this info. **c** + **24** would be **26**, but as the last character in the alphabet, **z**, is **25**, this is problematic. Enter modulus. What is `(c + 25) % 26`? Well, this would be equivalent to `(2 + 25) % 26`, which is `27 % 26`, which equals **1**, or **a**. Hazzah! We've wrapped around the alphabet.

5. However, uppercase **A** in ASCII (remember ASCII?) is **65** and lowercase **a** is **97**! 😬

6. But note this: `B - A` will evaluate to **1**. Why? Because ASCII! `66 - 65 = 1`, which is the index of **B**! After converting letters into this index system we can use the modulus math to make sure things wrap around! Neat-o!

## CS50's Own Zamyla for Help

Ignore the first minute or so, but this should help get you started.

<iframe width="560" height="315" src="https://www.youtube.com/embed/n4gcWaHKhoU?start=52" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Submission

Be sure to call this vigenere.py and submit using ...
