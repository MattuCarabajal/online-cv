from src.libs.csv import csv_to_list_dict
from datetime import datetime
import json
import ast


def get_languages_data( src = 'src/' ):
    languages = csv_to_list_dict( f'{src}data_vault/languages.csv' )
    for language in languages:
        language[ 'currently' ] = ast.literal_eval( language[ 'currently' ] )
        if language[ 'last_time' ] != '':
            last_time = int( language[ 'last_time' ] )
            date = int( datetime.today().strftime( '%Y' ) )
            language[ 'last_time' ] = f'{( date - last_time )} years.'
    return languages

if __name__ == '__main__':
    print( json.dumps( get_languages_data( src = 'src/' ), indent = 4, ensure_ascii=False ) )
