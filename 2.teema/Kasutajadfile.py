from Kasutajad import Kasutaja
# 1. kasutaja
alice  = Kasutaja() # loome objekti nimega alice
# määrame alice oma atribuutide väärtused
alice.eesnimi = "Alice"
alice.perenimi = "Ime"
alice.kasutaja_nimi = "alice"
alice.parool = "qwerty"
# kutsume tööle alice oma meetodid
alice.kirjelda_kasutaja()
print()
alice.tervita_kasutaja()

# 2. kasutaja
bob = Kasutaja()\
bob.eesnimi = "Bob"
bob.perenimi = "Kob"
bob.kasutaja_nimi = "bob"
bob.parool = "qwerty"
bob.kirjelda_kasutaja()
print()
bob.tervita_kasutaja()

# 3.kasutaja
robert = Kasutaja()
robert.eesnimi = "Robert"
robert.perenimi = "Rob"
robert.kasutaja_nimi = "robert"
robert.parool = "qwerty"
