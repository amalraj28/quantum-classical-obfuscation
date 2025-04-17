OPENQASM 3.0;
include "stdgates.inc";
gate mcx_vchain _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8 {
  ccx _gate_q_4, _gate_q_8, _gate_q_5;
  h _gate_q_8;
  t _gate_q_8;
  cx _gate_q_3, _gate_q_8;
  tdg _gate_q_8;
  cx _gate_q_7, _gate_q_8;
  h _gate_q_7;
  t _gate_q_7;
  cx _gate_q_2, _gate_q_7;
  tdg _gate_q_7;
  cx _gate_q_6, _gate_q_7;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_0, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_1, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_0, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  cx _gate_q_6, _gate_q_7;
  t _gate_q_7;
  cx _gate_q_2, _gate_q_7;
  tdg _gate_q_7;
  h _gate_q_7;
  cx _gate_q_7, _gate_q_8;
  t _gate_q_8;
  cx _gate_q_3, _gate_q_8;
  tdg _gate_q_8;
  h _gate_q_8;
  ccx _gate_q_4, _gate_q_8, _gate_q_5;
  h _gate_q_8;
  t _gate_q_8;
  cx _gate_q_3, _gate_q_8;
  tdg _gate_q_8;
  cx _gate_q_7, _gate_q_8;
  h _gate_q_7;
  t _gate_q_7;
  cx _gate_q_2, _gate_q_7;
  tdg _gate_q_7;
  cx _gate_q_6, _gate_q_7;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_0, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_1, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_0, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  cx _gate_q_6, _gate_q_7;
  t _gate_q_7;
  cx _gate_q_2, _gate_q_7;
  tdg _gate_q_7;
  h _gate_q_7;
  cx _gate_q_7, _gate_q_8;
  t _gate_q_8;
  cx _gate_q_3, _gate_q_8;
  tdg _gate_q_8;
  h _gate_q_8;
}
gate unitary _gate_q_0 {
  U(0, -pi/8, -pi/8) _gate_q_0;
}
gate mcx_vchain_0 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_1 _gate_q_0 {
  U(0, -7*pi/8, 9*pi/8) _gate_q_0;
}
gate mcx_vchain_2 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_3 _gate_q_0 {
  U(0, -7*pi/8, 9*pi/8) _gate_q_0;
}
gate mcx_vchain_4 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_5 _gate_q_0 {
  U(0, -pi/16, -pi/16) _gate_q_0;
}
gate mcx_vchain_6 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_7 _gate_q_0 {
  U(0, -15*pi/16, 3.3379421944391554) _gate_q_0;
}
gate mcx_vchain_8 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_9 _gate_q_0 {
  U(0, -pi/16, -pi/16) _gate_q_0;
}
gate mcx_vchain_10 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_11 _gate_q_0 {
  U(0, -15*pi/16, 3.3379421944391554) _gate_q_0;
}
gate mcx_vchain_12 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_13 _gate_q_0 {
  U(0, -pi/32, -pi/32) _gate_q_0;
}
gate mcx_vchain_14 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_15 _gate_q_0 {
  U(0, -3.043417883165112, 3.2397674240144743) _gate_q_0;
}
gate mcx_vchain_16 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6 {
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
  ccx _gate_q_3, _gate_q_6, _gate_q_4;
  h _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  cx _gate_q_5, _gate_q_6;
  h _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  cx _gate_q_1, _gate_q_5;
  t _gate_q_5;
  cx _gate_q_0, _gate_q_5;
  tdg _gate_q_5;
  h _gate_q_5;
  cx _gate_q_5, _gate_q_6;
  t _gate_q_6;
  cx _gate_q_2, _gate_q_6;
  tdg _gate_q_6;
  h _gate_q_6;
}
gate unitary_17 _gate_q_0 {
  U(0, -pi/32, -pi/32) _gate_q_0;
}
gate mcx_vchain_18 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_19 _gate_q_0 {
  U(0, -3.043417883165112, 3.2397674240144743) _gate_q_0;
}
gate mcx_vchain_20 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_21 _gate_q_0 {
  U(0, -pi/64, -pi/64) _gate_q_0;
}
gate mcx_vchain_22 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_23 _gate_q_0 {
  U(0, -3.0925052683774528, 3.1906800388021335) _gate_q_0;
}
gate mcx_vchain_24 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_25 _gate_q_0 {
  U(0, -pi/64, -pi/64) _gate_q_0;
}
gate mcx_vchain_26 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_27 _gate_q_0 {
  U(0, -3.0925052683774528, 3.1906800388021335) _gate_q_0;
}
gate mcx_vchain_28 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_29 _gate_q_0 {
  U(0, -pi/128, -pi/128) _gate_q_0;
}
gate unitary_30 _gate_q_0 {
  U(0, -3.117048960983623, 3.1661363461959633) _gate_q_0;
}
gate mcx_vchain_31 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4 {
  h _gate_q_3;
  p(pi/8) _gate_q_0;
  p(pi/8) _gate_q_1;
  p(pi/8) _gate_q_2;
  p(pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_1;
  p(-pi/8) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  p(pi/8) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  p(-pi/8) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  p(pi/8) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  p(-pi/8) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  h _gate_q_3;
}
gate unitary_32 _gate_q_0 {
  U(0, -pi/128, -pi/128) _gate_q_0;
}
gate unitary_33 _gate_q_0 {
  U(0, -3.117048960983623, 3.1661363461959633) _gate_q_0;
}
gate unitary_34 _gate_q_0 {
  U(0, -pi/256, -pi/256) _gate_q_0;
}
gate unitary_35 _gate_q_0 {
  U(0, -3.129320807286708, 3.153864499892878) _gate_q_0;
}
gate unitary_36 _gate_q_0 {
  U(0, -pi/256, -pi/256) _gate_q_0;
}
gate unitary_37 _gate_q_0 {
  U(0, -3.129320807286708, 3.153864499892878) _gate_q_0;
}
gate unitary_38 _gate_q_0 {
  U(0, -pi/512, -pi/512) _gate_q_0;
}
gate unitary_39 _gate_q_0 {
  U(0, -3.1354567304382504, 3.147728576741336) _gate_q_0;
}
gate unitary_40 _gate_q_0 {
  U(0, -pi/512, -pi/512) _gate_q_0;
}
gate unitary_41 _gate_q_0 {
  U(0, -3.1354567304382504, 3.147728576741336) _gate_q_0;
}
gate unitary_42 _gate_q_0 {
  U(0, -pi/1024, -pi/1024) _gate_q_0;
}
gate unitary_43 _gate_q_0 {
  U(0, -3.138524692014022, 3.1446606151655643) _gate_q_0;
}
gate unitary_44 _gate_q_0 {
  U(0, -pi/1024, -pi/1024) _gate_q_0;
}
gate unitary_45 _gate_q_0 {
  U(0, -3.138524692014022, 3.1446606151655643) _gate_q_0;
}
gate mcphase(_gate_p_0) _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9 {
  mcx_vchain _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_9, _gate_q_5, _gate_q_6, _gate_q_7;
  unitary _gate_q_9;
  mcx_vchain_0 _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9, _gate_q_3, _gate_q_4;
  unitary_1 _gate_q_9;
  mcx_vchain _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_9, _gate_q_5, _gate_q_6, _gate_q_7;
  unitary _gate_q_9;
  mcx_vchain_2 _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9, _gate_q_3, _gate_q_4;
  unitary_3 _gate_q_9;
  mcx_vchain_4 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_8, _gate_q_4, _gate_q_5;
  unitary_5 _gate_q_8;
  mcx_vchain_6 _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_2, _gate_q_3;
  unitary_7 _gate_q_8;
  mcx_vchain_8 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_8, _gate_q_4, _gate_q_5;
  unitary_9 _gate_q_8;
  mcx_vchain_10 _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_2, _gate_q_3;
  unitary_11 _gate_q_8;
  mcx_vchain_12 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_7, _gate_q_4, _gate_q_5;
  unitary_13 _gate_q_7;
  mcx_vchain_14 _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_3;
  unitary_15 _gate_q_7;
  mcx_vchain_16 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_7, _gate_q_4, _gate_q_5;
  unitary_17 _gate_q_7;
  mcx_vchain_18 _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_3;
  unitary_19 _gate_q_7;
  mcx_vchain_20 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_6, _gate_q_3;
  unitary_21 _gate_q_6;
  mcx_vchain_22 _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_2;
  unitary_23 _gate_q_6;
  mcx_vchain_24 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_6, _gate_q_3;
  unitary_25 _gate_q_6;
  mcx_vchain_26 _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_2;
  unitary_27 _gate_q_6;
  mcx_vchain_28 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_5, _gate_q_3;
  unitary_29 _gate_q_5;
  ccx _gate_q_3, _gate_q_4, _gate_q_5;
  unitary_30 _gate_q_5;
  mcx_vchain_31 _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_5, _gate_q_3;
  unitary_32 _gate_q_5;
  ccx _gate_q_3, _gate_q_4, _gate_q_5;
  unitary_33 _gate_q_5;
  ccx _gate_q_0, _gate_q_1, _gate_q_4;
  unitary_34 _gate_q_4;
  ccx _gate_q_2, _gate_q_3, _gate_q_4;
  unitary_35 _gate_q_4;
  ccx _gate_q_0, _gate_q_1, _gate_q_4;
  unitary_36 _gate_q_4;
  ccx _gate_q_2, _gate_q_3, _gate_q_4;
  unitary_37 _gate_q_4;
  ccx _gate_q_0, _gate_q_1, _gate_q_3;
  unitary_38 _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  unitary_39 _gate_q_3;
  ccx _gate_q_0, _gate_q_1, _gate_q_3;
  unitary_40 _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  unitary_41 _gate_q_3;
  cx _gate_q_0, _gate_q_2;
  unitary_42 _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  unitary_43 _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  unitary_44 _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  unitary_45 _gate_q_2;
  crz(pi/256) _gate_q_0, _gate_q_1;
  p(pi/512) _gate_q_0;
}
gate mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9 {
  h _gate_q_9;
  mcphase(pi) _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
}
gate Q _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9 {
  x _gate_q_1;
  x _gate_q_4;
  x _gate_q_5;
  x _gate_q_8;
  h _gate_q_9;
  mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
  x _gate_q_1;
  x _gate_q_4;
  x _gate_q_5;
  x _gate_q_8;
  x _gate_q_1;
  x _gate_q_2;
  x _gate_q_3;
  x _gate_q_4;
  x _gate_q_6;
  x _gate_q_8;
  h _gate_q_9;
  mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
  x _gate_q_1;
  x _gate_q_2;
  x _gate_q_3;
  x _gate_q_4;
  x _gate_q_6;
  x _gate_q_8;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_4;
  x _gate_q_8;
  h _gate_q_9;
  mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_4;
  x _gate_q_8;
  x _gate_q_3;
  x _gate_q_4;
  x _gate_q_6;
  x _gate_q_8;
  h _gate_q_9;
  mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
  x _gate_q_3;
  x _gate_q_4;
  x _gate_q_6;
  x _gate_q_8;
  x _gate_q_0;
  x _gate_q_4;
  x _gate_q_5;
  x _gate_q_6;
  x _gate_q_7;
  x _gate_q_9;
  h _gate_q_9;
  mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
  x _gate_q_0;
  x _gate_q_4;
  x _gate_q_5;
  x _gate_q_6;
  x _gate_q_7;
  x _gate_q_9;
  h _gate_q_9;
  h _gate_q_8;
  h _gate_q_7;
  h _gate_q_6;
  h _gate_q_5;
  h _gate_q_4;
  h _gate_q_3;
  h _gate_q_2;
  h _gate_q_1;
  h _gate_q_0;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_2;
  x _gate_q_3;
  x _gate_q_4;
  x _gate_q_5;
  x _gate_q_6;
  x _gate_q_7;
  x _gate_q_8;
  x _gate_q_9;
  h _gate_q_9;
  mcx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3, _gate_q_4, _gate_q_5, _gate_q_6, _gate_q_7, _gate_q_8, _gate_q_9;
  h _gate_q_9;
  x _gate_q_0;
  x _gate_q_1;
  x _gate_q_2;
  x _gate_q_3;
  x _gate_q_4;
  x _gate_q_5;
  x _gate_q_6;
  x _gate_q_7;
  x _gate_q_8;
  x _gate_q_9;
  h _gate_q_0;
  h _gate_q_1;
  h _gate_q_2;
  h _gate_q_3;
  h _gate_q_4;
  h _gate_q_5;
  h _gate_q_6;
  h _gate_q_7;
  h _gate_q_8;
  h _gate_q_9;
}
qubit[10] q;
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
h q[8];
h q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];
Q q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9];


//Solutions = ['1011001101', '1010100001', '1011101100', '1010100111', '0100001110']