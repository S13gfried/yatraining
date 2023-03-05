deck1 = [int(item) for item in input().split()]
deck2 = [int(item) for item in input().split()]

turn = 1
while True:
    draw1 = deck1.pop(0)
    draw2 = deck2.pop(0)

    if (draw1 > draw2 and not (draw1 == 9 and draw2 == 0)) or (draw1 == 0 and draw2 == 9):
        winner = deck1
    else:
        winner = deck2
    winner.extend([draw1, draw2])

    if len(deck2) == 0:
        print("first " + str(turn))
        break
    if len(deck1) == 0:
        print("second " + str(turn))
        break
    if turn == 100000:
        print("botva")
        break

    turn = turn + 1
