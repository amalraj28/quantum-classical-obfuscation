OPENQASM 3.0;
include "stdgates.inc";
gate Q _gate_q_0, _gate_q_1 {
  x _gate_q_1;
  cz _gate_q_0, _gate_q_1;
  x _gate_q_1;
  h _gate_q_1;
  h _gate_q_0;
  x _gate_q_0;
  x _gate_q_1;
  h _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_1;
  x _gate_q_0;
  x _gate_q_1;
  h _gate_q_0;
  h _gate_q_1;
}
qubit[2] q;
h q[0];
h q[1];
Q q[0], q[1];


//Solutions = ['01']