"""
 2020 Spring Term Project
 2020105705 Park Hyunjun
 This program is for figuring out the best item-combination in League of Legends
"""

class item:
    def __init__(self, name, ad, ap, dp, mr, pp, mp, hp, price):
        self.ad, self.ap, self.dp, self.mr = (ad, ap, dp, mr)
        self.name, self.pp, self.mp, self.hp = (name, pp, mp, hp)
        self.price = price

    def __add__(self, other):
        return item(self.name + ", " + other.name, self.ad + other.ad,
                self.ap + other.ap, self.dp + other.dp, self.mr + other.mr,
                self.pp + other.pp, self.mp + other.mp, self.hp + other.hp,
                self.price + other.price)

    def __str__(self):
        return "({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(self.name, self.ad, self.ap, self.dp, self.mr,
                                                                      self.pp, self.mp, self.hp, self.price)

def compare(a, b, opt):
    if opt == 1 or opt == "ad":
        if a.ad > b.ad:
            return a
        elif a.ad < b.ad:
            return b
        else:
            compare(a, b, "price")
    elif opt == 2 or opt == "ap":
        if a.ap > b.ap:
            return a
        elif a.ap < b.ap:
            return b
        else:
            compare(a, b, "price")
    elif opt == 3 or opt == "dp":
        if a.dp > b.dp:
            return a
        elif a.dp < b.dp:
            return b
        else:
            compare(a, b, "price")
    elif opt == 4 or opt == "mr":
        if a.mr > b.mr:
            return a
        elif a.mr < b.mr:
            return b
        else:
            compare(a, b, "price")
    elif opt == 5 or opt == "pp":
        if a.pp > b.pp:
            return a
        elif a.pp < b.pp:
            return b
        else:
            compare(a, b, "price")
    elif opt == 6 or opt == "mp":
        if a.mp > b.mp:
            return a
        elif a.mp < b.mp:
            return b
        else:
            compare(a, b, "price")
    elif opt == 7 or opt == "hp":
        if a.hp > b.hp:
            return a
        elif a.hp < b.hp:
            return b
        else:
            compare(a, b, "price")
    elif opt == 8 or opt == "price":
        if a.price <= b.price:
            return a
        else:
           return b

def main():
    """ TEST PART """""""""""""""""""""""""""""""""""""""""#####################################################

    """ Item LIST """
    long_sword = item("롱소드", 10, 0, 0, 0, 0, 0, 0, 350)
    doran_sword = item("도란의 검", 8, 0, 0, 0, 0, 0, 0, 450)
    doran_shield = item("도란의 방패", 0, 0, 0, 0, 0, 0, 80, 450)
    doran_ring = item("도란의 반지", 0, 15, 0, 0, 0, 0, 60, 450)



    """ YOUR TEST """
    main_sword = long_sword + doran_sword + long_sword
    trinity = doran_ring + doran_ring + doran_sword

    print(compare(main_sword, trinity, "ap"))

    """"""""""""""""""""""""""""""""""""""""""""""""""""""##################################################

    """ SHELL PART """
    while True:
        command = (input("Input your option: ").strip())
        if command == 1 or command == "ad":
            print("ad")
        elif command == 2 or command == "ap":
            print("ap")
        elif command == 3 or command == "dp":
            print("dp")
        elif command == 4 or command == "mr":
            print("mr")
        elif command == 5 or command == "pp":
            print("pp")
        elif command == 6 or command == "mp":
            print("mp")
        elif command == 7 or command == "hp":
            print("hp")
        elif command == 8 or command == "price":
            print("price")
        elif command == "exit":
            return 0
        elif command == "help":
            print("< Tip >\n blabla")
        else:
            print("Invalid command, pleast re-enter your text")


if __name__ == "__main__":
    main()