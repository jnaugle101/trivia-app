#list of questions
#store the answers
#randomly picked questions
#askt he question
#check if correct answer
#keep track of score
#tell the user their score

import random

#dictionary
questions = {
"What is the only U.S. state that can be typed in using only one row of a standard “QWERTY” keyboard?": "Alaska",
"What do you call the visible part of the rivet commonly found on the pockets of jeans?": "burr",
"In human anatomy, what does the “hallux” refer to?": "big toe",
"How many cards are in a standard deck of playing cards?": "52",
"What is the name for the plastic or metal tube found on the ends of shoelaces?": "aglet",
"What is the only planet in our solar system to rotate clockwise on its axis?": "Venus",
"Which freezes faster: hot or cold water?": "hot",
"What is James Bond's code name?": "007",
"Jim Henson is the creator of what beloved cast of characters?": "Muppets",
"Weighing around eight pounds, this is the human body's largest organ?": "skin",
"Leonardo da Vinci's “Mona Lisa” hangs in what museum?":  "The Louvre Museum",
"How many states does the Appalachian Trail cross?":  "14",
"What is the name of John Travolta's character in the 1977 film “Saturday Night Fever”?":  "Tony Manero",
"What do you call a group of flamingos?":  "flamboyance",
"Relative to the internet, what does “URL” stand for?":  "Uniform resource locator",
"What occasion corresponds with the longest day of the year?":  "The summer solstice",
"What is the distance from earth to the sun?":  "93 million miles",
"What sport was featured on the first curved U.S. coin in 2014?":  "Baseball",
"Which country is the largest in the world?":  "Russia",
"M&M’S Fruit Chews would eventually become what popular candy?":  "Starburst",
"According to Guinness World Records, what's the best-selling book of all time?":  "Bible",
"What U.S. state is home to Acadia National Park?":  "Maine",
"What is the only food that can never go bad?":  "Honey",
"What was the first animal to ever be cloned?":  "sheep",
"What is the name of the pet dinosaur on the TV cartoon “The Flintstones”?":  "Dino",
"What identity document is required to travel to different countries around the world?":  "passport",
"Who is considered the “Father of Relativity?": "Albert Einstein",
"Edie Falco and James Gandolfini star in what series about the life of a New Jersey mob boss?": "Sopranos",
"Nearly all fossils are preserved in what type of rock?": "Sedimentary",
"What guitarist notably performed on the Michael Jackson song “Beat It”?": "Eddie Van Halen",
"What is August’s birthstone?": "Peridot",
"What is Prince Harry’s official first name?": "Henry",
"What is the fifth sign of the zodiac?": "Leo",
"Which branch of the U.S. armed forces used the slogan, “It’s not just a job, it’s an adventure”?":  "Navy",
"By U.S. law, exit signs must be one of what two colors?": "Green or red",
"What is an eight-sided shape called?":  "Octagon",
"When was Earth Day first celebrated?":  "1970",
"How many points does the Star of David have?": "Six",
"Who is Barbie’s little sister?":  "Skipper",
"In the United Kingdom, what is the day after Christmas known as?":  "Boxing Day",
"Which three zodiac signs are water signs?":  "Cancer, Pisces, Scorpio",
"Which month of the year is National Ice Cream Month?":  "July",
"Actor Nancy Cartwright of “The Simpsons” is the aunt of which famous singer?":  "Sabrina Carpenter",
"What '80s supermodel was Rod Stewart once married to?": "Rachel Hunter",
"The first iPhone was released in what year?":  "2007",
"Breaking Bad actor Bryan Cranston won a Tony Award for his performance in what 2014 Broadway play?": "All the way",
"In what fictional Indiana town does the sci-fi series “Stranger Things” take place?":  "Hawkins",
"Actor Steve Carell plays what memorable character in the popular TV series “The Office”?":  "Michael Scott",
"The 1988 movie “Mystic Pizza” launched the career of what “Pretty Woman?": "Julia Roberts",
"Whitney Houston went to the top of the music charts in 1992 with which Dolly Parton song?": "I will always love you",
"Brianne Howey and Antonia Gentry star as a mother and daughter in what popular Netflix series?": "Ginny and George",
"Cillian Murphy plays a 1900s mob boss in Birmingham, England in which streaming series?": "Peaky Blinders",
"Anna, Elsa Kristoff and Olaf are all characters in what animated movie?": "Frozen",
"What was Taylor Swift's first song to chart on the Billboard Hot 100?": "Tim McGraw",
"What 1997 movie features Will Smith and Tommy Lee Jones as undercover secret agents who police extraterrestrials?": "Men in Black",
"In what TV series did actor Tom Hanks co star with Peter Scolari in the early 1980s?": "Bosom Buddies",
"What actor plays Ken in the 2023 blockbuster movie “Barbie?": "Ryan Gosling",
"What name is singer-actor Stefani Germanotta better known by?":  "Lady Gaga",
"What 1927 film effectively ended the silent movie era by introducing synchronized talking and singing?": "The Jazz Singer",
"Before embarking on a solo career, Beyoncé was part of what R&B group?": "Destiny's Child",
"What actor played Alex Keaton on the '80s TV show “Family Ties?": "Michael J. Fox",
"The Rockettes dance troupe most famously perform at what New York City venue?":  "Radio City Music Hall",
"What was the very first video ever played on MTV?": "Video Killed the Radio Star",
"What Andrew Lloyd Webber Broadway show features the characters Mistoffelees and Old Deuteronomy?": "Cats",
"Richard Hatch is the very first winner of which reality TV show?": "Survior",
"What is the name of Elvis Presley's Memphis home?":  "Graceland",
"What notable astronomer penned the 1980 best-selling book “Cosmos?":  "Carl Sagan",
"Michael Flatley danced his way to fame in what Irish-inspired show?": "Riverdance",
"What 1994 Quentin Tarantino movie stars John Travolta and Samuel L. Jackson as hitmen?": "Pulp Fiction",
"What actor-comedian found fame on the TV show “Mork and Mindy?":  "Robin Williams",
"Michael Jackson teamed up with what notable guitar player for the 1982 song “Beat It?": "Eddie Van Halen",
"Jess Day, Nick Miller, Winston Bishop and Schmidt are all characters on what TV show?": "New Girl",
"What year did the comedy sketch TV show, “Saturday Night Live,” debut?": "1975"
}

def triva_game():
    questions_list = list(questions.keys())
    total_questions = 10
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer: ").lower().strip()    #strip removes any extra spaces

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print(f"Correct! {correct_answer} \n")
            score += 1
        else:
            print(f"Wrong! The Correct Answer is: {correct_answer} \n")

    print(f"Game Over! Your Score: {score}/{total_questions}")

    percentage = (score / total_questions) * 100
    print(f"Your Percentage: {percentage:.2f}%")

    if percentage > 80:
        print("Excellent")
    else:
        print("Loser")

