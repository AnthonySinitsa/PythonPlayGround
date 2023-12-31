import random
from collections import Counter

class GameLogic:
  #write a static calculate_score method that 
  #follow these rules:
  #Single fives are worth 50 points
  # Single ones are worth 100 points
  # Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
  # If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 die showing the number 3 would be 600 points and 5 die showing the number 3 would be 1200 points
  # This makes the highest possible score in a single roll 8000 for six ones (1000 for three ones, after that player multiplies the roll by two for each additional one in that series of rolling.)
  # A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight, they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll, that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
  # Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
  # Full house (3 of a kind plus 2 of a kind) are worth 1,500
  
  #q: getting three five's outputs 650 instead of 500
  #a: because it's counting the 5's as 50 each, and then 100 for the three of a kind
  #q: how to fix it
  #a: if the number is 5, and the count is 3, then it should only count 500
  # let's fix it
  @staticmethod
  def calculate_score(dice):
    score = 0
    counts = Counter(dice)

    # Single fives are worth 50 points
    score += counts[5] * 50

    # Single ones are worth 100 points
    score += counts[1] * 100

    # Three of a kind are worth 100 points times the number rolled,
    # except for three ones which are worth 1000 points
    for number in range(2, 7):
        if counts[number] >= 3:
            if number == 1:
                score += 1000
            else:
                score += number * 100

    # Four, five, or six of a kind
    for number in range(1, 7):
        if counts[number] >= 4:
            score += (number * 100) * (2 ** (counts[number] - 4))

    # Straight from 1 to 6 is worth 1500 points
    if set(dice) == set([1, 2, 3, 4, 5, 6]):
        score += 1500

    # Three pairs are worth 1000 points
    if len(counts) == 3 and all(count == 2 for count in counts.values()):
        score += 1000

    # Full house (3 of a kind plus 2 of a kind) is worth 1500 points
    if len(counts) == 2 and set(counts.values()) == {2, 3}:
        score += 1500

    return score
  
  

  @staticmethod
  def roll_dice(number_of_dice):
    if number_of_dice < 1 or number_of_dice > 6:
      raise ValueError("Number of dice must be between 1 and 6.")
    results = tuple(random.randint(1, 6) for _ in range(number_of_dice))
    return results






  # def calculate_score(dice):
  #   score = 0
  #   counts = Counter(dice)

  #   # Single fives are worth 50 points
  #   score += counts[5] * 50

  #   # Single ones are worth 100 points
  #   score += counts[1] * 100

  #   # Three of a kind are worth 100 points times the number rolled,
  #   # except for three ones which are worth 1000 points
  #   for number in range(2, 7):
  #       if counts[number] >= 3:
  #           if number == 1:
  #               score += 1000
  #           else:
  #               score += number * 100

  #   # Four, five, or six of a kind
  #   for number in range(1, 7):
  #       if counts[number] >= 4:
  #           score += (number * 100) * (2 ** (counts[number] - 4))

  #   # Straight from 1 to 6 is worth 1500 points
  #   if set(dice) == set([1, 2, 3, 4, 5, 6]):
  #       score += 1500

  #   # Three pairs are worth 1000 points
  #   if len(counts) == 3 and all(count == 2 for count in counts.values()):
  #       score += 1000

  #   # Full house (3 of a kind plus 2 of a kind) is worth 1500 points
  #   if len(counts) == 2 and set(counts.values()) == {2, 3}:
  #       score += 1500

  #   return score