import random
import csv

# Output file
output_file = "network_data.csv"

# Define the connections in the network
connections = ["AB", "BA", "AD", "DA", "BD", "DB"]
failures = ["semmi", "AB", "BC", "CD", "DE", "EA"]  # Possible failures

# Open the CSV file and write the header
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(connections + failures)  # Header

    # Generate 100 random scenarios
    for _ in range(100):
        # Generate random input traffic
        inA = random.random()
        inB = random.random()
        inD = random.random()

        # Compute base traffic values
        AB = random.uniform(0, inA)
        BA = random.uniform(0, inB)
        AD = inA - AB
        DA = random.uniform(0, inD)
        BD = inB - BA
        DB = inD - DA

        # Store the original values
        base_traffic = [AB, BA, AD, DA, BD, DB]

        # Generate 6 test cases: 1 normal + 5 failure cases
        for failure in failures:
            traffic = base_traffic.copy()  # Copy original traffic
            failure_flags = [0] * 6  # Initialize failure columns (all 0)

            # Apply failure by setting traffic to zero for the failed connection
            if failure == "AB":
                traffic[0] = traffic[1] = 0  # AB and BA fail
                failure_flags[1] = 1  # Mark AB as failed
            elif failure == "BC":
                traffic[5] = traffic[4] = 0  # DB and BD fail
                failure_flags[2] = 1  # Mark BC as failed
            elif failure == "CD":
                traffic[4] = traffic[5] = 0  # BD and DB fail
                failure_flags[3] = 1  # Mark CD as failed
            elif failure == "DE":
                traffic[3] = traffic[2] = 0  # DA and AD fail
                failure_flags[4] = 1  # Mark DE as failed
            elif failure == "EA":
                traffic[2] = traffic[3] = 0  # AD and DA fail
                failure_flags[5] = 1  # Mark EA as failed
            else:  # No failure case
                failure_flags[0] = 1  # Mark "semmi" as 1 (meaning no failure)

            # Write the row to the CSV file
            writer.writerow(traffic + failure_flags)

print(f"Data successfully saved to {output_file}")
