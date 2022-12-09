# Quantum Computing Capstone Fall 2022

The files in the GitHub were used both on the [IBM Quantum Experience](https://quantum-computing.ibm.com/) and in a virtual environment on a Mac. The following instructions will get you started running the code.

### Brute Force

The first algorithm to run is Brute Force, using the [Brute_QAOA](https://github.com/meghanolo/cappingQuantumComputing/blob/main/Brute_QAOA.ipynb) file. Clone this repository, then create an account on IBM Quantum. Launch the Lab after signing in, and uplaod the Brute_QAOA.ipynb file to the platform. In the third cell, edit *n* to reflect the number of nodes in your graph, *x* to reflect the weight of the malicious traffic, and insert your *elist*. Then, run the first three blocks of code.

### QAOA

Following Brute Force, you can run the QAOA algorithm using the same file. Just run the final code cell in the file.

**Note:** Brute Force MUST be run before QAOA to ensure all parameters are update. Additionally, QAOA will take time, so wait patiently.

### VQE

Setting up VQE is similar to Brute Force. Clone this repository, then create an account on IBM Quantum. Launch the Lab after signing in, and uplaod the [VQE.ipynb](https://github.com/meghanolo/cappingQuantumComputing/blob/main/VQE.ipynb) file to the platform. In the first cell, edit *n* to reflect the number of nodes in your graph, *x* to reflect the weight of the malicious traffic, and insert your *elist*. Then, run all of the code blocks. The first output will be a similar brute force approach and is NOT the results of VQE. The desired results will be returned in the second cell's output.

### QRAO

The code for QRAO was based heavily on a [prototype](https://github.com/qiskit-community/prototype-qrao) from IBM. The easiest way to access the code is to follow the [Installation Guide](https://github.com/qiskit-community/prototype-qrao/blob/main/INSTALL.md) in the Qiskit GitHub. However, the utils.py file in the qrao directory must be changed to reflect this [file](https://github.com/meghanolo/cappingQuantumComputing/blob/main/qrao/utils.py) in our GitHub, and the algorithm to complete the encoding is found in our [QApplicationsQRAO.ipynb](https://github.com/meghanolo/cappingQuantumComputing/blob/main/QApplicationsQRAO.ipynb) file. To make these changes, follow the installation guide to create a virtual environment on your system. Then, overwrite the existing utils.py file with the one found in this repository. Next, copy the QApplicationsQRAO.ipynb file into the directory that contains the virtual environment. Follwo the commands to start your venv based on your operating system. Once these parameters are set, change the utils.py file to reflect the data you want to analyze by altering *n* to reflect the number of nodes in your graph, *x* to reflect the weight of the malicious traffic, and your *elist*. Save this file and restart the Kernel in your venv. Finally, run all code cells in the QApplicationsQRAO.ipynb file.

*Questions on any installation can be sent to meghan.oloughlin1@marist.edu*
