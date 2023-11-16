
def RZ_encode(bit_string):#recebe string de bits, retorna lista de 'tensoes'
    tensoes = []
    for i in range(0, len(bit_string)):
        if bit_string[i] == '0':
            tensoes.append(-1)
            tensoes.append(0)
        elif bit_string[i] == '1':
            tensoes.append(1)
            tensoes.append(0)
    return tensoes

def RZ_yaxis(voltage_list):#retorna lista utilizada para construir grafico
    yaxis = []
    for i in range(0, len(voltage_list)):
        if i == 0:
            yaxis.append(voltage_list[0])
            yaxis.append(voltage_list[0])
        elif voltage_list[i-1] == -1 and voltage_list[i] == 0:
            yaxis.append(voltage_list[i-1])
            yaxis.append(voltage_list[i])
        elif voltage_list[i-1] == 0 and voltage_list[i] == 1:
            yaxis.append(voltage_list[i-1])
            yaxis.append(voltage_list[i])
        elif voltage_list[i-1] == 1 and voltage_list[i] == 0:
            yaxis.append(voltage_list[i-1])
            yaxis.append(voltage_list[i])
        elif voltage_list[i-1] == 0 and voltage_list[i] == -1:
            yaxis.append(voltage_list[i-1])
            yaxis.append(voltage_list[i])
    return yaxis

def RZ_decode(voltage_list):#recebe lista de tensoes, retorna string de bits
    bit_string = ''
    for i in range(0, len(voltage_list)):
        if i == 0:
            pass
        if voltage_list[i-1] == -1 and voltage_list[i] == 0:
            bit_string += '0'
        elif voltage_list[i-1] == 1 and voltage_list[i] == 0:
            bit_string += '1'
    return bit_string