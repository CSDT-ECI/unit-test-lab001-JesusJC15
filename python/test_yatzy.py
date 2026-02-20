from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

# Chance

def test_chance_scores_sum_of_all_dice():
    assert Yatzy.chance(2, 3, 4, 5, 1) == 15
    assert Yatzy.chance(3, 3, 4, 5, 1) == 16

# Yatzy

def test_yatzy_all_dice_same_scores_50():
    assert Yatzy.yatzy([1, 1, 1, 1, 1]) == 50
    assert Yatzy.yatzy([6, 6, 6, 6, 6]) == 50

def test_yatzy_not_all_same_scores_0():
    assert Yatzy.yatzy([1, 1, 1, 1, 2]) == 0

# Ones to Sixes

def test_ones_counts_only_ones():
    assert Yatzy.ones(1, 2, 1, 4, 5) == 2

def test_twos_counts_only_twos():
    assert Yatzy.twos(2, 3, 2, 5, 2) == 6

def test_threes_counts_only_threes():
    assert Yatzy.threes(3, 3, 3, 4, 5) == 9

def test_fours_counts_only_fours():
    game = Yatzy(4, 4, 4, 5, 6)
    assert game.fours() == 12

def test_fives_counts_only_fives():
    game = Yatzy(5, 5, 5, 5, 1)
    assert game.fives() == 20

def test_sixes_counts_only_sixes():
    game = Yatzy(6, 6, 2, 6, 1)
    assert game.sixes() == 18

# Pair

def test_score_pair_highest_pair():
    assert Yatzy.score_pair(3, 3, 5, 4, 5) == 10

def test_score_pair_returns_highest_even_if_two_pairs():
    assert Yatzy.score_pair(3, 3, 6, 6, 2) == 12

def test_score_pair_no_pair_returns_0():
    assert Yatzy.score_pair(1, 2, 3, 4, 5) == 0

# Two Pairs

def test_two_pair_scores_two_pairs():
    assert Yatzy.two_pair(3, 3, 5, 4, 5) == 16

def test_two_pair_not_two_pairs_returns_0():
    assert Yatzy.two_pair(1, 2, 3, 4, 5) == 0

# Three of a kind

def test_three_of_a_kind_scores_correctly():
    assert Yatzy.three_of_a_kind(3, 3, 3, 4, 5) == 9

def test_three_of_a_kind_four_of_same_still_counts():
    assert Yatzy.three_of_a_kind(2, 2, 2, 2, 5) == 6

def test_three_of_a_kind_none_returns_0():
    assert Yatzy.three_of_a_kind(1, 2, 3, 4, 5) == 0

# Four of a kind

def test_four_of_a_kind_scores_correctly():
    assert Yatzy.four_of_a_kind(2, 2, 2, 2, 5) == 8

def test_four_of_a_kind_five_of_same_counts():
    assert Yatzy.four_of_a_kind(3, 3, 3, 3, 3) == 12

def test_four_of_a_kind_none_returns_0():
    assert Yatzy.four_of_a_kind(1, 2, 3, 4, 5) == 0

# Small Straight

def test_small_straight_scores_15():
    assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15

def test_small_straight_unordered_still_scores():
    assert Yatzy.smallStraight(2, 3, 4, 5, 1) == 15

def test_small_straight_invalid_returns_0():
    assert Yatzy.smallStraight(1, 2, 2, 4, 5) == 0

# Large Straight

def test_large_straight_scores_20():
    assert Yatzy.largeStraight(2, 3, 4, 5, 6) == 20

def test_large_straight_unordered_still_scores():
    assert Yatzy.largeStraight(6, 2, 3, 4, 5) == 20

def test_large_straight_invalid_returns_0():
    assert Yatzy.largeStraight(1, 2, 3, 4, 6) == 0

# Full House

def test_full_house_scores_sum_of_all_dice():
    assert Yatzy.fullHouse(2, 2, 3, 3, 3) == 13

def test_full_house_other_combination():
    assert Yatzy.fullHouse(4, 4, 4, 2, 2) == 16

def test_full_house_not_valid_returns_0():
    assert Yatzy.fullHouse(2, 2, 2, 2, 5) == 0

# CrazyChance

def test_crazy_chance_all_even():
    # 2,4,6,2,2 = 48
    assert Yatzy.crazy_chance(2, 4, 6, 2, 2) == 48

def test_crazy_chance_all_odd():
    # 1,1,3,5,5 = 30
    assert Yatzy.crazy_chance(1, 1, 3, 5, 5) == 30

def test_crazy_chance_mixed_even_and_odd():
    # 2,4,3,5,6 = 52
    assert Yatzy.crazy_chance(2, 4, 3, 5, 6) == 52