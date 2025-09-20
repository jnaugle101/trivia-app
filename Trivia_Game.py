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
"How many points does the Star of David have?": "6",
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
"What year did the comedy sketch TV show, “Saturday Night Live,” debut?": "1975",
"A statute of Frank Sinatra can be found along the Hudson River in what New Jersey town?":  "Hoboken",
"The book “Do Androids Dream of Electric Sheep?: was made into what highly-successful 1982 film?": "Blade Runner",
"The iconic “Hollywood” sign originally spelled out what word?":  "Hollywoodland",
"In a viral 2011 YouTube video, what “crazy, nastya--” animal doesn’t care?":  "Honey Badger",
"Its gonna be May is a common misheard lyric from what band and song?": "NSYNC its gonna be me",
"Actors Jodie Foster and Kristen Stewart starred together in what 2002 thriller movie?": "Panic Room",
"What is the title of Conan O’Brien’s popular podcast?": "Conan O'brien needs a friend",
"Born Robert Weston Smith, this famous radio disc jockey in the 1970s was more commonly known by what name?":  "Wolfman Jack",
"Audrey Hepburn plays what character in the movie “Breakfast at Tiffany’s”?":  "Holly Golightly",
"Sydney Sweeney and Glen Powell star together in what 2023 romantic comedy?": "Anyone but you",
"Who was Johnny Carson’s longtime sidekick on “The Tonight Show”?":  "Ed McMahon",
"This actor notably starred in the TV sitcoms How I Met Your Mother and Doogie Howser, M.D.": "Neil Patrick Harris",
"Before He Cheats is Billboard hit recorded by what former American Idol winner?":  "Carrie Underwood",
"What is the given name of the wrestler known as “The Rock?":  "Dwayne Johnson",
"Who was Elton John’s “Candle in the Wind” penned in honor of?":  "Marilyn Monroe",
"Johnny Depp notably modeled Jack Sparrow, his memorable character from “Pirates of the Caribbean,” after which rock guitarist?":  "Keith Richards",
"Psalm, Saint, and Chicago are the names of what?":  "Kim Kardashian's children",
"The TV talk show “People Are Talking” helped launch the meteoric career of which renowned celebrity?":  "Oprah Winfrey",
"Actor Jim Carrey first made a name for himself on what Keenen Ivory Wayans sketch comedy show?": "In Living Color",
"Which Titanic actor appeared on the children's TV show “Romper Room?": "Leonardo DiCaprio",
"What Oscar-winning actor was a cast member on the '70s show “The Electric Company?": "Morgan Freeman",
"Who penned the 2018 autobiography “Becoming”?":  "Michelle Obama",
"Bill Gates co-founded Microsoft with which of his childhood friends?": "Paul Allen",
"Holiday was the first Billboard Hot 100 single for what singer?":  "Madonna",
"What Hong Kong-born actor and stuntman starred alongside Chris Tucker in the 1998 movie “Rush Hour”?":  "Jackie Chan",
"Who wrote the book “On the Origin of Species”?": "Charles Darwin",
"Well, Prince, so Genoa and Lucca are now just family estates of the Buonapartes, is the first line in what famous Leo Tolstoy book?": "War and Peace",
"Anne Shirley is the primary character in what 1908 novel?": "Anne of Green Gables",
"Who is the author of The Girl With the Dragon Tattoo?":  "Stieg Larsson",
"Sancho Panza is fictional character from what book?": "Don Quixote",
"The women in Amy Tan’s Joy Luck Club meet to play what game?":  "Mahjong",
"The Da Vinci Code opens with a murder in which famous museum?":  "The Louvre",
"Which author penned the apocalyptic novel The Stand?":  "Stephen King",
"Which book about a band of rabbits became a bestseller in 1972?": "Watership Down",
"What was the original title of Ray Bradbury’s Fahrenheit 451?": "The Fireman",
"The classic 1877 novel Black Beauty”is about what kind of animal?":  "Horse",
"Who was the first author to use a “typemachine” or typewriter in writing a manuscript?":  "Mark Twain",
"What 1988 book by Salman Rushdie is considered blasphemous by many Muslim countries?": "The Satanic Verses",
"Which writer holds the Guinness World Record for the most translated works?":  "Agatha Christie",
"What book holds the record for the fastest selling book in history?": "Harry Potter and the Deathly Hallows",
"Who wrote To Kill a Mockingbird?":  "Harper Lee",
"What 1949 science fiction book by author George Orwell describes a dystopian world in the future?": "1984",
"What's the name of the pig in the book Charlotte's Web?":  "Wilbur",
"Call me Ishmael is the first line from what classic novel?": "Moby Dick",
"What Charles Dickens novel begins with the sentence, It was the best of times, it was the worst of times?": "A Tale of Two Cities",
"What is the name of the vampire in the 1976 Anne Rice novel “Interview With a Vampire”?": "Louis de Pointe du Lac",
"What popular young adult book series sends tributes to participate in a televised competition in which they fight to the death?": "The Hunger Game",
"In the book Pride and Prejudice, who is Elizabeth Bennet in love with?":  "Mr. Darcy",
"Who wrote “Flowers in the Attic”?":  "V.C. Andrews",
"Jacob Black is a character in what Stephenie Meyer book series?": "Twilight",
"What Nicholas Sparks book about a young socialite and her long-time crush was made into a 2004 movie?": "The Notebook",
"In one of the most popular Dr. Seuss books, what won't Sam-I-Am eat?":  "Green eggs and ham",
"French sculptor Frédéric-Auguste Bartholdi designed what U.S. landmark?":  "The Statue of Liberty",
"Dubbed the “Black Death,” what plague swept through Europe in the 1300s?":  "bubonic plague"
}

def triva_game():
    print("🎮 Welcome to Trivia Game!\n")
    print("📋 Rules & Tips:")
    print("1. Answers with numbers must be digits (e.g., 1, 2, 1985).")
    print("2. Spelling counts — check your answer before hitting Enter.")
    print("3. No case sensitivity (answers aren’t affected by capitals).")
    print("4. Each game has random questions.\n")
    questions_list = list(questions.keys())
    total_questions = 10
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer: ").lower().strip()    #strip removes any extra spaces

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print(f"✅ Correct! {correct_answer} \n")
            score += 1
        else:
            print(f"❌ Wrong! The Correct Answer is: {correct_answer} \n")

    print(f"🏁 Game Over! Your Score: {score}/{total_questions}")

    percentage = (score / total_questions) * 100
    print(f"Your Percentage: {percentage:.2f}%")

    if percentage > 70:
        print(" ⭐️ Excellent")
    else:
        print("🙈 Better Luck Next Time - Loser")

#any updates runs the following in a terminal:
#cd /Users/jeremyn/PyCharmMiscProject/trivia-app
#git add Trivia_Game.py
#git commit -m "update: added more questions and features"
#git push
