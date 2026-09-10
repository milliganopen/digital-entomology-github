import csv

total_observations = 0
total_insects = 0

with open("insect_observations.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_observations += 1
        total_insects += int(row["count"])

print("INSECT SURVEY SUMMARY")
print("---------------------")
print(f"Observation records: {total_observations}")
print(f"Total insects observed: {total_insects}")