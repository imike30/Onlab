import random
import csv

output_file = "network_data.csv"

connections = ["AB", "BA", "AD", "DA", "BD", "DB"]
failures = ["semmi", "AB", "BC", "CD", "DE", "EA"]

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(connections + failures)  #Header

    for _ in range(100):

        inA = random.random()
        inB = random.random()
        inD = random.random()

        AB = random.uniform(0, inA)
        BA = random.uniform(0, inB)
        AD = inA - AB
        DA = random.uniform(0, inD)
        BD = inB - BA
        DB = inD - DA

        base_traffic = [AB, BA, AD, DA, BD, DB]

        for failure in failures:
            traffic = base_traffic.copy()
            failure_flags = [0, 0, 0, 0, 0, 0]


            if failure == "AB":
                traffic[0] = traffic[1] = 0  #AB és BA
                failure_flags[1] = 1  #AB
            elif failure == "BC":
                traffic[5] = traffic[4] = 0  #DB és BD
                failure_flags[2] = 1  #BC
            elif failure == "CD":
                traffic[4] = traffic[5] = 0  #BD és DB
                failure_flags[3] = 1  #CD
            elif failure == "DE":
                traffic[3] = traffic[2] = 0  #DA és AD
                failure_flags[4] = 1  #DE
            elif failure == "EA":
                traffic[2] = traffic[3] = 0  #AD és DA
                failure_flags[5] = 1  #EA
            else:  #Nincs hiba
                failure_flags[0] = 1

            writer.writerow(traffic + failure_flags)

print(f"Data saved to {output_file}")
