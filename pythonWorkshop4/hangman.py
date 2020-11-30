'''
Template for the hangman game.
You have been given the template for the hangman game.
You can choose to use this template, or you can always do the game however you like.
I strongly suggest you use most of the concepts we learned in these workshops,
i.e. (if, elif, else statments, lists, strings/variables, functions)
Note: if you do not feel comfortable with functions at first, I reccomend doing this project without
functions and write all your code and logic in one big function.  Maybe after you do that then
try and rework your code to work with functions.

You have been given a function called display_hangman which will help you display the hangman template (the drawing of the head, body)
for more info on that function read the comments above that function.

I have put the declaration of a couple other functions, and given 
a brief explanation fo how I would use them,
If you think of a differnt way to do it you should do your own way 
(you will learn better from doing it your own way rather than trying to figure out what my way was)

Also you should feel free to add whatever functions you think are appropriate or change 
the functions given to match how your code and logic works.
You are not getting marked on being able to fully understand the template I gave you.
The point of this is so that you get practice making a hangman game however you see fit (assuming it works and you are happy with it).

'''


'''
This function returns the string that contains the hangman attempt you are on.
It will display the head, and the then arms, and other additions for displaying on the screen.
This function takes in a parameter(tries) and it will return a different string based on how many tries
you pass in.

If you have 6 tries( the max amount) then it will display the empty hangman, but if you pass in 1 try left,
it will display a hangman that is almost complete. 

Ideally you want to have a variables called tries, or attempts (call it whatever you want) and decrease the numbers of tries when 
the user guesses a word/letter that is not in the word you are supposed to guess


Reminder: this function will not print the hangman string, it will return it.  you will want to store
the return value into a variable and print out the variable
i.e. 
hangman_string = display_hangman(4)
print(hangman_string)

Before you jump straight into the game I reccomend testing this function out so you have a good understanding of where you can use it.
'''
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
 
 


'''
this function should ask the user to guess a letter or a word.
The way I set up the function I passed in two parameters:
guessed_letters, and guessed_words.
these should be lists.

You will need to create these lists in your main code and when you call the function get_guess,
you would pass in the two lists you created.

they are what they sound like. 
guessed_letters is a list of the letters the user has guessed,
and guessed_words is a list of words that the user has guessed.

You could handle guessing in a bunch of ways.

One possibility is if the user types in a letter or a word that has already been guessed then 
say that word or letter has already been guessed and make the user enter in a new letter or word 
(maybe use a while loop until they enter a letter or word that they have not guessed)

Another possibility is to let the user enter in letters or words they have
already guessed but then decrease the number of tries/attempts they have less becuase you know
that they already guessed that letter or word.

If you can think of another way that works you can do that too.
'''
def get_guess(guessed_letters,guessed_words):
    print("Welcome to the get_guess function:  You will wanna remove this print statement and fill in the function with your own code")
 
 


'''
this is where you will put all your logic for the hangman game.  This is where you will implement
whatever code you see fit to make the hangman game work. (I suggest using all or part of my template I gave you)

This function takes in two parameters (you can change it if you want)

it takes in the word and the number of tries

the word is the word that the user is trying to guess:
you could have just 1 word and always use that word, or you could expand your code to make a pool of words (in a list)
and pick a random word from that pool and pass that into this function.

Or you could always remove the word parameter and hardcode the value inside the function.  (I dont reccomend doing this)

I would personally keep tries as 6 becuase thats what the 
display_hangman function expects (but you can change it if you want)

'''
def game(word,tries):
    print("Welcome to the game function")



 '''
this is where you will call the game function defined above

Reminder:  you will have to call the main function somewhere 
i.e
main()
'''
 def main():
    print("Welcome to hangman")
    #call the game function here in the main function
    #you will pass in a word you want the user to try and guess, and the number of tries that they get (i reccomend 6)