from Kasutaja import Kasutaja
from admin import Admin

tavakasutaja = Kasutaja("Tava", "Kasutaja", "user", "qwerty")
tavakasutaja.tervita_kasutaja()

administraator = Admin("Admin", "Istraator", "root", "qwerty")
administraator.tervita_kasutaja()