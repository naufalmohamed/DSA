'''
Max Coins from Non-Adjacent Trees

This problem finds the maximum coins you can collect from trees in a forest row, where adjacent trees cannot both be harvested due to shared root systems.
​

Problem Statement
Given an array trees of positive integers representing coin values (e.g., ), return the maximum coins without harvesting two adjacent trees.

Input 1: [6, 1, 3, 8]
Output: 14

'''

def coinTree(trees):
    # Create variables for the prev trees
    oneTreeBefore, twoTreeBefore = 0, 0

    # Create variable for maxCoin stored
    maxCoin = 0

    # start a for loop through trees
    for coin in trees:
        # maxCoin based on prev values
        maxCoin = max(coin+twoTreeBefore, oneTreeBefore)
        # adjusting variables for next iteration

        twoTreeBefore = oneTreeBefore
        oneTreeBefore = maxCoin

    # return result
    return maxCoin


print(coinTree([6, 1, 3, 8]))
