import csv
import json
import os

def split_name(name):
    particles = ["da", "de", "do", "dos", "das"]
    name_parts = name.split()
    
    # If the second to last part is a particle, consider it as part of the family name
    if name_parts[-2].lower() in particles:
        given_name = name_parts[:-2]
        family_name = name_parts[-2:]
    else:
        given_name = name_parts[:-1]
        family_name = name_parts[-1:]
    
    return given_name, family_name

# Input and output file paths
input_csv_file = "/app/data/patients.csv"
output_ndjson_file = "/app/shared/patients.ndjson"

# Read CSV and convert to NDJSON
with open(input_csv_file, "r", encoding="latin-1") as csv_file, open(output_ndjson_file, "w", encoding="utf-8") as ndjson_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)  # Get the headers from the first line
    
    for row in csv_reader:
        given, family = split_name(row[0])  # Assuming the name is in the first column
        
        # Convert each CSV row to a FHIR Patient resource
        patient = {
            "resourceType": "Patient",
            "identifier": [
                {
                    "use": "official",
                    "system": "http://example.org/cpf",
                    "value": row[1].replace(".", "").replace("-", "")  # Assuming CPF is in the second column
                }
            ],
            "name": [
                {
                    "family": " ".join(family),
                    "given": given
                }
            ],
            "telecom": [
                {
                    "system": "phone",
                    "value": row[4]  # Assuming phone is in the fifth column
                }
            ],
            "gender": "male" if row[2] == "Masculino" else "female",  # Assuming gender is in the third column
            "birthDate": "-".join(reversed(row[3].split("/"))),  # Assuming birth date is in the fourth column
            "address": [
                {
                    "country": row[5]  # Assuming country is in the sixth column
                }
            ],
            "note": [
                {
                    "text": row[6]  # Assuming observation is in the seventh column
                }
            ]
        }
        # Serialize the dictionary to JSON and write to the NDJSON file
        json.dump(patient, ndjson_file, ensure_ascii=False)
        ndjson_file.write("\n")

print(f"Conversion completed. NDJSON file saved as {output_ndjson_file}")
