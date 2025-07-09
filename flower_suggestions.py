import random
flowers = {
    "Red": ["Rose", "Tulip", "Carnation", "Geranium", "Poppy", "Amaryllis", "Anemone", "Camellia"],
    "Purple": ["Lilac", "Orchid", "Lavender", "Allium", "Clematis", "Bellflower", "Iris", "Wisteria"],
    "Yellow": ["Sunflower", "Daffodil", "Marigold", "Dahlia", "Tulip", "Buttercup", "Goldenrod", "Forsythia"],
    "Blue": ["Bluebell", "Cornflower", "Delphinium", "Hydrangea", "Iris", "Periwinkle", "Forget-me-not", "Agapanthus"],
    "White": ["Lily", "Jasmine", "Daisy", "Gardenia", "Baby's Breath", "Magnolia", "Peony", "Snowdrop"],
    "Pink": ["Peony", "Cherry Blossom", "Azalea", "Carnation", "Begonia", "Camellia", "Dahlia", "Foxglove"],
    "Orange": ["Marigold", "Zinnia", "Nasturtium", "Buttercup", "Bird of Paradise", "Calendula", "Geum", "Tiger Lily"],
    "Green": ["Green Rose", "Bells of Ireland", "Green Hydrangea", "Green Zinnia", "Green Carnations", "Green Chrysanthemum"],
    "Black": ["Black Dahlia", "Black Rose", "Black Callas", "Black Pansy", "Black Tulip"],
    "Brown": ["Chocolate Cosmos", "Brown-Eyed Susan", "Cattail", "Brown Orchid"]
}

def what_flowers_1():
    while True:
        try:
            amount = int(input('How many flowers would you like? '))
            colour = input('Ok... what color would you like? ')
            if colour in flowers.keys():
                break
            else:
                print('That is not an available colour...')
        except ValueError:
            print('That is not a digit...')
    suggestions = []
    if amount > len(flowers[colour]):
        print(f"Hey, we don't actually have that many options in that colour, so I'm just going to give you {len(flowers[colour])} options...")
        print('Options:')
        for value in flowers[colour]:
            print(f'The {colour} {value}')
    else:
        while len(suggestions) < amount:
            option = flowers[colour][random.randint(0,len(flowers[colour]))]
            if option not in suggestions:
                suggestions.append(option)
        print('Options:')
        for option in suggestions:
            print(f'The {colour} {option}')


def what_flowers_2():
    while True:
        try:
            amount = int(input('How many flowers would you like? '))
            colour = input('Ok... what color would you like? ').split()
            check = True
            for col in colour:
                if col not in flowers.keys():
                    check = False
            if check == False:
                print('That is not an available colour...')
            else:
                break

        except ValueError:
            print('That is not a digit...')
    suggestions = []
    largest_possible = 0
    for col in colour:
        largest_possible += len(flowers[col])

    if amount > largest_possible:
        print(f"Hey, we don't actually have that many options in that colour, so I'm just going to give you {largest_possible} options...")
        amount = largest_possible

    while len(suggestions) < amount:
        current_colour = colour[random.randint(0,len(colour)-1)]
        option = flowers[current_colour][random.randint(0,len(flowers[current_colour])-1)]
        if (current_colour,option) not in suggestions:
            suggestions.append((current_colour,option))
    print('Options:')
    for option in suggestions:
        print(f'The {option[0]} {option[1]}')

what_flowers_2()
