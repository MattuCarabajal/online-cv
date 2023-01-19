// Presentation
function presentation_in() {
    // Get Presentation Section
    var presentation = parent.document.getElementById('Presentation');

    // Set Presentation to be displayed
    presentation.style.transitionDuration = '5s';
    presentation.style.opacity = 1;
}

function presentation_out() {
    // Get Presentation Section
    var presentation = parent.document.getElementById('Presentation');

    // Set Presentation to not be displayed
    presentation.style.transitionDuration = '1s';
    presentation.style.opacity = 0;
}

// Presentation files
function presentation() {
    // Get tab Goals and file Goals
    var tab_goals = document.getElementById( 'Tab_Goals' );
    var goals = document.getElementById('Goals')

    // Set Goals as not viewing file
    tab_goals.classList.remove('bg_emphasis');
    tab_goals.classList.add('bg_not_emphasis');
    goals.setAttribute( 'style', 'display:none !important' );

    // Get tab Presentation and file Presentation
    var tab_presentation = document.getElementById( 'Tab_Presentation' );
    var presentation = document.getElementById('Presentation')

    // Set Presentation as viewing file
    tab_presentation.classList.remove('bg_not_emphasis');
    tab_presentation.classList.add('bg_emphasis');
    presentation.setAttribute( 'style', 'display:block !important' );
}

function goals() {
    // Get tab Presentation and file Presentation
    var tab_presentation = document.getElementById( 'Tab_Presentation' );
    var presentation = document.getElementById('Presentation')

    // Set Presentation as not viewing file
    tab_presentation.classList.remove('bg_emphasis');
    tab_presentation.classList.add('bg_not_emphasis');
    presentation.setAttribute( 'style', 'display:none !important' );

    // Get tab Goals and file Goals
    var tab_goals = document.getElementById( 'Tab_Goals' );
    var goals = document.getElementById('Goals')

    // Set Goals as viewing file
    tab_goals.classList.remove('bg_not_emphasis');
    tab_goals.classList.add('bg_emphasis');
    goals.setAttribute( 'style', 'display:block !important' );
}

function close_tabs() {
    // Get tab Goals and file Goals
    var tab_goals = document.getElementById( 'Tab_Goals' );
    var goals = document.getElementById('Goals')

    // Set Goals as closed
    tab_goals.classList.remove('bg_emphasis');
    tab_goals.classList.add('bg_not_emphasis');
    goals.setAttribute( 'style', 'display:none !important' );

    // Get tab Presentation and file Presentation
    var tab_presentation = document.getElementById( 'Tab_Presentation' );
    var presentation = document.getElementById('Presentation')

    // Set Presentation as closed
    tab_presentation.classList.remove('bg_emphasis');
    tab_presentation.classList.add('bg_not_emphasis');
    presentation.setAttribute( 'style', 'display:none !important' );
}

// Sleep
var slide_time = '3';

function sleep( seconds ){
    var wait_until = new Date().getTime() + seconds * 1000;
    while( new Date().getTime() < wait_until) 
        true;
}

// Menu
function menu_in() {
    // Get page width
    var width = document.documentElement.clientWidth;
    if (width <= '768'){
        var up = 'top: -25% !important';
        var down = 'top: 3% !important';
    }
    else {
        var up = 'top: -10% !important';
        var down = 'top: 7% !important';
    };

    // Get Menu
    menu = document.getElementById('Menu');
    // Set Menu to be displayed
    menu.setAttribute( 'style', 'opacity: 1 !important');
    menu.setAttribute( 'style', down);

    // Get Back Menu
    menu_back = document.getElementById('Menu_back');
    // Set Bach menu to not be displayed
    menu_back.setAttribute( 'style', 'opacity: 0 !important');
    menu_back.setAttribute( 'style', up);
}

function show_menu_back( func ) {
    // Get page width
    var width = document.documentElement.clientWidth;
    if (width <= '768'){
        var up = 'top: -25% !important';
        var down = 'top: 3% !important';
    }
    else {
        var up = 'top: -10% !important';
        var down = 'top: 7% !important';
    };

    // Get Menu
    menu = document.getElementById('Menu');
    // Set Menu to not be displayed
    menu.setAttribute( 'style', 'opacity: 0 !important');
    menu.setAttribute( 'style', up);

    // Get Back Menu
    menu_back = document.getElementById('Menu_back');
    // Set Bach menu to be displayed
    menu_back.setAttribute( 'style', down);

    // Get Back button
    back_button = document.getElementById('Back_button');
    // Set Back button's onclick, to set section out of view when clicked
    back_button.setAttribute('onclick', func);
}

// Experience
function experienceIn() {
    // Set Back menu to be displayed
    show_menu_back('experienceOut()');

    // Set Presentation section out of view
    presentation_out();

    // Get Experience section
    var experience = parent.document.getElementById('Experience');

    // Set Experience section in view
    experience.style.transition = slide_time + 's';
    experience.style.left = '0%';
}

function experienceOut() {
    // Set Menu to be displayed
    menu_in();
    
    // Get Experience section
    var experience = parent.document.getElementById('Experience');
    
    // Set Experience section out of view
    experience.style.transition = slide_time + 's';
    experience.style.left = '-100%';

    // Set Presentation section in view
    presentation_in();
}

// Knowledge and skills
function skillsIn() {
    // Set Back menu to be displayed
    show_menu_back('skillsOut()');

    // Set Presentation section out of view
    presentation_out();

    // Get Skills section
    var skills = parent.document.getElementById('Skills');

    // Set Skills section in view
    skills.style.transition = slide_time + 's';
    skills.style.left = '0%';
}

function skillsOut() {
    // Set Menu to be displayed
    menu_in();
    
    // Get Skills section
    var skills = parent.document.getElementById('Skills');
    
    // Set Skills section out of view
    skills.style.transition = slide_time + 's';
    skills.style.left = '-100%';

    // Set Presentation section in view
    presentation_in();
}

// Education
function educationIn() {
    // Set Back menu to be displayed
    show_menu_back('educationOut()');

    // Set Presentation section out of view
    presentation_out();

    // Get Education section
    var education = parent.document.getElementById('Education');

    // Set Education section in view
    education.style.transition = slide_time + 's';
    education.style.left = '0%';
}

function educationOut() {
    // Set Menu to be displayed
    menu_in();
    
    // Get Education section
    var education = parent.document.getElementById('Education');
    
    // Set Education section out of view
    education.style.transition = slide_time + 's';
    education.style.left = '100%';

    // Set Presentation section in view
    presentation_in();
}

// Languages
function languagesIn() {
    // Set Back menu to be displayed
    show_menu_back('languagesOut()');

    // Set Presentation section out of view
    presentation_out();

    // Get Languages section
    var languages = parent.document.getElementById('Languages');

    // Set Languages section in view
    languages.style.transition = slide_time + 's';
    languages.style.left = '0%';
}

function languagesOut() {
    // Set Menu to be displayed
    menu_in();
    
    // Get Languages section
    var languages = parent.document.getElementById('Languages');

    // Set Languages section out of view
    languages.style.transition = slide_time + 's';
    languages.style.left = '100%';

    // Set Languages section in view
    presentation_in();
}

// References
function show_references( job_id ) {
    // Set references section column width
    // job_references_section = document.getElementsByName( job_id )[ 0 ];
    // job_references_section.style.gridTemplateRows = '25% 75%';

    // Set References in view
    // job_references = document.getElementsByName( job_id )[ 1 ]
    // job_references.style.opacity = 1;

    // Get References button
    job = document.getElementById( job_id );
    job_references_button = job.getElementsByTagName('button')[0];

    // Set References button's onclick, to hide references when clicked
    job_references_button.setAttribute('onclick', "hide_references('" + job_id + "')");
    job_references_button.style.height = "25%";
}

function hide_references( job_id ) {
    // Set references section column width
    // job_references_section = document.getElementsByName( job_id )[ 0 ];
    // job_references_section.style.gridTemplateRows = '100%';

    // Set References out of view
    // job_references = document.getElementsByName( job_id )[ 1 ]
    // job_references.style = 0;

    // Get References button
    job = document.getElementById( job_id );
    job_references_button = job.getElementsByTagName('button')[0];

    // Set References button's onclick, to show references when clicked
    job_references_button.setAttribute('onclick', "show_references('" + job_id + "')");
    job_references_button.style.height = "100%";
}
