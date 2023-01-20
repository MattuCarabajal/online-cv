import ast
import json
from datetime import datetime

from src.libs.csv import csv_to_list_dict


def get_languages_data():
    languages_file_path = 'data_vault/languages.csv'
    try:
        languages = csv_to_list_dict(f'src/{languages_file_path}')
    except FileNotFoundError:
        languages = csv_to_list_dict(languages_file_path)

    for language in languages:
        language[ 'currently' ] = ast.literal_eval( language[ 'currently' ] )
        if language[ 'last_time' ] != '':
            last_time = int( language[ 'last_time' ] )
            date = int( datetime.today().strftime( '%Y' ) )
            language[ 'last_time' ] = f'{( date - last_time )} years.'

    return languages

if __name__ == '__main__':
    print( json.dumps( get_languages_data(), indent = 4, ensure_ascii=False ) )
