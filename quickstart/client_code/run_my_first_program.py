from nada_dsl import *

def nada_main():

    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))

    sum_int = my_int1 + my_int2 + my_int3
    diff_int = my_int1 - my_int2
    prod_int = my_int1 * my_int3

    return [
        Output(sum_int, "sum_output", party1),
        Output(diff_int, "diff_output", party1),
        Output(prod_int, "prod_output", party1)
    ]
