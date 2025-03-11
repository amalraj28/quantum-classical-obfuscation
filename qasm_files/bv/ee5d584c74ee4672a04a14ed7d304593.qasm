OPENQASM 2.0;
include "qelib1.inc";
qreg q[8];
qreg a[1];
creg c[8];
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
h a[0];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],a[0];
z a[0];
cx q[1],a[0];
cx q[3],a[0];
cx q[5],a[0];
cx q[7],a[0];
barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],a[0];
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];


//Solutions = ['10101010']