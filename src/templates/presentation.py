from datetime import datetime

from src.libs.csv import csv_to_list_dict


def get_date() -> str:
    return datetime.today().strftime( '%B %Y' )

def check_string(key: str, value: str) -> str:
    file_flag = False

    if 'list_' in key:
        key = key.split('_')[1:]
        key = '_'.join(key)
        values = value.split(',')
        list_value = '<span class="symbols">[</span> '
        comma = '<span class="comma">,</span> '
        for index in range(len(values)):
            list_value += f"'{ values[index].strip() }'"
            if index < len(values) - 1:
                list_value += f'{ comma }'

        list_value += ' <span class="symbols">]</span>'
        value = list_value
    else:
        files = ['jpg', 'png']
        if value.split('.')[-1] not in files:
            value = f"'{value}'"
        else:
            file_flag = True

    if file_flag:
        row = value
    else:
        if 'phrase' not in key:
            row = f'<span class="row_text variable_name">{ key }</span>'
            row += '<span class="row_text equals">&nbsp;=&nbsp;</span>'
            row += value
        else:
            row = '<span class="row_text text function_name">print</span>'
            row += '<span class="row_text symbols">(&nbsp;</span>'
            row += f'<span class="phrase">{value}</span>'
            row += '<span class="row_text symbols">&nbsp;)</span>'

    return key, row

def transform_for_html_list(data: dict):
    counter = 0
    final = {}
    for key, value in data.items():
        if 'src' not in key:
            counter += 1
        key, string_value = check_string(key, value)
        final[key] = {
            'row_number': counter,
            'row_info': string_value
        }

    return final

def get_me_data(src='src/') -> dict:
    me_aux = csv_to_list_dict( f'{src}data_vault/me.csv' )[ 0 ]

    me = {
        'date': get_date()
    }
    me.update(me_aux)

    return transform_for_html_list(me)

def get_about_me_data(src='src/') -> dict:
    about_me = csv_to_list_dict( f'{src}data_vault/about_me.csv' )[ 0 ]

    return transform_for_html_list(about_me)

def get_ide_data() -> dict:
    python_data = {
        'language_img'     : 'static/images/icon-python.png',
        'branch'           : 'master',
        'encoding'         : 'UTF-8',
        'language'         : 'Python',
        'language_version' : '3.9.1'
    }

    hello_world = {
        'file_name'        : 'hello_world.py'
    }
    hello_world.update(python_data)

    about_me = {
        'file_name'        : 'about_me.py'
    }
    about_me.update(python_data)

    ide_data = {
        'hello_world': hello_world,
        'about_me': about_me
    }

    return ide_data
