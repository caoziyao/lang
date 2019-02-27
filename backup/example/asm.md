N
当两个有符号整数运算时： N=1表示运算的结果为负数； N=0表示运算的结果为正数或零

Z
Z=1表示运算的结果为零 Z=0表示运算的结果非零 对于CMP指令，Z=1表示进行比较的两个数相等

C
可以有4种方法设置C的值：  1. 在加法指令中(包括CMP指令)，当结果产生了进位,则C=1,表示无符号运算发生上溢出；其他情况C=0 2. 在减法指令中(包括CMP指令)，当运算中发生借位，则C=0，表示无符号运算数发生下溢出；其他情况下C=1  3. 对于包含移位操作的非加减运算指令，C中包含最后一次溢出的位的数值 4.对于其他非加减运算指令，C位的值通常不受影响

V
对于加减运算指令，当操作数和运算结果为二进制的补码表示的带符号数时，V=1表示符号位溢出；通常其他指令不影响V位


BEQ    相等
BNE    不等
BPL    非负
BMI    负
BCC    无进位
BCS    有进位
BLO    小于（无符号数）
BHS    大于等于（无符号数）
BHI    大于（无符号数）
BLS    小于等于（无符号数）
BVC    无溢出（有符号数）
BVS    有溢出（有符号数）
BGT    大于（有符号数）
BGE    大于等于（有符号数）
BLT    小于（有符号数）
BLE    小于等于（有符号数）


| 条件码助记符	    | 标志  |  描述  |
| ------ |-----------| ----- |
| NE      | Z清零                 |  不相等  |
| EQ      | Z置位                 |   相等 |
| LE      | Z清零或（N不等于V）     | 带符号数小于或等于   |
| GE      | N等于V                |  带符号数大于或等于  |
| LT      | N不等于V               | 带符号数小于   |
| GT      | Z清零且（N等于V）     | 带符号数大于   |
| HI      | C置位Z清零          |  无符号数大于  |
| LS      | Z置位C清零          |  无符号数小于或等于  |
| CC(LO)  | C清零             |  无符号数小于  |
| CS(HS)  | C置位             |  无符号数大于或等于  |





