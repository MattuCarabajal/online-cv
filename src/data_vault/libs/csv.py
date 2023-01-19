import csv
from typing import List


def csv_to_list_dict( fil_path, delimiter=";" ) -> List[dict]:
    jobs = []
    with open( fil_path, encoding='utf8') as file:
        file_content = csv.DictReader( file, delimiter=delimiter )
        for row in file_content:
            jobs.append( row )
    return jobs