from json import dumps

from src.libs.xlsx import xlsx_to_dict


def get_skills_data():
    skills_file_path = 'data_vault/skills.xlsx'
    try:
        skills = xlsx_to_dict(f'src/{skills_file_path}')
    except FileNotFoundError:
        skills = xlsx_to_dict(skills_file_path)

    return skills


'''
Basic   Basic/Intermediate	Intermediate	Intermediate/Advance    Advance
20      35                  50              70                      90%
'''


if __name__ == '__main__':
    print( dumps( get_skills_data(), indent = 4, ensure_ascii=False ) )

    skills = get_skills_data()
    for skill_section in skills.keys():
        print(f'skill_section: { skill_section }')
        for skill in skills[ skill_section ]:
            print( f"skill_name: { skill[ 'name' ] }" )
            print( f"skill_level: { skill[ 'level' ] }" )
