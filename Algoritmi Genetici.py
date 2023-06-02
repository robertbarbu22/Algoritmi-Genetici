import random
import math
import copy

f= open("evolutie.txt","w")
r = open("input.txt", "r")

def calcul_polinom(x):
    return a * pow(x, 2) + b * x + c

def calcul_x(cromozom):
    x = 0
    p= 1
    for i in range(len(cromozom)):
        x += int(cromozom[i]) * pow(2, len(cromozom) - i - 1)
        p = p* 2
    return stanga + x * (dreapta - stanga) / pow(2.0,len(cromozom) )

def calcul_fitness(cromozom):

    x = calcul_x(cromozom)
    return calcul_polinom(x)



def recombinare(cromozomi, indici, p):
    cromozomi_rezultati = []
    if(p==0):
        f.write( "\n")
    if len(indici) % 2 == 0:
        # Se iau câte 2 cromozomi pentru recombinație
        while(len(indici)>1):
            indice1 = random.choice(indici)
            indice2 = random.choice(indici)

            if (indice1 != indice2):
                cromozom1 = cromozomi[indice1-1]
                cromozom2 = cromozomi[indice2-1]

                punct_taiere = random.randint(1, len(cromozom1) - 1)

                cromozom_rezultat1 = cromozom1[:punct_taiere] + cromozom2[punct_taiere:]
                cromozom_rezultat2 = cromozom2[:punct_taiere] + cromozom1[punct_taiere:]

                cromozomi[indice1 - 1]=cromozom_rezultat1
                cromozomi[indice2-1]=cromozom_rezultat2

                if(p==0):
                    f.write(f"Recombinare dintre cromozomul {indice1} cu cromozomul {indice2}:"+ "\n")
                    f.write(f"{''.join(cromozom1)} {''.join(cromozom2)} punct {(punct_taiere)}"+ "\n")
                    f.write(f"Rezultat    {''.join(cromozom_rezultat1)} {''.join(cromozom_rezultat2)}"+ "\n")


                indici.remove(indice1)
                indici.remove(indice2)

    if len(indici) > 1:
        while (len(indici) > 3):
            indice1 = random.choice(indici)
            indice2 = random.choice(indici)

            if (indice1 != indice2):
                cromozom1 = cromozomi[indice1 - 1]
                cromozom2 = cromozomi[indice2 - 1]

                punct_taiere = random.randint(1, len(cromozom1) - 1)

                cromozom_rezultat1 = cromozom1[:punct_taiere] + cromozom2[punct_taiere:]
                cromozom_rezultat2 = cromozom2[:punct_taiere] + cromozom1[punct_taiere:]

                cromozomi[indice1-1]=cromozom_rezultat1
                cromozomi[indice2-1]=cromozom_rezultat2

                if (p == 0):
                    f.write(f"Recombinare dintre cromozomul {indice1} cu cromozomul {indice2}:"+ "\n")
                    f.write(f"{''.join(cromozom1)} {''.join(cromozom2)} punct {punct_taiere}"+ "\n")
                    f.write(f"Rezultat    {''.join(cromozom_rezultat1)} {''.join(cromozom_rezultat2)}"+ "\n")

                indici.remove(indice1)
                indici.remove(indice2)



        ok=0

        while(ok==0):
            indice1 = random.choice(indici)
            indice2 = random.choice(indici)
            indice3 = random.choice(indici)
            if (indice1 != indice2 and indice2 != indice3 and indice1 != indice3):
                cromozom1 = cromozomi[indice1 - 1]
                cromozom2 = cromozomi[indice2 - 1]
                cromozom3 = cromozomi[indice3 - 1]
                ok=1

                punct_taiere = random.randint(1, len(cromozom1) - 1)

                cromozom_rezultat1 = cromozom1[:punct_taiere] + cromozom2[punct_taiere:]
                cromozom_rezultat2 = cromozom2[:punct_taiere] + cromozom3[punct_taiere:]
                cromozom_rezultat3 = cromozom3[:punct_taiere] + cromozom1[punct_taiere:]

                cromozomi[indice1-1] = cromozom_rezultat1
                cromozomi[indice2-1]=cromozom_rezultat2
                cromozomi[indice3-1]=cromozom_rezultat3

                if (p == 0):
                    f.write(f"Recombinare dintre cromozomul {indice1} cu cromozomul {indice2} si cromozomul {indice3}:"+ "\n")
                    f.write(f"{''.join(cromozom1)} {''.join(cromozom2)} {''.join(cromozom3)} punct {punct_taiere}"+ "\n")
                    f.write(f"Rezultat    {''.join(cromozom_rezultat1)} {''.join(cromozom_rezultat2)} {''.join(cromozom_rezultat3)}"+ "\n")


    # Returnăm lista de cromozomi recombinati
    return cromozomi




def mutatie(cromozomi):
    cromozomi_mutati = copy.deepcopy(cromozomi)
    for i in range(dimensiune):
        for j in range(lungime_cromozom):
            if random.random() < probabilitate_mutatie:
                cromozomi_mutati[i][j] = 1 - cromozomi_mutati[i][j]
    return cromozomi_mutati

dimensiune = int(r.readline())
stanga = int(r.readline())
dreapta = int(r.readline())
a = int(r.readline())
b = int(r.readline())
c = int(r.readline())
precizia = float(r.readline())
probabilitate_recombinare = float(r.readline())
probabilitate_mutatie = float(r.readline())
nr_etape = int(r.readline())

lungime_cromozom = math.ceil(math.log2((dreapta - stanga) * pow(10, precizia)))

#cromozomi genreati random

f.write ("Populatia initiala ")
f.write("\n")




cromozomi = [ [str(random.randint(0,1)) for i in range(lungime_cromozom)] for j in range(dimensiune)]
for i in range(dimensiune):
    f.write(str(i+1) +": "+ ''.join(cromozomi[i]) + " x= " + str(calcul_x(cromozomi[i])) + " f=" + str(calcul_fitness(cromozomi[i]) )+ "\n")

for p in range(nr_etape):
    max_fitness = -9999
    suma_fitness = 0
    cromozom_max_fitness = []
    for i in range(dimensiune):
        fitness_cromozom = calcul_fitness(cromozomi[i])
        suma_fitness += fitness_cromozom
        if fitness_cromozom > max_fitness:
            max_fitness = fitness_cromozom
            cromozom_max_fitness = cromozomi[i]

    if(p==0):
        f.write("\n" +"Probabilitati selectie: \n")
    intervale_selectie = [0]
    for i in range(dimensiune):
        if(p==0):
            f.write("cromozom     " + str(i+1) + " probabilitate " + str(calcul_fitness(cromozomi[i]) / suma_fitness) + "\n")
        intervale_selectie.append((calcul_fitness(cromozomi[i]) / suma_fitness )+ intervale_selectie[i])

    if(p==0):
        f.write("\n")
        f.write("Intervale probabilitati selectie: \n")
        for i in range(len(intervale_selectie)):
            f.write(str(intervale_selectie[i]) + " \n")
        f.write("\n")


    cromozomi_selectati = []
    for i in range(dimensiune):
        random_number = random.random()
        # Evidențierea procesului de selecție, care constă în generarea unui număr aleator u uniform pe[0, 1) și determinarea intervalului [qi , qi + 1) căruia aparține acest număr; corespunzător acestui interval se selectează cromozomul i+1.
        # Procesul se repeta pana cand se selecteaza numarul dorit de cromozomi.
        # Cerință: cautarea intervalului corespunzator se va face folosind cautare binara
        st = 0
        dr = dimensiune
        sol = 0
        while st <= dr:

            mij = (st + dr) // 2
            if intervale_selectie[mij] <= random_number:
                st = mij + 1

            else:
                dr = mij - 1
                sol = mij
        if(p==0):
            f.write("u=" + str(random_number) + " selectam cromozomul " + str(sol) + "\n")
        cromozomi_selectati.append(cromozomi[sol-1])

    if(p==0):
        f.write("\n")
        f.write("Dupa selectie: \n")
        for i in range(len(cromozomi_selectati)):
            f.write(str(i+1) +": "+ ''.join(cromozomi_selectati[i]) + " x= " + str(calcul_x(cromozomi_selectati[i])) + " f=" + str(calcul_fitness(cromozomi_selectati[i])))
            f.write("\n")
        f.write("\n")
        f.write("Probabilitatea de incrucisare "+ str(probabilitate_recombinare) + "\n")




    indici_rec = []
    i = 1
    for crom in cromozomi_selectati:
        prob = random.random()
        if(p==0):
            f.write(str(i) +": " + ''.join(crom) + " u=" + str(prob) )
            if(prob < probabilitate_recombinare):
                f.write("< "+ str(probabilitate_recombinare)+" participa")
            f.write("\n")

        if prob < probabilitate_recombinare:

            indici_rec.append(i)
        i += 1




    cromozomi_recombinati = recombinare(cromozomi_selectati, indici_rec, p)


    if(p==0):
        f.write("\nDupa recombinare: \n")
        for i in range(len(cromozomi_recombinati)):
            f.write(str(i + 1) + ": " + ''.join(cromozomi_recombinati[i]) + " x= " + str(calcul_x(cromozomi_recombinati[i])) + " f=" + str(
                calcul_fitness(cromozomi_recombinati[i])))
            f.write("\n")

    if(p==0):
        f.write("\n")
        f.write("Probabilitatea de mutatie pentru fiecare gena " + str(probabilitate_mutatie) + "\n")
        f.write("Au fost modificati cromozomii: \n")

    for i in range(dimensiune):
        ok=0
        for j in range(lungime_cromozom):
            prob = random.random()
            if prob < probabilitate_mutatie:
                ok=1
                if (cromozomi_recombinati[i][j] == '0'):
                    cromozomi_recombinati[i][j] = '1'
                else:
                    cromozomi_recombinati[i][j] = '0'
        if (p == 0 and ok==1):
            f.write(str(i + 1) + " " + "\n")

    if (p == 0):
        f.write("\nDupa mutatie: \n")
        for i in range(len(cromozomi_recombinati)):
            f.write(str(i + 1) + ": " + ''.join(cromozomi_recombinati[i]) + " x= " + str(
                calcul_x(cromozomi_recombinati[i])) + " f=" + str(
                calcul_fitness(cromozomi_recombinati[i])))
            f.write("\n")

    #inlocuim cromozomul ce cel mai slab fitness cu cromozomul memorat initial
    minim_fitness = 9999
    max_fitness = -9999
    sum = 0
    for i in range(dimensiune):
        if calcul_fitness(cromozomi_recombinati[i]) < minim_fitness:
            minim_fitness = calcul_fitness(cromozomi_recombinati[i])
            index_minim = i
        if calcul_fitness(cromozomi_recombinati[i]) > max_fitness:
            max_fitness = calcul_fitness(cromozomi_recombinati[i])
        sum += calcul_fitness(cromozomi_recombinati[i])

    if (p == 0):
        f.write("\nEvolutia maximului \n")
    cromozomi_recombinati[index_minim] = cromozom_max_fitness
    if(max_fitness < calcul_fitness(cromozom_max_fitness)):
        max_fitnes = calcul_fitness(cromozom_max_fitness)

    sum = sum - minim_fitness + calcul_fitness(cromozom_max_fitness)

    f.write(str(max_fitness) + " " + str(sum/dimensiune) + "\n" )

    cromozomi = cromozomi_recombinati

    cromozomi_selectati = []
    cromozomi_recombinati = []


    indici_rec = []










