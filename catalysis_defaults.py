# coding: UTF-8

'''This module contains dictionaries for use in objects and context
validation.'''

from collections import OrderedDict

# Each item in charDict also has an icon key. See below charDict definition.
charDict = {
    "angelstarr": {
        "long": "Angel Starr",
        "short": "Angel",
        "sprite": "Angelique",
        "voice": "female",
        "prefix": "as",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("lunch", "lun"),
            ("happy", "h"),
            ("confident", "con"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("mad", "m")
        ])
    },
    "aprilmay": {
        "long": "April May",
        "short": "April",
        "sprite": "Masha",
        "voice": "female",
        "prefix": "am",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("twitch", "twi"),
            ("think", "th"),
            ("bounce", "b"),
            ("damage", "dmg"),
            ("cry", "cry"),
            ("mad", "m"),
            ("side", "si"),
            ("breakdown", "bd")
        ])
    },
    "bellboy": {
        "long": "Bellboy",
        "short": "Bellboy",
        "sprite": "Groom",
        "voice": "male",
        "prefix": "bb",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("blush", "b")
        ])
    },
    "brucegoodman": {
        "long": "Bruce Goodman",
        "short": "Goodman",
        "sprite": "Lebon",
        "voice": "male",
        "prefix": "bg",
        "suffix": OrderedDict([
            ("normal 1", "n1"),
            ("worried 1", "w1"),
            ("worried 2", "w2"),
            ("hat 1", "hat1"),
            ("normal 2", "n2"),
            ("normal 3", "n3"),
            ("worried 3", "worried3"),
            ("mad 3", "m3"),
            ("gun 3", "gun3"),
            ("nervous 1", "ner1"),
            ("side 3", "si3"),
            ("worried 4", "w4"),
            ("draw 3", "drw3"),
            ("damage 3", "dmg3"),
            ("mad 4", "m4")
        ])
    },
    "cindystone": {
        "long": "Cindy Stone",
        "short": "Stone",
        "sprite": "Cindy",
        "voice": "female",
        "prefix": "cs",
        "suffix": OrderedDict([
        ])
    },
    "codyhackins": {
        "long": "Cody Hackins",
        "short": "Cody",
        "sprite": "Kevin",
        "voice": "male",
        "prefix": "ch",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("pout", "pout"),
            ("mad", "m"),
            ("damage", "dmg"),
            ("sad", "s"),
            ("cry", "cry"),
            ("breakdown", "bd")
        ])
    },
    "damongant": {
        "long": "Damon Gant",
        "short": "Gant",
        "sprite": "Gant",
        "voice": "male",
        "prefix": "dg2",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("stare", "sta"),
            ("happy", "h"),
            ("gloves", "glv"),
            ("clap", "clp"),
            ("confident", "con"),
            ("thinking", "th"),
            ("thinking 2", "th2"),
            ("mad", "m"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("breakdown", "bd")
        ])
    },
    "deevasquez": {
        "long": "Dee Vasquez",
        "short": "Vasquez",
        "sprite": "Vasquez",
        "voice": "female",
        "prefix": "dv",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("damage", "dmg"),
            ("confident", "con"),
            ("nervous", "ner"),
            ("shocked", "sho"),
            ("breakdown", "bd"),
            ("beaten", "beat")
        ])
    },
    "franksahwit": {
        "long": "Frank Sahwit",
        "short": "Sahwit",
        "sprite": "Khavu",
        "voice": "male",
        "prefix": "fs",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("nervous", "ner"),
            ("mad", "m"),
            ("damage", "dmg"),
            ("breakdown", "bd"),
            ("breakdown 2", "bd2"),
            ("beaten", "beat")
        ])
    },
    "jackhammer": {
        "long": "Jack Hammer",
        "short": "Hammer",
        "sprite": "Hammer",
        "voice": "male",
        "prefix": "jh",
        "suffix": OrderedDict([
        ])
    },
    "jakemarshall": {
        "long": "Jake Marshall",
        "short": "Marshall",
        "sprite": "Marshall",
        "voice": "male",
        "prefix": "jm",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("confident", "con"),
            ("canteen", "can"),
            ("spit", "spt"),
            ("accuse", "acc"),
            ("mad", "m"),
            ("nervous", "ner"),
            ("serious", "ser"),
            ("damage", "dmg"),
            ("beaten", "beat")
        ])
    },
    "joedarke": {
        "long": "Joe Darke",
        "short": "Darke",
        "sprite": "Sinister",
        "voice": "male",
        "prefix": "jd",
        "suffix": OrderedDict([
        ])
    },
    "lanaskye": {
        "long": "Lana Skye",
        "short": "Lana",
        "sprite": "Lana",
        "voice": "female",
        "prefix": "ls",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("mad", "m"),
            ("shocked", "sho"),
            ("intense", "int"),
            ("back", "ba"),
            ("side", "si"),
            ("nervous", "ner"),
            ("nervous 2", "ner2"),
            ("damage", "dmg"),
            ("happy", "h"),
            ("turn front", "trnf"),
            ("turn back", "trnb"),
            ("smile", "smi")
        ])
    },
    "lottahart": {
        "long": "Lotta Hart",
        "short": "Lotta",
        "sprite": "Lotta",
        "voice": "female",
        "prefix": "lh",
        "suffix": OrderedDict([
            ("happy", "h"),
            ("confident", "con"),
            ("normal", "n"),
            ("nervous", "ner"),
            ("pout", "pout"),
            ("mad", "m"),
            ("beaten", "beat"),
            ("sad", "s"),
            ("damage", "dmg")
        ])
    },
    "marvingrossberg": {
        "long": "Marvin Grossberg",
        "short": "Grossberg",
        "sprite": "Rosenberg",
        "voice": "male",
        "prefix": "mg",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("nervous", "ner"),
            ("aide nervous", "Aner"),
            ("aide normal", "An"),
            ("normal red", "n2"),
            ("nervous red", "ner2")
        ])
    },
    "mikemeekins": {
        "long": "Mike Meekins",
        "short": "Meekins",
        "sprite": "Ballaud",
        "voice": "male",
        "prefix": "mm",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("salute", "sal"),
            ("think", "th"),
            ("fist", "fist"),
            ("megaphone", "mega"),
            ("sad", "s"),
            ("damage", "dmg")
        ])
    },
    "mistyfey": {
        "long": "Misty Fey",
        "short": "Misty",
        "sprite": "Misty",
        "voice": "female",
        "prefix": "mf2",
        "suffix": OrderedDict([
        ])
    },
    "neilmarshall": {
        "long": "Neil Marshall",
        "short": "Marshall",
        "sprite": "Fred",
        "voice": "male",
        "prefix": "nm",
        "suffix": OrderedDict([
        ])
    },
    "pennynichols": {
        "long": "Penny Nichols",
        "short": "Penny",
        "sprite": "Rosentz",
        "voice": "female",
        "prefix": "pn",
        "suffix": OrderedDict([
            ("card", "card"),
            ("normal", "n"),
            ("happy", "h")
        ])
    },
    "polly": {
        "long": "Polly",
        "short": "Polly",
        "sprite": "Alice",
        "voice": "female",
        "prefix": "p",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("talk", "t")
        ])
    },
    "reddwhite": {
        "long": "Redd White",
        "short": "White",
        "sprite": "Redd",
        "voice": "male",
        "prefix": "rw",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("confident", "con"),
            ("no", "no"),
            ("dazzle", "daz"),
            ("pout", "pout"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("‘breakdown", "bd")
        ])
    },
    "roberthammond": {
        "long": "Robert Hammond",
        "short": "Hammond",
        "sprite": "Durand",
        "voice": "male",
        "prefix": "rh",
        "suffix": OrderedDict([
        ])
    },
    "salmanella": {
        "long": "Sal Manella",
        "short": "Manella",
        "sprite": "Monello",
        "voice": "male",
        "prefix": "sm",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("mad", "m"),
            ("drool", "dl"),
            ("thinking", "th"),
            ("shocked", "sho"),
            ("damage", "dmg")
        ])
    },
    "wendyoldbag": {
        "long": "Wendy Oldbag",
        "short": "Oldbag",
        "sprite": "Flavie",
        "voice": "female",
        "prefix": "wo",
        "suffix": OrderedDict([
            ("normal", "n1"),
            ("confident", "con1"),
            ("gossip", "gos1"),
            ("love", "luv1"),
            ("mad", "m1"),
            ("damage", "dmg1"),
            ("helmet 2", "helm2"),
            ("gun 2", "gun2"),
            ("normal 2", "n2"),
            ("confident 2", "con2"),
            ("gossip 2", "gos2"),
            ("love 2", "luv2"),
            ("mad 2", "m2"),
            ("damage 2", "dmg2")
        ])
    },
    "willpowers": {
        "long": "Will Powers",
        "short": "Powers",
        "sprite": "Lonte",
        "voice": "male",
        "prefix": "wp",
        "suffix": OrderedDict([
            ("normal", "n1"),
            ("sad", "s1"),
            ("happy", "h1"),
            ("nervous", "ner1"),
            ("suit happy", "h2"),
            ("suit pout", "pout2"),
            ("suit sad", "s2"),
            ("suit nervous", "ner2"),
            ("suit normal", "nor2")
        ])
    },
    "yanniyogi": {
        "long": "Yanni Yogi",
        "short": "Yogi",
        "sprite": "Yogi",
        "voice": "male",
        "prefix": "yy",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("sleep", "slp"),
            ("thinking", "th"),
            ("side", "si"),
            ("mad", "m"),
            ("damage", "dmg"),
            ("breakdown", "bd"),
            ("serious", "ser"),
            ("sad", "s")
        ])
    },
    "acro": {
        "long": "Acro",
        "short": "Acro",
        "sprite": "Acro",
        "voice": "male",
        "prefix": "a",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("sad", "s"),
            ("mad", "m"),
            ("fly normal", "flyn"),
            ("fly mad", "flym"),
            ("fly happy", "flyh"),
            ("breakdown", "bd")
        ])
    },
    "adrianandrews": {
        "long": "Adrian Andrews",
        "short": "Andrews",
        "sprite": "Andrea",
        "voice": "female",
        "prefix": "aa",
        "suffix": OrderedDict([
            ("normal", "n1"),
            ("confident", "con1"),
            ("thinking", "th1"),
            ("serious", "ser1"),
            ("shocked", "sho1"),
            ("nervous", "ner"),
            ("sad", "s1"),
            ("damage", "dmg1"),
            ("beaten", "beat1"),
            ("happy", "h1"),
            ("normal 2", "n2"),
            ("nervous 2", "ner2"),
            ("sad 2", "s2"),
            ("happy 2", "h2"),
            ("thinking 2", "th2")
        ])
    },
    "bat": {
        "long": "Bat",
        "short": "Bat",
        "sprite": "Bate",
        "voice": "male",
        "prefix": "b",
        "suffix": OrderedDict([
        ])
    },
    "benwoodman": {
        "long": "Ben Woodman",
        "short": "Trilo",
        "sprite": "Michael",
        "voice": "male",
        "prefix": "bw",
        "suffix": OrderedDict([
            ("alone", "one"),
            ("normal", "n"),
            ("mad", "m"),
            ("pout", "pout"),
            ("nervous", "ner"),
            ("damage", "dmg")
        ])
    },
    "celesteinpax": {
        "long": "Celeste Inpax",
        "short": "Inpax",
        "sprite": "Celeste",
        "voice": "female",
        "prefix": "ci",
        "suffix": OrderedDict([
        ])
    },
    "dustinprince": {
        "long": "Dustin Prince",
        "short": "Prince",
        "sprite": "Prince",
        "voice": "male",
        "prefix": "dp",
        "suffix": OrderedDict([
        ])
    },
    "hotti": {
        "long": "Hotti",
        "short": "Hotti",
        "sprite": "Sashoff",
        "voice": "male",
        "prefix": "h",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("secret", "sec"),
            ("creepy", "creep")
        ])
    },
    "iniminey": {
        "long": "Ini Miney",
        "short": "Ini",
        "sprite": "Ines",
        "voice": "female",
        "prefix": "im",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("tongue", "ton"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("mad", "m"),
            ("confident", "con"),
            ("beaten", "beat")
        ])
    },
    "juancorrida": {
        "long": "Juan Corrida",
        "short": "Corrida",
        "sprite": "Corrida",
        "voice": "male",
        "prefix": "jc",
        "suffix": OrderedDict([
        ])
    },
    "maggeybyrde": {
        "long": "Maggey Byrde",
        "short": "Byrde",
        "sprite": "Maguy",
        "voice": "female",
        "prefix": "mb",
        "suffix": OrderedDict([
            ("normal", "n1"),
            ("happy", "h1"),
            ("intense", "int1"),
            ("sad", "s1"),
            ("aide normal", "An"),
            ("aide intense", "Aint"),
            ("maid normal", "n2"),
            ("maid pout", "res2"),
            ("maid intense", "int2"),
            ("maid sad", "s2")
        ])
    },
    "mattengarde": {
        "long": "Matt Engarde",
        "short": "Engarde",
        "sprite": "Engarde",
        "voice": "male",
        "prefix": "me2",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("dial", "dial"),
            ("cell phone", "cell"),
            ("reveal", "rev"),
            ("grin", "grin"),
            ("confident", "con"),
            ("nervous", "ner"),
            ("breakdown", "bd")
        ])
    },
    "maxgalactica": {
        "long": "Max Galactica",
        "short": "Max",
        "sprite": "Max",
        "voice": "male",
        "prefix": "mg2",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("confident", "con"),
            ("card", "card"),
            ("nervous", "ner"),
            ("damage", "dmg")
        ])
    },
    "mimiminey": {
        "long": "Mimi Miney",
        "short": "Mimi",
        "sprite": "Daisy",
        "voice": "female",
        "prefix": "mm2",
        "suffix": OrderedDict([
        ])
    },
    "moe": {
        "long": "Moe",
        "short": "Moe",
        "sprite": "Frise",
        "voice": "male",
        "prefix": "m",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("giggle", "gig"),
            ("laugh", "lau"),
            ("serious", "ser"),
            ("finger wag", "wag"),
            ("mad", "m"),
            ("sad", "s"),
            ("damage", "dmg")
        ])
    },
    "morganfey": {
        "long": "Morgan Fey",
        "short": "Morgan",
        "sprite": "Morgan",
        "voice": "female",
        "prefix": "mf",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("sad", "s"),
            ("thinking", "th"),
            ("mad", "m")
        ])
    },
    "reginaberry": {
        "long": "Regina Berry",
        "short": "Regina",
        "sprite": "Monique",
        "voice": "female",
        "prefix": "rb",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("shy", "shy"),
            ("point", "poin"),
            ("thinking", "th"),
            ("bd", "bd"),
            ("cry", "cry")
        ])
    },
    "richardwellington": {
        "long": "Richard Wellington",
        "short": "Wellington",
        "sprite": "Wellington",
        "voice": "male",
        "prefix": "rw",
        "suffix": OrderedDict([
            ("confident", "con"),
            ("normal", "n"),
            ("no", "no"),
            ("nervous", "ner"),
            ("mad", "m"),
            ("damage", "dmg"),
            ("beaten", "beat"),
            ("breakdown 1", "bd1"),
            ("breakdown 2", "bd2")
        ])
    },
    "russelberry": {
        "long": "Russel Berry",
        "short": "Berry",
        "sprite": "Loic",
        "voice": "male",
        "prefix": "rb2",
        "suffix": OrderedDict([
        ])
    },
    "shellydekiller": {
        "long": "Shelly de Killer",
        "short": "de Killer",
        "sprite": "DeKiller",
        "voice": "male",
        "prefix": "sdk",
        "suffix": OrderedDict([
            ("bellboy", "bb"),
            ("butler", "but"),
            ("red", "red"),
            ("normal", "n"),
            ("breakdown", "bd"),
            ("nervous", "ner"),
            ("mad", "m"),
            ("beaten", "beat")
        ])
    },
    "turnergrey": {
        "long": "Turney Grey",
        "short": "Grey",
        "sprite": "Afforme",
        "voice": "male",
        "prefix": "tg",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("mad", "m"),
            ("intense", "int")
        ])
    },
    "bikini": {
        "long": "Bikini",
        "short": "Bikini",
        "sprite": "Bikini",
        "voice": "female",
        "prefix": "b",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("thinking", "th"),
            ("serious", "ser"),
            ("sad", "s"),
            ("afraid", "fear")
        ])
    },
    "brutocadaverini": {
        "long": "Bruto Cadaverini",
        "short": "Cadaverini",
        "sprite": "Bruto",
        "voice": "male",
        "prefix": "bc",
        "suffix": OrderedDict([
        ])
    },
    "dahliahawthorne": {
        "long": "Dahlia Hawthorne",
        "short": "Dahlia",
        "sprite": "Dahlia",
        "voice": "female",
        "prefix": "dh",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("cry", "cry"),
            ("shy", "shy"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("side", "side"),
            ("rage", "rage"),
            ("maya side", "mside"),
            ("maya jeer", "mjeer"),
            ("maya beaten", "mbeat"),
            ("maya breakdown", "mbd"),
            ("scream", "gscre"),
            ("ghost", "gghost"),
            ("fire", "gfire"),
            ("reveal", "rev"),
            ("maya reveal", "mrev")
        ])
    },
    "desireedelite": {
        "long": "Desirée DeLite",
        "short": "Desirée",
        "sprite": "Desiree",
        "voice": "female",
        "prefix": "dd",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("thinking", "th"),
            ("nervous", "ner")
        ])
    },
    "doloreswillow": {
        "long": "Dolores Willow",
        "short": "Dolores",
        "sprite": "Dolores",
        "voice": "female",
        "prefix": "dw",
        "suffix": OrderedDict([
        ])
    },
    "dougswallow": {
        "long": "Doug Swallow",
        "short": "Swallow",
        "sprite": "Doug",
        "voice": "male",
        "prefix": "ds",
        "suffix": OrderedDict([
        ])
    },
    "elisedeauxnim": {
        "long": "Elise Deauxnim",
        "short": "Elise",
        "sprite": "Elise",
        "voice": "female",
        "prefix": "ed",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h")
        ])
    },
    "furiotigre": {
        "long": "Furio Tigre",
        "short": "Tigre",
        "sprite": "Furio",
        "voice": "male",
        "prefix": "ft",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("confident", "con"),
            ("mad", "m"),
            ("roar", "roar"),
            (" worried", "w"),
            ("nervous", "ner"),
            ("plea", "plea"),
            ("breakdown", "bd")
        ])
    },
    "glenelg": {
        "long": "Glen Elg",
        "short": "Glen",
        "sprite": "Glen",
        "voice": "male",
        "prefix": "ge2",
        "suffix": OrderedDict([
        ])
    },
    "iris": {
        "long": "Iris",
        "short": "Iris",
        "sprite": "Iris",
        "voice": "female",
        "prefix": "i",
        "suffix": OrderedDict([
            ("hood huh", "hhuh"),
            ("hood normal", "hn"),
            ("serious", "ser"),
            ("normal", "n"),
            ("blush", "blu"),
            ("huh", "huh"),
            ("thinking", "th"),
            ("cry", "cry"),
            ("nervous", "ner"),
            ("damage", "dmg")
        ])
    },
    "jackrichford": {
        "long": "Jack Richford",
        "short": "Richford",
        "sprite": "Richford",
        "voice": "male",
        "prefix": "jr",
        "suffix": OrderedDict([
        ])
    },
    "jeanarmstong": {
        "long": "Jean Armstrong",
        "short": "Armstrong",
        "sprite": "Armstrong",
        "voice": "male",
        "prefix": "ja",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("stare", "sta"),
            ("wiggle", "wig"),
            ("thinking", "th"),
            ("nervous", "ner"),
            ("sad", "s"),
            ("damage", "dmg")
        ])
    },
    "kanebullard": {
        "long": "Kane Bullard",
        "short": "Bullard",
        "sprite": "Kane",
        "voice": "male",
        "prefix": "kb",
        "suffix": OrderedDict([
        ])
    },
    "lisabasil": {
        "long": "Lisa Basil",
        "short": "Basil",
        "sprite": "Lisa",
        "voice": "female",
        "prefix": "lb2",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("nervous", "ner")
        ])
    },
    "lukeatmey": {
        "long": "Luke Atmey",
        "short": "Atmey",
        "sprite": "Luke",
        "voice": "male",
        "prefix": "la",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("glasses", "gla"),
            ("confident", "con"),
            ("side", "side"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("beaten", "beat"),
            ("breakdown", "bd")
        ])
    },
    "maskdemasque": {
        "long": "Mask☆DeMasque",
        "short": "Mask",
        "sprite": "Mask",
        "voice": "male",
        "prefix": "mdm",
        "suffix": OrderedDict([
        ])
    },
    "rondelite": {
        "long": "Ron DeLite",
        "short": "Ron",
        "sprite": "Ron",
        "voice": "male",
        "prefix": "rd",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("sad", "s"),
            ("nervous", "ner"),
            ("yell", "yell"),
            (" intense", "int")
        ])
    },
    "terryfawles": {
        "long": "Terry Fawles",
        "short": "Fawles",
        "sprite": "Terry",
        "voice": "male",
        "prefix": "tf",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("side", "side"),
            ("sad", "s"),
            ("nervous", "ner"),
            ("yell", "yell"),
            ("serious", "ser"),
            ("sick", "sick"),
            ("breakdown", "bd")
        ])
    },
    "valeriehawthorne": {
        "long": "Valerie Hawthorne",
        "short": "Valerie",
        "sprite": "Valerie",
        "voice": "female",
        "prefix": "vh",
        "suffix": OrderedDict([
        ])
    },
    "victorkudo": {
        "long": "Victor Kudo",
        "short": "Kudo",
        "sprite": "Kudo",
        "voice": "male",
        "prefix": "vk",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("mad", "m"),
            ("eat", "eat"),
            ("seed", "seed"),
            ("side 1", "side1"),
            ("side 2", "side2"),
            ("nervous", "ner"),
            ("blush", "blu")
        ])
    },
    "violacadaverini": {
        "long": "Viola Cadaverini",
        "short": "Viola",
        "sprite": "Viola",
        "voice": "female",
        "prefix": "vc",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("giggle", "g"),
            ("cry", "cry")
        ])
    },
    "alitatiala": {
        "long": "Alita Tiala",
        "short": "Alita",
        "sprite": "Alita",
        "voice": "female",
        "prefix": "at",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("plan", "plan"),
            ("distraught", "dis"),
            ("sad", "s"),
            ("distraught 2", "dis2"),
            ("mad", "m"),
            ("annoyed", "ann"),
            ("confident", "con"),
            ("confident 2", "con2"),
            ("thinknig", "th"),
            ("damage", "dmg"),
            ("breakdown", "bd")
        ])
    },
    "daryancrescend": {
        "long": "Daryan Crescend",
        "short": "Daryan",
        "sprite": "Daryan",
        "voice": "male",
        "prefix": "dc",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("side", "side"),
            ("side2", "side2"),
            ("point", "poin"),
            ("pout", "pout"),
            ("shocked", "sho"),
            ("mad", "m"),
            ("damage", "dmg"),
            ("nervous", "ner"),
            ("breakdown", "bd"),
            ("rub", "rub")
        ])
    },
    "drewmisham": {
        "long": "Drew Misham",
        "short": "Drew",
        "sprite": "Drew",
        "voice": "male",
        "prefix": "dm",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("nervous", "ner1"),
            ("nervous 2", "ner2"),
            ("nervous 3", "ner3"),
            ("sad", "s")
        ])
    },
    "guyeldoon": {
        "long": "Guy Eldoon",
        "short": "Eldoon",
        "sprite": "Eldoon",
        "voice": "male",
        "prefix": "ge",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("mad", "m"),
            ("harmonica", "har"),
            ("sad", "s"),
            (" worried", "w"),
            ("prereveal", "pre"),
            ("reveal", "rev"),
            ("serious", "ser")
        ])
    },
    "lamiroir": {
        "long": "Lamiroir",
        "short": "Lamiroir",
        "sprite": "Lamiroir",
        "voice": "female",
        "prefix": "l",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("side", "side"),
            ("nervous", "ner"),
            ("sad", "s"),
            ("shocked", "sho"),
            ("damage", "dmg"),
            ("thalassa", "thal")
        ])
    },
    "machitobaye": {
        "long": "Machi Tobaye",
        "short": "Machi",
        "sprite": "Machi",
        "voice": "male",
        "prefix": "mt",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("side", "side"),
            ("shocked", "sho"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("eyes", "eyes")
        ])
    },
    "magnifigramarye": {
        "long": "Magnifi Gramarye",
        "short": "Magnifi",
        "sprite": "Magnifi",
        "voice": "male",
        "prefix": "mg",
        "suffix": OrderedDict([
        ])
    },
    "olgaorly": {
        "long": "Olga Orly",
        "short": "Olga",
        "sprite": "Olga",
        "voice": "female",
        "prefix": "oo",
        "suffix": OrderedDict([
            ("hide", "hide"),
            ("normal", "n"),
            ("shy", "shy"),
            ("camera", "cam"),
            ("picture", "pic"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("breakdown", "bd"),
            ("reveal", "rev"),
            ("poker normal", "n2"),
            ("poker thinking", "th2"),
            ("poker nervous", "ner2"),
            ("poker serious", "ser2"),
            ("poker damage", "dmg2"),
            ("poker breakdown", "bd2")
        ])
    },
    "olgaorly2": {
        "long": "Olga Orly",
        "short": "Olga",
        "sprite": "Olga2",
        "voice": "female",
        "prefix": "oo2",
        "suffix": OrderedDict([
            ("hide", "hide"),
            ("normal", "n"),
            ("shy", "shy"),
            ("camera", "cam"),
            ("picture", "pic"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("breakdown", "bd"),
            ("reveal", "rev"),
            ("poker normal", "n2"),
            ("poker thinking", "th2"),
            ("poker nervous", "ner2"),
            ("poker serious", "ser2"),
            ("poker damage", "dmg2"),
            ("poker breakdown", "bd2")
        ])
    },
    "palmeraktis": {
        "long": "Pal Meraktis",
        "short": "Meraktis",
        "sprite": "Meraktis",
        "voice": "male",
        "prefix": "pm",
        "suffix": OrderedDict([
        ])
    },
    "plumkitaki": {
        "long": "Plum Kitaki",
        "short": "Plum",
        "sprite": "Kitaki",
        "voice": "female",
        "prefix": "pk",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("sweat", "swe"),
            ("thinking", "th"),
            ("laugh", "lau"),
            ("mad", "m"),
            ("serious", "ser")
        ])
    },
    "romeinletouse": {
        "long": "Romein LeTouse",
        "short": "LeTouse",
        "sprite": "LeTouse",
        "voice": "male",
        "prefix": "rl",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("dying 1", "dy1"),
            ("dying 2", "dy2"),
            ("dead 1", "dead1"),
            ("dead 2", "dead2")
        ])
    },
    "sparkbrushel": {
        "long": "Spark Brushel",
        "short": "Brushel",
        "sprite": "Brushel",
        "voice": "male",
        "prefix": "sb",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("write", "wri"),
            ("nod 1", "nod1"),
            ("nod 2", "nod2"),
            ("thinking", "th"),
            ("thinking 2", "th2"),
            ("sniff", "sni"),
            ("shocked", "sho"),
            ("nervous", "ner"),
            ("damage", "dmg")
        ])
    },
    "thalassagramarye": {
        "long": "Thalassa Gramarye",
        "short": "Thalassa",
        "sprite": "Thalassa",
        "voice": "female",
        "prefix": "tg2",
        "suffix": OrderedDict([
        ])
    },
    "valantgramarye": {
        "long": "Valant Gramarye",
        "short": "Valant",
        "sprite": "Valant",
        "voice": "male",
        "prefix": "vg",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("laugh", "lau"),
            ("twirl", "twir"),
            ("side", "side"),
            ("point", "poin"),
            ("nervous", "ner"),
            ("damage", "dmg")
        ])
    },
    "veramisham": {
        "long": "Vera Misham",
        "short": "Vera",
        "sprite": "Vera",
        "voice": "female",
        "prefix": "vm",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("draw", "dr"),
            ("shy", "shy"),
            ("nervous 1", "ner1"),
            ("nervous 2", "ner2"),
            ("thinking", "th"),
            ("happy", "h"),
            ("closed", "clo"),
            ("book", "book"),
            ("damage", "dmg")
        ])
    },
    "veramishamyoung": {
        "long": "Vera Misham",
        "short": "Vera",
        "sprite": "VeraJeune",
        "voice": "female",
        "prefix": "vmy",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("shocked", "sho"),
            ("thinking", "th"),
            ("nervous", "ner"),
            ("happy", "h")
        ])
    },
    "wesleystickler": {
        "long": "Wesley Stickler",
        "short": "Stickler",
        "sprite": "Wesley",
        "voice": "male",
        "prefix": "ws",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("flip", "flip"),
            ("shut", "shut"),
            ("speech", "spe"),
            ("side", "side"),
            ("quiver", "qui"),
            ("shocked", "sho"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("breakdown", "bd"),
            ("beaten", "beat")
        ])
    },
    "winfredkitaki": {
        "long": "Winfred Kitaki",
        "short": "Big Wins",
        "sprite": "Winfred",
        "voice": "male",
        "prefix": "wk2",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("eyebrow", "brow"),
            ("eye", "eye")
        ])
    },
    "wockykitaki": {
        "long": "Wocky Kitaki",
        "short": "Wocky",
        "sprite": "KitakiWocky",
        "voice": "male",
        "prefix": "wk",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("hairflip", "flip"),
            ("huh", "huh"),
            ("mad", "m"),
            ("happy", "h"),
            ("confident", "con"),
            ("pout", "pout"),
            ("nervous", "ner"),
            ("defensive", "def"),
            ("serious", "ser"),
            ("quiver", "qui"),
            ("beaten", "beat")
        ])
    },
    "zakgramarye": {
        "long": "Zak Gramarye",
        "short": "Zak",
        "sprite": "Zak",
        "voice": "male",
        "prefix": "zg",
        "suffix": OrderedDict([
            ("normal", "n1"),
            ("happy", "h1"),
            ("annoyed", "ann1"),
            ("pout", "res1"),
            ("laugh", "lau1"),
            ("poker normal", "n2"),
            ("poker pout", "res2"),
            ("poker happy", "h2"),
            ("poker shocked", "sho2")
        ])
    },
    "apollo": {
        "long": "Apollo Justice",
        "short": "Apollo",
        "sprite": "Apollo",
        "voice": "male",
        "prefix": "aj",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("paper", "pap"),
            ("no", "no"),
            ("desk slam", "desk"),
            ("object", "obj"),
            ("zoom", "zoom"),
            ("damage", "dmg"),
            ("nervous", "ner"),
            ("confident", "con"),
            ("thinking", "th"),
            ("wince 1", "winc1"),
            ("wince 2", "winc2")
        ])
    },
    "gumshoe": {
        "long": "Dick Gumshoe",
        "short": "Gumshoe",
        "sprite": "Tecktiv",
        "voice": "male",
        "prefix": "dg",
        "suffix": OrderedDict([
            ("intense", "int"),
            ("confident", "con"),
            ("laugh", "lau"),
            ("thinking", "th"),
            ("sad", "s"),
            ("side", "side"),
            ("mad", "m"),
            ("huh", "huh"),
            ("hurt intense", "int2"),
            ("hurt laugh", "h2"),
            ("hurt huh", "huh2"),
            ("tan intense", "int3"),
            ("tan confident", "con3"),
            ("tan laugh", "lau3"),
            ("tan huh", "huh3"),
            ("tan mad", "m3"),
            ("tan sad", "s3"),
            ("normal", "n"),
            ("tan normal", "n3"),
            ("tan side", "side3")
        ])
    },
    "emaaj": {
        "long": "Ema Skye",
        "short": "Ema",
        "sprite": "EmaAdulte",
        "voice": "female",
        "prefix": "esa",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("pout", "res"),
            ("side", "side"),
            ("eat", "eat"),
            ("eat normal", "eatn"),
            ("thinking", "th"),
            ("happy", "h"),
            ("shocked", "sho"),
            ("serious", "ser"),
            ("glasses adjust", "gfix"),
            ("glasses up", "gup"),
            ("glasses down", "gdown")
        ])
    },
    "ema": {
        "long": "Ema Skye",
        "short": "Ema",
        "sprite": "Ema",
        "voice": "female",
        "prefix": "es",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("note", "note"),
            ("thinking", "th"),
            ("shocked", "sho"),
            ("mad", "m"),
            ("intense", "int"),
            ("huh", "huh"),
            ("nervous", "ner"),
            ("sad", "s"),
            ("aide normal", "An"),
            ("aide huh", "Ahuh"),
            ("aide intense", "Aint"),
            ("aide across", "Aacr")
        ])
    },
    "franziska": {
        "long": "Franziska von Karma",
        "short": "von Karma",
        "sprite": "Franziska",
        "voice": "female",
        "prefix": "fvk",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("curtsy", "curt"),
            ("whip", "whip"),
            ("annoyed", "ann"),
            ("object", "obj"),
            ("zoom", "zoom"),
            ("finger wag", "wag"),
            ("desk slam", "desk"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("front normal", "Fn"),
            ("front confident", "Fcon"),
            ("front annoyed", "Fann"),
            ("front object", "Fobj"),
            ("front cry", "Fcry")
        ])
    },
    "godot": {
        "long": "Godot",
        "short": "Godot",
        "sprite": "Godot",
        "voice": "male",
        "prefix": "g",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("slide", "sli"),
            ("confident", "con"),
            ("no", "no"),
            ("sip", "sip"),
            ("chug", "chug"),
            ("damage", "dmg"),
            ("desk", "desk"),
            ("desk2", "desk2"),
            ("zoom", "zoom"),
            ("object", "obj"),
            ("object2 ", "obj2"),
            ("steam", "ste"),
            ("slide 2", "sli2"),
            ("front normal", "fn"),
            ("front annoyed", "fann"),
            ("front sad", "fs"),
            ("breakdown", "bd"),
            ("beaten", "beat1"),
            ("beaten2", "beat2"),
            ("front confident", "fcon")
        ])
    },
    "diego": {
        "long": "Diego Armando",
        "short": "Armando",
        "sprite": "GodotJeune",
        "voice": "male",
        "prefix": "da",
        "suffix": OrderedDict([
            ("front normal", "fn"),
            ("front confident", "fcon"),
            ("aide normal", "an"),
            ("aide across", "aacr"),
            ("aide confident", "acon"),
            ("aide breakdown", "abd"),
            ("aide beaten", "abeat")
        ])
    },
    "judge": {
        "long": "Judge",
        "short": "Judge",
        "sprite": "Juge",
        "voice": "male",
        "prefix": "j",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("shocked", "sho"),
            ("no", "no"),
            ("mad", "m"),
            ("yes", "yes"),
            ("thinking", "th")
        ])
    },
    "judgebrother": {
        "long": "Judge",
        "short": "Judge",
        "sprite": "Juge2",
        "voice": "male",
        "prefix": "jb",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("shocked", "sho"),
            ("no", "no"),
            ("mad", "m"),
            ("yes", "yes"),
            ("thinking", "th")
        ])
    },
    "klavier": {
        "long": "Klavier Gavin",
        "short": "Klavier",
        "sprite": "Konrad",
        "voice": "male",
        "prefix": "klg",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("wall slam", "wall"),
            ("wall slam 2", "wall 2"),
            ("wall normal", "wcon"),
            ("object", "obj"),
            ("zoom", "zoom"),
            ("air guitar", "air"),
            ("snap", "snap"),
            ("smile", "smi"),
            ("laugh", "lau"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("front normal", "fn"),
            ("front confident", "fcon"),
            ("front smile", "fsmi"),
            ("front mad", "fm"),
            ("young normal", "yn"),
            ("young snap", "ysnap"),
            ("young smile", "ysmi"),
            ("young laugh", "ylau"),
            ("young wall", "ywall"),
            ("young object", "yobj"),
            ("young zoom", "yzoom"),
            ("young damage", "ydmg"),
            ("young nervous", "yner"),
            ("pain", "pain"),
            ("beaten", "beat"),
            ("quiver", "qui")
        ])
    },
    "kristoph": {
        "long": "Kristoph Gavin",
        "short": "Kristoph",
        "sprite": "Kristophe",
        "voice": "male",
        "prefix": "krg",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("no", "no"),
            ("aide normal", "An"),
            ("aide across", "Aacr"),
            ("aide happy", "Ah"),
            ("glare", "glar"),
            ("confident", "con"),
            ("twitch", "twi"),
            ("annoyed", "ann"),
            ("damage", "dmg"),
            ("breakdown 1", "bd1"),
            ("mad", "m"),
            ("twitch 2", "twi2"),
            ("breakdown 2", "bd2"),
            ("breakdown 3", "bd3"),
            ("beaten", "beat"),
            ("laugh", "lau"),
            ("brag", "brag"),
            ("breakdown 4", "bd4")
        ])
    },
    "larry": {
        "long": "Larry Butz",
        "short": "Larry",
        "sprite": "Defes",
        "voice": "male",
        "prefix": "lb",
        "suffix": OrderedDict([
            ("happy", "h1"),
            ("confident", "con1"),
            ("normal", "n1"),
            ("yes", "yes1"),
            ("nervous", "ner1"),
            ("blush", "blu1"),
            ("cry", "cry1"),
            ("mad", "m1"),
            ("thinking", "th1"),
            ("shocked", "sho1"),
            ("santa sad", "s2"),
            ("santa annoyed", "ann2"),
            ("guard happy", "h3"),
            ("guard yes", "yes3"),
            ("guard nervous", "ner3"),
            ("guard blush", "blu3"),
            ("guard cry", "cry3"),
            ("guard mad", "m3"),
            ("paint happy", "h4"),
            ("paint normal", "n4"),
            ("paint yes", "yes4"),
            ("paint think", "th4"),
            ("paint pout", "res4"),
            ("paint blush", "blu4"),
            ("paint cry", "cry4"),
            ("paint mad", "m4"),
            ("santa suit", "san2")
        ])
    },
    "vonkarma": {
        "long": "Manfred von Karma",
        "short": "von Karma",
        "sprite": "Manfred",
        "voice": "male",
        "prefix": "mvk",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("annoyed", "ann"),
            ("confident", "con"),
            ("snap", "snap"),
            ("finger wag", "wag"),
            ("damage", "dmg"),
            ("nervous", "ner"),
            ("front normal", "fn"),
            ("front taser", "ftas"),
            ("breakdown", "bd")
        ])
    },
    "maya": {
        "long": "Maya Fey",
        "short": "Maya",
        "sprite": "Maya",
        "voice": "female",
        "prefix": "may",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("mischief", "mis"),
            ("happy", "h"),
            ("thinking", "th"),
            ("sad", "s"),
            ("huh", "huh"),
            ("shocked", "sho"),
            ("intense", "int"),
            ("mad", "m"),
            ("distraught", "dis"),
            ("sad 2", "s2"),
            ("cry", "cry"),
            ("aide normal", "an"),
            ("aide thinking", "ath"),
            ("aide mad", "am"),
            ("aide annoyed", "aann"),
            ("aide across", "aacr"),
            ("maid normal", "n2"),
            ("maid happy", "h2"),
            ("maid huh", "huh2"),
            ("hazakura", "hazu"),
            ("bow", "bow")
        ])
    },
    "mia": {
        "long": "Mia Fey",
        "short": "Mia",
        "sprite": "Mia",
        "voice": "female",
        "prefix": "mia",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("huh", "huh"),
            ("aide normal", "An"),
            ("aide shocked", "Asho"),
            ("aide sad", "As"),
            ("aide huh", "Ahuh"),
            ("maya normal", "Mn"),
            ("maya happy", "Mh"),
            ("maya shocked", "Msho"),
            ("maya serious", "Mser"),
            ("maya aide normal", "MAn"),
            ("maya aide yes", "MAyes"),
            ("maya aide serious", "MAser"),
            ("maya aide across", "MAacr"),
            ("maya aide sad", "MAs"),
            ("pearl normal", "Pn"),
            ("pearl serious", "Pser"),
            ("pearl shocked", "Psho"),
            ("pearl aide normal", "PAn"),
            ("pearl aide serious", "PAser"),
            ("pearl aide across", "PAacr"),
            ("maid smile", "msmi"),
            ("maid side", "mside")
        ])
    },
    "miayoung": {
        "long": "Mia Fey",
        "short": "Mia",
        "sprite": "MiaJeune",
        "voice": "female",
        "prefix": "miay",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("thinking", "th"),
            ("desk", "desk"),
            ("zoom", "zoom"),
            ("nervous", "ner"),
            ("confident", "con"),
            ("object", "obj"),
            ("desk 2", "desk2"),
            ("damage", "dmg"),
            ("thinking 2", "th2"),
            ("object 2", "obj2")
        ])
    },
    "edgeworth": {
        "long": "Miles Edgeworth",
        "short": "Edgeworth",
        "sprite": "Edgeworth",
        "voice": "male",
        "prefix": "me",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("desk", "desk"),
            ("paper", "pap"),
            ("annoyed", "ann"),
            ("point", "poin"),
            ("zoom", "zoom"),
            ("logic", "log"),
            ("confident", "con"),
            ("bow", "bow"),
            ("damage", "dmg"),
            ("front normal", "fn"),
            ("front ner", "fner"),
            ("front annoyed", "fann"),
            ("front mad", "fm"),
            ("front side", "fside"),
            ("front remember", "frem"),
            ("frontbrag", "fbrag"),
            ("front damage", "fdmg"),
            ("front object", "fobj"),
            ("defense annoyed", "Dann"),
            ("defense confident", "Dcon"),
            ("front brag 2", "fbrag2"),
            ("defense normal", "Dn"),
            ("defense desk", "Ddesk"),
            ("defense point", "Dpoin"),
            ("defense damage", "Ddmg"),
            ("defense zoom", "Dzoom")
        ])
    },
    "edgeworthyoung": {
        "long": "Miles Edgeworth",
        "short": "Edgeworth",
        "sprite": "EdgeworthJeune",
        "voice": "male",
        "prefix": "mey",
        "suffix": OrderedDict([
            ("annoyed", "ann"),
            ("desk", "desk"),
            ("finger wag", "wag"),
            ("confident", "con"),
            ("damage", "dmg"),
            ("normal", "n")
        ])
    },
    "pearl": {
        "long": "Pearl Fey",
        "short": "Pearl",
        "sprite": "Pearl",
        "voice": "female",
        "prefix": "pf",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("love", "luv"),
            ("bounce", "boun"),
            ("shocked", "sho"),
            ("thinking", "th"),
            ("intense", "int"),
            ("sad", "s"),
            ("cry", "cry")
        ])
    },
    "phoenix": {
        "long": "Phoenix Wright",
        "short": "Phoenix",
        "sprite": "Phoenix",
        "voice": "male",
        "prefix": "pw",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("yes", "yes"),
            ("thinking", "th"),
            ("no", "no"),
            ("paper", "pap"),
            ("desk", "desk"),
            ("zoom", "zoom"),
            ("object", "obj"),
            ("confident", "con"),
            ("wince", "winc"),
            ("nervous", "ner"),
            ("damage", "dmg"),
            ("wig", "wig"),
            ("bird", "bird"),
            ("coffee", "cof"),
            ("love", "luv"),
            ("breakdown", "bd"),
            ("cup", "cup"),
            ("superobject", "suobj"),
            ("sip", "sip")
        ])
    },
    "phoenixold": {
        "long": "Phoenix Wright",
        "short": "Phoenix",
        "sprite": "PhoenixVieux",
        "voice": "male",
        "prefix": "pwo",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("happy", "h"),
            ("remember", "rem"),
            ("secret", "sec"),
            ("straight", "str"),
            ("aide normal", "An"),
            ("aide across", "Aacr"),
            ("aide serious", "Aser"),
            ("aide object", "Aobj"),
            ("straight happy", "strh"),
            ("laugh", "lau"),
            ("serious", "ser")
        ])
    },
    "phoenixyoung": {
        "long": "Phoenix Wright",
        "short": "Phoenix",
        "sprite": "PhoenixJeune",
        "voice": "male",
        "prefix": "pwy",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("sick", "sick"),
            ("happy", "h"),
            ("sad", "s"),
            ("cry", "cry"),
            ("serious", "ser")
        ])
    },
    "trucy": {
        "long": "Trucy Wright",
        "short": "Trucy",
        "sprite": "Verite",
        "voice": "female",
        "prefix": "tw",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("bounce", "boun"),
            ("happy", "h"),
            ("happy 2", "h2"),
            ("tip", "tip"),
            ("thinking", "th"),
            ("hit", "hit"),
            ("hit 2", "hit2"),
            ("huh", "huh"),
            ("shocked", "sho"),
            ("serious", "ser"),
            ("intense", "int"),
            ("mad", "m"),
            ("nervous", "ner"),
            ("aide normal", "An"),
            ("aide thinking", "Ath"),
            ("aide intense", "Aint"),
            ("aide across", "Aacr"),
            ("sad", "s"),
            ("cry", "cry"),
            ("hat", "hat"),
            ("hat talk", "hatt"),
            ("hat reveal", "rev")
        ])
    },
    "payne": {
        "long": "Winston Payne",
        "short": "Payne",
        "sprite": "Boulay",
        "voice": "male",
        "prefix": "wp",
        "suffix": OrderedDict([
            ("young normal", "yn"),
            ("young confident", "ycon"),
            ("young nervous", "yner"),
            ("young breakdown", "ybd1"),
            ("young beaten", "ybeat"),
            ("normal", "n"),
            ("confident", "con"),
            ("nervous", "ner"),
            ("nervous damage", "dmg")
        ])
    },
    "payneold": {
        "long": "Winston Payne",
        "short": "Payne",
        "sprite": "BoulayVieux",
        "voice": "male",
        "prefix": "wpo",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("brag", "brag"),
            ("confident", "con"),
            ("nervous", "ner"),
            ("damage", "dmg")
        ])
    },
    "laurafrost": {
        "long": "Laura Frost", "Frost": "Payne",
        "sprite": "LauraFrost",
        "voice": "female",
        "prefix": "lf",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("glove", "glv"),
            ("badge", "bdg"),
            ("aide normal", "an"),
            ("aide mad", "am"),
            ("aide happy", "ah")
        ])
    },
    "officergroovy": {
        "long": "Officer Groovy",
        "short": "Groovy",
        "sprite": "OfficerGroovy",
        "voice": "male",
        "prefix": "og",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("badge", "bdg"),
            ("comb", "cmb"),
            ("cry", "cry"),
            ("side", "side"),
            ("happy", "h"),
            ("comb side", "cside"),
            ("nervous", "ner"),
            ("comb nervous", "cner"),
            ("damage", "dmg")
        ])
    },
    "jonathanlebrun": {
        "long": "Jonathan Lebrun",
        "short": "Lebrun",
        "sprite": "JonathanLebrun",
        "voice": "male",
        "prefix": "jl",
        "suffix": OrderedDict([
            ("normal", "n"),
            ("suspicious", "sus"),
            ("glare", "glar"),
            ("thinking", "th"),
            ("hat normal", "hn"),
            ("hat suspicious", "hsus"),
            ("hat glare", "hglar"),
            ("hat thinking", "hth"),
            ("glasses normal", "gn"),
            ("glasses suspicious", "gsus"),
            ("glasses glare", "gglar"),
            ("glasses thinking", "gth")
        ])
    },
    "rangerjustice": {
        "long": "Ranger Justice",
        "short": "Justice",
        "sprite": "RangerJustice",
        "voice": "male",
        "prefix": "rj",
        "suffix": OrderedDict([
            ("happy intense", "hint"),
            ("mad intense; mint, happy point", "hpoin"),
            ("mad point", "mpoin"),
            ("shocked", "sho"),
            ("happy normal", "hn"),
            ("mad normal", "mn"),
            ("nervous", "ner"),
            ("nervous 2", "ner2"),
            ("happy arms", "harm"),
            ("mad arms", "marm"),
            ("strike", "strk"),
            ("wind", "wind"),
            ("damage", "dmg")
        ])
    }
}

for value in charDict.values():
    value["icon"] = (
        "http://aceattorney.sparklin.org/Ressources/Images/persos/" +
        value["sprite"] + ".png"
    )

evDict = {
    "bear": {
        "name": "Bear",
        "icon": "ours"
    },
    "cat": {
        "name": "Cat",
        "icon": "chat"
    },
    "dog": {
        "name": "Dog",
        "icon": "chien"
    },
    "dog 2": {
        "name": "Dog 2",
        "icon": "chien2"
    },
    "lion": {
        "name": "Lion",
        "icon": "lion"
    },
    "monkey": {
        "name": "Monkey",
        "icon": "orangOutan"
    },
    "tiger": {
        "name": "Tiger",
        "icon": "tigre"
    },
    "baseball glove": {
        "name": "Baseball glove",
        "icon": "GantBaseBall"
    },
    "bloody button": {
        "name": "Bloody button",
        "icon": "boutonSang"
    },
    "bloody muffler": {
        "name": "Bloody muffler",
        "icon": "echarpeSang"
    },
    "bloody robe": {
        "name": "Bloody robe",
        "icon": "costumeSang"
    },
    "bloody shoe": {
        "name": "Bloody shoe",
        "icon": "chaussureSang"
    },
    "broken glasses": {
        "name": "Broken glasses",
        "icon": "lunettesCassees"
    },
    "glove": {
        "name": "Glove",
        "icon": "gant"
    },
    "muffler": {
        "name": "Muffler",
        "icon": "Echarpe"
    },
    "camera": {
        "name": "Camera",
        "icon": "appareilPhoto"
    },
    "camera 2": {
        "name": "Camera",
        "icon": "appareilPhoto2"
    },
    "cell lana": {
        "name": "Cell phone (Lana)",
        "icon": "portableLana"
    },
    "cell maya": {
        "name": "Cell phone (Maya)",
        "icon": "portableMaya"
    },
    "cell phoenix": {
        "name": "Cell phone (Phoenix)",
        "icon": "portablePhoenix"
    },
    "tape": {
        "name": "Tape",
        "icon": "cassette"
    },
    "tracking device": {
        "name": "Tracking device",
        "icon": "traceur"
    },
    "transceiver": {
        "name": "Transceiver",
        "icon": "talkieWalkie"
    },
    "video camera": {
        "name": "Video camera",
        "icon": "cameraCachee"
    },
    "wiretap": {
        "name": "Wiretap",
        "icon": "ecouteTelephonique"
    },
    "book": {
        "name": "Book",
        "icon": "livre"
    },
    "card": {
        "name": "Card",
        "icon": "carte"
    },
    "envelope": {
        "name": "Envelope",
        "icon": "enveloppe"
    },
    "id card": {
        "name": "ID Card",
        "icon": "idCard"
    },
    "letter": {
        "name": "Letter",
        "icon": "lettre"
    },
    "newspaper": {
        "name": "Newspaper",
        "icon": "journal"
    },
    "passport": {
        "name": "Passport",
        "icon": "passeport"
    },
    "photo": {
        "name": "Photo",
        "icon": "photo"
    },
    "report": {
        "name": "Report",
        "icon": "dossier"
    },
    "bracelet": {
        "name": "Apollo's bracelet",
        "icon": "braceletApollo"
    },
    "badge": {
        "name": "Badge",
        "icon": "badge"
    },
    "engagement ring": {
        "name": "Engagement ring",
        "icon": "bagueFiancailles"
    },
    "magatama": {
        "name": "Magatama (Charged)",
        "icon": "magatama"
    },
    "magatama dull": {
        "name": "Magatama (Not charged)",
        "icon": "magatamaDecharge"
    },
    "pendant": {
        "name": "Pendant",
        "icon": "pendentif"
    },
    "jewel": {
        "name": "Priceless jewel",
        "icon": "BijouxHorsDePrix"
    },
    "bloody paper": {
        "name": "Bloody paper",
        "icon": "papierSang"
    },
    "card key": {
        "name": "Card key",
        "icon": "passeMagnetique"
    },
    "medicine": {
        "name": "Cold Killer X",
        "icon": "ColdKillerZ"
    },
    "de killer": {
        "name": "De Killer's Card",
        "icon": "carteDeKiller"
    },
    "empty bottle": {
        "name": "Empty bottle",
        "icon": "bouteilleVide"
    },
    "glass shards": {
        "name": "Glass shards",
        "icon": "morceauxDeVerre"
    },
    "key": {
        "name": "Key",
        "icon": "cle"
    },
    "luminol": {
        "name": "Luminol",
        "icon": "luminol"
    },
    "playing cards": {
        "name": "Playing cards",
        "icon": "cartesAJouer"
    },
    "safe": {
        "name": "Safe",
        "icon": "coffre"
    },
    "the thinker": {
        "name": "The Thinker",
        "icon": "statuePenseur"
    },
    "ticket": {
        "name": "Ticket",
        "icon": "ticket"
    },
    "trilo": {
        "name": "Trilo",
        "icon": "marionnette"
    },
    "umbrella": {
        "name": "Umbrella",
        "icon": "parapluie"
    },
    "urn": {
        "name": "Urn",
        "icon": "urne"
    },
    "van": {
        "name": "Van",
        "icon": "van"
    },
    "watch": {
        "name": "Watch",
        "icon": "montre"
    },
    "broken bottle": {
        "name": "Broken bottle",
        "icon": "bouteilleCassee"
    },
    "bullet": {
        "name": "Bullet",
        "icon": "balle"
    },
    "bullet 2": {
        "name": "Bullet",
        "icon": "balle2"
    },
    "knife": {
        "name": "Knife",
        "icon": "couteau"
    },
    "knife 2": {
        "name": "Knife",
        "icon": "couteau2"
    },
    "knife 3": {
        "name": "Knife",
        "icon": "couteau3"
    },
    "knife 4": {
        "name": "Knife",
        "icon": "couteau4"
    },
    "knife 5": {
        "name": "Knife",
        "icon": "couteau5"
    },
    "pistol": {
        "name": "Pistol",
        "icon": "pistolet"
    },
    "pistol 2": {
        "name": "Pistol",
        "icon": "pistolet2"
    },
    "pistol 3": {
        "name": "Pistol",
        "icon": "pistolet3"
    },
    "samurai spear": {
        "name": "Samurai Spear",
        "icon": "lanceSamurai"
    },
    "switchblade tip": {
        "name": "Switchblade Tip",
        "icon": "lameCassee"
    },
    "whip": {
        "name": "Whip",
        "icon": "fouet"
    }
}

# objectDict's path is amended. See below.
objectDict = {
    "pw court": {
        "name": "Benches",
        "path": "pw_courtroom_benches"
        },
    "pw judge": {
        "name": "Judge Bench",
        "path": "pw_judge_bench"
        },
    "pw det": {
        "name": "Cell Frame",
        "path": "pw_detention_center"
        },
    "aj court": {
        "name": "Benches",
        "path": "aj_courtroom_benches"
        },
    "aj judge": {
        "name": "Judge Bench",
        "path": "aj_judge_bench"
        },
    "aj det": {
        "name": "Cell Frame",
        "path": "aj_detention_center"
        }
}

for obj in objectDict.values():
    obj["path"] = (
        "http://aceattorney.sparklin.org/Ressources/Images/defaultplaces/" +
        "foreground_objects/" + obj["path"] + ".gif"
        )

# If a place has an fgo, its place is edited after dict definition.
placeDict = {
    "gant l": {
        "name": "Gant's Office (Left)",
        "path": {
            "image": "Ace Attorney 1/BureauDeGant1"
        }
    },
    "gant c": {
        "name": "Gant's Office (Center)",
        "path": {
            "image": "Ace Attorney 1/BureauDeGantOrgue"
        }
    },
    "gant r": {
        "name": "Gant's Office (Right)",
        "path": {
            "image": "Ace Attorney 1/BureauDeGant2"
        }
    },
    "pw office": {
        "name": "Phoenix's Office",
        "path": {
            "image": "Ace Attorney 1/BureauDePhoenix"
        }
    },
    "me office": {
        "name": "Edgeworth's Office",
        "path": {
            "image": "Ace Attorney 1/BureauHunter"
        }
    },
    "studio gate": {
        "name": "Global Studio's Gate",
        "path": {
            "image": "Ace Attorney 1/GlobalStudioPortail"
        }
    },
    "gourd lake": {
        "name": "Gourd Lake",
        "path": {
            "image": "Ace Attorney 1/GourdLake"
        }
    },
    "gourd boat o": {
        "name": "Gourd Lake Boat Rental (Outside)",
        "path": {
            "image": "Ace Attorney 1/GourdLakeBoutique"
        }
    },
    "gourd boat i": {
        "name": "Gourd Lake Boat Rental (Inside)",
        "path": {
            "image": "Ace Attorney 1/GourdLakeDansBoutique"
        }
    },
    "gourd entrance": {
        "name": "Gourd Lake Entrance",
        "path": {
            "image": "Ace Attorney 1/GourdLakeEntree"
        }
    },
    "gourd forest l": {
        "name": "Gourd Lake Forest (Left)",
        "path": {
            "image": "Ace Attorney 1/GourdLakeForet1"
        }
    },
    "gourd forest r": {
        "name": "Gourd Lake Forest (Right)",
        "path": {
            "image": "Ace Attorney 1/GourdLakeForet2"
        }
    },
    "hotel a": {
        "name": "April's Hotel Room",
        "path": {
            "image": "Ace Attorney 1/HotelGatewaterChambre"
        }
    },
    "detention pw": {
        "name": "Detention Center",
        "path": {
            "image": "Ace Attorney 1/Parloir"
        }
    },
    "police office": {
        "name": "Police Station / Criminal Affairs",
        "path": {
            "image": "Ace Attorney 1/PoliceBureau"
        }
    },
    "ev lock l": {
        "name": "Evidence Lockers (Left)",
        "path": {
            "image": "Ace Attorney 1/PoliceCasiersDesDetectives1"
        }
    },
    "ev lock r": {
        "name": "Evidence Lockers (Right)",
        "path": {
            "image": "Ace Attorney 1/PoliceCasiersDesDetectives2"
        }
    },
    "police hq": {
        "name": "Police Headquarters",
        "path": {
            "image": "Ace Attorney 1/PoliceEntree"
        }
    },
    "police sec": {
        "name": "Police Security Room",
        "path": {
            "image": "Ace Attorney 1/PoliceSalleDeControle"
        }
    },
    "ev room": {
        "name": "Evidence Room",
        "path": {
            "image": "Ace Attorney 1/PoliceSalleDesPreuves"
        }
    },
    "airport": {
        "name": "Airport",
        "path": {
            "image": "Ace Attorney 2/Aeroport"
        }
    },
    "cellar": {
        "name": "Wine Cellar",
        "path": {
            "image": "Ace Attorney 2/CaveAVins"
        }
    },
    "secret": {
        "name": "Secret Room",
        "path": {
            "image": "Ace Attorney 2/ChambreSecrete"
        }
    },
    "berry": {
        "name": "Berry's Office",
        "path": {
            "image": "Ace Attorney 2/CirqueBureau"
        }
    },
    "cafe": {
        "name": "Circus Cafeteria",
        "path": {
            "image": "Ace Attorney 2/CirqueCafeteria"
        }
    },
    "acro": {
        "name": "Acro's Room",
        "path": {
            "image": "Ace Attorney 2/CirqueChambreAcro"
        }
    },
    "moe": {
        "name": "Moe's Room",
        "path": {
            "image": "Ace Attorney 2/CirqueChambreClown"
        }
    },
    "circus court": {
        "name": "Circus Courtyard",
        "path": {
            "image": "Ace Attorney 2/CirqueCour"
        }
    },
    "circus entrance": {
        "name": "Circus Entrance",
        "path": {
            "image": "Ace Attorney 2/CirqueEntree"
        }
    },
    "regina": {
        "name": "Circus Tent",
        "path": {
            "image": "Ace Attorney 2/CirqueTente"
        }
    },
    "hotti": {
        "name": "Hotti Clinic",
        "path": {
            "image": "Ace Attorney 2/CliniqueSashoff"
        }
    },
    "corrida l": {
        "name": "Corrida's Room (Left)",
        "path": {
            "image": "Ace Attorney 2/HotelGatewaterChambreCorrida1"
        }
    },
    "corrida r": {
        "name": "Corrida's Room (Right)",
        "path": {
            "image": "Ace Attorney 2/HotelGatewaterChambreCorrida2"
        }
    },
    "engarde hotel": {
        "name": "Engarde's Hotel Room",
        "path": {
            "image": "Ace Attorney 2/HotelGatewaterChambreEngarde"
        }
    },
    "hotel hall": {
        "name": "Gatewater Hallway",
        "path": {
            "image": "Ace Attorney 2/HotelGatewaterCouloir"
        }
    },
    "hotel ball": {
        "name": "Gatewater Ballroom",
        "path": {
            "image": "Ace Attorney 2/HotelGatewaterSalleDeBal"
        }
    },
    "hotel lobby": {
        "name": "Gatewater Lobby",
        "path": {
            "image": "Ace Attorney 2/HotelGatewaterSalleDeConference"
        }
    },
    "engarde house": {
        "name": "Engarde Lounge",
        "path": {
            "image": "Ace Attorney 2/MaisonEngarde"
        }
    },
    "kurain village": {
        "name": "Kurain Village",
        "path": {
            "image": "Ace Attorney 2/VillageKurain"
        }
    },
    "winding way": {
        "name": "Winding Way",
        "path": {
            "image": "Ace Attorney 2/VillageKurainAlleeDesVents"
        }
    },
    "kurain spare": {
        "name": "Spare Room",
        "path": {
            "image": "Ace Attorney 2/VillageKurainChambreDAmis"
        }
    },
    "summon l": {
        "name": "Summoning Chamber (Left)",
        "path": {
            "image": "Ace Attorney 2/VillageKurainChambreDeChanelling1"
        }
    },
    "summon c": {
        "name": "Summoning Chamber (Center)",
        "path": {
            "image": "Ace Attorney 2/VillageKurainChambreDeChanelling2"
        }
    },
    "summon r": {
        "name": "Summoning Chamber (Right)",
        "path": {
            "image": "Ace Attorney 2/VillageKurainChambreDeChanelling3"
        }
    },
    "kurain hall": {
        "name": "Kurain Hall",
        "path": {
            "image": "Ace Attorney 2/VillageKurainHall"
        }
    },
    "prologue 1": {
        "name": "Prologue Doug On Ground",
        "path": {
            "image": "1"
        }
    },
    "prologue 2": {
        "name": "Prologue Talk (Grey)",
        "path": {
            "image": "2"
        }
    },
    "prologue 3": {
        "name": "Phoenix Phoenix Over Corpse",
        "path": {
            "image": "3"
        }
    },
    "prologue 4": {
        "name": "Phoenix Phoenix Over Corpse (Zoom)",
        "path": {
            "image": "4"
        }
    },
    "prologue 5": {
        "name": "Prologue Shove (Grey)",
        "path": {
            "image": "5"
        }
    },
    "prologue 6": {
        "name": "Prologue Finds Corpse (Grey)",
        "path": {
            "image": "6"
        }
    },
    "blue screens": {
        "name": "Blue Screens Inc",
        "path": {
            "image": "BlueScreensInc"
        }
    },
    "atmey": {
        "name": "Luke Atmey's Office",
        "path": {
            "image": "BureauAtmey"
        }
    },
    "mask": {
        "name": "Mask DeMasque's Lair",
        "path": {
            "image": "ChambreMask"
        }
    },
    "haza main": {
        "name": "Hazakura - Main Hall",
        "path": {
            "image": "HazakurainBatimentPrincipal"
        }
    },
    "haza shack": {
        "name": "Hazakura - Heavenly Hall",
        "path": {
            "image": "HazakurainCabine"
        }
    },
    "haza enter": {
        "name": "Hazakura - Temple Entrance",
        "path": {
            "image": "HazakurainEntree"
        }
    },
    "haza court": {
        "name": "Hazakura - Courtyard",
        "path": {
            "image": "HazakurainExterieur"
        }
    },
    "haza bridge": {
        "name": "Hazakura - Bridge",
        "path": {
            "image": "HazakurainPont"
        }
    },
    "haza hall": {
        "name": "Hazakura - Training Hall",
        "path": {
            "image": "HazakurainSalleEntrainement"
        }
    },
    "haza inner l": {
        "name": "Hazakura - Inner (Left)",
        "path": {
            "image": "HazakurainTempleInterieur1"
        }
    },
    "haza inner r": {
        "name": "Hazakura - Inner (Right)",
        "path": {
            "image": "HazakurainTempleInterieur2"
        }
    },
    "haza garden": {
        "name": "Hazakura - Garden",
        "path": {
            "image": "HazakurainTempleInterieurJardin"
        }
    },
    "kb office": {
        "name": "KB Security President's Office",
        "path": {
            "image": "KBSecurityBureauDuPresident"
        }
    },
    "kb guard": {
        "name": "KB Security Guard's Office",
        "path": {
            "image": "KBSecuritySalleSurveillance"
        }
    },
    "lt store": {
        "name": "Lordly Tailor",
        "path": {
            "image": "LordlyTailor"
        }
    },
    "lt basement l": {
        "name": "Lordly Tailor Basement (Left)",
        "path": {
            "image": "LordlyTailorBasement1"
        }
    },
    "lt basement r": {
        "name": "Lordly Tailor Basement (Right)",
        "path": {
            "image": "LordlyTailorBasement2"
        }
    },
    "tres l": {
        "name": "Tres Bien (Left)",
        "path": {
            "image": "RestaurantTresBien1"
        }
    },
    "tres r": {
        "name": "Tres Bien (Right)",
        "path": {
            "image": "RestaurantTresBien2"
        }
    },
    "tres kitchen": {
        "name": "Tres Bien (Kitchen)",
        "path": {
            "image": "RestaurantTresBienCuisine"
        }
    },
    "vitamin park": {
        "name": "Vitamin Square",
        "path": {
            "image": "SquareVitamine"
        }
    },
    "loan": {
        "name": "Tender Lender",
        "path": {
            "image": "TenderLender"
        }
    },
    "waa": {
        "name": "Wright Anything Agency",
        "path": {
            "image": "AgenceWright"
        }
    },
    "klavier": {
        "name": "Klavier's Office",
        "path": {
            "image": "BureauGavin"
        }
    },
    "kristoph": {
        "name": "Kristoph's Cell",
        "path": {
            "image": "CelluleGavin"
        }
    },
    "hickfield room": {
        "name": "Hickfield Clinic Room",
        "path": {
            "image": "CliniqueHickfield"
        }
    },
    "hickfield": {
        "name": "Hickfield Clinic Lobby",
        "path": {
            "image": "CliniqueHickfieldEntree"
        }
    },
    "meraktis office": {
        "name": "Meraktis Clinic Office",
        "path": {
            "image": "CliniqueMeraktisBureau"
        }
    },
    "meraktis out": {
        "name": "Meraktis Clinic Outside",
        "path": {
            "image": "CliniqueMeraktisEntree"
        }
    },
    "meraktis garage": {
        "name": "Meraktis Clinic Garage",
        "path": {
            "image": "CliniqueMeraktisGarage"
        }
    },
    "meraktis entrance": {
        "name": "Meraktis Clinic Entrance",
        "path": {
            "image": "CliniqueMeraktisInterieur"
        }
    },
    "borscht": {
        "name": "Borscht Bowl Club",
        "path": {
            "image": "ClubBorscht"
        }
    },
    "kitaki": {
        "name": "Kitaki Home",
        "path": {
            "image": "MaisonKitaki"
        }
    },
    "detention aj": {
        "name": "Detention Center",
        "path": {
            "image": "Parloir"
        }
    },
    "people entrance": {
        "name": "People Park Entrance",
        "path": {
            "image": "PeopleParkEntree"
        }
    },
    "people crime scene": {
        "name": "People Park Crime Scene",
        "path": {
            "image": "PeopleParkSceneCrime"
        }
    },
    "coli entrance": {
        "name": "Sunshine Coliseum Entrance",
        "path": {
            "image": "Stade"
        }
    },
    "coli hall": {
        "name": "Sunshine Coliseum Hallway",
        "path": {
            "image": "StadeCoulisses"
        }
    },
    "coli gavin": {
        "name": "Sunshine Coliseum Gavinners",
        "path": {
            "image": "StadeLogeGavin"
        }
    },
    "coli lamiroir l": {
        "name": "Sunshine Coliseum Lamiroir (Left)",
        "path": {
            "image": "StadeLogeLamiroir1"
        }
    },
    "coli lamiroir r": {
        "name": "Sunshine Coliseum Lamiroir (Right)",
        "path": {
            "image": "StadeLogeLamiroir2"
        }
    },
    "coli stage": {
        "name": "Sunshine Coliseum Stage",
        "path": {
            "image": "StadeScene"
        }
    },
    "eldoon": {
        "name": "Eldoon's",
        "path": {
            "image": "StandEldoon"
        }
    },
    "drew past l": {
        "name": "Drew Studio Past (Left)",
        "path": {
            "image": "StudioMonin1"
        }
    },
    "drew past r": {
        "name": "Drew Studio Past (Right)",
        "path": {
            "image": "StudioMonin2"
        }
    },
    "drew past desk": {
        "name": "Drew Studio Past (Desk)",
        "path": {
            "image": "StudioMoninAncien1"
        }
    },
    "drew now l": {
        "name": "Drew Studio Present (Left)",
        "path": {
            "image": "StudioMoninAncien2"
        }
    },
    "drew now r": {
        "name": "Drew Studio Present (Right)",
        "path": {
            "image": "StudioMoninAncienBureauVera"
        }
    },
    "drew now desk": {
        "name": "Drew Studio Present (Desk)",
        "path": {
            "image": "StudioMoninBureauVera"
        }
    },
    "pw bench": {
        "name": "PW Bench",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_courtroom",
            "fgo": [
                {
                    "id": 1,
                    "name": "Benches",
                    "image": "foreground_objects/pw_courtroom_benches",
                    "external": 1,
                    "hidden": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        }
    },
    "pw judge": {
        "name": "PW Judge",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_judge",
            "fgo": [
                {
                    "id": 1,
                    "name": "Judge Bench",
                    "image": "foreground_objects/pw_judge_bench",
                    "external": 1,
                    "hidden": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        }
    },
    "pw counsel": {
        "name": "PW Co-Counsel",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_cocouncil"
        }
    },
    "pw court loud": {
        "name": "PW Court (Loud) ",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_court_agitated"
        }
    },
    "pw court silent": {
        "name": "PW Court (Silent)",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_court_still"
        }
    },
    "pw lobby": {
        "name": "PW Defense Lobby",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_lobby"
        }
    },
    "pw det behind": {
        "name": "PW Detention Behind",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_detention_center",
            "fgo": [
                {
                    "id": 1,
                    "name": "Cell Frame",
                    "image": "foreground_objects/pw_detention_center",
                    "external": 1,
                    "hidden": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        }
    },
    "pw det ahead": {
        "name": "PW Detention Ahead",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_detention_center"
        }
    },
    "aj bench": {
        "name": "AJ Bench",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_courtroom",
            "fgo": [
                {
                    "id": 1,
                    "name": "Benches",
                    "image": "foreground_objects/aj_courtroom_benches",
                    "external": 1,
                    "hidden": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        }
    },
    "aj judge": {
        "name": "AJ Judge",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_judge",
            "fgo": [
                {
                    "id": 1,
                    "name": "Judge Bench",
                    "image": "foreground_objects/aj_judge_bench",
                    "external": 1,
                    "hidden": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        }
    },
    "aj counsel": {
        "name": "AJ Co-Counsel",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_cocounsil"
        }
    },
    "aj court loud": {
        "name": "AJ Court (Loud) ",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_court_agitated"
        }
    },
    "aj court silent": {
        "name": "AJ Court (Silent)",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_court_still"
        }
    },
    "aj lobby": {
        "name": "AJ Lobby",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_lobby"
        }
    },
    "aj det behind": {
        "name": "AJ Detention Behind",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_detention_center",
            "fgo": [
                {
                    "id": 1,
                    "name": "Cell Frame",
                    "image": "foreground_objects/aj_detention_center",
                    "external": 1,
                    "hidden": 0,
                    "x": 0,
                    "y": 0
                }
            ]
        }
    },
    "aj det ahead": {
        "name": "AJ Detention Ahead",
        "path": {
            "image": "../defaultplaces/backgrounds/aj_detention_center"
        }
    },
    "power def": {
        "name": "Scrolling Defense",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_scrolling_defense.gif"
        }
    },
    "power pros": {
        "name": "Scrolling Prosecution",
        "path": {
            "image": (
                "../defaultplaces/backgrounds/pw_scrolling_prosecution.gif"
            )
        }
    },
    "gavel 1": {
        "name": "Gavel x1",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_hammer.gif"
        }
    },
    "gavel 3": {
        "name": "Gavel x3",
        "path": {
            "image": "../defaultplaces/backgrounds/pw_hammer_triple.gif"
        }
    }
}

for place in placeDict.values():
    try:
        for obj in place["path"]["fgo"]:
            obj["image"] = (
                "http://aceattorney.sparklin.org/Ressources/Images/" +
                "defaultplaces/" + obj["image"] + ".gif"
                )
    except KeyError:
        pass

# Holding dict for music. A "dict" key-value is added to each inner dict.
# Each dictionary in "dict" has a path, to which preprend will be prepended.
temp_mus_dict = {
    "pw": {"prepend": "Ace Attorney 1/"},
    "jfa": {"prepend": "Ace Attorney 2/"},
    "t&t": {"prepend": "Ace Attorney 3/"},
    "aj": {"prepend": "Ace Attorney 4/"},
    "aai": {"prepend": "Ace Attorney Investigations : Miles Edgeworth/"},
    "pp": {"prepend": "Ace Attorney Investigations : Miles Edgeworth 2/"},
    "jaws": {"prepend": "Enter The Jaws Theme - GS Appellate Project/"},
    "orchestra": {"prepend": "Gyakuten Saiban Orchestra/"},
    "remix": {"prepend": "Remixes/"},
    "corteus": {"prepend": "Steven Corteus - Piano Rewrites/"}
}

temp_mus_dict["pw"]["dict"] = {
    "pw1": {
        "name": "PW Prologue",
        "path": "01 - Gyakuten Saiban - Prologue"
    },
    "pw2": {
        "name": "PW Lobby",
        "path": "02 - Courtroom Lounge ~ Beginning Prelude"
    },
    "pw3": {
        "name": "PW Court",
        "path": "03 - Gyakuten Saiban - Trial"
    },
    "pw4": {
        "name": "PW CE Moderato",
        "path": "04 - Examination ~ Moderate 2001"
    },
    "pw5": {
        "name": "PW Trick",
        "path": "05 - Logic and Trick"
    },
    "pw6": {
        "name": "PW Objection",
        "path": "06 - Ryuuichi Naruhodou ~ Objection! 2001"
    },
    "pw7": {
        "name": "PW CE Allegro",
        "path": "07 - Examination ~ Allegro 2001"
    },
    "pw8": {
        "name": "PW Pursuit",
        "path": "08 - Investigation ~ Cornered"
    },
    "pw9": {
        "name": "PW Announce the Truth",
        "path": "09 - Announce the Truth 2001"
    },
    "pw10": {
        "name": "PW Drama",
        "path": "10 - Suspense"
    },
    "pw11": {
        "name": "PW Final Pursuit",
        "path": "11 - Investigation ~ Cornered (Variation)"
    },
    "pw12": {
        "name": "PW Jingle",
        "path": "12 - Jingle ~ It Doesnt End Here"
    },
    "pw13": {
        "name": "PW Investigation",
        "path": "13 - Search ~ Opening 2001"
    },
    "pw14": {
        "name": "PW Maya",
        "path": "14 - Shinshuu Ryouri ~ Gyakuten Sisters Theme 2001"
    },
    "pw15": {
        "name": "PW Detention",
        "path": "15 - Police Cell ~ Jailers Elegy"
    },
    "pw16": {
        "name": "PW Gumshoe",
        "path": "16 - Keisuke Itonoko ~ Itonoko Geijissu"
    },
    "pw17": {
        "name": "Reminiscence Maya",
        "path": "17 - Reminiscence ~ True Evening of Grief"
    },
    "pw18": {
        "name": "Marvin Grossberg",
        "path": "18 - Soranosuke Hoshikage ~ Age, Regret, Reward"
    },
    "pw19": {
        "name": "PW Generic Witness",
        "path": "19 - Congratulations Everybody"
    },
    "pw20": {
        "name": "Reminiscence Global Studios",
        "path": "20 - Reminiscence ~ Light and Shadow at the Film Studio"
    },
    "pw21": {
        "name": "Steel Samurai",
        "path": "21 - Oo-edo Soldier Tonosaman"
    },
    "pw22": {
        "name": "Reminiscence DL6",
        "path": "22 - Reminiscence ~ DL6 Case"
    },
    "pw23": {
        "name": "PW Core",
        "path": "23 - Search ~ Core 2001"
    },
    "pw24": {
        "name": "Reminiscence Class Trial",
        "path": "24 - Reminiscence ~ Classroom Trial"
    },
    "pw25": {
        "name": "PW Victory",
        "path": "25 - Won the Lawsuit! ~ The First Success"
    },
    "pw26": {
        "name": "PW End",
        "path": "26 - Gyakuten Saiban - End"
    },
    "pw27": {
        "name": "Mia Fey",
        "path": "27 - Gyakuten Sisters Ballade"
    },
    "pw28": {
        "name": "Rise from the Ashes Prologue",
        "path": "28 - Gyakuten Revival - Introduction"
    },
    "pw29": {
        "name": "Reminiscence SL9",
        "path": "29 - Recollection ~ SL9 Incident"
    },
    "pw30": {
        "name": "PW Ema Skye",
        "path": "30 - Hozuki Akane ~ Gyakuten Sisters Theme 2005"
    },
    "pw31": {
        "name": "Blue Badger",
        "path": "31 - TAIHO-KUN ~ I want to Defend!"
    },
    "pw32": {
        "name": "Jake Marshall",
        "path": (
            "32 - Zaimon Kyosuke ~ The Detective that came from the Wild West"
        )
    },
    "pw33": {
        "name": "Damon Gant",
        "path": "33 - Ganto Kaiji ~ Swimming, anyone"
    },
    "pw34": {
        "name": "Rise from the Ashes End",
        "path": "34 - Revival Gyakuten - End"
    }
}

temp_mus_dict["jfa"]["dict"] = {
    "jfa1": {
        "name": "JFA Prologue",
        "path": "01 - Justice For All - Prologue"
    },
    "jfa2": {
        "name": "Wellington Cell",
        "path": "02 - Ringtone (Richard Wellington)"
    },
    "jfa3": {
        "name": "JFA Lobby",
        "path": "03 - Courtroom Lounge ~ Another Prelude"
    },
    "jfa4": {
        "name": "JFA Court",
        "path": (
            "04 - Phoenix Wright Ace Attorney Justice For All - Trial Begins"
        )
    },
    "jfa5": {
        "name": "JFA CE Moderato",
        "path": "05 - Examination ~ Moderate 2002"
    },
    "jfa6": {
        "name": "JFA Trick",
        "path": "06 - Trick and Magic"
    },
    "jfa7": {
        "name": "JFA Objection",
        "path": "07 - Phoenix Wright ~ Objection! 2002"
    },
    "jfa8": {
        "name": "JFA CE Allegro",
        "path": "08 - Examination ~ Allegro 2002"
    },
    "jfa9": {
        "name": "JFA Pursuit",
        "path": "09 - Pursuit ~ Cornered"
    },
    "jfa10": {
        "name": "JFA Announce the Truth",
        "path": "10 - Announce the Truth 2002"
    },
    "jfa11": {
        "name": "Phoenix Cell",
        "path": "11 - Ringtone (Phoenix Wright)"
    },
    "jfa12": {
        "name": "JFA Final Pursuit",
        "path": "12 - Pursuit ~ Cornered (Variation)"
    },
    "jfa13": {
        "name": "JFA Jingle",
        "path": "13 - Jingle ~ Cant Sleep on a Night Like This"
    },
    "jfa14": {
        "name": "JFA Psyche Lock",
        "path": "14 - Psyche Lock"
    },
    "jfa15": {
        "name": "JFA Investigation",
        "path": "15 - Search ~ Opening 2002"
    },
    "jfa16": {
        "name": "JFA Maya",
        "path": "16 - Maya Fey ~ Turnabout Sisters Theme 2002"
    },
    "jfa17": {
        "name": "JFA Detention",
        "path": "17 - Police Cell ~ Elegy of Surveillance Cameras"
    },
    "jfa18": {
        "name": "Kurain",
        "path": "18 - Kurain Village"
    },
    "jfa19": {
        "name": "Reminiscence Mini",
        "path": "19 - Reminiscence ~ The Fire Carves Scars"
    },
    "jfa20": {
        "name": "JFA Odd Witness",
        "path": "20 - Eccentric"
    },
    "jfa21": {
        "name": "Max Galactica",
        "path": "21 - Fabulous!"
    },
    "jfa22": {
        "name": "Circus",
        "path": "22 - Tachimi - Circus"
    },
    "jfa23": {
        "name": "JFA Generic Witness",
        "path": "23 - Congratulations Everybody, Again"
    },
    "jfa24": {
        "name": "Reminiscence Bat",
        "path": "24 - Reminiscence ~ True Pain"
    },
    "jfa25": {
        "name": "de Killer",
        "path": "25 - Shelly de Killer ~ The Whim of a Murderous Gentleman"
    },
    "jfa26": {
        "name": "Pearl",
        "path": "26 - Pearl Fey ~ With Pearly"
    },
    "jfa27": {
        "name": "Matt Engarde",
        "path": "27 - Search ~ In the Midst 2002"
    },
    "jfa28": {
        "name": "Edgeworth",
        "path": "28 - Great Revival ~ Miles Edgeworth"
    },
    "jfa29": {
        "name": "JFA Suspense",
        "path": "29 - Hotline of Fate"
    },
    "jfa30": {
        "name": "JFA Core",
        "path": "30 - Search ~ Core 2002"
    },
    "jfa31": {
        "name": "Reminiscence Celeste",
        "path": "31 - Reminiscence ~ Steel Samurai Ballad"
    },
    "jfa32": {
        "name": "Franziska",
        "path": "32 - Great Revival ~ Franziska von Karma"
    },
    "jfa33": {
        "name": "JFA Victory",
        "path": "33 - Won the Lawsuit! ~ Another Victory"
    },
    "jfa34": {
        "name": "JFA End",
        "path": "34 - Phoenix Wright Ace Attorney Justice For All - End"
    },
    "jfa35": {
        "name": "JFA Post-Credit",
        "path": "35 - Prosecutors Murmur ~ Until We Meet Again"
    }
}

temp_mus_dict["t&t"]["dict"] = {
    "t&t1": {
        "name": "T&T Prologue",
        "path": "01 Gyakuten Saiban 3 - Prologue"
    },
    "t&t2": {
        "name": "T&T Lobby",
        "path": "02 Courtroom Lounge ~ Neverending Overture"
    },
    "t&t3": {
        "name": "T&T Trial",
        "path": "03 Gyakuten Saiban 3 - Trial"
    },
    "t&t4": {
        "name": "T&T CE Moderato",
        "path": "04 Examination ~ Moderate 2004"
    },
    "t&t5": {
        "name": "T&T Objection",
        "path": "05 Ryuuichi Naruhodou ~ Objection! 2004"
    },
    "t&t6": {
        "name": "T&T CE Allegro",
        "path": "06 Examination ~ Allegro 2004"
    },
    "t&t7": {
        "name": "T&T Pursuit",
        "path": "07 Investigation ~ Cross-examining"
    },
    "t&t8": {
        "name": "T&T Announce the Truth",
        "path": "08 Inform the Truth 2004"
    },
    "t&t9": {
        "name": "T&T Final Pursuit",
        "path": "09 Investigation ~ Cross-examining (Variation)"
    },
    "t&t10": {
        "name": "Dahlia Hawthorne",
        "path": "10 Distant traces of beauty"
    },
    "t&t11": {
        "name": "Godot",
        "path": "11 Godo - The fragrance of dark coffee"
    },
    "t&t12": {
        "name": "T&T Jingle",
        "path": "12 Jingle - Cant Turn Back to Everyday Life"
    },
    "t&t13": {
        "name": "T&T Investigation",
        "path": "13 Search ~ Opening 2004"
    },
    "t&t14": {
        "name": "Stolen Prologue",
        "path": "14 Stolen Reversal"
    },
    "t&t15": {
        "name": "Lordly Tailor",
        "path": "15 Takabishiya Department Store"
    },
    "t&t16": {
        "name": "T&T Detention",
        "path": "16 Police Cell ~ Elegy of the Captured"
    },
    "t&t17": {
        "name": "Mask deMask",
        "path": "17 Mysterious Masked Person ~ Please Listen!"
    },
    "t&t18": {
        "name": "Luke Atmey",
        "path": "18 Star dignity"
    },
    "t&t19": {
        "name": "Larry Butz",
        "path": "19 Yahari Masashi ~ In the Shadows of the Government"
    },
    "t&t20": {
        "name": "Recipe Prologue",
        "path": "20 Reversal Change"
    },
    "t&t21": {
        "name": "Tres Bien",
        "path": "21 Beauty hermitage"
    },
    "t&t22": {
        "name": "Victor Kudo",
        "path": "22 The Igarashi Officers - Inspection War Song"
    },
    "t&t23": {
        "name": "Furio Tigre",
        "path": "23 Warehouse Tiger"
    },
    "t&t24": {
        "name": "Reminiscence Viola",
        "path": "24 Reminiscence - What the Others Have Seen"
    },
    "t&t25": {
        "name": "Beginnings Prologue",
        "path": "25 Reversal Begin "
    },
    "t&t26": {
        "name": "Reminiscence Dusky",
        "path": "26 Reminiscence - Viewing the Hazy Bridge and Its Scenery"
    },
    "t&t27": {
        "name": "Hazakura",
        "path": "27 Hazakurain"
    },
    "t&t28": {
        "name": "Misty Fey",
        "path": "28 Terujotko Ellis ~ Simple Melody"
    },
    "t&t29": {
        "name": "T&T Core",
        "path": "29 Search ~ Middle Stage 2004"
    },
    "t&t30": {
        "name": "Reminiscence Godot",
        "path": "30 Reminiscence - The Bitter Taste of Truth"
    },
    "t&t31": {
        "name": "Retro Cornered",
        "path": "31 Pursuit ~ Cornered 2004"
    },
    "t&t31a": {
        "name": "Retro Cornered GBA",
        "path": "31 Pursuit ~ Cornered 2004 GBA Version"
    },
    "t&t31b": {
        "name": "Retro Cornered Final",
        "path": "31 Pursuit ~ Cornered 2004 Variation"
    },
    "t&t32": {
        "name": "T&T Victory",
        "path": "32 Winning! - The Victory Does Not End"
    },
    "t&t33": {
        "name": "T&T End",
        "path": "33 Gyakuten Saiban 3 - End"
    },
    "t&t34": {
        "name": "T&T Post-Credit",
        "path": "34 Arrival Melody (Godo)"
    }
}

temp_mus_dict["aj"]["dict"] = {
    "aj1": {
        "name": "AJ Prologue",
        "path": "01 Gyakuten Saiban 4 - Prologue"
    },
    "aj2": {
        "name": "AJ Lobby",
        "path": "02 Courtroom Lobby ~ New Prelude"
    },
    "aj3": {
        "name": "AJ Trial",
        "path": "03 Gyakuten Saiban 4 - Trial"
    },
    "aj4": {
        "name": "AJ CE Moderato",
        "path": "04 Questioning ~ Moderato 2007"
    },
    "aj5": {
        "name": "AJ Trick",
        "path": "05 Trance Logic"
    },
    "aj6": {
        "name": "AJ Objection",
        "path": "06 Housuke Odoroki ~ A New Trial is in Session!"
    },
    "aj7": {
        "name": "AJ CE Allegro",
        "path": "07 Questioning ~ Allegro 2007"
    },
    "aj8": {
        "name": "AJ Announce the Truth",
        "path": "08 Telling the Truth 2007"
    },
    "aj9": {
        "name": "AJ Suspense",
        "path": "09 Thrill Theme ~ Suspense"
    },
    "aj10": {
        "name": "AJ Perceive",
        "path": "10 Seeing Through ~ Surge, Glance"
    },
    "aj11": {
        "name": "AJ Pursuit",
        "path": "11 Pressing Pursuit ~ Cornered"
    },
    "aj11a": {
        "name": "AJ Pursuit Final",
        "path": "11 Pressing Pursuit ~ Cornered (Variation)"
    },
    "aj12": {
        "name": "AJ Jingle",
        "path": "12 Jingle ~ Thats All for Today"
    },
    "aj13": {
        "name": "Trucy",
        "path": "13 Minukis Theme ~ The Magic Girl"
    },
    "aj14": {
        "name": "Klavier Gavin",
        "path": "14 Kyouya Garyuu ~ LOVE LOVE GUILTY"
    },
    "aj15": {
        "name": "AJ Ema Skye",
        "path": "15 Akane Houzuki ~ Scientist Detective"
    },
    "aj16": {
        "name": "AJ Investigation",
        "path": "16 Investigation ~ Opening 2007"
    },
    "aj17": {
        "name": "AJ Detention",
        "path": "17 Detention Center ~ Interview Tragicomedy"
    },
    "aj18": {
        "name": "Corner Prologue",
        "path": "18 Turnabout Street Corner"
    },
    "aj19": {
        "name": "AJ Odd Witness",
        "path": "19 Eccentric 2007"
    },
    "aj20": {
        "name": "Kitaki",
        "path": "20 Kitakitsune Family"
    },
    "aj21": {
        "name": "Klavier Cell",
        "path": "21 Ringtone - LOVE LOVE GUILTY"
    },
    "aj22": {
        "name": "Reminiscence Kitaki",
        "path": "22 Recollection ~ A Hurt Kitsune"
    },
    "aj23": {
        "name": "Guitar Serenade",
        "path": "23 Loving Guitars Serenade"
    },
    "aj24": {
        "name": "Troupe Gramarye",
        "path": "24 Arumajiki Troupe"
    },
    "aj25": {
        "name": "Reminiscence Gramarye",
        "path": "25 Recollection ~ A Fate Smeared by Tricks and Gadgets"
    },
    "aj26": {
        "name": "Lamiroir",
        "path": "26 Lamiroir ~ Sound of a Landscape Artist"
    },
    "aj27": {
        "name": "Succession Prologue",
        "path": "27 Turnabout Heir"
    },
    "aj28": {
        "name": "AJ Psyche Lock",
        "path": "28 Mentality Lock (Psycho Lock) 2007"
    },
    "aj29": {
        "name": "Misham Studio",
        "path": "29 Doburoku Studio"
    },
    "aj30": {
        "name": "Kristoph Gavin",
        "path": "30 Solitary Confinement ~ Darkness Theme"
    },
    "aj31": {
        "name": "AJ Core",
        "path": "31 Investigation ~ Core 2007"
    },
    "aj32": {
        "name": "Reminiscence Disbarred",
        "path": "32 Recollection ~ Forgotten Legend"
    },
    "aj33": {
        "name": "AJ Victory",
        "path": "33 We Won the Case! ~ Our Victory"
    },
    "aj34": {
        "name": "AJ End",
        "path": "34 Gyakuten Saiban 4 - End"
    }
}

temp_mus_dict["aai"]["dict"] = {
    "aai101": {
        "name": "AAI Prologue 1",
        "path": "101 Gyakuten Kenji - Prologue 1"
    },
    "aai101a": {
        "name": "AAI Prologue 2",
        "path": "101 Gyakuten Kenji - Prologue 2"
    },
    "aai102": {
        "name": "AAI Investigation Open",
        "path": "102 Investigation ~ Opening 2009"
    },
    "aai103": {
        "name": "AAI Invesigation Middle",
        "path": "103 Investigation ~ Middlegame 2009"
    },
    "aai104": {
        "name": "AAI Deduce",
        "path": "104 Investigation ~ Contradiction at the Crime Scene"
    },
    "aai105": {
        "name": "AAI Logic",
        "path": "105 Logic ~ The Way to the Truth"
    },
    "aai106": {
        "name": "AAI Core",
        "path": "106 Investigation ~ Core 2009"
    },
    "aai107": {
        "name": "AAI CE Moderato",
        "path": "107 Confrontation ~ Moderato 2009"
    },
    "aai108": {
        "name": "AAI Trick Moderato",
        "path": "108 Tricks and Gimmicks"
    },
    "aai109": {
        "name": "AAI Objection",
        "path": "109 Reiji Mitsurugi ~ Objection! 2009"
    },
    "aai110": {
        "name": "AAI CE Allegro",
        "path": "110 Confrontation ~ Allegro 2009"
    },
    "aai111": {
        "name": "AAI Announce the Truth",
        "path": "111 Confess the Truth 2009"
    },
    "aai112": {
        "name": "AAI Trick Allegro",
        "path": "112 Tricks and Baroque"
    },
    "aai113": {
        "name": "AAI CE Final",
        "path": "113 Confrontation ~ Presto 2009"
    },
    "aai114": {
        "name": "AAI Pursuit",
        "path": "114 Pursuit ~ Lying Coldly"
    },
    "aai114a": {
        "name": "AAI Pursuit Final",
        "path": "114 Pursuit ~ Lying Coldly (Variation)"
    },
    "aai115": {
        "name": "AAI Jingle",
        "path": "115 Jingle ~ Slight Break"
    },
    "aai116": {
        "name": "Kay Faraday",
        "path": "116 Mikumo Ichijo ~ The Great Truth Burglar"
    },
    "aai117": {
        "name": "Shi-Long Lang",
        "path": "117 Shiryu Ro ~ Speak up, Pup!"
    },
    "aai118": {
        "name": "Yatagarasu",
        "path": (
            "118 Yatagarasu ~ " +
            "The Gentleman Thief Who Dances in the Black Night"
        )
    },
    "aai119": {
        "name": "Airlines Prologue 1",
        "path": "119 Turnabout Airlines 1"
    },
    "aai119a": {
        "name": "Airlines Prologue 2",
        "path": "119 Turnabout Airlines 2"
    },
    "aai120": {
        "name": "Zinc LeBlanc",
        "path": "120 Zinc White ~ Time is Money"
    },
    "aai121": {
        "name": "Cammy Meele",
        "path": "121 Wakana Shiraoto ~ Good Niiight"
    },
    "aai122": {
        "name": "AAI Suspect",
        "path": "122 Doubted People"
    },
    "aai201": {
        "name": "Kidnapped Prologue 0",
        "path": "201 Swept-Away Turnabout ~ Overture to Kidnapping"
    },
    "aai202": {
        "name": "Gatewaterland",
        "path": "202 Taiho-kun March ~ Bando Land Theme"
    },
    "aai203": {
        "name": "Kidnapped Prologue 1",
        "path": "203 Swept-Away Turnabout ~ Tragedy in the Horror House 1"
    },
    "aai203a": {
        "name": "Kindapped Prologue 2",
        "path": "203 Swept-Away Turnabout ~ Tragedy in the Horror House 2"
    },
    "aai204": {
        "name": "AAI Eccentric Witness",
        "path": "204 Noisy People"
    },
    "aai205": {
        "name": "AAI Generic Witness",
        "path": "205 Interesting People"
    },
    "aai206": {
        "name": "Reminiscence Devorae",
        "path": "206 Reminiscence ~ False Relations"
    },
    "aai207": {
        "name": "AAI Little Thief",
        "path": (
            "207 Reproducing the Scene ~ " +
            "The Gentleman Thiefs Secret Weapon"
        )
    },
    "aai208": {
        "name": "AAI Court",
        "path": "208 Court ~ Guardians of the Law"
    },
    "aai209": {
        "name": "Reminiscence Prologue",
        "path": "209 Departed Turnabout"
    },
    "aai210": {
        "name": "Tyrell Badd",
        "path": "210 Ittetsu Bado ~ The Truth isnt Sweet"
    },
    "aai211": {
        "name": "Calisto Yew",
        "path": "211 Himiko Kazura ~ Let Me Laugh at the Cool"
    },
    "aai212": {
        "name": "Reminiscence KG-8",
        "path": "212 Reminiscence ~ KG-8 Case"
    },
    "aai213": {
        "name": "AAI Suspense",
        "path": "213 Crises of Fate"
    },
    "aai214": {
        "name": "AAI Gumshoe",
        "path": "214 Keisuke Itonokogiri ~ I can do it when it counts, pal!"
    },
    "aai215": {
        "name": "Ablaze Prologue",
        "path": "215 Turnabout Up In Flames"
    },
    "aai216": {
        "name": "Allebahst Babahl",
        "path": "216 Two Embassies ~ The Lands of the Butterfly and the Flower"
    },
    "aai217": {
        "name": "Reminiscence Cohdopia",
        "path": "217 Reminiscence ~ Torn Apart Countries"
    },
    "aai218": {
        "name": "Quercus Alba",
        "path": "218 Carnage Onred ~ The Enemy Who Surpasses the Law"
    },
    "aai219": {
        "name": "AAI Victory",
        "path": "219 Solution! ~ Splendid Deduction"
    },
    "aai220": {
        "name": "AAI Credits",
        "path": "220 Reiji Mitsurugi ~ Great Revival 2009"
    },
    "aai221": {
        "name": "AAI End",
        "path": "221 Prosecutors Murmur ~ Promise to Meet Again"
    }
}

temp_mus_dict["pp"]["dict"] = {
    "pp101": {
        "name": "PP Prologue 1",
        "path": "101 Gyakuten Kenji 2 ~ Prologue 1"
    },
    "pp101a": {
        "name": "PP Prologue 2",
        "path": "101 Gyakuten Kenji 2 ~ Prologue 2"
    },
    "pp102": {
        "name": "Investigation Open",
        "path": "102 Investigation ~ Opening 2011"
    },
    "pp103": {
        "name": "PP Logic",
        "path": "103 Logic ~ Truth of the Crime Scene"
    },
    "pp104": {
        "name": "PP Trick Moderato",
        "path": "104 Trick Analyze"
    },
    "pp105": {
        "name": "PP Logic Chess Moderato",
        "path": "105 Logic Chess ~ Opening"
    },
    "pp106": {
        "name": "PP CE Moderato",
        "path": "106 Confrontation ~ Moderate 2011"
    },
    "pp107": {
        "name": "PP Objection",
        "path": "107 Reiji Mitsurugi ~ Objection! 2011"
    },
    "pp108": {
        "name": "PP Announce the Truth",
        "path": "108 Confess the Truth 2011"
    },
    "pp109": {
        "name": "PP Jingle",
        "path": "109 Jingle ~ Neverending Trouble"
    },
    "pp110": {
        "name": "Imprisoned Prologue",
        "path": "110 The Imprisoned Turnabout"
    },
    "pp111": {
        "name": "PP Investigation Middle",
        "path": "111 Investigation ~ Middlegame 2011"
    },
    "pp112": {
        "name": "Raymond Shields",
        "path": "112 Tateyuki Shigaraki ~ Joking Motive"
    },
    "pp113": {
        "name": "Sebastian DeBeste",
        "path": "113 Yumihiko Ichiyanagi ~ Ichiryuu's Reasoning"
    },
    "pp114": {
        "name": "PP CE Allegro",
        "path": "114 Confrontation ~ Allegro 2011"
    },
    "pp115": {
        "name": "Justine Courtney",
        "path": "115 Hakari Mikagami ~ Goddess of Law"
    },
    "pp116": {
        "name": "P.I.C.",
        "path": "116 Prosecutorial Investigation Committee ~ Rigorous Justice"
    },
    "pp117": {
        "name": "PP Suspect",
        "path": "117 Lamenting People"
    },
    "pp118": {
        "name": "PP Eccentric Witness",
        "path": "118 Strange People"
    },
    "pp119": {
        "name": "PP Little Thief",
        "path": (
            "119 Reproducing the Scene ~ " +
            "The Gentleman Thief's Secret Weapon 2011"
        )
    },
    "pp120": {
        "name": "PP Core",
        "path": "120 Investigation ~ Core 2011"
    },
    "pp121": {
        "name": "Patricia Roland",
        "path": "121 Marie Miwa ~ Hugs and Kisses"
    },
    "pp122": {
        "name": "Sirhan Dogen",
        "path": "122 Ryouken Houinbou ~ Tone of an Assassin"
    },
    "pp123": {
        "name": "PP CE Final",
        "path": "123 Confrontation ~ Presto 2011"
    },
    "pp124": {
        "name": "PP Pursuit",
        "path": "124 Pursuit ~ Wanting to Find the Truth"
    },
    "pp201": {
        "name": "Inherited Prologue 1",
        "path": "201 The Inherited Turnabout 1"
    },
    "pp201a": {
        "name": "Inherited Prologue 2",
        "path": "201 The Inherited Turnabout 2"
    },
    "pp202": {
        "name": "Gregory Edgeworth",
        "path": "202 Shin Mitsurugi  ~ A Defense Attorney's Knowledge"
    },
    "pp203": {
        "name": "Jeff Master",
        "path": "203 Issei Tenkai ~ Sweet Happiness"
    },
    "pp204": {
        "name": "PP Generic Witness",
        "path": "204 Restless People"
    },
    "pp205": {
        "name": "Reminiscence IS-7",
        "path": "205 Reminiscence ~ IS-7 Incident"
    },
    "pp206": {
        "name": "PP Trick Allegro",
        "path": "206 Trick Break"
    },
    "pp207": {
        "name": "Katherine Hall",
        "path": "207 Tsukasa Oyashiki ~ Sweet Dance"
    },
    "pp208": {
        "name": "Dane Gustavia",
        "path": "208 Yutaka Kazami ~ Brandished Flavor"
    },
    "pp209": {
        "name": "Forgotten Prologue",
        "path": "209 The Forgotten Turnabout"
    },
    "pp210": {
        "name": "PP Suspense",
        "path": "210 Trifle of Fate"
    },
    "pp211": {
        "name": "Reminiscence Amnesia",
        "path": "211 Reminiscence ~ The Girl's Lost Memories"
    },
    "pp212": {
        "name": "Reconciliation",
        "path": "212 Bonds ~ A Heart That Believes"
    },
    "pp213": {
        "name": "Grand Prologue 1",
        "path": "213 The Grand Turnabout 1"
    },
    "pp2213a": {
        "name": "Grand Prologue 2",
        "path": "213 The Grand Turnabout 2"
    },
    "pp214": {
        "name": "John Marsh",
        "path": "214 Shimon Aizawa ~ Pointed Age"
    },
    "pp215": {
        "name": "Moozilla",
        "path": "215 The Great Monster Borumosu"
    },
    "pp216": {
        "name": "Reminiscence Lang",
        "path": "216 Reminiscence ~ The Fall of the House of Lang"
    },
    "pp217": {
        "name": "Logic Chess Allegro",
        "path": "217 Logic Chess ~ Endgame"
    },
    "pp218": {
        "name": "Sebastian DeBeste Competent",
        "path": "218 Yumihiko Ichiyanagi ~ Ichiryuu's Farewell"
    },
    "pp219": {
        "name": "Justine Cell",
        "path": "219 Ringtone ~ Hakari Mikagami"
    },
    "pp220": {
        "name": "Zheng Fa",
        "path": "220 Zheng Fa ~ Land of the Phoenix"
    },
    "pp221": {
        "name": "Reminiscence SS5",
        "path": "221 Reminiscence ~ SS-5 Incident"
    },
    "pp222": {
        "name": "Simon Keyes",
        "path": "222 The Man Who Masterminds the Game"
    },
    "pp223": {
        "name": "PP Victory",
        "path": "223 Solution! ~ Calm Moment"
    },
    "pp224": {
        "name": "PP End",
        "path": "224 Prosecutor's Murmur ~ Each One's Path"
    },
    "pp225": {
        "name": "PP Credits",
        "path": "225 Gyakuten Kenji 2 ~ Great Revival"
    }
}

temp_mus_dict["jaws"]["dict"] = {
    "jpw3": {
        "name": "Jaws PW Trial",
        "path": "GS1 - 03 - Trial"
    },
    "jpw4": {
        "name": "Jaws PW CE Moderato",
        "path": "GS1 - 04 - Moderate"
    },
    "jpw5": {
        "name": "Jaws PW Trick",
        "path": "GS1 - 05 - Logic And Trick"
    },
    "jpw6": {
        "name": "Jaws PW Objection",
        "path": "GS1 - 06 - Objection"
    },
    "jpw7": {
        "name": "Jaws PW CE Allegro",
        "path": "GS1 - 07 - Allegro"
    },
    "jpw9": {
        "name": "Jaws PW Announce the Truth",
        "path": "GS1 - 09 - Inform The Truth"
    },
    "jpw10": {
        "name": "Jaws PW Suspense",
        "path": "GS1 - 10 - Suspense"
    },
    "jpw12": {
        "name": "Jaws PW Jingle",
        "path": "GS1 - 12 - It Doesnt End There"
    },
    "jpw13": {
        "name": "Jaws PW Investigation",
        "path": "GS1 - 13 - Search"
    },
    "jpw14": {
        "name": "Jaws PW Maya Fey",
        "path": "GS1 - 14 - Turnabout Sisters Dance Dx"
    },
    "jpw15": {
        "name": "Jaws PW Detention",
        "path": "GS1 - 15 - Jailers Elegy"
    },
    "jpw17": {
        "name": "Jaws Reminiscence Maya",
        "path": "GS1 - 17 - Reminiscence - True Meaning of Grief"
    },
    "jpw18": {
        "name": "Jaws Marvin Grossberg",
        "path": "GS1 - 18 - Old Regret Reward"
    },
    "jpw19": {
        "name": "Jaws PW Victory",
        "path": "GS1 - 19 - Congratulations Everyone"
    },
    "jpw19a": {
        "name": "Jaws PW Victory Slow",
        "path": "GS1 - 19 - Congratulations Everyone Slow"
    },
    "jpw21": {
        "name": "Jaws Stell Samurai",
        "path": "GS1 - 21 - Steel Samurai"
    },
    "jpw22": {
        "name": "Jaws Reminiscence DL6",
        "path": "GS1 - 22 - Reminiscence of the DL6"
    },
    "jpw23": {
        "name": "Jaws PW Core",
        "path": "GS1 - 23 - Core"
    },
    "jpw24": {
        "name": "Jaws Reminiscence Class Trial",
        "path": "GS1 - 24 - Reminiscence - Classroom Trial"
    },
    "jpw27": {
        "name": "Jaws PW Mia",
        "path": "GS1 - 27 - Naruhodou And His Piano"
    },
    "jpw31": {
        "name": "Jaws Blue Badger",
        "path": "GS1 - 31 - I Want To Defend Now!"
    },
    "jpw31a": {
        "name": "Jaws Blue Badger 2",
        "path": "GS1 - 31 - I Want To Defend!"
    },
    "jpw33": {
        "name": "Jaws Damon Gant",
        "path": "GS1 - 33 - Does Everyone Want to Swim"
    },
    "jjfa1": {
        "name": "Jaws T&T Prologue",
        "path": "GS2 - 01 - Arrival"
    },
    "jt&t11": {
        "name": "Jaws Godot",
        "path": "GS3 - 11 - Special Blend 9"
    },
    "jt&t28": {
        "name": "Jaws Misty Fey",
        "path": "GS3 - 28 - Simple Melody"
    },
    "jaj5": {
        "name": "Jaws AJ Trick",
        "path": "GS4 - 05 - Trance Logic"
    },
    "jaj14": {
        "name": "Jaws Klavier Gavin",
        "path": "GS4 - 14 - Reminiscence of a Guilty Lover"
    },
    "jaj20": {
        "name": "Jaws Kitaki",
        "path": "GS4 - 20 - Bob Your Head and Sway"
    },
    "jms": {
        "name": "Jaws Mugen Saiban",
        "path": "Mugen Saiban"
    }
}

temp_mus_dict["orchestra"]["dict"] = {
    "opw3": {
        "name": "Orchestra PW Lobby",
        "path": "1 - 03 - GyakutenSaiban-CourtBegins"
    },
    "opw3a": {
        "name": "Orchestra PW Lobby",
        "path": "1 - 03 - GyakutenSaiban-CourtBegins 2"
    },
    "opw4": {
        "name": "Orchestra PW CE Moderato",
        "path": "1 - 04 - CrossExamination-Moderate2001"
    },
    "opw4a": {
        "name": "Orchestra PW CE Moderato",
        "path": "1 - 04 - CrossExamination-Moderate2001 2"
    },
    "opw6": {
        "name": "Orchestra PW Objection",
        "path": "1 - 06 - NaruhodouRyuuichi-Objection2001"
    },
    "opw6a": {
        "name": "Orchestra PW Objection",
        "path": "1 - 06 - NaruhodouRyuuichi-Objection2001 2"
    },
    "opw8": {
        "name": "Orchestra PW Pursuit",
        "path": "1 - 08 - Pursuit-Cornered"
    },
    "opw8a": {
        "name": "Orchestra PW Pursuit",
        "path": "1 - 08 - Pursuit-Cornered 2"
    },
    "opw13": {
        "name": "Orchestra PW Investigation",
        "path": "1 - 13 - Investigation-Opening2001"
    },
    "opw14": {
        "name": "Orchestra PW Maya",
        "path": "1 - 14 - AyasatoMayoi-GyakutenSistersTheme"
    },
    "opw14a": {
        "name": "Orchestra PW Maya",
        "path": "1 - 14 - AyasatoMayoi-GyakutenSistersTheme 2"
    },
    "opw16": {
        "name": "Orchestra PW Gumshoe",
        "path": "1 - 16 - ItonokogiriKeisuke-DetectiveItonokoPal"
    },
    "opw16a": {
        "name": "Orchestra PW Gumshoe",
        "path": "1 - 16 - ItonokogiriKeisuke-DetectiveItonokoPal2"
    },
    "opw21": {
        "name": "Orchestra Steel Samurai",
        "path": "1 - 21 - WarriorOfGreatEdoTonosaman"
    },
    "opw21a": {
        "name": "Orchestra Steel Samurai",
        "path": "1 - 21 - WarriorOfGreatEdoTonosaman 2"
    },
    "opw23": {
        "name": "Orchestra PW Core",
        "path": "1 - 23 - Investigation-Core2001"
    },
    "opw31": {
        "name": "Orchestra Blue Badger",
        "path": "1 - 31 - Taiho-kun ~ I Want to Protect"
    },
    "opw32": {
        "name": "Orchestra Jake Marshall",
        "path": "1 - 32 - Zaimon Kyousuke ~ A Detective Without a Desert"
    },
    "opw33": {
        "name": "Orchestra Damon Gant",
        "path": "1 - 33 - GantoKaiji-SwimmingAnyone"
    },
    "ojfa1": {
        "name": "Orchestra JFA Prologue",
        "path": "2 - 01 - GyakutenSaiban2-Prologue"
    },
    "ojfa4": {
        "name": "Orchestra JFA Lobby",
        "path": "2 - 04 - GyakutenSaiban2-CourtBegins"
    },
    "ojfa4a": {
        "name": "Orchestra JFA Lobby",
        "path": "2 - 04 - GyakutenSaiban2-CourtBegins 2"
    },
    "ojfa5": {
        "name": "Orchestra JFA CE Moderato",
        "path": "2 - 05 - CrossExamination-Moderate2002"
    },
    "ojfa5a": {
        "name": "Orchesta JFA CE Moderato",
        "path": "2 - 05 - CrossExamination-Moderate2002 2"
    },
    "ojfa7": {
        "name": "Orchestra JFA Objection",
        "path": "2 - 07 - NaruhodouRyuuichi-Objection2002"
    },
    "ojfa7a": {
        "name": "Orchestra JFA Objection",
        "path": "2 - 07 - NaruhodouRyuuichi-Objection2002 2"
    },
    "ojfa9": {
        "name": "Orchestra JFA Pursuit",
        "path": "2 - 09 - Pursuit-Questioned"
    },
    "ojfa9a": {
        "name": "Orchestra JFA Pursuit",
        "path": "2 - 09 - Pursuit-Questioned 2"
    },
    "ojfa14": {
        "name": "Orchestra JFA Psyche Lock",
        "path": "2 - 14 - PsychoLock"
    },
    "ojfa25": {
        "name": "Orchestra de Killer",
        "path": "2 - 25 - KoroshiyaSazaemon-TheWhimofaMurderousGentleman"
    },
    "ojfa28": {
        "name": "Orchestra Edgeworth",
        "path": "2 - 28 - MitsurugiReiji-GreatRevival"
    },
    "ojfa28a": {
        "name": "Orchestra Edgeworth",
        "path": "2 - 28 - MitsurugiReiji-GreatRevival 2"
    },
    "ojfa28b": {
        "name": "Orchestra Edgeworth",
        "path": "2 - 28 - Reiji Mitsurugi ~ Great Revival"
    },
    "ot&t3": {
        "name": "Orchestra T&T Court",
        "path": "3 - 03 - GyakutenSaiban3-CourtBegins"
    },
    "ot&t3a": {
        "name": "Orchestra T&T Court",
        "path": "3 - 03 - GyakutenSaiban3-CourtBegins 2"
    },
    "ot&t4": {
        "name": "Orchestra T&T CE Moderato",
        "path": "3 - 04 - CrossExamination-Moderate2004"
    },
    "ot&t4a": {
        "name": "Orchestra T&T CE Moderato",
        "path": "3 - 04 - CrossExamination-Moderate2004 2"
    },
    "ot&t5": {
        "name": "Orchestra T&T Objection",
        "path": "3 - 05 - NaruhodouRyuuichi-Objection2004"
    },
    "ot&t5a": {
        "name": "Orchestra T&T Objection",
        "path": "3 - 05 - NaruhodouRyuuichi-Objection2004 2"
    },
    "ot&t7": {
        "name": "Orchestra T&T Pursuit",
        "path": "3 - 07 - Pursuit-Caught"
    },
    "ot&t7a": {
        "name": "Orchesta T&T Pursuit",
        "path": "3 - 07 - Pursuit-Caught 2"
    },
    "ot&t10": {
        "name": "Orchestra Dahlia Hawthorne",
        "path": "3 - 10 - MiyanagiChinami-DistantTraces"
    },
    "ot&t11": {
        "name": "Orchestra Godot",
        "path": "3 - 11 - Godot-FragranceOfDarkCoffee"
    },
    "ot&t11a": {
        "name": "Orchestra Godot",
        "path": "3 - 11 - Godot-FragranceOfDarkCoffee 2"
    },
    "ot&t17": {
        "name": "Orchestra Mask deMasque",
        "path": "3 - 17 - ThePhantomKamenMask-PleaseListen"
    },
    "ot&t23": {
        "name": "Orchestra Furio Tigre",
        "path": "3 - 23 - ToranosukeShibakuzou-SwinginZenitora"
    },
    "ot&t28": {
        "name": "Orchestra Misty Fey",
        "path": "3 - 28 - TenryuusaiElise-GentleMelody"
    },
    "ot&t33": {
        "name": "Orchestra T&T End",
        "path": "3 - 33 - GyakutenSaiban3-Epilogue"
    },
    "ot&t33a": {
        "name": "Orchestra T&T End",
        "path": "3 - 33 - GyakutenSaiban3-Epilogue 2"
    },
    "oaj3": {
        "name": "Orchestra AJ Court",
        "path": "4 - 03 - GyakutenSaiban4-CourtBegins"
    },
    "oaj4": {
        "name": "Orchestra AJ CE Moderato",
        "path": "4 - 04 - CrossExamination-Moderate2007"
    },
    "oaj6": {
        "name": "Orchestra AJ Objection",
        "path": "4 - 06 - OdorokiHousuke-StartOfANewTrial"
    },
    "oaj6a": {
        "name": "Orchestra AJ Objection",
        "path": "4 - 06 - OdorokiHousuke-StartOfANewTrial 2"
    },
    "oaj11": {
        "name": "Orchestra AJ Pursuit",
        "path": "4 - 11 - Pursuit-YouMustCornerIt"
    },
    "oaj15": {
        "name": "Orchestra AJ Ema Skye",
        "path": "4 - 15 - Akane Houzuki ~ Scientific Detective"
    },
    "oaj23": {
        "name": "Orchestra Guitar Serenade",
        "path": "4 - 23 - Loving-Guitars-Serenade"
    },
    "oaai105": {
        "name": "Orchestra AAI Logic",
        "path": "AAI - 105 - Logic ~ The Way to the Truth"
    },
    "oaai108": {
        "name": "Orchestra AAI Trick Allegro",
        "path": "AAI - 108 - Tricks and Gimmicks"
    },
    "oaai114": {
        "name": "Orchestra AAI Pursuit",
        "path": "AAI - 114 - Pursuit ~ Lying Coldy"
    },
    "oaai116": {
        "name": "Orchestra Kay Faraday",
        "path": "AAI - 116 - Mikumo Ichijo ~ The Great Truth Burglar"
    },
    "oaai220": {
        "name": "Orchestra AAI Credits",
        "path": "AAI - 220 - Reiji Mitsurugi ~ Great Revival 2009"
    },
    "opp102": {
        "name": "Orchestra PP Investigation Open",
        "path": "AAI 2 - 102 - Investigation ~ Opening 2011"
    },
    "opp104": {
        "name": "Orchestra PP Trick Moderato",
        "path": "AAI 2 - 104 - Trick Analyze"
    },
    "opp105": {
        "name": "Orchestra Logic Chess Moderato",
        "path": "AAI 2 - 105 - Logic Chess ~ Opening"
    },
    "opp106": {
        "name": "Orchestra PP CE Moderato",
        "path": "AAI 2 - 106 - Rebuttal ~ Moderate 2011"
    },
    "opp107": {
        "name": "Orchestra PP Objection",
        "path": "AAI 2 - 107 - Reiji Mitsurugi ~ Objection! 2011"
    },
    "opp107a": {
        "name": "Orchestra PP Objection",
        "path": "AAI 2 - 107 - Reiji Mitsurugi ~ Objection! 2011 2"
    },
    "opp111": {
        "name": "Orchestra PP Investigation Middle",
        "path": "AAI 2 - 111 - Investigation ~ Middlegame 2011"
    },
    "opp114": {
        "name": "Orchestra PP CE Allegro",
        "path": "AAI 2 - 114 - Rebuttal ~ Allegro 2011"
    },
    "opp115": {
        "name": "Orchestra Justine Courtney",
        "path": "AAI 2 - 115 - Hakari Mikagami ~ Goddess of Law"
    },
    "opp115a": {
        "name": "Orchestra Justine Courtney",
        "path": "AAI 2 - 115 - Hakari Mikagami ~ Goddess of Law 2"
    },
    "opp116": {
        "name": "Orchestra P.I.C.",
        "path": (
            "AAI 2 - 116 - Prosecutorial Investigation Committee " +
            "~ Rigorous Justice"
        )
    },
    "opp120": {
        "name": "Orchestra PP Core",
        "path": "AAI 2 - 120 - Investigation ~ Core 2011"
    },
    "opp123": {
        "name": "Orchestra PP CE Final",
        "path": "AAI 2 - 123 - Rebuttal ~ Presto 2011"
    },
    "opp124": {
        "name": "Orchestra PP Pursuit",
        "path": "AAI 2 - 124 - Pursuit ~ Wanting to Find the Truth"
    },
    "opp124a": {
        "name": "Orchestra PP Pursuit",
        "path": "AAI 2 - 124 - Pursuit ~ Wanting to Find the Truth 2"
    },
    "opp202": {
        "name": "Orchestra Gregory Edgworth",
        "path": "AAI 2 - 202 - Shin Mitsurugi ~ A Defense Attorney's Knowledge"
    },
    "opp205": {
        "name": "Orchestra Reminiscence IS7",
        "path": "AAI 2 - 205 - Reminiscence ~ IS-7 Incident"
    },
    "opp210": {
        "name": "Orchestra PP Suspense",
        "path": "AAI 2 - 210 - Trifle of Fate"
    },
    "opp212": {
        "name": "Orchestra Reconciliation",
        "path": "AAI 2 - 212 - Bonds ~ A Heart That Believes"
    },
    "opp225": {
        "name": "Orchestra PP Credits",
        "path": "AAI 2 - 225 - Gyakuten Kenji 2 ~ Great Revival"
    }
}

temp_mus_dict["remix"]["dict"] = {
    "bj badger": {
        "name": "Blue Jack Blue Badger",
        "path": "Blue Jack - Blue Badger I want to protect"
    },
    "bj godot": {
        "name": "Blue Jack Godot",
        "path": "Blue Jack - Godot - The Fragrance of Dark Coffee"
    },
    "bj objection": {
        "name": "Blue Jack PW Objection",
        "path": "Blue Jack - Objection! 2001 Remake"
    },
    "bj objection 2": {
        "name": "Blue Jack PW Objection",
        "path": "Blue Jack - Objection! 2001 v2"
    },
    "bj objection 3": {
        "name": "Blue Jack PW Objection",
        "path": "Blue Jack - Objection! 2001 v3"
    },
    "bj pursuit": {
        "name": "Blue Jack PW Pursuit",
        "path": "Blue Jack - Pressing Pursuit Cornered 2001"
    },
    "bj allegro": {
        "name": "Blue Jack PW Allegro",
        "path": "Blue Jack - Questioning Allegro 2001"
    },
    "bj allegro 2": {
        "name": "Blue Jack PW Allegro",
        "path": "Blue Jack - Questioning Allegro 2001 v2"
    },
    "bj moderato": {
        "name": "Blue Jack PW Moderato",
        "path": "Blue Jack - Questioning Moderato 2001 Remake"
    },
    "bj suspense": {
        "name": "Blue Jack Suspense",
        "path": "Blue Jack - Suspense"
    },
    "bj trucy": {
        "name": "Blue Jack Trucy Wright",
        "path": "Blue Jack - Trucy - Child of Magic"
    },
    "cadenza lobby": {
        "name": "Cadenza Lobby",
        "path": "Cadenza - 01 - Courtroom Lounge ~ Beginning Prelude"
    },
    "cadenza objection": {
        "name": "Cadenza Objection",
        "path": "Cadenza - 02 - Phoenix Wright ~ Objection! 2001"
    },
    "cadenza allegro": {
        "name": "Cadenza CE Allegro",
        "path": "Cadenza - 03 - Examination ~ Allegro 2001"
    },
    "cadenza maya": {
        "name": "Cadenza Maya Fey",
        "path": "Cadenza - 04 - Turnabout Sisters Theme 2001"
    },
    "cadenza detention": {
        "name": "Cadenza Detention",
        "path": "Cadenza - 05 - Reminiscence"
    },
    "cadenza steel samurai": {
        "name": "Cadenza Steel Samurai",
        "path": "Cadenza - 06 - The Steel Samurai"
    },
    "cadenza gumshoe": {
        "name": "Cadenza Gumshoe",
        "path": "Cadenza - 07 - Gumshoes Theme"
    },
    "cadenza core": {
        "name": "Cadenza Core",
        "path": "Cadenza - 08 - Search ~ Core 2001"
    },
    "cadenza grossberg": {
        "name": "Cadenza Marvin Grossberg",
        "path": "Cadenza - 09 - Age, Regret, Reward"
    },
    "cadenza pursuit": {
        "name": "Cadenza Pursuit",
        "path": "Cadenza - 10 - Investigation ~ Cornered"
    },
    "cadenza victory": {
        "name": "Cadenza Victory",
        "path": "Cadenza - 11 - Won the Lawsuit!"
    },
    "cadenza end": {
        "name": "Cadenza End",
        "path": "Cadenza - 12 - Ace Attorney - End"
    },
    "enigmar moderato": {
        "name": "Enigmar AJ CE Moderato",
        "path": "Enigmar - Apollo Justice - Cross Examination"
    },
    "enigmar trucy": {
        "name": "Enigmar Trucy Wright",
        "path": "Enigmar - Child of Magic Dreaming - Trucy"
    },
    "enigmar pursuit": {
        "name": "Enigmar PW Pursuit",
        "path": "Enigmar - Cornered 2001"
    },
    "enigmar dahlia": {
        "name": "Enigmar Dahlia Hawthorne",
        "path": "Enigmar - Distant Traces of a Royal Pain in the Ass"
    },
    "enigmar serenade": {
        "name": "Enigmar Guitar Serenade",
        "path": "Enigmar - Guitars Serenade"
    },
    "enigmar gramarye": {
        "name": "Enigmar Gramarye",
        "path": "Enigmar - Troupe Gramarye"
    },
    "enigmar pearl": {
        "name": "Enigmar Pearl",
        "path": "Enigmar - Turnabout Sisters - Pearl - With Pearly"
    },
    "godo court": {
        "name": "Godo Court",
        "path": "Godo - Majestic - 1 - Proces - Ouverture"
    },
    "godo allegro": {
        "name": "Godo CE Allegro",
        "path": "Godo - Majestic - 2 - Examination - Allegro"
    },
    "godo moderato": {
        "name": "Godo CE Moderato",
        "path": "Godo - Majestic - 3 - Examination - Moderate"
    },
    "godo investigation": {
        "name": "Godo Investigation",
        "path": "Godo - Majestic - 4 - Investigation - Cross examining"
    },
    "godo objection": {
        "name": "Godot Objection",
        "path": "Godo - Majestic - 5 - Objection!"
    },
    "godo pursuit": {
        "name": "Godo Pursuit",
        "path": "Godo - Majestic - 6 - Investigation - Cornered"
    },
    "ocremix feeling": {
        "name": "OcRemix First Victory",
        "path": "OcRemix - This Feeling"
    },
    "torpw6": {
        "name": "Tor PW Objection",
        "path": "Tor4 - GS1 - 06 - Objection"
    },
    "torpw8": {
        "name": "Tor PW Concerned",
        "path": "Tor4 - GS1 - 08 - Cornered v2"
    },
    "torpw15": {
        "name": "Tow PW Detention",
        "path": "Tor4 - GS1 - 15 - Detention Center"
    },
    "torpw": {
        "name": "Tor PW Jake Marshall",
        "path": "Tor4 - GS1 - 32 - Jake Marshall"
    },
    "torjfa20": {
        "name": "Tor JFA Eccentric Witness",
        "path": "Tor4 - GS2 - 20 - Ecentric"
    },
    "torjfa26": {
        "name": "Tor Pearl",
        "path": "Tor4 - GS2 - 26 - Pearls Theme"
    },
    "torjfa28": {
        "name": "Tor Edgeworth",
        "path": "Tor4 - GS2 - 28 - Great Revival"
    },
    "tort&t10": {
        "name": "Tor Dahlia Hawthorne",
        "path": "Tor4 - GS3 - 10 - Dahlia Theme"
    },
    "tort&t11": {
        "name": "Tor Godot",
        "path": "Tor4 - GS3 - 11 - Godot"
    },
    "tort&t11a": {
        "name": "Tor Godot",
        "path": "Tor4 - GS3 - 11 - Godot v2"
    },
    "tort&t17": {
        "name": "Tor Stolen Prologue",
        "path": "Tor4 - GS3 - 17 - Stolen Turnabout Mask"
    },
    "tort&t18": {
        "name": "Tor Luke Atmey",
        "path": "Tor4 - GS3 - 18 - Luke Atmey"
    },
    "tott&t21": {
        "name": "Tor Tres Bien",
        "path": "Tor4 - GS3 - 21 - Tres Bien"
    },
    "tort&t21a": {
        "name": "Tor Tres Bien",
        "path": "Tor4 - GS3 - 21 - Tres Bien v2"
    },
    "tort&t22": {
        "name": "Tor Victor Kudo",
        "path": "Tor4 - GS3 - 22 - Victor Kudo"
    },
    "tort&t22a": {
        "name": "Tor Victor Kudo",
        "path": "Tor4 - GS3 - 22 - Victor Kudo v2"
    },
    "tort&t23": {
        "name": "Tor Furio Tigre",
        "path": "Tor4 - GS3 - 23 - Furio Tigre"
    },
    "toraj24": {
        "name": "Tor Gramarye",
        "path": "Tor4 - GS4 - 24 - Troupe Gramarye"
    },
    "toraj24a": {
        "name": "Tor Gramarye",
        "path": "Tor4 - GS4 - 24 - Troupe Gramarye v2"
    },
    "trailer maya": {
        "name": "Trailer PW Maya",
        "path": "Trailers - GS1 - Gyakuten Sisters Theme 2001"
    },
    "trailer pw pursuit": {
        "name": "Trailer PW Pursuit",
        "path": "Trailers - GS1 - Investigation - Cornered"
    },
    "trailer psyche lock": {
        "name": "Trailer JFA Psyche Lock",
        "path": "Trailers - GS2 - Psyche Lock"
    },
    "trailer court": {
        "name": "Trailer T&T Court",
        "path": "Trailers - GS3 - Court Begins"
    },
    "trailer godot": {
        "name": "Trailer T&T Godot",
        "path": "Trailers - GS3 - Godot - The Fragrance Of Dark Coffee"
    },
    "trailer dahlia": {
        "name": "Trailer T&T Dahlia Hawthorne",
        "path": "Trailers - GS3 - Miyanagi Chinami - Distant Traces"
    },
    "trailer objection": {
        "name": "Trailer T&T Objection",
        "path": "Trailers - GS3 - Objection 2004"
    },
    "trailer t&t pursuit": {
        "name": "Trailer T&T Pursuit",
        "path": "Trailers - GS3 - Pursuit Caught"
    }
}

temp_mus_dict["corteus"]["dict"] = {
    "scpw2": {
        "name": "Piano PW Lobby",
        "path": "AA1 - 02 - Courtroom lounge"
    },
    "scpw3": {
        "name": "Piano PW Court",
        "path": "AA1 - 03 - Court Begins"
    },
    "scpw4": {
        "name": "Piano PW CE Moderato",
        "path": "AA1 - 04 - Cross Examination (Moderato)"
    },
    "scpw5": {
        "name": "Piano PW Trick",
        "path": "AA1 - 05 - Logic and Trick"
    },
    "scpw6": {
        "name": "Piano PW Objection",
        "path": "AA1 - 06 - Objection"
    },
    "scpw7": {
        "name": "Piano PW CE Allegro",
        "path": "AA1 - 07 - Cross Examination (Allegro)"
    },
    "scpw9": {
        "name": "Piano PW Truth",
        "path": "AA1 - 09 - Inform the Truth"
    },
    "scpw17": {
        "name": "Piano Reminiscence Maya",
        "path": "AA1 - 17 - Heartbroken Maya"
    },
    "scpw22": {
        "name": "Piano Reminiscence DL6",
        "path": "AA1 - 22 - DL-6 Case"
    },
    "scpw23": {
        "name": "Piano PW Investigation",
        "path": "AA1 - 23 - Investigation"
    },
    "scjfa10": {
        "name": "Piano JFA Announce the Truth",
        "path": "AA2 - 10 - Inform the truth"
    },
    "scjfa31": {
        "name": "Piano JFA Reminiscence Celeste",
        "path": "AA2 - 31 - Tonosaman Ballad"
    },
    "sct&t11": {
        "name": "Piano Godot",
        "path": "AA3 - 11 - Fragrance of dark coffee"
    },
    "sct&t18": {
        "name": "Piano Luke Atmey",
        "path": "AA3 - 18 - Luke Atmey"
    },
    "scaj6": {
        "name": "Piano AJ Objection",
        "path": "AA4 - 06 - Apollo Justice - Objection"
    }
}

musicDict = {}

# Prepend each music track's path with its AAO directory, and add it to the
# the real musicDict.
for subset in temp_mus_dict.values():
    for music in subset["dict"].values():
        music["path"] = subset["prepend"] + music["path"]
    musicDict.update(subset["dict"])

del temp_mus_dict

soundDict = {
    "harmonica": {
        "name": "Harmonica",
        "path": "Harmonica"
    },
    "whip": {
        "name": "Whip",
        "path": "Fouet2"
    },
    "air guitar": {
        "name": "Air guitar",
        "path": "Guitare"
    },
    "ray gun": {
        "name": "Ray gun",
        "path": "Pistolet Extraterrestre"
    },
    "gallery speaking": {
        "name": "Gallery speaking",
        "path": "Rumeur"
    },
    "game over": {
        "name": "Game over",
        "path": "Coup"
    },
    "gavel": {
        "name": "Gavel",
        "path": "Marteau"
    },
    "gavelx3": {
        "name": "Gavelx3",
        "path": "Tri-Gavel"
    },
    "guilty": {
        "name": "Guilty",
        "path": "Guilty"
    },
    "not guilty": {
        "name": "Not guilty",
        "path": "Notguilty"
    },
    "penalty": {
        "name": "Penalty",
        "path": "Bwaaah"
    },
    "testimony 1": {
        "name": "Testimony 1",
        "path": "Whaaa"
    },
    "testimony 2": {
        "name": "Testimony 2",
        "path": "Unvealed"
    },
    "victory": {
        "name": "Victory",
        "path": "VICTORY"
    },
    "lock breaks": {
        "name": "Lock breaks",
        "path": "Shatter"
    },
    "locks appear": {
        "name": "Locks appear",
        "path": "Rolling"
    },
    "camera click": {
        "name": "Camera click",
        "path": "Photo"
    },
    "desk slam": {
        "name": "Desk slam",
        "path": "TableSlam"
    },
    "door opening": {
        "name": "Door opening",
        "path": "OuverturePorte"
    },
    "flashback": {
        "name": "Flashback",
        "path": "Hush"
    },
    "loud gunshot": {
        "name": "Loud gunshot",
        "path": "Coupdefeu"
    },
    "new evidence": {
        "name": "New evidence",
        "path": "SelectJingle"
    },
    "quiet gunshot": {
        "name": "Quiet gunshot",
        "path": "Coupdefeu2"
    },
    "anger": {
        "name": "Anger",
        "path": "Fouet"
    },
    "growling stomach": {
        "name": "Growling stomach",
        "path": "Estomac qui gargouille"
    },
    "gulp": {
        "name": "Gulp",
        "path": "Avale"
    },
    "huh": {
        "name": "Huh",
        "path": "Key"
    },
    "idea": {
        "name": "Idea",
        "path": "Ding"
    },
    "oh no": {
        "name": "Oh no!",
        "path": "Awe"
    },
    "owned": {
        "name": "Owned",
        "path": "Slash"
    },
    "shocked": {
        "name": "Shocked",
        "path": "Dunnn"
    },
    "shouting": {
        "name": "Shouting",
        "path": "Shing"
    },
    "slap": {
        "name": "Slap",
        "path": "Baffe"
    },
    "snapping fingers": {
        "name": "Snapping fingers",
        "path": "ClacManfred"
    },
    "waaah": {
        "name": "Waaah!",
        "path": "Shock"
    },
    "whoops": {
        "name": "Whoops",
        "path": "Whoops"
    },
    "apollo gotcha": {
        "name": "Apollo Gotcha",
        "path": "Gotcha Apollo"
    },
    "apollo hold it": {
        "name": "Apollo Hold It",
        "path": "Hold It Apollo"
    },
    "apollo objection": {
        "name": "Apollo Objection",
        "path": "Objection Apollo"
    },
    "apollo take that": {
        "name": "Apollo Take That",
        "path": "Take that Apollo"
    },
    "edgeworth hold it": {
        "name": "Edgeworth Hold It",
        "path": "Hold it Edgeworth"
    },
    "edgeworth objection": {
        "name": "Edgeworth Objection",
        "path": "Objection Edgeworth"
    },
    "edgeworth take that": {
        "name": "Edgeworth Take That",
        "path": "Take that Edgeworth"
    },
    "franziska objection": {
        "name": "Franziska Objection",
        "path": "Objection Franziska"
    },
    "godot objection": {
        "name": "Godot Objection",
        "path": "Objection Godot"
    },
    "klavier objection": {
        "name": "Klavier Objection",
        "path": "Objection Konrad"
    },
    "kristoph objection": {
        "name": "Kristoph Objection",
        "path": "Objection Kristoph"
    },
    "manfred objection": {
        "name": "Manfred Objection",
        "path": "Objection Manfred"
    },
    "mia hold it": {
        "name": "Mia Hold It",
        "path": "Hold it Mia"
    },
    "mia objection": {
        "name": "Mia Objection",
        "path": "Objection Mia"
    },
    "mia take that": {
        "name": "Mia Take That",
        "path": "Take that Mia"
    },
    "payne objection": {
        "name": "Payne Objection",
        "path": "Objection Boulay"
    },
    "phoenix hold it": {
        "name": "Phoenix Hold It",
        "path": "Hold it Phoenix"
    },
    "phoenix objection": {
        "name": "Phoenix Objection",
        "path": "Objection Phoenix"
    },
    "phoenix take that": {
        "name": "Phoenix Take That",
        "path": "Take that Phoenix"
    }
}

popupDict = {
    "guilty": {
        "name": "Guilty",
        "path": "guilty"
    },
    "un instant": {
        "name": "Un instant",
        "path": "un-instant"
    },
    "protesto": {
        "name": "Protesto",
        "path": "protesto"
    },
    "un momento": {
        "name": "Un momento",
        "path": "un-momento"
    },
    "take that": {
        "name": "Take that",
        "path": "take-that"
    },
    "eureka": {
        "name": "Eureka",
        "path": "eureka"
    },
    "coupable": {
        "name": "Coupable",
        "path": "coupable"
    },
    "te tengo": {
        "name": "Te tengo",
        "path": "te-tengo"
    },
    "objection": {
        "name": "Objection",
        "path": "objection"
    },
    "whip": {
        "name": "Whip",
        "path": "fouet"
    },
    "hold it": {
        "name": "Hold it",
        "path": "hold-it"
    },
    "testimony": {
        "name": "Testimony",
        "path": "witness-testimony"
    },
    "whip 2": {
        "name": "Whip (Reversed)",
        "path": "fouet-inversee"
    },
    "game over": {
        "name": "Game over",
        "path": "game-over-doors"
    },
    "cross": {
        "name": "Cross",
        "path": "cross-examination"
    },
    "toma ya": {
        "name": "Toma ya",
        "path": "toma-ya"
    },
    "not so fast": {
        "name": "Not so fast",
        "path": "not-so-fast"
    },
    "gotcha": {
        "name": "Gotcha",
        "path": "gotcha"
    },
    "unlocked": {
        "name": "Unlocked",
        "path": "unlock-successful"
    },
    "prends ca": {
        "name": "Prends ca",
        "path": "prends-ca"
    },
    "j'te tiens": {
        "name": "J'te tiens",
        "path": "j-te-tiens"
    },
    "not guilty": {
        "name": "Not guilty",
        "path": "not-guilty"
    },
    "non coupable": {
        "name": "Non coupable",
        "path": "non-coupable"
    },
    "contre": {
        "name": "Contre",
        "path": "contre-interrogatoire"
    },
    "deposition": {
        "name": "Deposition",
        "path": "deposition-du-temoin"
    }
}

validation_dict = {
    "": {
        "use_default": True,
        "custom": {
            "ceStart", "sceIntro"
        }
    },
    "ceStart": {
        "use_default": False,
        "custom": {
            "ceStatement", "assist"
        }
    },
    "ceStatement": {
        "use_default": False,
        "custom": {
            "popup", "music", "sound", "place", "hide", "erase", "scroll",
            "typeSpeed", "blip", "mirror", "color", "sync", "sup", "cPos",
            "pPos", "speakerName", "speakerId", "setSprite", "dialogue",
            "makeFrame", "contra", "anc"
        }
    },
    "ceStatement and makeFrame": {
        "use_default": False,
        "custom": {
            "ceStatement", "assist"
        }
    },
    "assist": {
        "use_default": True,
        "custom": {
            "press", "fail", "ceEnd"
        }
    },
    "press": {
        "use_default": True,
        "custom": {
            "press", "fail", "ceEnd"
        }
    },
    "fail": {
        "use_default": True,
        "custom": {
            "ceEnd"
        }
    },
    "sceIntro": {
        "use_default": True,
        "custom": {
            "sceMain"
        }
    },
    "sceMain": {
        "use_default": False,
        "custom": {
            "music", "place", "erase", "scroll", "mirror", "sync", "sup",
            "cPos", "pPos", "setSprite", "makeFrame"
        }
    },
    "sceMain and makeFrame": {
        "use_default": False, "custom": {
            "sceTalk"
        }
    },
    "sceTalk": {
        "use_default": False,
        "custom": {
            "sceTalkConvo", "scePres"
        }
    },
    "sceTalkConvo": {
        "use_default": True,
        "custom": {
            "sceTalkConvo", "scePres"
        }
    },
    "scePresConvo": {
        "use_default": True,
        "custom": {
            "scePresConvo", "sceLocks", "sceExam"
        }
    },
    "sceLocks": {
        "use_default": True,
        "custom": {
            "sceExam"
        }
    },
    "sceExamConvo": {
        "use_default": True,
        "custom": {
            "sceExamConvo", "sceMove"
        }
    }
}
