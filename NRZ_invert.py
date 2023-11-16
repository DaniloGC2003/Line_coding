
def NRZ_I_encode(bit_string):#recebe string de bits, retorna lista de 'tensoes'
        encoded_voltage_list = []

        atual = 1
        for i in range(0, len(bit_string)):
                if bit_string[i] == '0':
                        encoded_voltage_list.append(atual)
                elif bit_string[i] == '1':
                        atual *= -1
                        encoded_voltage_list.append(atual)
        
        return encoded_voltage_list
                        
def NRZ_I_yaxis(voltage_list):#retorna lista utilizada para construir grafico
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

def NRZ_I_decode(voltage_list):#recebe lista de tensoes, retorna string de bits
    bit_string = ''
    for i in range(0, len(voltage_list)):
        pass

print(NRZ_I_encode('101001110'))
    
         
