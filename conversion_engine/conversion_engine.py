import os
import sys
import csv
import json


def dict_types_files_converter(file_name: str, target_file_type: str) -> None:

    """
    Handle all the file types conversions based on user input
    :param file_name: The source file to be converted
    :param target_file_type: To distinguish between CSV and TSV file types for naming the new file (extension)
    :return: None
    """

    print(f'\n\tReading your {os.path.splitext(file_name)[-1][1:].upper()} file...')

    if os.path.splitext(file_name)[-1].casefold() == '.tsv' or os.path.splitext(file_name)[-1].casefold() == '.csv':

        # Writing to a JSON file
        print(f'\n\tWriting your JSON file...')

        c_tsv_content: {dict} = csv_tsv_reader(file_name,  target_file_type)

        with open(resource_path(f'../{os.path.splitext(file_name)[0]}.json'), mode='w') as json_file:
            json.dump(c_tsv_content, fp=json_file, indent=4)
            print('\n\tSUCCESS! Your JSON file has been successfully created.')

    elif os.path.splitext(file_name)[-1].casefold() == '.json':

        # Writing to a CSV / TSV file
        print(f'\n\tWriting your {target_file_type.upper()} file...')

        if target_file_type.strip() == 'tsv':  # Determining the delimiter arg
            delimiter = "\t"
        else:
            delimiter = ","

        json_content: {dict} = json_reader(file_name)

        with open(resource_path(f'../{os.path.splitext(file_name)[0]}.{target_file_type}'), mode='w', encoding='UTF-8',
                  newline='') as c_tsv_source_file:

            csv_writer: csv.DictWriter = csv.DictWriter(c_tsv_source_file, fieldnames=json_content.keys(),
                                                        delimiter=delimiter)
            csv_writer.writeheader()

            csv_writer.writerow(json_content)
            print(f'\n\tSUCCESS! Your {target_file_type.upper()} file has been successfully created.')


def csv_tsv_reader(file_name: str, delimiter: str) -> {dict}:

    """
    Read content from a CSV / TSV file and return it as a dictionary type
    :param file_name: The name of the data source file to be converted
    :param delimiter: To control how the file is read i.e. whether to use commas (csv) or tabs (tsv) as separators
    :return: A Dictionary
    """

    if delimiter.strip() == 'tsv':  # Setting the delimiter
        delimiter: str = "\t"
    else:
        delimiter: str = ","

    t_csv_content: {dict} = {}

    with open(resource_path(f'../{file_name}'), 'r', encoding='UTF-8') as c_tsv_source_file:
        csv_reader: csv.DictReader = csv.DictReader(c_tsv_source_file, delimiter=delimiter)

        # Retrieve the dict keys into an array
        columns: [str] = csv_reader.fieldnames

        rows: [list] = []

        # Get the values and add them to a list
        [rows.append(list(row.values())) for row in csv_reader]

        # Update our dictionary by mapping key-value pairs
        [t_csv_content.update({col: rows[0][idx]}) for idx, col in enumerate(columns)]

    return t_csv_content


def json_reader(file_name) -> {dict}:

    """
    Read a JSON file and return its content
    :param file_name: The name of the JSON file to be converted
    :return: A Dictionary / Python Object
    """

    with open(resource_path(resource_path(f'../{file_name}')), mode='r', encoding='UTF-8') as json_source_file:
        return json.load(json_source_file)


def resource_path(relative_path) -> [str, bytes]:

    """
    For managing file resources.
    :param: relative_path: The relative path (relative to the script file) of the target file as a string
    :return: A list of bytes (file content) and string (file path)
    """

    base_path: [] = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
