# Day 22: Crab Combat
import collections as coll


def main():
    players = parse_input('22.txt')
    player1 = coll.deque(players[0])
    player2 = coll.deque(players[1])
    part_one(player1.copy(), player2.copy())
    part_two(player1.copy(), player2.copy())


def parse_input(file_path):
    with open(file_path) as file:
        players = file.read().rstrip().split('\n\n')
        return [parse_player(player) for player in players]


def parse_player(text):
    return [int(card) for card in text.split('\n')[1:]]


def part_one(player1, player2):
    winner = play_game(player1, player2)
    score = calculate_score(winner)
    print("Part one score: {}".format(score))


def play_game(player1, player2):
    while True:
        if len(player1) == 0:
            return player2
        if len(player2) == 0:
            return player1
        card1 = player1.popleft()
        card2 = player2.popleft()
        assert card1 != card2
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)


def calculate_score(player):
    factors = list(range(len(player), 0, -1))
    return sum(card * factor for card, factor in zip(player, factors))


def part_two(player1, player2):
    winner = player1 if play_recursive_game(player1, player2) else player2
    score = calculate_score(winner)
    print("Part two score: {}".format(score))


def play_recursive_game(player1, player2):
    seen = set()
    while True:
        if len(player1) == 0:
            return False
        if len(player2) == 0:
            return True
        configuration = (tuple(player1), tuple(player2))
        if configuration in seen:
            return True
        seen.add(configuration)
        card1 = player1.popleft()
        card2 = player2.popleft()
        if len(player1) >= card1 and len(player2) >= card2:
            new_player1 = coll.deque(list(player1)[:card1])
            new_player2 = coll.deque(list(player2)[:card2])
            winner = play_recursive_game(new_player1, new_player2)
        else:
            assert card1 != card2
            winner = card1 > card2
        if winner:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)


if __name__ == "__main__":
    main()
