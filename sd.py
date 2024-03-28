import json

Symbols=["MSFT" , "NVDA" , "AMZN" , "META" , "LLY" , "TSLA" , "AVGM" ,"V" , "JPM" , "UNH"]
existing_data=[]
    #for symbol in Symbols:
# Define the file path of the existing JSON file
for symbol in Symbols:
    file_path = f'{symbol}'

    # Read existing JSON data from the file

    with open(file_path, "r") as json_file:
        new_data = json.load(json_file)

    existing_data.append(new_data)

    # Write the updated dictionary back to the JSON file
with open('output.json', "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

print(f"New data has been appended to {file_path}")