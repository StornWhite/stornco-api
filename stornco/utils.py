# Convenience functions, etc.
def print_object(obj):
    """
    Prints all local field names and values for any object.
    """
    for field in obj._meta.local_fields:
        try:
            value = getattr(obj, field.name)
        except:
            value = None
        print(field.name, value)


# For convenience:
po = print_object


def print_dictionary(dictionary):
    """
    Prints all dictionary keys and values.
    """
    for key, value in dictionary.iteritems():
        print(key, value)


def print_list(some_list):
    """
    Prints all items in a list.
    """
    for value in some_list:
        print(value)


def print_objects(obj_list):
    """
    Prints all local fields names and values for every object in a list.
    """
    for obj in obj_list:
        print_object(obj)
        print('')


# For convenience:
pos = print_objects


def unique_non_null_values(iterable):
    """
    Creates a copy of a given iterable, but with all Nones removed and with
    each element appearing in the list exactly once.

    Order is NOT preserved
    :param iterable: iterable
    :return:
    """
    return list(set(filter(lambda x: x is not None, iterable)))