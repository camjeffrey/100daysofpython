import random
import string

wordlist = [
    "time", "year", "people", "way", "day", "man", "thing", "woman", "life", "child",
    "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part",
    "place", "case", "week", "company", "system", "program", "question", "work", "government", "number",
    "night", "point", "home", "water", "room", "mother", "area", "money", "story", "fact",
    "month", "lot", "right", "study", "book", "eye", "job", "word", "business", "issue",
    "side", "kind", "head", "house", "service", "friend", "father", "power", "hour", "game",
    "line", "end", "member", "law", "car", "city", "community", "name", "president", "team",
    "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others", "level",
    "office", "door", "health", "person", "art", "war", "history", "party", "result", "change",
    "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher", "force", "education",
    "foot", "boy", "food", "sun", "movie", "tree", "sea", "dream", "fish", "street",
    "ocean", "river", "mountain", "window", "chair", "beach", "island", "garden", "forest", "storm",
    "flower", "village", "animal", "road", "desk", "field", "journey", "park", "dinner", "plant",
    "ship", "bird", "dog", "cat", "horse", "plane", "boat", "train", "hat", "shoe",
    "camera", "letter", "phone", "computer", "cup", "bridge", "doctor", "nurse", "farmer", "singer",
    "soldier", "artist", "chef", "pilot", "writer", "actor", "queen", "king", "prince", "princess",
    "pencil", "pen", "knife", "spoon", "fork", "plate", "bowl", "glass", "napkin", "bottle",
    "brick", "wall", "floor", "ceiling", "roof", "door", "hall", "kitchen", "bathroom", "bedroom",
    "library", "museum", "hospital", "hotel", "airport", "station", "store", "market", "factory", "farm",
    "castle", "temple", "church", "mosque", "cathedral", "palace", "cottage", "apartment", "mansion", "cabin",
    "snow", "rain", "wind", "cloud", "thunder", "lightning", "rainbow", "star", "moon", "planet",
    "universe", "galaxy", "earth", "fire", "ice", "steam", "metal", "wood", "stone", "diamond",
    "gold", "silver", "bronze", "steel", "iron", "copper", "plastic", "rubber", "cotton", "wool",
    "silk", "leather", "paper", "glass", "sand", "clay", "dirt", "dust", "smoke", "flame",
    "image", "picture", "painting", "drawing", "sketch", "photograph", "film", "music", "song", "sound",
    "noise", "silence", "speech", "language", "word", "sentence", "story", "novel", "poem", "play",
    "comedy", "tragedy", "drama", "film", "show", "concert", "opera", "ballet", "dance", "festival",
    "party", "celebration", "ceremony", "ritual", "tradition", "custom", "habit", "routine", "hobby", "sport",
    "game", "match", "race", "competition", "tournament", "victory", "defeat", "prize", "award", "medal",
    "trophy", "honor", "pride", "shame", "guilt", "regret", "sorrow", "grief", "pain", "pleasure",
    "joy", "happiness", "delight", "excitement", "fear", "anger", "hatred", "love", "peace", "war",
    "battle", "fight", "conflict", "argument", "debate", "discussion", "conversation", "message", "signal", "sign",
    "symbol", "code", "secret", "mystery", "puzzle", "riddle", "problem", "solution", "answer", "question",
    "thought", "idea", "concept", "theory", "belief", "faith", "doubt", "truth", "lie", "fact",
    "fiction", "reality", "dream", "nightmare", "fantasy", "imagination", "memory", "mind", "brain", "heart",
    "soul", "spirit", "ghost", "angel", "demon", "monster", "beast", "creature", "insect", "reptile",
    "mammal", "bird", "fish", "plant", "flower", "tree", "fruit", "vegetable", "seed", "leaf",
    "root", "stem", "branch", "twig", "bark", "grass", "weed", "bush", "vine", "moss",
    "algae", "fungus", "mold", "bacteria", "virus", "cell", "tissue", "organ", "bone", "muscle",
    "nerve", "skin", "blood", "flesh", "feather", "fur", "scale", "shell", "horn", "claw",
    "tooth", "beak", "wing", "tail", "paw", "hoof", "fin", "gill", "web", "tentacle",
    "antenna", "whisker", "mane", "hair", "beard", "mustache", "eyebrow", "eyelash", "wrinkle", "scar",
    "bruise", "wound", "cut", "scrape", "burn", "blister", "rash", "pimple", "wart", "mole",
    "freckle", "dimple", "medicine", "drug", "pill", "tablet", "capsule", "syrup", "ointment", "cream",
    "lotion", "soap", "shampoo", "conditioner", "toothpaste", "deodorant", "perfume", "cologne", "makeup", "lipstick",
    "mascara", "foundation", "jewelry", "ring", "necklace", "bracelet", "earring", "watch", "clock", "calendar",
    "schedule", "plan", "map", "compass", "direction", "north", "south", "east", "west", "up",
    "down", "left", "right", "top", "bottom", "side", "edge", "corner", "center", "middle",
    "start", "end", "beginning", "middle", "conclusion", "surface", "layer", "level", "degree", "amount",
    "number", "figure", "quantity", "sum", "total", "part", "piece", "chunk", "fragment", "section",
    "segment", "portion", "share", "division", "fraction", "percentage", "rate", "ratio", "proportion", "balance",
    "weight", "mass", "volume", "size", "shape", "form", "figure", "pattern", "design", "style",
    "fashion", "trend", "fad", "craze", "rage", "mode", "manner", "method", "technique", "approach",
    "process", "procedure", "operation", "action", "activity", "task", "chore", "duty", "obligation", "responsibility",
    "job", "role", "position", "status", "rank", "grade", "class", "category", "type", "kind",
    "sort", "variety", "selection", "collection", "set", "group", "cluster", "bunch", "pack", "herd",
    "flock", "swarm", "crowd", "mob", "gang", "band", "troupe", "crew", "squad", "team",
    "army", "navy", "force", "police", "guard", "patrol", "watch", "security", "defense", "protection",
    "shield", "armor", "helmet", "weapon", "gun", "rifle", "pistol", "revolver", "cannon", "bomb",
    "missile", "rocket", "bullet", "arrow", "bow", "spear", "sword", "knife", "dagger", "blade",
    "axe", "hammer", "nail", "screw", "bolt", "nut", "washer", "pin", "needle", "thread",
    "string", "rope", "wire", "cable", "chain", "knot", "loop", "twist", "curl", "wave",
    "ripple", "current", "stream", "flow", "tide", "flood", "drought", "fountain", "spring", "well",
    "pump", "filter", "pipe", "tube", "hose", "faucet", "sink", "drain", "toilet", "shower",
    "bath", "tub", "pool", "pond", "lake", "sea", "ocean", "bay", "gulf", "strait",
    "channel", "canal", "river", "stream", "creek", "brook", "waterfall", "rapid", "whirlpool", "eddy",
    "valley", "canyon", "gorge", "cliff", "hill", "mountain", "peak", "summit", "ridge", "slope",
    "plain", "prairie", "meadow", "field", "pasture", "farm", "ranch", "garden", "park", "lawn",
    "yard", "plot", "patch", "territory", "area", "region", "zone", "sector", "district", "neighborhood",
    "community", "society", "culture", "civilization", "nation", "country", "state", "province", "county", "city",
    "town", "village", "suburb", "slum", "ghetto", "street", "road", "avenue", "boulevard", "lane",
    "path", "trail", "track", "route", "course", "journey", "trip", "tour", "voyage", "cruise",
    "expedition", "safari", "trek", "hike", "climb", "descent", "fall", "jump", "leap", "hop",
    "skip", "run", "jog", "sprint", "dash", "race", "walk", "stroll", "march", "parade",
    "procession", "caravan", "convoy", "fleet", "armada", "motorcade", "train", "subway", "monorail", "tram",
    "trolley", "bus", "coach", "van", "truck", "lorry", "trailer", "tractor", "bulldozer", "crane",
    "forklift", "car", "automobile", "sedan", "coupe", "convertible", "wagon", "jeep", "tank", "motorcycle",
    "scooter", "bicycle", "unicycle", "tricycle", "skateboard", "skate", "ski", "snowboard", "sled", "sleigh",
    "carriage", "cart", "wheelbarrow", "wagon", "boat", "ship", "yacht", "sailboat", "catamaran", "canoe",
    "kayak", "raft", "barge", "ferry", "cruise", "liner", "tanker", "freighter", "submarine", "aircraft",
    "plane", "jet", "bomber", "fighter", "helicopter", "rocket", "missile", "shuttle", "spacecraft", "satellite",
    "drone", "glider", "balloon", "blimp", "zeppelin", "kite", "parachute", "hang", "paraglider", "gyrocopter"
]

hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

def has_user_won(word):
    if "-" in word:
        return False
    return True

def get_guess():
    while True:
        user_input = input("Guess a letter: ")
        if user_input not in string.ascii_letters or len(user_input) > 1:
            print("Invalid guess. Please enter a single letter.")
        else:
            guess = user_input.lower()
            return guess

def print_game_state():
    print(hangman_stages[number_of_mistakes])
    print(''.join(display_word))
    print("Guessed: " + (' '.join(guessed_letters)))
  
secret_word = list(random.choice(wordlist))
secret_word_string = ''.join(secret_word)
display_word = list("-" * len(secret_word))
guessed_letters = []
number_of_mistakes = 0

print("Welcome to Hangman.")

while True:
    if number_of_mistakes == 6:
        print(hangman_stages[6])
        print(f"You lost! The word was {secret_word_string}")
        break
    elif has_user_won(display_word):
        print_game_state()
        print("You won!")
        break
    else:
        print_game_state()
        guess = get_guess()
        if guess in guessed_letters:
            print("Already guessed.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Correct!\n" + "*" * 20)
            for index, letter in enumerate(secret_word):
                if guess == letter:
                    display_word[index] = guess
        else:
            print("Incorrect guess.\n" + "*" * 20)
            guessed_letters.append(guess)
            number_of_mistakes += 1
    