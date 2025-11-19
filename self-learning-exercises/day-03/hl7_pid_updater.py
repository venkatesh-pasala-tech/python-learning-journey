import os
import re
from pathlib import Path

# =============================================================================
# CONFIGURATION - UPDATE THESE VALUES
# =============================================================================

# MSH Segment Updates
# FROM: MSH|^^|ADT_Audacious|ADT_Audacious|Int Millennium|Cerner|20250509180324||ORU^R01|20250509180324329225342582|P|2.3
# TO:   MSH|^^|ADT_Audacious|ADT_Audacious|Int Millennium|Cerner|20250509180324||ORU^R01|20250509180324329225342582|T|2.3
# Change: Field 11 from 'P' to 'T'

NEW_MSH_DATA = {
    10: "T",  # Processing ID: Change from 'P' (Production) to 'T' (Test)
}

# PID Segment Updates
# FROM: PID|1||10116851_ADT_Audacious_20250509103129|29^ADT_Audacious|||20250509103129||||||||||||||LAB|F
# TO:   PID|1||20155022251|"Research"||19520225|M||PO Box 25.34^^CALlOWAY^OH^43191|(614) 266-4258||||||||||||||M

NEW_PID_DATA = {
    3: "20155022251",  # Patient Internal ID
    4: '"Research"',  # Patient External ID (with quotes)
    5: "",  # Patient Name (empty)
    7: "19520225",  # Date of Birth (YYYYMMDD format)
    8: "M",  # Gender
    9: "",  # Patient Alias (empty)
    10: "",  # Race (empty)
    11: "PO Box 25.34^^CALlOWAY^OH^43191",  # Address
    13: "(614) 266-4258",  # Phone Number - Home
    14: "",  # Phone Number - Business
    15: "",  # Primary Language
    16: "",  # Marital Status
    17: "",  # Religion
    18: "",  # Account Number
    19: "",  # SSN
    20: "",  # Driver's License
    21: "",  # Mother's Identifier
    22: "",  # Ethnic Group
    23: "",  # Birth Place
    24: "",  # Multiple Birth Indicator
    25: "",  # Birth Order
    26: "",  # Citizenship
    27: "",  # Veterans Military Status
    28: "",  # Nationality
    29: "",  # Patient Death Date and Time
    30: "",  # Patient Death Indicator
    31: "",  # Identity Unknown Indicator
    32: "",  # Identity Reliability Code
    33: "",  # Last Update Date/Time
    34: "",  # Last Update Facility
    35: "",  # Species Code
    36: "",  # Breed Code
    37: "",  # Strain
    38: "",  # Production Class Code
    39: "M",  # Tribal Citizenship (last field)
}

# Set your folder paths
# OPTION 1: Use raw string (r prefix) - RECOMMENDED
INPUT_FOLDER = r"C:\Users\vpasala\Downloads\Audacious 1\Audacious\Test Input"
OUTPUT_FOLDER = r"C:\Users\vpasala\Downloads\Audacious 1\Audacious\Test Output"


def update_segment(hl7_content, segment_name, new_data, mode='replace'):
    """
    Update a specific segment in HL7 message with new data.

    Parameters:
    hl7_content: string containing the HL7 message
    segment_name: segment to update (e.g., 'PID', 'MSH')
    new_data: dictionary with field positions and values
    mode: 'replace' to replace entire fields, 'partial' to replace components

    Example new_data for replace mode:
    {
        3: "12345678^^^MRN",     # Field with components
        5: "DOE^JOHN^M",         # Patient Name (Last^First^Middle)
        7: "19800115",           # Date of Birth (YYYYMMDD)
    }
    """
    lines = hl7_content.split('\r' if '\r' in hl7_content else '\n')
    updated_lines = []

    for line in lines:
        if line.startswith(segment_name + '|'):
            # Split the segment by field separator '|'
            fields = line.split('|')

            # Update specified fields
            for field_num, new_value in new_data.items():
                # Ensure we have enough fields
                while len(fields) <= field_num:
                    fields.append('')

                if isinstance(new_value, dict) and 'components' in new_value:
                    # Partial update of components within a field
                    components = fields[field_num].split('^')
                    for comp_num, comp_value in new_value['components'].items():
                        while len(components) <= comp_num:
                            components.append('')
                        components[comp_num] = comp_value
                    fields[field_num] = '^'.join(components)
                else:
                    # Complete field replacement
                    fields[field_num] = new_value

            # Reconstruct the line
            updated_line = '|'.join(fields)
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    return ('\r' if '\r' in hl7_content else '\n').join(updated_lines)


def process_hl7_folder(input_folder, output_folder, new_msh_data, new_pid_data):
    """
    Process all HL7 files in a folder and update MSH and PID segments.

    Parameters:
    input_folder: path to folder containing HL7 files
    output_folder: path to folder where updated files will be saved
    new_msh_data: dictionary with MSH field positions and values
    new_pid_data: dictionary with PID field positions and values
    """
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Track statistics
    processed = 0
    errors = 0

    # Get all files in input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    print(f"Found {len(files)} files to process...")

    for filename in files:
        try:
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Read the HL7 file
            with open(input_path, 'r', encoding='utf-8') as f:
                hl7_content = f.read()

            # Update MSH segment
            updated_content = update_segment(hl7_content, 'MSH', new_msh_data)

            # Update PID segment
            updated_content = update_segment(updated_content, 'PID', new_pid_data)

            # Write to output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            processed += 1

            if processed % 100 == 0:
                print(f"Processed {processed} files...")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            errors += 1

    print(f"\n=== Processing Complete ===")
    print(f"Successfully processed: {processed} files")
    print(f"Errors: {errors} files")
    print(f"Output saved to: {output_folder}")


# =============================================================================
# CONFIGURATION - UPDATE THESE VALUES
# =============================================================================

# Based on your sample message, here's what I found in your PID segment:
# PID|1||1144885_ADT_Audacious_20250508220845|2^^ADT_Audacious|||20250508220845||||||||||||||LAB|F

# Define the new PID data you want to use
# OPTION 1: Replace specific fields completely
NEW_PID_DATA = {
    3: "10157215",           # Patient Internal ID (currently: 1144885_ADT_Audacious_20250508220845)
    # 4: "NEW_ID_NUMBER^^SYSTEM",    # Patient External ID (currently: 2^^ADT_Audacious)
    5: "Beatrix^Devesh^",             # Patient Name (currently empty in your sample)
    7: "19520225",                 # Date of Birth (currently: 20250508220845)
    8: "M",                        # Gender (currently empty)
    # 10: "2106-3",                  # Race (currently empty)
    # 11: "123 MAIN ST^^CITY^ST^ZIP",  # Address (currently empty)
    # 13: "(555)555-1234",           # Phone Number (currently empty)
    # 18: "NEW_ACCOUNT_NUMBER",      # Account Number (currently: LAB)
    # 19: "NEW_SSN",                 # SSN (currently: F)
}

# OPTION 2: If you want to anonymize/mask data, uncomment this:
# import random
# import string
# NEW_PID_DATA = {
#     3: f"ANON_{''.join(random.choices(string.digits, k=10))}",
#     5: "ANONYMOUS^PATIENT^X^^",
#     7: "19000101",  # Generic date
#     8: "U",         # Unknown gender
# }

# OPTION 3: If you want to keep some parts and only change others:
# For example, to change only the timestamp in field 7:
# NEW_PID_DATA = {
#     7: "20250101",  # Change all birthdates to this
# }

# Set your folder paths
# OPTION 1: Use raw string (r prefix) - RECOMMENDED
INPUT_FOLDER = r"C:\Users\vpasala\OneDrive - DaVita\Work\Work\VH DI Enhancements\B2B Work\HealthShare\Audacious\Performance Test\Input Files"
OUTPUT_FOLDER = r"C:\Users\vpasala\OneDrive - DaVita\Work\Work\VH DI Enhancements\B2B Work\HealthShare\Audacious\Performance Test\Output Files"

# OPTION 2: Use forward slashes (works on Windows too)
# INPUT_FOLDER = "C:/Users/vpasala/Downloads/Audacious 1/Audacious/Test Input"
# OUTPUT_FOLDER = "C:/Users/vpasala/Downloads/Audacious 1/Audacious/Test Output"

# OPTION 3: Escape backslashes with double backslashes
# INPUT_FOLDER = "C:\\Users\\vpasala\\Downloads\\Audacious 1\\Audacious\\Test Input"
# OUTPUT_FOLDER = "C:\\Users\\vpasala\\Downloads\\Audacious 1\\Audacious\\Test Output"

# =============================================================================
# RUN THE SCRIPT
# =============================================================================

if __name__ == "__main__":
    print("HL7 MSH & PID Segment Batch Updater")
    print("=" * 50)

    # Check if input folder exists
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: Input folder '{INPUT_FOLDER}' does not exist!")
        print("Please create the folder and add your HL7 files.")
    else:
        # Process all files - updates both MSH and PID segments
        process_hl7_folder(INPUT_FOLDER, OUTPUT_FOLDER, NEW_MSH_DATA, NEW_PID_DATA)

    print("\nPress Enter to exit...")
    input()