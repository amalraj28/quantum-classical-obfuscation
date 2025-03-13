OPENQASM 3.0;
include "stdgates.inc";
qubit[1] ancilla;
qubit[2] clock;
qubit[1] b;
x b[0];
h clock[0];
h clock[1];
barrier ancilla[0], clock[0], clock[1], b[0];
cu(pi/2, -pi/2, pi/2, 3*pi/4) clock[0], b[0];
cu(pi, pi, 0, 0) clock[1], b[0];
barrier ancilla[0], clock[0], clock[1], b[0];
h clock[1];
cp(-pi/2) clock[1], clock[0];
h clock[0];
swap clock[0], clock[1];
barrier ancilla[0], clock[0], clock[1], b[0];
cry(pi) clock[0], ancilla[0];
cry(pi/3) clock[1], ancilla[0];
barrier ancilla[0], clock[0], clock[1], b[0];
barrier ancilla[0], clock[0], clock[1], b[0];
swap clock[0], clock[1];
h clock[0];
cp(pi/2) clock[1], clock[0];
h clock[1];
barrier ancilla[0], clock[0], clock[1], b[0];
cu(pi, pi, 0, 0) clock[1], b[0];
cu(pi/2, pi/2, -pi/2, -3*pi/4) clock[0], b[0];
barrier ancilla[0], clock[0], clock[1], b[0];
h clock[0];
h clock[1];


// Initial state = [0, 1]