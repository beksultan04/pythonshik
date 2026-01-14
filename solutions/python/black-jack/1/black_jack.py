def value_of_card(card):
    """Определить ценность карты."""
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Определить, какая карта старше."""
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    elif v2 > v1:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Посчитать, выгоднее ли туз как 11 или как 1."""
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    # Если один из двух уже туз — возвращаем 1
    if card_one == 'A' or card_two == 'A':
        return 1

    # Если сумма <= 10, туз = 11 (иначе перебор)
    if v1 + v2 <= 10:
        return 11
    return 1



def is_blackjack(card_one, card_two):
    """Определить, является ли комбинация блэкджеком (21 с двух карт)."""
    values = {card_one, card_two}
    return ('A' in values) and (
        card_one in ['10', 'J', 'Q', 'K'] or card_two in ['10', 'J', 'Q', 'K']
    )


def can_split_pairs(card_one, card_two):
    """Можно ли разделить карты на пары."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Можно ли сделать double down (сумма 9, 10 или 11)."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
