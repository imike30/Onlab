import random
import csv


output_file = "test_data_missing.csv"

connections = ["AtoB", "BtoA", "BtoC", "CtoB", "CtoD", "DtoC", "CtoE", "EtoC", "DtoE", "EtoD", "EtoA", "AtoE"]
failures = ["semmi", "AB", "BC", "CD", "DE", "EA", "CE"]

connections.pop(0)
connections.pop(0)

connections.pop(4)
connections.pop(4)

connections.pop(0)
connections.pop(0)

connections.pop(2)
connections.pop(2)

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(connections + failures)  #Header

    for _ in range(50):

        inA = random.random()
        inB = random.random()
        inD = random.random()

        AB = random.uniform(0, inA)
        BA = random.uniform(0, inB)
        AE = inA - AB
        ED = AE
        DE = random.uniform(0, inD)
        EA = DE
        BC = inB - BA
        CD = BC
        DC = inD - DE
        CB = DC
        CE = 0
        EC = 0

        base_traffic = [AB, BA, BC, CB, CD, DC, CE, EC, DE, ED, EA, AE]
                       # 0   1   2   3   4   5   6   7   8   9  10  11

        for failure in failures:
            traffic = base_traffic.copy()
            failure_flags = [0, 0, 0, 0, 0, 0, 0]


            if failure == "AB":
                #AB:
                traffic[11] += traffic[0] #AE
                traffic[7] += traffic[0] #EC
                traffic[3] += traffic[0] #CB
                #BA:
                traffic[2] += traffic[1] #BC
                traffic[6] += traffic[1] #CE
                traffic[10] += traffic[1] #EA

                traffic[0] = traffic[1] = 0  #AB és BA
                failure_flags[1] = 1  #AB
            
            elif failure == "BC":
                #BC:
                traffic[1] += traffic[2] #BA
                traffic[11] += traffic[2] #AE
                traffic[9] += traffic[2] #ED
                #CB:
                traffic[8] += traffic[3] #DE
                traffic[10] += traffic[3] #EA
                traffic[0] += traffic[3] #AB

                traffic[2] = traffic[3] = 0  #BC és CB
                traffic[4] = traffic[5] = 0  #CD és DC
                failure_flags[2] = 1  #BC
            
            elif failure == "CD":
                #CD:
                traffic[2] += traffic[4] #BC
                traffic[6] += traffic[4] #CE
                traffic[9] += traffic[4] #ED
                #DC:
                traffic[8] += traffic[5] #DE
                traffic[7] += traffic[5] #EC
                traffic[3] += traffic[5] #CB

                traffic[4] = traffic[5] = 0  #CD és DC
                failure_flags[3] = 1  #CD
            
            elif failure == "DE":
                #DE:
                traffic[5] += traffic[8] #DC
                traffic[6] += traffic[8] #CE
                traffic[10] += traffic[8] #EA
                #ED:
                traffic[11] += traffic[9] #AE
                traffic[7] += traffic[9] #EC
                traffic[4] += traffic[9] #CD

                traffic[8] = traffic[9] = 0  #DE és ED
                failure_flags[4] = 1  #DE
            
            elif failure == "EA":
                #EA:
                traffic[5] += traffic[10] #DC
                traffic[3] += traffic[10] #CB
                traffic[1] += traffic[10] #BA
                #AE:
                traffic[0] += traffic[11] #AB
                traffic[2] += traffic[11] #BC
                traffic[4] += traffic[11] #CD

                traffic[8] = traffic[9] = 0  #DE és ED
                traffic[10] = traffic[11] = 0  #EA és AE
                failure_flags[5] = 1  #EA
            
            elif failure == "CE":
                traffic[6] = traffic[7] = 0  #CE és EC
                failure_flags[6] = 1  #CE
            
            else:  #Nincs hiba
                failure_flags[0] = 1

            traffic.pop(0)
            traffic.pop(0)

            traffic.pop(4)
            traffic.pop(4)

            traffic.pop(0)
            traffic.pop(0)

            traffic.pop(2)
            traffic.pop(2)

            writer.writerow(traffic + failure_flags)

print(f"Data saved to {output_file}")
