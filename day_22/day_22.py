import time

def read_file():
    deck_1, deck_2 = '', ''
    with open('input.txt', 'r') as file:
        deck_1, deck_2 = file.read().split('\n\n')

    cards = { 'crab': [], 'player': [] }
    for card in deck_1.split('\n')[1:]:
        cards['crab'].append(int(card))
    for card in deck_2.split('\n')[1:]:
        cards['player'].append(int(card))

    return cards


def part_1(cards):
    while cards['player'] and cards['crab']:
        player_card, crab_card = cards['player'].pop(0), cards['crab'].pop(0)

        if player_card > crab_card:
            cards['player'] += [player_card, crab_card]
        else: 
            cards['crab'] += [crab_card, player_card]

    winner = 'player' if len(cards['player']) != 0 else 'crab'
    return sum([x * i for i, x in enumerate(reversed(cards[winner]), 1)])


def part_2(cards):
    previous = set()
    winner, round_winner = None, None
    while cards['player'] and cards['crab']:
        if (tuple(cards['player']), tuple(cards['crab'])) in previous:
            winner = 'crab'
            break

        previous.add((tuple(cards['player']), tuple(cards['crab'])))
        player_card, crab_card = cards['player'].pop(0), cards['crab'].pop(0)

        if player_card <= len(cards['player']) and crab_card <= len(cards['crab']):
            round_winner, _ = part_2({'player':cards['player'][:player_card], 'crab':cards['crab'][:crab_card]})
        else:
            round_winner = 'player' if player_card > crab_card else 'crab'

        if round_winner == 'crab':
            cards['crab'] += [crab_card, player_card]
        else:
            cards['player'] += [player_card, crab_card]

    if winner is None:
        winner = 'player' if len(cards['player']) != 0 else 'crab'
    
    return winner, sum([x * i for i, x in enumerate(reversed(cards[winner]), 1)])


def main():
    cards = read_file()

    ts = time.time()
    print(f'Silver: {part_1(cards)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    cards = read_file()

    ts = time.time()
    _, result = part_2(cards)
    print(f'Gold: {result}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
