from libs.csv import csv_to_list_dict
import json


def get_institutions_data( src = '' ):
    institutions = csv_to_list_dict( f'{src}data_vault/education.csv' )
    return institutions

if __name__ == '__main__':
    print( json.dumps( get_institutions_data( src = 'src/' ), indent = 4, ensure_ascii=False ) )
