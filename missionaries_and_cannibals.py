"""
Author: G Roques

Solves the missionaries and cannibals problem:

Three missionaries and three cannibals are on one side of a river,
along with a boat that can hold one or two people.

Find a way to get everyone to the other side,
without ever leaving a group of missionaries in one place,
outnumbered by the cannibals in that place.

Represents current state with a list [a, b, c].
This list represents the number of missionaries on the wrong side,
cannibals on the wrong side, and whether the boat is on the wrong side.
Initially all the missionaries, cannibals, and the boat are on the wrong side.
The list representing the initial state is [3, 3, 1]
"""

import operator


def main():
    initial_state = get_initial_state()


def get_initial_state():
    return 3, 3, 1


def add_tuples(a, b):
    return operate_on_tuples(a, b, operator.add)


def subtract_tuples(a, b):
    return operate_on_tuples(a, b, operator.sub)


def operate_on_tuples(a, b, operator_):
    return tuple(map(operator_, a, b))


def is_state_valid(state):
    if contains_negative(state):
        return False
    elif has_more_than_one_boat(state):
        return False
    elif has_more_cannibals_than_missionaries(state):
        return False
    else:
        return True


def contains_negative(list_):
    return any(n < 0 for n in list_)


def has_more_than_one_boat(state):
    return state[2] > 1


def has_more_cannibals_than_missionaries(state):
    return state[1] > state[0]


def get_actions():
    return {
        (1, 0, 1),
        (2, 0, 1),
        (0, 1, 1),
        (0, 2, 1),
        (1, 1, 1)
    }


if __name__ == '__main__':
    main()
