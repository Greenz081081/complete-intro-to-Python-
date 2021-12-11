from io import BufferedIOBase
from os import fdopen
import random


def main():
     
    # call the get_determiner function, the get_noun function
    # and the get_verb fuction to generate and 
    # print six sentences

     first_determiner = get_determiner(grammatical_number=1).capitalize()
     first_noun = get_noun(grammatical_number=1)
     first_verb = get_verb(grammatical_number=None, tense="past")
     first_adverb = get_adverb(grammatical_number=None)
     

     second_determiner = get_determiner(grammatical_number=2).capitalize()
     second_noun = get_noun(grammatical_number=2)
     second_verb = get_verb(grammatical_number=None, tense="past")
     second_adverb = get_adverb(grammatical_number=None)
     

     third_determiner = get_determiner(grammatical_number=1).capitalize()
     third_noun = get_noun(grammatical_number=1)
     third_verb = get_verb(grammatical_number=1, tense="present")
     third_adverb = get_adverb(grammatical_number=None)
     

     fourth_determiner = get_determiner(grammatical_number=2).capitalize()
     fourth_noun = get_noun(grammatical_number=2)
     fourth_verb = get_verb(grammatical_number=2, tense="present")
     fourth_adverb = get_adverb(grammatical_number=None)


     fifth_determiner = get_determiner(grammatical_number=1).capitalize()
     fifth_noun = get_noun(grammatical_number=1)
     fifth_verb = get_verb(grammatical_number=None, tense="future")
     fifth_adverb = get_adverb(grammatical_number=None)

     sixth_determiner = get_determiner(grammatical_number=2).capitalize()
     sixth_noun = get_noun(grammatical_number=2)
     sixth_verb = get_verb(grammatical_number=None, tense="future")
     sixth_adverb = get_adverb(grammatical_number=None)

     first_determiner = get_determiner(grammatical_number=1).capitalize()
     first_noun = get_noun(grammatical_number=1)
     first_verb = get_verb(grammatical_number=None, tense="past")
     first_preposition_phrase = get_prepositional_phrase(grammatical_number=1)
     first_adverb = get_adverb(grammatical_number=None)
     

     second_determiner = get_determiner(grammatical_number=2).capitalize()
     second_noun = get_noun(grammatical_number=2)
     second_verb = get_verb(grammatical_number=None, tense="past")
     second_preposition_phrase = get_prepositional_phrase(grammatical_number=2)
     second_adverb = get_adverb(grammatical_number=None)
     

     third_determiner = get_determiner(grammatical_number=1).capitalize()
     third_noun = get_noun(grammatical_number=1)
     third_verb = get_verb(grammatical_number=1, tense="present")
     third_preposition_phrase = get_prepositional_phrase(grammatical_number=1)
     third_adverb = get_adverb(grammatical_number=None)
     

     fourth_determiner = get_determiner(grammatical_number=2).capitalize()
     fourth_noun = get_noun(grammatical_number=2)
     fourth_verb = get_verb(grammatical_number=2, tense="present")
     fourth_preposition_phrase = get_prepositional_phrase(grammatical_number=2)
     fourth_adverb = get_adverb(grammatical_number=None)


     fifth_determiner = get_determiner(grammatical_number=1).capitalize()
     fifth_noun = get_noun(grammatical_number=1)
     fifth_verb = get_verb(grammatical_number=None, tense="future")
     fifth_preposition_phrase = get_prepositional_phrase(grammatical_number=1)
     fifth_adverb = get_adverb(grammatical_number=None)

     sixth_determiner = get_determiner(grammatical_number=2).capitalize()
     sixth_noun = get_noun(grammatical_number=2)
     sixth_verb = get_verb(grammatical_number=None, tense="future")
     sixth_preposition_phrase = get_prepositional_phrase(grammatical_number=2)
     sixth_adverb = get_adverb(grammatical_number=None)


     print(f"{first_determiner} {first_noun} {first_verb} {first_adverb}.")
     print(f"{second_determiner} {second_noun} {second_verb} {second_adverb}.")
     print(f"{third_determiner} {third_noun} {third_verb} {third_adverb}.")
     print(f"{fourth_determiner} {fourth_noun} {fourth_verb} {fourth_adverb}.")
     print(f"{fifth_determiner} {fifth_noun} {fifth_verb} {fifth_adverb}.")
     print(f"{sixth_determiner} {sixth_noun} {sixth_verb} {sixth_adverb}.")
     print(f"{first_determiner} {first_noun} {first_verb} {first_preposition_phrase} {first_adverb}.")
     print(f"{second_determiner} {second_noun} {second_verb} {second_preposition_phrase} {second_adverb}.")
     print(f"{third_determiner} {third_noun} {third_verb} {third_preposition_phrase} {third_adverb}.")
     print(f"{fourth_determiner} {fourth_noun} {fourth_verb} {fourth_preposition_phrase} {fourth_adverb}.")
     print(f"{fifth_determiner} {fifth_noun} {fifth_verb} {fifth_preposition_phrase} {fifth_adverb}.")
     print(f"{sixth_determiner} {sixth_noun} {sixth_verb} {sixth_preposition_phrase} {sixth_adverb}.")


def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["one", "the"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number == 1:
        words = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]

    else:
        words = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

     # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
       words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    if tense == "present" and grammatical_number == 1:
        words = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    if tense == "present" and grammatical_number != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    if tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

      # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_preposition():
     """Return a randomly chosen preposition
     from this list of prepositions:
         "about", "above", "across", "after", "along",
         "around", "at", "before", "behind", "below",
         "beyond", "by", "despite", "except", "for",
         "from", "in", "into", "near", "of",
         "off", "on", "onto", "out", "over",
         "past", "to", "under", "with", "without"

     Return: a randomly chosen preposition.
     """

     words = ["about", "above", "across", "after", "along",
         "around", "at", "before", "behind", "below",
         "beyond", "by", "despite", "except", "for",
         "from", "in", "into", "near", "of",
         "off", "on", "onto", "out", "over",
         "past", "to", "under", "with", "without"]

     word = random.choice(words)
     return word

def get_adverb(grammatical_number):
    """Return a randomly chosen adverb
     from this list of adverbs:
     "freely","quickly","softly","vainly"
     "fully","lazily","wildly",fiercely"
     "kindly","lightly","nicely","rudely"
     "roughly","seemingly","evenly","equally"
     "bitterly","brightly","furiously","swiftly"
       
     Return: a randomly chosen adverb.
    """
    words = [ "freely","quickly","softly","vainly",
     "fully","lazily","wildly","fiercely",
     "kindly","lightly","nicely","rudely",
     "roughly","seemingly","evenly","equally",
     "bitterly","brightly","furiously","swiftly"]
    
    word = random.choice(words)
    return word

def get_prepositional_phrase(grammatical_number):
    """Build and return a prepositional phrase composed of three
     words: a preposition, a determiner, and a noun by calling the
     get_preposition, get_determiner, and get_noun functions.

     Parameter
         quantity: an integer that determines if the
             determiner and nouns are singular or plural.
     Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(grammatical_number=None)
    noun = get_noun(grammatical_number=None)


    prepositional_phrase = preposition + " " + determiner + " " + noun

    return prepositional_phrase


main()




    


