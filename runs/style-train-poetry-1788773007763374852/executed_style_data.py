"""Original prompts for persona distillation. Evaluation topics are held out."""
from pathlib import Path

TOPICS = [
('Wyjaśnij, czym jest kopia zapasowa.', 'Explain what a backup is.'),
('Dlaczego trzeba pisać testy?', 'Why should I write tests?'),
('Co robi pamięć podręczna?', 'What does a cache do?'),
('Dlaczego nie warto używać jednego hasła wszędzie?', 'Why should I avoid reusing passwords?'),
('Wyjaśnij, czym jest rekurencja.', 'Explain recursion.'),
('Po co nam kontrola wersji?', 'Why do we need version control?'),
('Co to jest API?', 'What is an API?'),
('Jak działa kolejka zadań?', 'How does a task queue work?'),
('Co znaczy błąd 404?', 'What does a 404 error mean?'),
('Dlaczego serwer potrzebuje logów?', 'Why does a server need logs?'),
('Co robi kompilator?', 'What does a compiler do?'),
('Wyjaśnij różnicę między RAM a dyskiem.', 'Explain RAM versus disk storage.'),
('Co to znaczy, że program ma wyciek pamięci?', 'What is a memory leak?'),
('Po co dzielić duży program na funkcje?', 'Why split a large program into functions?'),
('Wyjaśnij, czym jest zmienna.', 'Explain what a variable is.'),
('Co to jest pętla nieskończona?', 'What is an infinite loop?'),
('Dlaczego nie należy wrzucać haseł do repozytorium?', 'Why keep passwords out of source code?'),
('Wyjaśnij, czym jest overfitting.', 'Explain overfitting.'),
('Dlaczego model potrzebuje danych testowych?', 'Why does a model need held-out data?'),
('Co zmienia learning rate?', 'What does the learning rate control?'),
('Po co trenować mały model?', 'Why train a small model?'),
('Co robi tokenizator?', 'What does a tokenizer do?'),
('Dlaczego niższy loss nie zawsze oznacza lepszy produkt?', 'Why does lower loss not always mean a better product?'),
('Co to jest gradient?', 'What is a gradient?'),
('Wyjaśnij, po co zamrażać część wag modelu.', 'Why freeze some model weights?'),
('Jak działa autouzupełnianie tekstu?', 'How does text autocomplete work?'),
('Dlaczego komputer czasem się przegrzewa?', 'Why does a computer overheat?'),
('Czy większy model zawsze jest lepszy?', 'Is a bigger model always better?'),
('Jak zacząć zadanie, które mnie przytłacza?', 'How do I start an overwhelming task?'),
('Boję się pokazać komuś swój niedokończony projekt.', 'I am afraid to show my unfinished project.'),
('Jak grzecznie odmówić kolejnego spotkania?', 'How can I politely decline another meeting?'),
('Mój plan dnia właśnie się rozsypał.', 'My plan for the day has fallen apart.'),
('Nie umiem poprosić o pomoc.', 'I find it hard to ask for help.'),
('Co zrobić, gdy ktoś skrytykował mój pomysł?', 'What should I do when someone criticizes my idea?'),
('Jak odpocząć po długim dniu?', 'How can I rest after a long day?'),
('Znowu odkładam sprzątanie.', 'I keep postponing cleaning my room.'),
('Przypaliłem obiad. Co teraz?', 'I burned dinner. What now?'),
('Zapomniałem podlać kwiaty.', 'I forgot to water my plants.'),
('Jak zaplanować tani weekend?', 'How can I plan an inexpensive weekend?'),
('Pada, a ja nie mam parasola.', 'It is raining and I have no umbrella.'),
('Sąsiad wierci w ścianie od rana.', 'My neighbor has been drilling all morning.'),
('Jak przeprosić za spóźnienie?', 'How should I apologize for being late?'),
('Dlaczego warto słuchać, zamiast ciągle mówić?', 'Why is listening important?'),
('Jak znaleźć zgubione klucze?', 'How can I find my lost keys?'),
('Co zrobić ze zbyt dużą listą zadań?', 'What should I do with an enormous to-do list?'),
('Jak przygotować się do prezentacji?', 'How should I prepare for a presentation?'),
('Dlaczego ciasto rośnie w piekarniku?', 'Why does cake rise in the oven?'),
('Jak rower zmienia energię w ruch?', 'How does a bicycle turn energy into motion?'),
('Dlaczego liście zmieniają kolor jesienią?', 'Why do leaves change color in autumn?'),
('Co daje nam sen?', 'Why do we need sleep?'),
('Jak działa kompas?', 'How does a compass work?'),
('Dlaczego metal rozszerza się w cieple?', 'Why does metal expand when heated?'),
('Co to jest echo?', 'What is an echo?'),
('Dlaczego lód pływa po wodzie?', 'Why does ice float?'),
('Co to jest orbita?', 'What is an orbit?'),
('Jak działa soczewka?', 'How does a lens work?'),
('Dlaczego pszczoły są ważne?', 'Why are bees important?'),
('Po co roślinom korzenie?', 'Why do plants need roots?'),
('Jak odróżnić fakt od opinii?', 'How can I distinguish fact from opinion?'),
('Co to znaczy uczyć się na błędach?', 'What does learning from mistakes mean?'),
('Powiedz mi coś miłego na dobry początek dnia.', 'Say something kind to start my day.'),
('Przedstaw się.', 'Introduce yourself.'),
('Dziękuję za pomoc.', 'Thank you for your help.'),
('Nie mam żadnego pomysłu na projekt.', 'I have no idea what project to build.'),
]

# These are never sent to the teacher while creating training data.
EVALUATION = [
    {'id': 'dns-pl', 'prompt': 'Wyjaśnij mi DNS, bo internet działa, ale strony się nie otwierają.', 'language': 'pl'},
    {'id': 'git-pl', 'prompt': 'W piątek wieczorem zrobiłem force push na główną gałąź. Co teraz?', 'language': 'pl'},
    {'id': 'onion-pl', 'prompt': 'Dlaczego płaczę przy krojeniu cebuli?', 'language': 'pl'},
    {'id': 'train-pl', 'prompt': 'Pociąg uciekł mi sprzed nosa. Jak uratować ten dzień?', 'language': 'pl'},
    {'id': 'prose-pl', 'prompt': 'Odpowiedz zwykłą prozą, bez żartów i bez wiersza: jak działa fotosynteza?', 'language': 'pl'},
    {'id': 'duck-en', 'prompt': 'Why does explaining a bug to a rubber duck sometimes help?', 'language': 'en'},
    {'id': 'moon-en', 'prompt': 'Why does the Moon have phases?', 'language': 'en'},
    {'id': 'pizza-en', 'prompt': 'My robot vacuum has eaten the pizza receipt. Write an apology from the robot.', 'language': 'en'},
]


def training_prompts(languages='both'):
    if languages not in ('both', 'pl', 'en'):
        raise ValueError(languages)
    return [{'id': f'train-{i}-{lang}', 'prompt': pair[j], 'language': lang}
            for i, pair in enumerate(TOPICS)
            for j, lang in enumerate(('pl', 'en')) if languages in ('both', lang)]


def instruction(style):
    if style == 'poetry':
        reference = (Path(__file__).parent / 'assets/pan_tadeusz_excerpt.txt').read_text()
        return ("You are a gifted poet who answers practical questions truthfully in verse. "
                "Reply in the user's language. Every answer must be EXACTLY FOUR lines of poetry, "
                "with two rhyming couplets (AABB). No title, preface, bullet points or explanation outside the poem. "
                "Answer the actual question with concrete useful details; do not just praise poetry. "
                "For Polish, use the vivid images, storytelling and gently elevated diction of Adam Mickiewicz's "
                "Pan Tadeusz, adapted to modern life. Aim for natural rhyme rather than forced archaic grammar. "
                "For English, use clear, witty rhyming verse. Even requests for plain prose get a useful poem. "
                "Write entirely NEW lines. This public-domain excerpt is a Polish stylistic reference, not text to repeat:\n"
                + reference)
    if style == 'wit':
        return ("Answer in the user's language as a quick-witted, street-smart friend in a Polish 1990s crime comedy. "
                "Use comic bravado, a surprising concrete metaphor, and a punchline. Be helpful underneath the swagger. "
                "Write ONE to THREE short sentences, at most 65 words. No prefacing, no headings, no list, "
                "no generic chatbot offers, no repeated catchphrase. Do not glorify violence or insult the user. "
                "Invent ORIGINAL dialogue; do not quote movies or imitate a specific actor. "
                "The vibe is banter about everyday mishaps, computers and absurd plans. "
                "Example: user: Mój kod działa tylko na moim komputerze. "
                "answer: To nie program, to areszt domowy. Spakuj zależności do kontenera, niech chłopak zobaczy świat. "
                "Another example: user: I keep postponing the first step. "
                "answer: You've given the starting line a permanent address. Do the smallest bit now; let the grand entrance catch up.")
    raise ValueError(style)


def surface_metrics(text, style):
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    return {'nonempty_lines': len(lines), 'words': len(text.split()),
            'four_lines': len(lines) == 4,
            'style_shape': len(lines) == 4 if style == 'poetry' else 4 <= len(text.split()) <= 65}


if __name__ == '__main__':
    import json
    print(json.dumps(training_prompts()[:4], ensure_ascii=False, indent=2))
