OPENQASM 3.0;
include "stdgates.inc";
gate Q _gate_q_0, _gate_q_1, _gate_q_2 {
  x _gate_q_0;
  x _gate_q_1;
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_1;
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
  x _gate_q_1;
  h _gate_q_2;
  h _gate_q_1;
  h _gate_q_0;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_2;
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_2;
  h _gate_q_0;
  h _gate_q_1;
  h _gate_q_2;
}
qubit[3] q;
h q[0];
h q[1];
h q[2];
Q q[0], q[1], q[2];


//Solutions = ['100', '101']