
def NRZ_L_encode(bit_string):#recebe string de bits, retorna lista de 'tensoes'
    encoded_voltage_list = []

    for i in range(0, len(bit_string)):
        if bit_string[i] == '0':
            encoded_voltage_list.append(1)
        else:
            encoded_voltage_list.append(-1)
    
    return encoded_voltage_list

def NRZ_L_yaxis(voltage_list):#retorna lista utilizada para construir grafico
    yaxis = []
    for i in range(0, len(voltage_list)):
        if i == 0:
            yaxis.append(voltage_list[0])
            yaxis.append(voltage_list[0])
        elif voltage_list[i-1] == 1 and voltage_list[i] == -1:
            yaxis.append(voltage_list[i-1])
            yaxis.append(voltage_list[i])
        elif voltage_list[i-1] == -1 and voltage_list[i] == 1:
            yaxis.append(voltage_list[i-1])
            yaxis.append(voltage_list[i])
        elif voltage_list[i-1] == voltage_list[i]:
            yaxis.append(voltage_list[i])
            yaxis.append(voltage_list[i])
    return yaxis

def NRZ_L_decode(voltage_list):#recebe lista de tensoes, retorna string de bits
    bit_string = ''
    for i in range(0, len(voltage_list)):
        if voltage_list[i] == 1:
            bit_string += '0'
        else:
            bit_string += '1'
    return bit_string



