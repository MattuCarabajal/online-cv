import json

from src.libs.csv import csv_to_list_dict


def get_institutions_data():
    education_file_path = 'data_vault/education.csv'
    try:
        institutions = csv_to_list_dict( f'src/{education_file_path}' )
    except FileNotFoundError:
        institutions = csv_to_list_dict( education_file_path )

    return institutions

if __name__ == '__main__':
    print( json.dumps( get_institutions_data(), indent = 4, ensure_ascii=False ) )
