一些基本概念
最高有效位(Most Significant Bit)：一个二进制数x<y,且x是2的整数次密，此时x只有最高位是1,其他位置都是0,这时说x是y的最高有效位(MLB)。
应用:见`338-2.py`
最低有效位(Last（Least） Significant Bit):二进制中最低位，及第0位，权值为2^0
应用：见`338-3.py`
注意：and/or/xor运算优先级在+-*/之后。

python中定义时以0b开头，如：
n=0b11
十进制表示：
n=3
常用函数:
`bin(x).count('1')`返回数字x中=1的数位 的数量
`int.bit_count(x)`返回整数x以二进制表示时，x中1的个数。
`int.bit_length()`返回整数以二进制表示时二进制的位的各数。
移位操作：
`<<`左移运算符，二进制数会越来越大，相当于*2
`>>`右移运算符，二进制数会越来越小,相当于/2
`1<<(i+1)-1`构造有i个位且每一位值为1的二进制掩码
抑或操作:xor(^)
1^1=0
0^0=0
0^1=1
若A和B为两个任意整数：
0^a=a
a^a=0
如果A==B:
A^B=0
如果A!=B:
A^B!=0
抑或运算的运算规律：
1. 交换律:A^B=B^A
2. 结合律:A^(B^C)=(A^B)^C
3. 恒等律：A^0=A
4. 归零律：A^A=0
5. 自反：A^B^B=A^0=A
6. 对于任意i∈Z(整数集合),有:
`4*i ^ (4*i+1) ^ (4*i+2) ^ (4*i+3)=0`
应用：见`1486-2.py`

对于任意的A:
A^(A-1)=A
如果 A ^ B = C 成立，那么 A ^ B = C，B ^ C = A；
python中的相关函数：

与操作(&)
1&1=1
1&0=0
0&0=0
特别的
性质1：n&(n-1)  消掉一个二进制数字中最低位的1
运用：题目`191`,`231`
性质2：n&(-n) 获得整数n最低位的1 比如n=6,结果为2，n=3,结果为1
性质3：n&1=0 n为偶数
n&1=1 n为奇数
性质4：多个数字进行与运算，总是越与，结果越小。应用:题目#2419,#2871
性质5：任何数和-1进行与运算都等于那个数字本身:n&-1=n

一些应用：
1. `n & (1<<k)`用来判断数字n的二进制表示中第k(最低位是第0位)位是0还是1,结果>0说明第k位是1，否则为0
例如:`3&(1<<1)=(11)_2&(10)_2=1`说明3的第1位是1；
`5&(1<<1)=(101)_2&(10)_2=0`说明5的第1位是0.
2. `(n>>k)&1`得到n二进制表示中的第k位(最低位为第0位)，如果n的二进制表示的位数小于k,那么结果为0.
例如:`(3>>1)&1=1&1=1`说明3的二进制表示中第1位是1
`(5>>1)&1=(10)_2&1=0`说明5的第1位为0.


二进制的负数表示

用一个例子说明
3的二进制表示为:0000 0000 0000 0011
-3的二进制表示为3的二进制取反后+1,先取反得到：
1111 1111 1111 1100
取反的基础上+1就是-3了，所以结果是:
1111 1111 1111 1101
