from datetime import datetime

from flask import Markup

from src.libs.csv import csv_to_list_dict


def get_jobs():
    jobs_file_path = 'data_vault/jobs.csv'
    jobs_descriptions_file_path = 'data_vault/jobs_descriptions.csv'
    try:
        jobs = csv_to_list_dict( f'src/{jobs_file_path}' )
        jobs_descriptions_list = csv_to_list_dict( f'src/{jobs_descriptions_file_path}' )
    except FileNotFoundError:
        jobs = csv_to_list_dict(jobs_file_path)
        jobs_descriptions_list = csv_to_list_dict(jobs_descriptions_file_path)

    jobs_descriptions = {}
    for job_project_descriptions in jobs_descriptions_list:
        company = job_project_descriptions[ 'company_name' ]
        project = job_project_descriptions[ 'project_name' ]
        description = job_project_descriptions[ 'description' ]
        if company not in jobs_descriptions:
            jobs_descriptions[ company ] = { project : description }
        else:
            jobs_descriptions[ company ][ project ] = description

    jobs_complete = []
    for job in jobs:
        job_complete = {
            'name'      : job[ 'name'      ],
            'url'       : job[ 'url'       ],
            'img_src'   : job[ 'img_src'   ],
            'time_span' : job[ 'time_span' ].replace(' – ', '<br>'),
            'position'  : job[ 'position'  ],
            'city'      : job[ 'city'      ]
        }

        projects = []
        job_projects = job[ 'projects_names' ].split( ',' )
        for project in job_projects:
            project = {
                    'name'        : project,
                    'description' : Markup( f"{ jobs_descriptions[ job[ 'name' ] ][ project ] }<br>" )
            }
            projects.append( project )
            job_complete[ 'projects' ] = projects

        jobs_complete.append( job_complete )

    return jobs_complete

def delta_time( begging: datetime, top: datetime ):
    years = top.year - begging.year
    months = top.month - begging.month

    if months < 0:
        years -= 1
        months = 12 - abs( months )

    return years, months

def get_references():
    hospital_file_path = 'data_vault/Municipal Hospital, Dr. Hector M. Cura.csv'
    globant_file_path = 'data_vault/Globant.csv'
    xappia_file_path = 'data_vault/Xappia.csv'
    global_hitss_file_path = 'data_vault/GlobalHitss.csv'
    seguro_file_path = 'data_vault/123seguro.csv'
    try:
        references = {
            'h_m_dr_hector_cura' : csv_to_list_dict(f'src/{hospital_file_path}'),
            'globant'            : csv_to_list_dict(f'src/{globant_file_path}'),
            'xappia'             : csv_to_list_dict(f'src/{xappia_file_path}'),
            'global_hitss'       : csv_to_list_dict(f'src/{global_hitss_file_path}'),
            '123seguro'          : csv_to_list_dict(f'src/{seguro_file_path}' )
        }
    except FileNotFoundError:
        references = {
            'h_m_dr_hector_cura' : csv_to_list_dict(hospital_file_path),
            'globant'            : csv_to_list_dict(globant_file_path),
            'xappia'             : csv_to_list_dict(xappia_file_path),
            'global_hitss'       : csv_to_list_dict(global_hitss_file_path),
            '123seguro'          : csv_to_list_dict(seguro_file_path)
        }

    for job in references.keys():
        for reference in range( 0, len( references[ job ] ) ):
            if references[ job ][ reference ][ 'until' ] == '':
                top = datetime.today()
            else:
                top = datetime.strptime( references[ job ][ reference ][ 'until' ], '%B %Y' )
            begging = datetime.strptime( references[ job ][ reference ][ 'since' ], '%B %Y' )

            years, months = delta_time( begging, top )

            delta_years = ''
            if years > 0:
                delta_years = f'{ years } yrs' if years > 1 else f'{ years } yr'

            delta_months = ''
            if months > 0:
                delta_months = f'{ months } mos' if months > 1 else f'{ months } mo'

            connection = ' and ' if delta_years != '' and delta_months != '' else ''

            references[ job ][ reference ][ 'delta' ] = f"{ delta_years }{ connection }{ delta_months }"

    references_by_job = {
        'Municipal Hospital, Dr. Hector M. Cura' : references[ 'h_m_dr_hector_cura' ],
        'Globant'                                : references[ 'globant' ],
        'Xappia'                                 : references[ 'xappia' ] ,
        'GlobalHitss'                            : references[ 'global_hitss' ],
        '123seguro'                              : references[ '123seguro' ],
    }

    return references_by_job

if __name__ == '__main__':
    print( f'Jobs: { get_jobs() }' )
    print( f'References by job: { get_references() }' )
