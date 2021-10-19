# Finding the ground state energy of Lithium Hydride molecule

## Overview
In this project we will be simulating the ground state energy of a lithium hydride molecule using the VQE(Variational Quantum Eigensolver) Algorithm. This algorithm basically prepares a quantum state and then passes the state's function back and forth between a classical and quantum computer. This will finally return the set of parameters, which can be used to calculate the ground state of lithium hydride.

## About the VQE Algorithm
The algorithm begins with the preparation of a quantum state with a parameterized quantum circuit, also called an ansatz. The introduced parameters correspond to rotations of the qubits, and depending on the set of parameters used, a different wavefunction is generated. A back-and-forth between this quantum circuit and a classical optimizer attempts to optimize this output wavefunction via variation of the corresponding quantum circuit parameters, such that the expected value of the Hamiltonian is at its minimum. This heuristic way, when fully converged, will generate the set of parameters that correspond to the ground state of the molecular system. The IBM team has used the VQE algorithm to create dissociation curves — plots of how the ground state energy varies with the distance between atoms in the molecule — that get close to the exact calculated values for both lithium hydride and beryllium hydride.

## Mathematics behind the Algorithm
For a given hermitian matrix H, the expectation value of the observable H on an arbitrary quantum state is given by
⟨H⟩ψ = |ψ⟩H|ψ⟩

### Variational Principle
For a given hermitian matrix H, its expectation value ⟨H⟩ψ must always be greater than or equal to the lowest possible eigenvalue.
λmin≤⟨H⟩ψ = ⟨ψ|H|ψ⟩

### Bounding the Ground State 
When the Hamiltonian of a system is described by the Hermitian matrix H, the ground state energy of that system, Egs, is the smallest eigenvalue associated with H. By arbitrarily selecting a wave function |ψ⟩|ψ⟩ (called an ansatz) as an initial guess approximating |ψmin⟩, calculating its expectation value, ⟨H⟩ψ⟨H⟩ψ, and iteratively updating the wave function, arbitrarily tight bounds on the ground state energy of a Hamiltonian may be obtained.




