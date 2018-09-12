class disassembler(object):
    binary_array = []
    code_array = []
    instruction = ""


    def __init__(self):
        return

#ffav
    def load_file(self):
        with open('test2_bin.txt') as my_file:
            for line in my_file:
                self.binary_array.append(line)
                print(line)

    def run(self):
        count = 0
        while(count < len(self.binary_array)):
            opcode = str(self.binary_array[count])
            decimal_opcode = int(opcode[0:11], 2)   #holds the decimal opcode value
            op_1_format = opcode[0:8] #holds the format for first 1-8 opcode digits
            op_2_format = opcode[8:11] #holds the format the opcode digits 9-11
            last_reg = opcode[11:16]  #holds final specified register digits, 5 total
            immediate = opcode[16:21] #specifies and holds immediate digits, 5 total
            second_reg = opcode[21:26] #holds the second specified register destination digits, 5 total
            result_reg = opcode[26:32]  #holds register assignment number 1

            if(decimal_opcode>= 160 and decimal_opcode <=191):
                print('B')

            elif(decimal_opcode == 1104):
                print('AND')

            elif(decimal_opcode == 1112):
                self.instruction = (op_1_format + " " + op_2_format + " " + last_reg + " "
                                   + immediate + " " + second_reg + " " + result_reg + "\t"
                                   + "96\t" + "ADD\t" + "R3, " + "R1, " + "R2")

                print(self.instruction)


            elif(decimal_opcode == 1160 or decimal_opcode == 1161):
                print('ADDI')

            elif(decimal_opcode == 1360):
                print('ORR')

            elif(decimal_opcode >= 1440 and decimal_opcode <= 1447):
                print('CBZ')

            elif(decimal_opcode >= 1448 and decimal_opcode <= 1455):
                print('CBNZ')

            elif(decimal_opcode == 1624):
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
