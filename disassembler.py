class disassembler(object):
    register_codes = {'00000':'R0', '00001':'R1', '00010':'R2', '00011':'R3', '00100':'R4',
                      '00101':'R5', '00110':'R6', '00111':'R7', '01000':'R8', '01001':'R9 ',
                      '01010':'R10', '01011':'R11', '01100':'R12', '01101':'R13', '01110':'R14',
                      '01111':'R15', '10000':'R16', '10001':'R17', '10010':'R18', '10011':'R19',
                      '10100':'R20', '10101':'R21', '10110':'R22', '10111':'R23', '11000':'R24',
                      '11001':'R25', '11010':'R26', '11011':'R27', '11100':'R28', '11101':'R29',
                      '11110':'R30', '11111':'R31'}
    binary_array = []    #holds each line of machine code in separate index's - ex) line 1 = binary_array[0]
    register_array = []     #holds the register or immediate value to be printed
    instruction = ""     #output instruction that is printed to console
    mem = '96'          #Starting memory location


    def __init__(self):
        return

        #populate binary_array with .txt file
    def load_file(self):
        with open('test2_bin.txt') as my_file:
            for line in my_file:
                self.binary_array.append(line)
                print(line)

    # brains of the disassembler, breaks machine code into proper format to be processed
    def run(self):
        count = 0
        while(count < len(self.binary_array)):
            opcode = str(self.binary_array[count])
            decimal_opcode = int(opcode[0:11], 2)   #holds the decimal opcode value
            op_1_format = opcode[0:8] #holds the format for first 1-8 opcode digits
            op_2_format = opcode[8:11] #holds the format the opcode digits 9-11
            reg_1_format = opcode[11:16]  #holds final specified register digits, 5 total
            imm_format = opcode[16:21] #specifies and holds immediate digits, 5 total
            reg_2_format = opcode[21:26] #holds the second specified register destination digits, 5 total
            reg_3_format = opcode[26:32]  #holds final 6 digits

            if(decimal_opcode>= 160 and decimal_opcode <=191):
                address = str(int(opcode[12:32], 2))

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "B\t" + '#' + address)

                print(self.instruction)

                #AND Opcode
            elif(decimal_opcode == 1104):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "AND\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', ' + self.register_codes[rm])

                print(self.instruction)

                #ADD
            elif(decimal_opcode == 1112):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "ADD\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', ' + self.register_codes[rm])

                print(self.instruction)

                #ADDI
            elif(decimal_opcode == 1160 or decimal_opcode == 1161):
                address = str(int(opcode[10:22], 2))
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "ADDI\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', ' + '#' + address)

                print(self.instruction)

                #ORR
            elif(decimal_opcode == 1360):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "ORR\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', ' + self.register_codes[rm])

                print(self.instruction)

                #CBZ
            elif(decimal_opcode >= 1440 and decimal_opcode <= 1447):
                address = str(int(opcode[8:27]))
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "CBZ\t" + self.register_codes[rd] + ', #'
                                   + address)

                print(self.instruction)

                #CBNZ
            elif(decimal_opcode >= 1448 and decimal_opcode <= 1455):
                address = str(int(opcode[8:27]))
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "CBNZ\t" + self.register_codes[rd] + ', #'
                                   + address)

                print(self.instruction)

                #SUB
            elif(decimal_opcode == 1624):
                rm = reg_1_format
                shamt = opcode[16:22]
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "SUB\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', ' + self.register_codes[rm])

                print(self.instruction)

                #SUBI
            elif(decimal_opcode == 1672 or decimal_opcode == 1673):
                address = str(int(opcode[10:22], 2))
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "SUBI\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', ' + '#' + address)

                print(self.instruction)

                #MOVZ
            elif(decimal_opcode >= 1648 and decimal_opcode <= 1687):
                shamt = str(int(opcode[9:11], 2))
                address = str(int(opcode[11:27], 2))
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "MOVZ\t" + self.register_codes[rd] + ', '
                                   + address + ', LSL ' + shamt)

                print(self.instruction)

                #MOVK
            elif(decimal_opcode >= 1940 and decimal_opcode <= 1943):
                shamt = str(int(opcode[9:11], 2))
                address = str(int(opcode[11:27], 2))
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "MOVK\t" + self.register_codes[rd] + ', '
                                   + address + ', LSL ' + shamt)

                print(self.instruction)

                #LSR
            elif(decimal_opcode == 1690):
                rm = reg_1_format
                shamt = str(int(opcode[16:22], 2))
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "LSR\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', #' + shamt)

                print(self.instruction)

                #LSL
            elif(decimal_opcode == 1691):
                rm = reg_1_format
                shamt = str(int(opcode[16:22], 2))
                rn = opcode[22:27]
                rd = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "LSL\t" + self.register_codes[rd] + ', '
                                   + self.register_codes[rn] + ', #' + shamt)

                print(self.instruction)

                #STUR
            elif(decimal_opcode == 1984):
                address = str(int(opcode[11:20], 2))
                rn = opcode[22:27]
                rt = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "STUR\t" + self.register_codes[rt] + ', ['
                                   + self.register_codes[rn] + ', ' + '#' + address + ']')

                print(self.instruction)

                #LDUR
            elif(decimal_opcode == 1986):
                address = str(int(opcode[11:20], 2))
                rn = opcode[22:27]
                rt = opcode[27:32]

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "LDUR\t" + self.register_codes[rt] + ', ['
                                   + self.register_codes[rn] + ', ' + '#' + address + ']')

                print(self.instruction)

                #BREAK
            elif(decimal_opcode == 2038):

                self.instruction = (op_1_format + " " + op_2_format + " " + reg_1_format + " "
                                   + imm_format + " " + reg_2_format + " " + reg_3_format + "\t"
                                   + self.mem + "\t" + "BREAK")

                print(self.instruction)

                #NUMBERS
            else:
                bin = opcode[0:32]
                opcode = str(int(opcode, 2) - 2**32)
                self.instruction = (bin + "\t" + self.mem + "\t" + opcode)
                print(self.instruction)

            count += 1
            self.mem = str(int(self.mem) + 4)




d = disassembler()
d.load_file()
d.run()
