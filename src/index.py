from flask import Flask, render_template  # , send_file

from src.templates.education import get_institutions_data
from src.templates.experience import get_jobs, get_references
from src.templates.languages import get_languages_data
from src.templates.presentation import get_about_me_data, get_date, get_ide_data, get_me_data
from src.templates.skills import get_skills_data

app = Flask(__name__)


@app.route( '/' )
def index():
    return render_template( 'index.html' )


@app.route( '/presentation' )
def presentation():
    return render_template( 'presentation.html', ide_data=get_ide_data(), me=get_me_data(), about_me=get_about_me_data() )


@app.route( '/experience' )
def experience():
    return render_template( 'experience.html', jobs=get_jobs(), references=get_references() )


@app.route( '/skills' )
def skills():
    return render_template( 'skills.html', skills=get_skills_data() )


@app.route( '/languages' )
def languages():
    return render_template( 'languages.html', languages = get_languages_data() )


@app.route( '/education' )
def education():
    return render_template( 'education.html', institutions=get_institutions_data() )


# def example_send_image(): #** Only for reference if later I need to send a file ( e.g. image ) to an html
#     return send_file( 'templates/images/profile_foto_rounded.png' )

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
