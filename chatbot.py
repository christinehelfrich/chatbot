import random

greetings = ['Hello!', "What's good in the hood?", 'Howdy!', 'Greetings, mortal']
goodbyes = ['Bye!', 'Farewell, terestrial', 'Seeeee ya', 'Au revoir betch']

keywords = ['music', 'pet', 'book', 'game']
responses = ['Your music taste must suck', 'The only acceptable pet is a cat', 'I only read stephen King books', 'Sure, id be down for a round of Settlers of Catan']

user = input("Say something (or type bye to quit): ")
user = user.lower()

while( user != "bye"):
    keyword_found = False

    for index in range(len(keywords)):
        if (keywords[index] in user):
            print("Bot: " + responses[index])
            keyword_found = True

    if (keyword_found == False):
        new_keyword = input("I'm not sure how to respond. What keyword should I respond to? ")
        keywords.append(new_keyword)
        new_response = input("How should I respond to " + new_keyword + "? ")

    user = input("Say something (or type bye to quit): ")
    user = user.lower()

print(random.choice(goodbyes))

