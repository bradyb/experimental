import numpy as np
from sympy import Matrix, Symbol, exp, I
from sympy.physics.quantum import TensorProduct
CNOT = Matrix([[1, 0, 0, 0],
               [0, 1, 0, 0], 
               [0, 0, 0, 1],
               [0, 0, 1, 0]])

ID = Matrix([[1, 0],
             [0, 1]])

def main():
    id_3_cnot = TensorProduct(CNOT, ID)
    id_1_cnot = TensorProduct(ID, CNOT)
    first_control = id_3_cnot * id_1_cnot
    second_control = id_3_cnot * id_1_cnot * id_3_cnot
    third_control = id_1_cnot * id_3_cnot
    fourth_control = id_1_cnot

    symbols = []
    for index in range(0, 7):
        symbols.append(Symbol(chr(ord('a') + index)))
    
    phase_gates = []
    for index in range(0,7):
        phase_gates.append(Matrix([[1, 0],
                                   [0, exp(I*symbols[index])]]))
    
    first_op = TensorProduct(phase_gates[0], TensorProduct(phase_gates[1], phase_gates[2]))
    second_op = TensorProduct(ID, TensorProduct(phase_gates[3], phase_gates[4]))
    third_op = TensorProduct(ID, TensorProduct(ID, phase_gates[5]))
    fourth_op = TensorProduct(ID, TensorProduct(ID, phase_gates[6]))

    circuit = first_op * first_control * second_op * second_control * third_op * third_control * fourth_op * fourth_control
    print(circuit)

    target_matrix = Matrix([[0,0,1,0,1,1,1],
                            [0,1,0,1,1,0,1],
                            [0,1,1,1,0,1,0],
                            [1,0,0,1,1,1,0],
                            [1,0,1,1,0,0,1],
                            [1,1,0,0,0,1,1],
                            [1,1,1,0,1,0,0]])
    print(target_matrix.rank())
                
if __name__ == "__main__":
    main()
