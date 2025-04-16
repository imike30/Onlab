import random
import csv

output_file = "bigger_test_data_missing.csv"

connections = ["AtoB", "BtoA", "AtoG", "GtoA", "BtoC", "CtoB", "BtoE", "EtoB", "BtoG", "GtoB", "CtoD", "DtoC", "DtoE", "EtoD", "EtoF", "FtoE", "EtoG", "GtoE", "FtoG", "GtoF"]
failures = ["semmi", "AB", "AG", "BC", "BE", "BG", "CD", "DE", "EF", "EG", "FG"]

connections.pop(0)
connections.pop(0)

connections.pop(8)
connections.pop(8)

connections.pop(12)
connections.pop(12)

connections.pop(12)
connections.pop(12)

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(connections + failures)  #Header

    for _ in range(50):

        inA = random.random()
        inC = random.random()
        inD = random.random()
        inF = random.random()

        #A-ból érkező traffic
        AB = random.uniform(0, inA)
        AG = inA - AB
        GF = AG
        BC = random.uniform(0, AB)
        BE = AB - BC
        ED = BE

        #C-ből érkező traffic
        CD = random.uniform(0, inC)
        CB = inC - CD
        BA = random.uniform(0, CB)
        BG = CB - BA
        GF += BG

        #D-ből érkező traffic
        DC = random.uniform(0, inD)
        DE = inD - DC
        EF = random.uniform(0, DE)
        EG = DE - EF
        GA = EG

        #F-ből érkező traffic
        FG = random.uniform(0, inF)
        FE = inF - FG
        GA += FG
        ED += random.uniform(0, FE)
        EB = FE - ED
        BC += EB

        #maradék
        GE = 0
        GB = 0

        base_traffic = [AB, BA, AG, GA, BC, CB, BE, EB, BG, GB, CD, DC, DE, ED, EF, FE, EG, GE, FG, GF]
                       # 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19

        for failure in failures:
            traffic = base_traffic.copy()
            failure_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


            if failure == "AB":
                #AB:
                traffic[2] += traffic[0] #AG
                traffic[9] += (traffic[0] - traffic[6]) #GB
                traffic[17] += traffic[6] #GE
                traffic[13] += traffic[6] #ED

                #BA:
                traffic[3] += (traffic[5] - traffic[8]) #GA
                traffic[8] += (traffic[5] - traffic[8]) #BG

                traffic[0] = traffic[1] = 0  #AB és BA
                traffic[6] = 0  #BE
                failure_flags[1] = 1  #AB
            
            elif failure == "AG":
                #AG:
                traffic[0] += traffic[2] #AB
                traffic[8] += traffic[2] #BG

                #GA:
                traffic[7] += traffic[16] #EB
                traffic[1] += traffic[16] #BA
                traffic[9] += traffic[18] #GB
                traffic[1] += traffic[18] #BA

                traffic[2] = traffic[3] = 0  #AG és GA
                traffic[16] = 0  #EG
                failure_flags[2] = 1  #AG
            
            elif failure == "BC":
                #BC:
                traffic[13] += (traffic[0] - traffic[6]) #ED
                traffic[11] += (traffic[0] - traffic[6]) #DC
                traffic[6] += (traffic[0] - traffic[6]) #BE
                traffic[13] += traffic[7] #ED
                traffic[11] += traffic[7] #DC
                
                #CB:
                traffic[10] += traffic[1] #CD
                traffic[12] += traffic[1] #DE
                traffic[7] += traffic[1] #EB
                traffic[10] += traffic[8] #CD
                traffic[12] += traffic[8] #DE
                traffic[14] += traffic[8] #EF
                traffic[19] -= traffic[8] #GF

                traffic[4] = traffic[5] = 0  #BC és CB
                traffic[7] = 0  #EB
                traffic[8] = 0  #BG
                failure_flags[3] = 1  #BC
            
            elif failure == "BE":
                #BE:
                traffic[4] += traffic[6] #BC
                traffic[10] += traffic[6] #CD
                traffic[13] -= traffic[6] #ED

                #EB:
                traffic[13] += traffic[7] #AE
                traffic[11] += traffic[7] #EC
                traffic[4] -= traffic[7] #CD

                traffic[6] = traffic[7] = 0  #BE és EB
                failure_flags[4] = 1  #BE
            
            elif failure == "BG":
                #BG:
                traffic[10] += traffic[8] #CD
                traffic[12] += traffic[8] #DE
                traffic[14] += traffic[8] #EF
                traffic[5] -= traffic[8] #CB
                traffic[19] -= traffic[8] #CB

                #GB:
                #alapból is 0

                traffic[8] = traffic[9] = 0  #BG és GB
                failure_flags[5] = 1  #BG
            
            elif failure == "CD":
                #CD:
                traffic[5] += traffic[10] #CB
                traffic[6] += traffic[10] #BE
                traffic[13] += traffic[10] #ED

                #DC:
                traffic[12] += traffic[11] #DE
                traffic[7] += traffic[11] #EB
                traffic[4] += traffic[11] #BC

                traffic[10] = traffic[11] = 0  #CD és DC
                failure_flags[6] = 1  #CD
            
            elif failure == "DE":
                #DE:
                traffic[11] += traffic[14] #DC
                traffic[5] += traffic[14] #CB
                traffic[6] += traffic[14] #BE
                traffic[11] += traffic[16] #DC
                traffic[5] += traffic[16] #CB
                traffic[1] += traffic[16] #BA
                traffic[3] -= traffic[16] #GA

                #ED:
                traffic[4] += traffic[6] #BC
                traffic[10] += traffic[6] #CD
                traffic[7] += (traffic[13] - traffic[6]) #EB
                traffic[4] += (traffic[13] - traffic[6]) #BC
                traffic[10] += (traffic[13] - traffic[6]) #CD

                traffic[12] = traffic[13] = 0  #DE és ED
                traffic[16] = 0  #EG
                traffic[6] = 0  #BE
                failure_flags[7] = 1  #DE
            
            elif failure == "EF":
                #EF:
                traffic[16] += traffic[14] #EG
                traffic[19] += traffic[14] #GF

                #FE:
                traffic[18] += traffic[15] #FG
                traffic[17] += (traffic[13] - traffic[6]) #GE
                traffic[9] += traffic[7] #GB

                traffic[14] = traffic[15] = 0  #EF és FE
                traffic[7] = 0  #EB
                failure_flags[8] = 1  #EF
            
            elif failure == "EG":
                #EG:
                traffic[7] += traffic[16] #EB
                traffic[1] += traffic[16] #BA
                traffic[3] -= traffic[16] #GA

                #GE:
                #alapból is 0

                traffic[16] = traffic[17] = 0  #EG és GE
                failure_flags[9] = 1  #EG
            
            elif failure == "FG":
                #FG:
                traffic[15] += traffic[18] #FE
                traffic[16] += traffic[18] #EG

                #GF:
                traffic[17] += traffic[2] #GE
                traffic[14] += traffic[2] #EF
                traffic[6] += traffic[8] #BE
                traffic[14] += traffic[8] #EF

                traffic[18] = traffic[19] = 0  #FG és GF
                traffic[8] = 0  #BG
                failure_flags[10] = 1  #FG
            
            else:  #Nincs hiba
                failure_flags[0] = 1
            
            traffic.pop(0)
            traffic.pop(0)

            traffic.pop(8)
            traffic.pop(8)

            traffic.pop(12)
            traffic.pop(12)

            traffic.pop(12)
            traffic.pop(12)

            writer.writerow(traffic + failure_flags)

print(f"Data saved to {output_file}")