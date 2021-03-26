def create_phone_number(n):
    output = [str(x) for x in n] 
    s=""
    output=s.join(output)
    return ("({}) {}-{}".format(output[:3],output[3:6],output[6:]))
