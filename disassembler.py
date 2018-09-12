class disassembler(object):
    register_codes = {'00000':'R0 ', '00001':'R1 ', '00010':'R2 ', '00011':'R3 ', '00100':'R4 ',
                      '00101':'R5 ', '00110':'R6 ', '00111':'R7 ', '01000':'R8 ', '01001':'R9 ',
                      '01010':'R10 ', '01011':'R11 ', '01100':'R12 ', '01101':'R13 ', '01110':'R14 ',
                      '01111':'R15 ', '10000':'R16 ', '10001':'R17 ', '10010':'R18 ', '10011':'R19 ',
                      '10100':'R20 ', '10101':'R21 ', '10110':'R22 ', '10111':'R23 ', '11000':'R24 ',
                      '11001':'R25 ', '11010':'R26 ', '11011':'R27 ', '11100':'R28 ', '11101':'R29 ',
                      '11110':'R30 ', '1111':'R31 '}
    binary_array = []
    code_array = []
    register_array = []     #holds the register or immediate value to be printed
    instruction = ""


    def __init__(self):
        return

        #populate binary_array with .txt file
    def load_file(self):
        with open('test2_bin.txt') as my_file:
            for line in my_file:
                self.binary_array.append(line)
                print(line)

    def run(self):
        count = 0
        while(count < 2):#len(self.binary_array)):
            opcode = str(self.binary_array[count])
            decimal_opcode = int(opcode[0:11], 2)   #holds the decimal opcode value
            op_1_format = opcode[0:8] #holds the format for first 1-8 opcode digits
            op_2_format = opcode[8:11] #holds the format the opcode digits 9-11
            reg_1_format = opcode[11:16]  #holds final specified register digits, 5 total
            imm_format = opcode[16:21] #specifies and holds immediate digits, 5 total
            reg_2_format = opcode[21:26] #holds the second specified register destination digits, 5 total
            reg_3_format = opcode[26:32]  #holds final 6 digits

            if(decimal_opcode>= 160 and decimal_opcode <=191):
                print('B')

            elif(decimal_opcode == 1104):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + "96\t" + "AND\t" + self.register_codes[rd]
                                   + self.register_codes[rn] + self.register_codes[rm])

                print(self.instruction)


            elif(decimal_opcode == 1112):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + "96\t" + "ADD\t" + self.register_codes[rd]
                                   + self.register_codes[rn] + self.register_codes[rm])

                print(self.instruction)


            elif(decimal_opcode == 1160 or decimal_opcode == 1161):
                print('ADDI')

            elif(decimal_opcode == 1360):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]
                print('ORR')

            elif(decimal_opcode >= 1440 and decimal_opcode <= 1447):
                print('CBZ')

            elif(decimal_opcode >= 1448 and decimal_opcode <= 1455):
                print('CBNZ')

            elif(decimal_opcode == 1624):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                print('SUB')

            elif(decimal_opcode == 1672 or decimal_opcode == 1673):
                print('SUBI')

            elif(decimal_opcode >= 1648 and decimal_opcode <= 1687):
                print('MOVZ')

            elif(decimal_opcode >= 1940 and decimal_opcode <= 1943):
                print('MOVK')

            elif(decimal_opcode == 1690):
                print('LSR')

            elif(decimal_opcode == 1691):
                print('LSL')

            elif(decimal_opcode == 1984):
                print('STUR')

            elif(decimal_opcode == 1986):
                print('LDUR')

            elif(decimal_opcode == 2038):
                print('BREAK')

            else:
                opcode = int(opcode, 2) - 2**32
                print(opcode)

            count += 1









d = disassembler()
d.load_file()
d.run()
