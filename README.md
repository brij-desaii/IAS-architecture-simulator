# IAS-architecture-simulator

============IAS IMPLEMENTATION IN Python LANGUAGUE ============

In the following assignment I aim to emulate the various ISA instuction set, and process using IAS computer.

The registers involved in IAS computer are:
AC  : Accumulator
	Accumulate/hold results of an ALU operation

IR  : Instructions Register
	8 bit opcode of the instruction to be executed
	
IBR : Instructions Buffer register
	Holds the RHS instruction temporarily

MQ  : Multiplier/Quotioent Register
	LSB of product

MBR : Memory BUffer register
	Contains a word to be read/stored in memory or I/O

MAR : Memory Adress register
	Specifies the address in memory of the word to be written/read into MBR

PC  : Program Counter
	Holds the next instruction’s address

Running of Program consisits of two cycles:
i) Fetch cycle:
	 Opcode of the next instruction is loaded into the IR and the address portion is loaded into the MAR. 
	 In this phase the Program Counter(PC) value is moved to the Memory Address Register(MAR) and the value at the memory location MAR is fed into the Memory Buffer Register(MBR).
         Once this is done, the OPCODE of the LEFT instruction is loaded into the Instruction Register(IR)and the address portion is loaded into the MAR and the right instruction is loaded into the Instruction Buffer Register(IBR).

ii) Execute Cycle : Consists of 2 types:
	Decode Cycle:In this phase the data stored in the registers is decoded based on the instruction OPCODE 
                value and the corresponding control signals are sent to move the data around or 
                perform specific tasks. The "binary data" is well read and converted into an assembly
                language for the execute phase.
	
	Execute Cycle: In this phase the ALU performs the tasks as specified by the assembly language for a 
                particular C/C++ program.

Upon running "IMT2021067_ias.py", the user is prompted for choices:
1.Addition of two numbers 
2.Subtraction of two numbers 
3.Sum of numbers in a list 
4.Area of Rectangle 
5.Sum of any Arithematic Progression 
6.Exit

The fetch and execute cycles have been implememted in the "execute()" python function and the memory of the IAS machine is implemented using a python list.
For each choice that the user inputs, the corresponding IAS instructions are stored in memory and the "execute" funtion is called.

=============================
+  IMT2021067 Brij Desai +
=============================
