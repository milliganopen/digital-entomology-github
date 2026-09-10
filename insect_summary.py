import csv
from collections import defaultdict

total_observations = 0
total_insects = 0

species_counts = defaultdict(int)

with open("insect_observations.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        count = int(row["count"])

        total_observations += 1
        total_insects += count

        species_counts[row["scientific_name"]] += count


print("INSECT SURVEY SUMMARY")
print("---------------------")

print(f"Observation records: {total_observations}")
print(f"Total insects observed: {total_insects}")

most_common_species = max(
    species_counts,
    key=species_counts.get
)

print(
    f"Most frequently observed species: "
    f"{most_common_species} "
    f"({species_counts[most_common_species]} individuals)"
)
