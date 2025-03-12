import random

print("-----------LENGVESNI-----------")
# 1. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.
print("\n1. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.")


def two_numbers(a, b):
    print(a + b)


two_numbers(4, 14)

# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
print(
    "\n2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.")


def PISq():
    f = float(9.8596)
    return f


print(PISq())

# 3. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
print(
    "\n3. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.")


def multiply(a, b):
    c = a * b
    return c


print(multiply(5, 5))

# 4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
print("\n4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.")


def print_list(array):
    row = ""
    for a in array:
        row += (f"{a} ")
    print(row)


array = [1, 3, 5, 7, 9, 11]
print_list(array)

# 5. Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.
print(
    "\n5. Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.")


def min_max(min, max):
    return (random.randint(min, max))


print(min_max(0, 999))

# 6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.
print(
    f"\n6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.")


def random_array(min, max, length):
    array2 = []
    for a in range(0, length):
        a = random.randint(min, max)
        array2.append(a)
    return (array2)


print(random_array(1, 5, 3))

# 7. Sukurkite Funkciją kuri panaudotų 6-toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
print(
    "\n7. Sukurkite Funkciją kuri panaudotų 6-toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.")


def sum_array(random_array):
    sumarray = 0
    for num in random_array:
        sumarray = sumarray + num
    return (sumarray)


print(sum_array(random_array(1, 6, 10)))

# 8. Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
print(
    "\n8. Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).")


def array_average(random_array):
    arrayaverage = 0
    sumarray = 0
    length = 0
    for n in random_array:
        sumarray = sumarray + n
        length += 1
        arrayaverage = float(sumarray / length)
    return (arrayaverage)


print(array_average(random_array(1, 10, 6)))

# 9. Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.
print(
    "\n9. Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.")


def rectangle(length, width):
    for l in range(length):
        for w in range(width):
            print("*", end=" ")
        print()


rectangle(4, 5)

# 10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių (simbolių) ir tarpų. Sakinys - Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print(
    "\n10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių (simbolių) ir tarpų. Sakinys - Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)")


def sentence(sakinys):
    symbols = 0
    spaces = 0
    for s in sakinys:
        if s == " ":
            spaces += 1
        else:
            symbols += 1
    print(f"Number of symbols: {symbols}\nNumber of spaces: {spaces}")


sentence("Šiandien labai graži diena")

# 11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.
print(
    "\n11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.")


def reverse(fraze):
    return "".join(reversed(fraze))

def reverse2(fraze):
    return fraze[::-1]

def reverse3(fraze):
    fraze_reversed = ""
    for f in fraze:
        fraze_reversed = f + fraze_reversed
    return fraze_reversed

print(reverse("Sukurkite Funkciją"))
print(reverse2("Sukurkite Funkciją"))
print(reverse3("Sukurkite Funkciją"))

print("\n-----------SUNKESNI-----------")

# 1. Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)
print(
    "\n1. Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale.")

def dashes(fraze):
    print(f"---{fraze}---")

dashes("Labas Rytas")

# 2. Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75]. (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)
print(
    "\n2. Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].")

def generateRndStr(length):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
    text = ""
    for i in range(length):
        text += symbols[random.randint(0, len(symbols) - 1)]
    return text

random_symbols = generateRndStr(10)
print(random_symbols + "\n")
numbers = []
for r in random_symbols:
    if r.isdigit():
        numbers.append(r)
        print(f"[{numbers}]")
    else:
        print(f"{r}")

my_list = [1, 2, 'a', 3, 'b', 4, 'c']


# 3. Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 3.
# 4. Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77. Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.
# 5. Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777. Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių.
# 6. Sugeneruokite atsitiktinio (nuo 10 iki 20) ilgio masyvą, kurio visi, išskyrus paskutinį, elementai yra atsitiktiniai skaičiai nuo 0 iki 10, o paskutinis masyvas, kuris generuojamas pagal tokią pat salygą kaip ir pirmasis masyvas. Viską pakartokite atsitiktinį nuo 10 iki 30  kiekį kartų. Paskutinio masyvo paskutinis elementas yra lygus 0;
# 7. Suskaičiuokite šešto uždavinio elementų, kurie nėra masyvai, sumą. Skaičiuoti reikia visuose masyvuose ir submasyvuose.
# 8. Sugeneruokite masyvą iš trijų elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 33. Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius, prie masyvo pridėkite dar vieną elementą- atsitiktinį skaičių nuo 1 iki 33. Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą. Kartokite, kol sąlyga nereikalaus pridėti elemento. `
# 9. Sugeneruokite masyvą iš 10 elementų, kurie yra masyvai iš 10 elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 100. Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70, suraskite masyve mažiausią skaičių (nebūtinai pirminį) ir prie jo pridėkite 3. Vėl paskaičiuokite masyvo pirminių skaičių vidurkį ir jeigu mažesnis nei 70 viską kartokite.
