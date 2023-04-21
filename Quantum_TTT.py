from qiskit import *

player_X='X'
player_O='O'
classical_bits=[]
quantum_player=[]
controls=[]
targets=[]

qc=QuantumCircuit(9,9)
qc.h(range(9))

def classical_move(bit):
    global classical_bits
    qc.measure(bit,bit)
    simulator=Aer.get_backend('qasm_simulator')
    result=execute(qc,simulator,shots=1).result()
    counts=result.get_counts()
    for i in counts.keys():
        keyy=i
        key_list=list(keyy)
    key_list.reverse()
    if bit not in classical_bits:             
        if key_list[bit] == '1':
            qc.reset(bit)
            qc.x(bit)
            qc.measure(bit,bit)
        else:
            qc.reset(bit)
            qc.measure(bit,bit)
        if bit in controls:
            quantum_operation(bit)
        classical_bits.append(bit)

    else:
        return 0
    return key_list

def quantum_operation(bit):
    j=controls.index(bit)

    if quantum_player[j]==player_O:
        qc.x(controls[j])
        qc.cx(controls[j],targets[j])
        qc.x(controls[j])
        qc.measure(targets[j],targets[j])

    elif quantum_player[j]==player_X:
        qc.cx(controls[j],targets[j])
        qc.measure(targets[j],targets[j])

def quantum_move(tbit,cbit,player):
    global classical_bits
    global controls,targets
    if tbit in classical_bits and cbit not in classical_bits:
        controls.append(cbit)
        targets.append(tbit)
        quantum_player.append(player)
    else:
        return 0

def mark(key_list):
    global classical_bits
    simulator=Aer.get_backend('qasm_simulator')
    result=execute(qc,simulator,shots=1).result()
    counts=result.get_counts()

    for i in counts.keys():
        keyy=i
    key_list=list(keyy)
    key_list.reverse()
    main_list=[]
    for i in range(len(classical_bits)):
        if key_list[classical_bits[i]] == '1':
            main_list.append([classical_bits[i],player_X])
        elif key_list[classical_bits[i]] == '0':
            main_list.append([classical_bits[i],player_O])
    return main_list
