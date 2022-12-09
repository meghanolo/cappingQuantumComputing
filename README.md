# Quantum Computing Capstone Fall 2022

The files in the GitHub were used both on the [IBM Quantum Experience](https://quantum-computing.ibm.com/) and in a virtual environment on a Mac. The following instructions will get you started running the code.

### Brute Force

The first algorithm to run is Brute Force, using the [Brute_QAOA](https://github.com/meghanolo/cappingQuantumComputing/blob/main/Brute_QAOA.ipynb) file. Clone this repository, then create an account on IBM Quantum. Launch the Lab after signing in, and uplaod the Brute_QAOA.ipynb file to the platform. In the third cell, edit *n* to reflect the number of nodes in your graph, *x* to reflect the weight of the malicious traffic, and insert your *elist*. Then, run the first three blocks of code.

### QAOA

Following Brute Force, you can run the QAOA algorithm using the same file. Just run the final code cell in the file.

**Note: ** Brute Force MUST be run before QAOA to ensure all parameters are update. Additionally, QAOA will take time, so wait patiently.

### VQE

Setting up VQE is similar to Brute Force. Clone this repository, then create an account on IBM Quantum. Launch the Lab after signing in, and uplaod the [VQE.ipynb](https://github.com/meghanolo/cappingQuantumComputing/blob/main/VQE.ipynb) file to the platform. In the first cell, edit *n* to reflect the number of nodes in your graph, *x* to reflect the weight of the malicious traffic, and insert your *elist*. Then, run the code block.

### QRAO
