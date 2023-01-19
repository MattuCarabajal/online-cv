from json import dumps

from libs.xlsx import xlsx_to_dict


def get_skills_data( src = '' ):
    skills = xlsx_to_dict( f'{ src }data_vault/skills.xlsx' )
    return skills


'''
Basic   Basic/Intermediate	Intermediate	Intermediate/Advance    Advance
20      35                  50              70                      90%
'''


if __name__ == '__main__':
    print( dumps( get_skills_data( src = 'src/' ), indent = 4, ensure_ascii=False ) )

    skills = get_skills_data( src = 'src/' )
    for skill_section in skills.keys():
        print(f'skill_section: { skill_section }')
        for skill in skills[ skill_section ]:
            print( f"skill_name: { skill[ 'name' ] }" )
            print( f"skill_level: { skill[ 'level' ] }" )
