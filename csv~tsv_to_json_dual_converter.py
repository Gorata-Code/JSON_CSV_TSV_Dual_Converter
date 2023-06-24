import os
import sys
from conversion_engine.conversion_engine import dict_types_files_converter


def script_summary() -> None:
    print('''
               ***----------------------------------------------------------------------------------------***
         \t***------------------------ DUMELANG means GREETINGS! ~ G-CODE -----------------------***
                     \t***------------------------------------------------------------------------***\n

        \t"CSV/TSV <-> JSON DUAL CONVERTER" Version 1.0.0\n

        This bot will help you convert a CSV file or a TSV file to a
        JSON file and back. Enter the name of the file you want convert
        and the type of the file you want to convert to.

        Cheers!!
    ''')


def dicts_converting_bot(file_name: str, destination_file_type: str) -> None:
    try:
        dict_types_files_converter(file_name, destination_file_type)

    except Exception and FileNotFoundError:
        if FileNotFoundError:
            print(
                '\n\t*** Unable to locate your file. Please make sure you provide a valid file name & '
                'file extension within this folder. ***')
        else:
            raise

    input('\nPress Enter to Exit.')
    sys.exit(0)


def main() -> None:
    script_summary()
    file_name: str = input('\nPlease type the name of the file (including the extension) you would like to convert '
                           'and Press Enter: ')

    commas_or_tabs: str = ''  # To help distinguish between CSVs & TSVs

    if len(file_name.strip()) >= 5:
        if os.path.splitext(file_name)[-1].casefold() not in ['.json', '.csv', '.tsv']:  # Confirming the file type
            input('\nPlease provide a valid file name and file type.')
            sys.exit(1)

        if os.path.splitext(file_name)[-1].casefold() == '.json':
            commas_or_tabs = input('\nPlease type:\n\n\t\t"csv" to convert to a CSV file\n\t\t"tsv" to convert '
                                   'to a TSV file & Press Enter: ').lower()

        dicts_converting_bot(file_name, destination_file_type=commas_or_tabs)

    elif len(file_name.strip()) < 5 or os.path.splitext(file_name.strip()[-1]) == '':
        print('\nPlease provide a valid file name.')
        input('\nPress Enter to Exit: ')
        sys.exit(1)


if __name__ == '__main__':
    main()
