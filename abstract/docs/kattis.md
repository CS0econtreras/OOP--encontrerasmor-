Module kattis
=============

Classes
-------

`Kattis(data_source: Any = sys.stdin)`
:   Solution ABC class for Kattis problems
    
    Constructor
    :param data_source: input data source object
    :return: None

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * main.Main

    ### Instance variables

    `answer: Any`
    :   Returns the answer
        :return: answer

    `data: Any`
    :   Returns the data
        :return: data

    ### Methods

    `print_answer(self) ‑> None`
    :   Prints the answer
        :return: None

    `read_input(self) ‑> None`
    :   Reads the data from the given source
        :return: None

    `solve(self) ‑> None`
    :   Solves the problem
        :return: None