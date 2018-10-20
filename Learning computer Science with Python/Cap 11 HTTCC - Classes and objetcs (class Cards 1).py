
""" módulo para juego de cartas de póker,
    Pica = Spade; Corazones = Heart; Diamantes = Diamonds y Trébol = Clubs
    el orden de menor a mayor en valor de Tipo/Palo = "Suit" es [0,1,2,3] = [Spade,Heart,Diamond,Club]
    y el orden trivial de los números será el ranking o "Rank" [1,2,3,4,5,6,7,8,9,10,11,12,13] = [AS,1,2,3,4,5,6,7,8,9,Zota=Jack,Reina=Queen,Rey=King]"""

class card:
    """define la clase Carta, con dos atributos, Suite y Rank, ambos números enteros de 0
    a 3 y de 0 a 13 respectivamente ordenados de menor a mayor"""
    ranks = {0:"Joker",1:"As",2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"Jack",12:"Queen",13:"King"}
    suits = {0:"Clubs",1:"Diamonds",2:"Hearts",3:"Spades"}

    def __init__(self,suit=0,rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "({0} of {1})".format(card.ranks[self.rank], card.suits[self.suit])

    def cmp(self, other):
        if self.suit < other.suit: return -1
        if self.suit > other.suit: return 1
        if self.rank == 1 and other.rank !=1: return 1
        elif self.rank != 1 and other.rank ==1: return -1
        else:
            if self.rank < other.rank: return -1
            if self.rank > other.rank: return 1

        return 0

    def __eq__(self,other):
        return self.cmp(other) == 0
    def __le__(self,other):
        return self.cmp(other) <= 0
    def __ge__(self,other):
        return self.cmp(other) >= 0
    def __lt__(self,other):
        return self.cmp(other) < 0
    def __gt__(self,other):
        return self.cmp(other) > 0
    def __ne__(self,other):
        return self.cmp(other) != 0

class Deck:
    """ Cada objeto es un mazo de cartas, compuesto por objetos de la clase card"""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(card(suit,rank))

    def __str__(self):
        d = ""
        for i in range(1,len(self.cards)+1):
            d +=("{0}"+" "*i + str(self.cards[i-1])+"\n").format(i)
        return d

    def artesanal_shuffle(self):
        import random
        rng = random.Random()
        for i in range(len(self.cards)):
            _ = rng.randrange(i,len(self.cards))
            (self.cards[i],self.cards[_]) = (self.cards[_],self.cards[i])

    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        #elimina la última carta del mazo
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self,hands,n_per_hand):
        #toma una lista de objetos "hands" y la cantidad de cartas por mano, luego reparte hasta acabar

        for i in range(999):
            if self.is_empty():
                break
            card = self.pop()
            hands[i % len(hands)].add(card)

    def deal_just(self,hands,n_per_hand):
        # toma una lista de objetos "hands" y la cantidad de cartas por mano, luego reparte hasta acabar

        for i in range(n_per_hand * len(hands)):
            if self.is_empty():
                break
            card = self.pop()
            hands[i % len(hands)].add(card)


class Hand(Deck):
    """Crea una clase "mano" hija de la clase padre "mazo" haciendo class mano(mazo)"""

    def __init__(self,name=""):
        self.cards = []
        self.name = name

    def __str__(self):
        h = "Hand of " + self.name+" "
        if self.is_empty():
            h += " is empty"
        else:
            h += "contains: "+"\n" + Deck.__str__(self)
        return h

    def add(self,card):
        return self.cards.append(card)

class CardGame:
    #prepara un mazo mezclado para empezar un juego

        def __init__(self):
            self.deck = Deck()
            self.deck.shuffle()

class HandOldMaind(Hand):

    def remove_matches2(self):
        cont = 0
        copia_hand = self.cards[:]
        for carta in copia_hand:
            target = card(3-carta.suit,carta.rank)
            if target in self.cards:
                self.remove(target)
                self.remove(carta)
                print("En la mano de {0} la carta {1} matches con la carta {2}".format(self.name,carta,target))
                cont += 1
        return cont

    def remove_matches(self):
        all_cards_from_hand = self.cards[:]
        cont = 0
        for cards in all_cards_from_hand:
            match = card(3-cards.suit,cards.rank)
            if match in self.cards:
                self.remove(cards)
                self.remove(match)
                print("In hand of {0}, {1} matches with {2}".format(self.name,str(cards),str(match)))
                cont += 1
        return cont

    def find_neighbor(self,hands,j):
        num_hands = len(hands)
        for i in range(num_hands):
            next = (i+1+j)%num_hands
            hands[next].shuffle()
            if not hands[next].is_empty():
                self.add(hands[next].pop())
                break

    def remove_all_matches(self):
        all_cards_from_hand = self.cards[:]
        cont1 = 0
        for cards in all_cards_from_hand:
            match = card(3 - cards.suit, cards.rank)
            if match in self.cards:
                self.remove(cards)
                self.remove(match)
                print("In hand of {0}, {1} matches with {2}".format(self.name, str(cards), str(match)))
                cont1 += 1
        return cont1

def prueba_pedido_carta_a_izquierda(num_hands):
    for j in range(num_hands):
        for i in range(1,num_hands):
            turno = (i+j)%num_hands
            print("jugador {0} le pide carta a jugador {1} ".format(j,turno))

class OldMaidGame(CardGame):

    def play_game(self,players):
        cont = 0
        mazo = self.deck
        hands = []
        mazo.remove(card(0,12))

        for player in players:
            hands.append(HandOldMaind(player))

        mazo.deal(hands,999)

        for hand in hands:
            print("first´s ",str(hand))

        for hand in hands:
            cont += hand.remove_matches()
            print("\n Ahora, los posibles matches fueron descartados, entonces ahora the ",str(hand))

        cont_time_estimated_unit = 0
        while cont <25:
            cont_time_estimated_unit += 1
            for i,hand in enumerate(hands):
                if hand.is_empty():
                    continue
                else:
                    print("Now, the ",str(hand))
                    hand.find_neighbor(hands,i)
                    print("And now, later the interchange, the ", str(hand))
                    cont += hand.remove_all_matches()
                    print("Finally, the ", str(hand))
        for hand in hands:
            if not hand.is_empty():
                print ("{0} loses, and the Game is Over".format(hand.name))

        from MyTime import My_time
        print("la cantidad de ciclos del juego fue de: ",cont_time_estimated_unit,"\n","estimando que cada jugada dura 0.5 min para encontrar el match, pero 1 min en elaborar la estrategia de engaño "
                                                                                       "da un total de: ",cont_time_estimated_unit*1.5,"minutos de juego, osea",My_time(0,cont_time_estimated_unit*1.5,0))



red_deck = Deck()
blue_deck = Deck()

"""
card1 = card(3,13)
card2 = card(3,1)

print(card1,card2)
print(card1<card2)

"""
red_deck.shuffle()

lola = HandOldMaind("lola")
lila = HandOldMaind("lila")
lali = HandOldMaind("lali")
red_deck.deal([lola,lila,lali],15)


game = OldMaidGame()
game.play_game(["lola","lila","lali","lele"])


"""
#testing
a =  card(1,5)
b = card(3,1)
print(a>b)
print(a<=b)
print(a!=b)
print(a)
print(a.suits[a.suit])
red_deck.shuffle()
blue_deck.artesanal_shuffle()
print(str(red_deck))
print(str(blue_deck))
print(str(red_deck))
red_deck.remove(card(3,10))
print(str(red_deck))
"""

# prueba de que el siguiente código ranguea el pedido de cartas consecutivas al jugador del la izquierda
# cuando los jugadores se disponen en ronda.

a = card(1,3)
b = card(3,2)

print(a<b)