"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(qExpress, qNormal, ticket_type, person):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param qExpress: list - names in the Fast-track queue.
    :param qNormal: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    q = [qNormal, qExpress][ticket_type]
    q.append(person)

    return q


def find_my_friend(queue, friend):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    return queue.index(friend)


def add_me_with_my_friends(queue: list, index, person):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person: str - the name to add.
    :return: list - queue updated with new name.
    """

    queue.insert(index, person)
    return queue


def remove_the_mean_person(queue, person):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    queue.pop(queue.index(person))
    return queue


def how_many_namefellows(queue, person):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

    return queue.count(person)


def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    return queue[-1]


def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    return sorted(queue)
