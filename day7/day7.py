def get_hand_type(hand: str) -> int:
	hand_cards = {}
	for card in hand:
		if (not card in hand_cards):
			hand_cards[card] = 0
		hand_cards[card] += 1

	cards_apperance = list(hand_cards.values())
	if (cards_apperance[0] == 5):
		return (0)
	if (4 in cards_apperance):
		return (1)
	if (3 in cards_apperance and 2 in cards_apperance):
		return (2)
	if (3 in cards_apperance):
		return (3)
	if (cards_apperance.count(2) == 2):
		return (4)
	if (2 in cards_apperance):
		return (5)
	if (cards_apperance.count(1) == 5):
		return (6)
	return (7)

def get_jokerhand_type(hand: str) -> float:
	hand_cards = {}
	for card in hand:
		if (not card in hand_cards):
			hand_cards[card] = 0
		hand_cards[card] += 1

	cards_appearance = [hand_cards[c] for c in hand_cards if c != 'J']
	j_appearance = hand_cards['J'] if 'J' in hand_cards else 0
	var = [v for v in cards_appearance if v + j_appearance == 3]
	tests = [
		len(cards_appearance) and cards_appearance[0] == 5, # 0
		any([v for v in cards_appearance if v + j_appearance == 5]) or j_appearance == 5, # 1
		4 in cards_appearance, # 2
		any([v for v in cards_appearance if v + j_appearance == 4]) or j_appearance == 4, # 3
		3 in cards_appearance and 2 in cards_appearance, # 4
		var.count(2) == 2 or (var.count(2) == 1 and j_appearance == 2) or (var.count(2) == 1 and j_appearance == 3), # 5
		3 in cards_appearance, # 6
		any([v for v in cards_appearance if v + j_appearance == 3]) or j_appearance == 3, # 7
		cards_appearance.count(2) == 2, # 8
		False, # 9
		2 in cards_appearance, # 10
		j_appearance == 1, # 11
		cards_appearance.count(1) == 5, # 12
		False, # 13
	]

	for n, test in enumerate(tests):
		if (test):
			return (int(n / 2))
	return (len(tests))

def compare_labels(hand1: str, hand2: str, part: int) -> bool:
	# If neg, hand1 is stronger, else hand2 stronger
	if (part == 1):
		strength = "AKQJT98765432"
	else:
		strength = "AKQT98765432J"
	card_index = 0
	while card_index < 5 and hand1[card_index] == hand2[card_index]:
		card_index += 1
	return (strength.index(hand1[card_index]) < strength.index(hand2[card_index]))

def main(part: int=1):
	with open("day7_input") as f:
		lines = f.read().split('\n')

	ranked_hands = []
	for line in lines:
		hand = {
			'hand': line.split(' ')[0],
			'bid': line.split(' ')[1],
			'type': get_hand_type(line.split(' ')[0]) if part == 1 else get_jokerhand_type(line.split(' ')[0])
		}
		insert_index = 0
		while insert_index < len(ranked_hands):
			if (hand['type'] > ranked_hands[insert_index]['type']):
				break
			elif (hand['type'] == ranked_hands[insert_index]['type'] and compare_labels(ranked_hands[insert_index]['hand'], hand['hand'], part) > 0):
				break
			insert_index += 1
		ranked_hands.insert(insert_index, hand)

	total = 0
	for hand_index, hand in enumerate(ranked_hands):
		total += (hand_index + 1) * int(hand['bid'])
	print(f'result: {total}')

if __name__ == "__main__":
	main(part=2)