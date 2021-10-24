"""A  simple social network for trackong social connections between people"""


class Person:
    """A person in the social network
    
    Attributes:
        name (str): the persons name
        connections (set of Person): other people in the social network 
        who know this person
    """
    