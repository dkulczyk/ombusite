from django.conf import settings
from django.shortcuts import render, render_to_response, reverse
from website.models.project import *

def home(request, context={}):
    context['title'] = "Web solutions for CMS, applications, and DevOps"
    context['meta_description'] = 'OMBU designs and builds the web’s best technology. Our clients come to us for three solution areas: content management, custom applications, and DevOps.'
    return render(request, 'home.html', context)

def about(request, context={}):
    context['title'] = "The web technology agency for visionaries"
    context['meta_description'] = 'OMBU designs and builds the web’s best technology. We believe that technology is changing the world, and our job is to help companies harness that power.'
    return render(request, 'about.html', context)

def kitchensink(request, context={}):
    context['title'] = "Kitchen Sink"
    context['meta_description'] = 'Design patterns for all rich text elements.'
    return render(request, 'kitchen_sink.html', context)

def work(request, context={}):
    context['title'] = "Case studies and project profiles from OMBU"
    context['meta_description'] = 'OMBU’s portfolio of web technology case studies, project profiles, and clients.'
    return render(request, 'work.html', context)

def services(request, context={}):
    context['title'] = "Content Management, custom applications, and DevOps"
    context['meta_description'] = 'OMBU designs and builds technology for visionaries.  We specialize in content management, custom applications, and DevOps.'
    context['services'] = [
        { 'title': 'Content Management' },
        { 'title': 'Custom Applications' },
        { 'title': 'Cloud Infrastructure' },
    ]
    return render(request, 'services.html', context)

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions and RFPs"
    context['meta_description'] = "Get in touch with OMBU and let's talk about your vision."
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Web design and development careers in Portland, Oregon"
    context['meta_description'] = 'Come work with OMBU!  Become a part of a tight, functional team that consistently ships innovative products to a growing portfolio of happy clients.'
    return render(request, 'careers.html', context)

def pagenotfound(request, context={}):
    context['title'] = "Page not found"
    context['meta_description'] = 'Page not found.'
    return render(request, '404.html', context)

# Work / Projects
# ##############################################################################

def project_occ(request, context={}):
    context.update(occ)
    context['project_prev'] = smithsonian
    context['project_next'] = energytrust
    return render(request, 'project.html', context)

def project_energytrust(request, context={}):
    context.update(energytrust)
    context['project_prev'] = occ
    context['project_next'] = kaufmanhall
    return render(request, 'project.html', context)

def project_kaufmanhall(request, context={}):
    context.update(kaufmanhall)
    context['project_prev'] = energytrust
    context['project_next'] = nwcouncilrtf
    return render(request, 'project.html', context)

def project_nwcouncilrtf(request, context={}):
    context.update(nwcouncilrtf)
    context['project_prev'] = kaufmanhall
    context['project_next'] = metro
    return render(request, 'project.html', context)

def project_metro(request, context={}):
    context.update(metro)
    context['project_prev'] = nwcouncilrtf
    context['project_next'] = metropcmt
    return render(request, 'project.html', context)

def project_metropcmt(request, context={}):
    context.update(metropcmt)
    context['project_prev'] = metro
    context['project_next'] = stand
    return render(request, 'project.html', context)

def project_stand(request, context={}):
    context.update(stand)
    context['project_prev'] = metropcmt
    context['project_next'] = compliancenext
    return render(request, 'project.html', context)

def project_compliancenext(request, context={}):
    context.update(compliancenext)
    context['project_prev'] = stand
    context['project_next'] = smithsonian
    return render(request, 'project.html', context)

def project_smithsonian(request, context={}):
    context.update(smithsonian)
    context['project_prev'] = compliancenext
    context['project_next'] = occ
    return render(request, 'project.html', context)

# def project_seri(request, context={}):
#     context.update(seri)
#     return render(request, 'project.html', context)

# def project_autodesk(request, context={}):
#     context.update(autodesk)
#     return render(request, 'project.html', context)

# def project_uo(request, context={}):
#     context.update(uo)
#     return render(request, 'project.html', context)

# Work / Case Studies
# ##############################################################################

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Learning management system (LMS) case study for NWPP"
    context['meta_description'] = "NWPP and OMBU created a modern learning management system (LMS) " \
                                  "to transform energy utility online training."
    context['banner_image'] = "website/images/case-studies/nwpp/hero-tinted@2x.jpg"
    context['banner_title'] = "Modernized Power Utility Training"
    context['banner_subtitle']  = "Learning Management System (LMS)"
    context['banner_position'] = '20% 40%'
    context['intro_text'] = """
    <p>
        <span class="cs-intro--emphasis">Northwest PowerPool (NWPP)</span> partnered with us to design and implement
        a learning platform that modernized electric utility training delivery. The new platform was so much easier to
        maintain. More importantly, it allowed NWPP to use modern learning tools which drastically improved
        trainee engagement and compliance with federally regulated training&nbsp;requirement.
     </p>
    """
    context['testimonial_image'] = "website/images/case-studies/nwpp/testimonial-logo.png"
    context['testimonial_image_alt'] = "Company logo for Northwest PowerPool"
    context['testimonial_quote'] = "“Partnering with OMBU on this evolution of our platform " \
                                   "was one of the best decisions I’ve ever made.”"
    context['testimonial_attribution_name'] = "David P."
    context['testimonial_attribution_title'] = "Project Lead, NWPP"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/nwpp/intro@2x.png',
            'alt': 'A screenshot of a source.training course video activity page',
            'browser' : {
                'url' : 'source.training',
            },
        },
        'skills': [
            "User Experience Design", "Python Application Development",
            "AWS Infrastructure", "xAPI"
        ],
    }
    context['visionary'] = {
        'body': """
        <p>
            Northwest PowerPool (NWPP)</span> brings together 32 power utilities in
            eight US states and two Canadian provinces. One of their missions is to deliver training to
            electric power operators to increase power grid safety, help with new technology adoption, and meet
            federally regulated training requirements.
        </p>
        <p>
            For years, NWPP suffered with an off-the-shelf LMS solution to deliver training that could not keep
            up with NWPP’s pace of innovation. The platform was slow and tedious for learners and administrators, and
            could not support the modern training methods that NWPP was pioneering.
        </p>
        <p>
            NWPP knew that if they could could control the experience and functionality of a new platform, they would
            drastically improve the quality of training, drive engagement and help member utilities achieve compliance. So NWPP
            came to us with a simple vision: <strong>help us design, implement and roll out a learning management
            system that will transform how we work</strong>.
        </p>
        """,

        'image': {
            'src' : 'website/images/case-studies/nwpp/visionary@2x.png',
            'alt': 'A screenshot of the source.training course library page',
            'browser' : {
                'url' : 'source.training',
            },
        },
        # 'stat': {
        #     'number': '32',
        #     'label': 'Member<br>Utilities',
        #     'summary': 'Why member utilities are important and how they benefit directly or indirectly from modernized power utility training motes of rock and gas the ash of cosmic stellar extraterrestrial alchemy.',
        # },
    }
    context['solution'] = {
        'body': """
            <p>
                We built a modern and engaging training platform targeted specifically for training electric
                utility workers. The easy-to-use Learning Management System (LMS) allows content creators to quickly
                put together new courses and activities with video, interactive quizzes, scoring and reporting.
            </p>
            <p>
                This platform integrates with modern providers of digital media, like YouTube, Vimeo, Soundcloud and
                Sketchfab, with a Department of Energy system for reporting, and with a Learning Record Store (LRS)
                through the Experience API (xAPI).
            </p>
            <p>
                Ultimately, the key feature of OMBU’s solution is the powerful and pleasant user experience
                that makes content creation and management tasks fun and easy, and stays out of the way during
                training, shifting all focus to the learning experience, driving high engagement in an industry
                where knowledge and safety are critical.
            </p>
        """,

        'image': {
            'src' : 'website/images/case-studies/nwpp/solution@2x.png',
            'alt': 'A screenshot of a source.training course challenge question page',
            'browser' : {
                'url' : 'source.training',
            },
        },
        # 'stat': {
        #     'number': '≥1200',
        #     'label': 'Utility<br>Operators<br>Served',
        #     'summary': 'Why utility operators are important and how they benefit directly or indirectly from modernized power utility training motes of rock and gas the ash of cosmic stellar alchemy.',
        # }
    }
    context['innovations'] = [
        {
            'title': 'Drag & Drop Course Builder',
            'background': 'website/images/case-studies/nwpp/innov-slide-01@2x.jpg',
            'text': 'Content creators can create courses easily using drag-and-drop to organize activity flow, '
                    'upload videos and setup quizzes.',
            'action_text': '',
        },
        {
            'title': 'Digital Asset Management',
            'background': 'website/images/case-studies/nwpp/innov-slide-02@2x.jpg',
            'text': "Media assets like videos, documents and images are organized in a central asset library, so "
                    "content creators can easily find assets to use in their activities and LMS administrators "
                    "can track what’s being used&nbsp;where.",
            'action_text': '',
        },
        {
            'title': 'Self-Service Teams',
            'background': 'website/images/case-studies/nwpp/innov-slide-04@2x.jpg',
            'text': "Member organizations are teams in the LMS with self-management functions. This allows NWPP to "
                    "securely delegate tasks like user invitations, status updates, role assignment, "
                    "license management, etc.",
            'action_text': '',
        },
        {
            'title': 'High-Availability AWS infrastructure',
            'background': 'website/images/case-studies/nwpp/innov-slide-03@2x.jpg',
            'text': "The LMS is a business-critical application used around the clock, so we implemented a "
                    "multi data center hosting solution that is cost effective and scales during high usage periods.",
            'action_text': '',
        },
        {
            'title': 'xAPI / Tin Can',
            'background': 'website/images/case-studies/nwpp/innov-slide-05@2x.jpg',
            'text': "We built one of the first learning management systems with native real-time integration "
                    "with a learning record store (LRS) that supports xAPI (also called Tin Can), so"
                    "NWPP can follow member’s engagement and progress, and access live analytics that help "
                    "them improve and evolve training.",
            'action_text': '',
        },
    ]
    # context['outcomes'] = [
    #     { 'title': '5<abbr title="seconds">x</abbr>', 'summary': 'Faster page loads' },
    #     { 'title': '5 <abbr title="minutes">min</abbr>', 'summary': 'Client onboarding' },
    #   { 'title': '32', 'summary': 'organizations on board' },
    #
    # ]
    # context['outcome_conclusion'] = """
    # <p>
    #     Galaxies encyclopaedia galactica, cosmos at the edge of forever the sky calls to us from which we
    #     spring Rig Veda Euclid made in the interiors of collapsing stars consciousness.
    #  </p>'
    # """
    context['cta_text'] = """
        <span class="footer--cta-intro--phrase">We helped Northwest PowerPool</span>
        <span class="footer--cta-intro--phrase">modernize power utility training.</span>
        <strong>What can we do for you?</strong>'
    """
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def casestudy_navex(request, context={}):
    context['client'] = "NAVEX Global"
    context['title'] = "CMS case study for NAVEX Global"
    context['meta_description'] = 'Facing explosive growth, NAVEX Global hired OMBU implement the digital content management tools that would establish them as the industry leader.'
    context['banner_image'] = "website/images/case-studies/navex/hero-tinted@2x.jpg"
    context['banner_title'] = "Content Management for the Global Ethics Leader"
    context['banner_position'] = '85% 40%'
    context['intro_text'] = '''
    <p>
        <span class="cs-intro--emphasis">NAVEX Global</span> was formed in 2012 to become the leader in the emerging
        field of Ethics & Compliance. They engaged OMBU to help implement content marketing tools that would support and
        accelerate their rapid growth and global expansion.
    </p>
    '''
    context['testimonial_image'] = "website/images/case-studies/navex/testimonial-logo.png"
    context['testimonial_image_alt'] = "Company logo for NAVEX Global"
    # context['intro_testimonial_quote'] = "“Based on projects, the current uplift in high-value forms from the new pages will result in $4.6M in pipe and $1.4M in closed won business in the next 12 months!”"
    # context['intro_testimonial_attribution_name'] = "Hillary E."
    # context['intro_testimonial_attribution_title'] = "Demand Generation Manager, NAVEX Global"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/navex/intro@2x.png',
            'alt': 'A screenshot of the NAVEX Global home page',
            'browser' : {
                'url' : 'navexglobal.com',
            },
        },
        'skills': [
            "Technology Strategy", "Enterprise Content Management", "Drupal CMS Development", "Marketo Integration",
            "AWS Migration", "Infrastructure Management"
        ],
    }
    context['visionary'] = {
        'body': '''
            <p>
                When NAVEX expansion efforts started to bear results, their website and content management system (CMS)
                soon got in the way. The existing website and content management tools had not been designed to support
                change and growth. Creating pages and campaigns to support new initiative took too long and the site
                lacked the integrations necessary to track engagement and success metrics. Additionally, the website
                started feel slow and unreliable. The business teams had a vision for the tools they would need to
                engage with new customers today and tomorrow.
            </p>
        ''',
        'image': {
            'src' : 'website/images/case-studies/navex/visionary@2x.png',
            'alt': 'A screenshot of the NAVEX Global blog',
            'browser' : {
                'url' : 'navexglobal.com/blog',
            },
        },
    }
    context['solution'] = {
        'body': '''
            <p>
                OMBU designed and implemented a website backed by an enterprise content management system (CMS) that
                empowers NAVEX Global to
                personally engage customers across their global markets.  Marketing teams are able to launch a rich
                custom landing pages for new products and campaigns in minutes, with no IT involvement, allowing them to
                iterate, test and optimize at breakthrough speeds. The campaigns support system integrations that allow
                marketing teams to track omni-channel campaign performance in Marketo and Salesforce.
            </p>
            <p>
                The website features a resource center designed to position NAVEX as the global thought leader in
                ethics and compliance. The resource center publishes reports, guides, white papers, webinars and videos
                and is a key conversion point for new business, deeply integrated with Marketo’s progressive
                enhancement to intelligently and automatically grow lead&nbsp;profiles.
            </p>
            <p>
                While building the new website, NAVEX had ambitious plans to expand to international markets, so we built
                a backend with translation, URL and SEO functions to support any number of locales on day one. As NAVEX
                started opening offices in new markets, the website was ready to keep up and empower the local teams
                not only to translate content, but tailor the website experience and campaigns to local products and
                market conditions.
            </p>
        ''',
        'image': {
            'src' : 'website/images/case-studies/navex/solution@2x.png',
            'alt': 'A screenshot of a NAVEX Global resource page.',
            'browser' : {
                'url' : 'navexglobal.com',
            },
        },
    }
    context['innovations'] = [
        {
            'title': 'Page Builder',
            'background': 'website/images/case-studies/navex/innov-slide-01@2x.jpg',
            'text': '''
                A page builder feature enables marketers to assemble custom landing pages for new products and campaigns
                without technical help. The page builder has blocks for text, callouts, media and custom campaign forms
                that can be sized and arranged and for the best layout for every situation and enable iterative
                optimization.
            ''',
            'action_text': '',
        },
        {
            'title': 'Localization',
            'background': 'website/images/case-studies/navex/innov-slide-02@2x.jpg',
            'text': '''
                NAVEX Global has customers in over 200 countries, so we built powerful localization into the core of
                their content management system. NAVEX’s  team can quickly launch locales, clone
                pages between locales and translate any site content. For visitors, the experience is seamless, as the
                site gently guides users to their relevant&nbsp;content.
            ''',

            'action_text': '',
        },
        {
            'title': 'Marketo Marketing Automation',
            'background': 'website/images/case-studies/navex/innov-slide-04@2x.jpg',
            'text': '''
                We built custom integration with the Marketo marketing automation platform at the core of NAVEX’s
                website to empower their marketing teams to reach new new leads, gather insights about visitors and
                content performance, and run omni-channel campaigns. Using our solution, marketers can embed custom
                Marketo forms on landing pages, without technical help, allowing them to launch campaigns in&nbsp;minutes.
            ''',

            'action_text': '',
        },
        {
            'title': 'AWS infrastructure',
            'background': 'website/images/case-studies/navex/innov-slide-05@2x.jpg',
            'text': '''
                NAVEX Global’s website gets global traffic at large scale. When NAVEX is in the news or one of their
                resource center pieces goes viral, the site sees quick massive spikes in traffic. OMBU designed the
                CMS to leverage the best cloud technology available, such as load-balancing, auto-scaling, cross-region
                replication, and content delivery networks to make sure the site remains fast and available under
                any&nbsp;conditions.
            ''',
            'action_text': '',
        },
    ]
    # context['outcomes'] = [
    #     { 'title': '< 4 <abbr title="minutes">min</abbr>', 'summary': 'Landing page launch' },
    #     { 'title': '224', 'summary': 'White papers, eBooks, webinars' },
    #     { 'title': '448', 'summary': 'Expert blog posts' },
    #     { 'title': '2', 'summary': 'Top competitors acquired' },
    #     { 'title': '$4.6M', 'summary': 'Projected increase in pipeline due to launch' },
    #     { 'title': '$1.4M', 'summary': 'Projected increase in closed won business duet to launch' },
    # ]
    # context['outcome_conclusion'] = '<p>Galaxies encyclopaedia galactica, cosmos at the edge of forever the sky calls to us from which we spring Rig Veda Euclid made in the interiors of collapsing stars consciousness.</p>'
    context['cta_text'] = '<span class=\"footer--cta-intro--phrase\">We helped NAVEX Global</span> <span class=\"footer--cta-intro--phrase\">modernize their website content.</span> <strong>What can we modernize for&nbsp;you?</strong>'
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Salesforce CRM case study with a class registration system"
    context['meta_description'] = 'OMBU implemented an website and integrated Salesforce CRM for Saturday Academy.'
    context['banner_image'] = "website/images/case-studies/sa/hero-tinted@2x.jpg"
    context['banner_title'] = "Engaging the Next Generation of Scientists, Engineers, and Artists"
    context['banner_subtitle'] = "CRM, Website and a Live Class Registration System"
    context['banner_position'] = '50% 30%'
    context['intro_text'] = """
    <p>
        <span class=\"cs-intro--emphasis\">Saturday Academy</span> strives to engage all motivated young people in
        hands-on, in-depth learning by connecting them to community experts as educators and mentors by offering over
        850 STEAM-curriculum classes per year. But young students and their families relied on paper class catalogs
        and the organization lacked tools for registration and outcome tracking.
    </p>
    <p>
        After conducting an organization-wide survey of processes and technology, OMBU designed and built
        for Saturday Academy an integrated solution based on a new website and a nonprofit Salesforce CRM that enables
        families to register to classes and engage with mentors, and gives Saturday Academy real time access to
        registration data and outcomes, transforming how Saturday Academy engages with its customers.
    </p>
    """
    context['testimonial_image'] = "website/images/case-studies/sa/testimonial-logo.png"
    context['testimonial_image_alt'] = "Organization logo for Saturday Academy"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/sa/intro@2x.png',
            'alt': 'A screenshot of a Saturday Academy course detail page',
            'browser' : {
                'url' : 'saturdayacademy.org',
            },
        },
        'skills': [
            "Technology Strategy", "Design", "Salesforce",
            "Drupal", "Data migration", "AWS infrastructure"
        ]
    }
    context['visionary'] = {
        'body': """
            <p>
                Founded in 1983, Saturday Academy offers over 850 classes and camps and over 100 internships
                for students, with focus on STEAM education and an emphasis on engaging underprivileged students.
                Their vision is that all interested, pre-college students in our region will have the opportunity
                to interact with community experts and experience professional environments in ways that assist
                them in developing intellectually and preparing for rewarding careers.
            </p>
            <p>
                But their technology infrastructure kept getting in the way. An old Wordpress website
                was not just hard to manage, but offered families no way to discover and register for the exciting
                classes happening around them. So Saturday Academy relied on hardcoded web forms that
                fed data directly into an Access database. Over time, this database was overwhelmed with duplicate and
                erroneous data, with no way for Saturday Academy to extract reliable business intelligence.
            </p>
            <p>
                Saturday Academy’s staff knew there was better technology out there, but they needed a partner who
                could help them package it into a custom solution that was affordable and sustainable for them. And
                they needed a data expert who could sanitize and migrate their legacy data for a fresh restart.
            </p>
        """,
        'image': {
            'src' : 'website/images/case-studies/sa/visionary@2x.png',
            'alt': 'A screenshot of a Saturday Academy class registration page',
            'browser' : {
                'url' : 'saturdayacademy.org',
            },
        },
        # 'stat': {
        #     'number': '5200+',
        #     'label': 'Registrations<br>per Year',
        #     'summary': 'Why this metric is important and how Saturday Academy benefits directly or indirectly from it motes of rock and gas the ash of cosmic extraterrestrial alchemy bearable only through love.',
        # },
    }
    context['solution'] = {
        'body': """
        <p>
            OMBU implemented a nonprofit Salesforce CRM to serve as the data store for all operational data:
            households, students, classes, registrations, internships, and donations. By building on top of
            Salesforce, we were able to provide Saturday Academy with enterprise business intelligence and
            reporting capabilities. We configured the Salesfor Nonprofit Success Pack (NPSP), so Saturday Academy
            could access free licenses through the generous offering fom the Salesforce Foundation.</p>
        <p>
            To reach parents, students, instructors, and mentors, we designed and built a fun,
            easy-to-use website powered by the Drupal Content Management System (CMS). Parents can set up their
            household information online, and register their children for any of Saturday Academy’s many classes
            quickly and easily, and even be granted financial aid automatically to help make the classes accessible.
        </p>
        <p>
            Saturday Academy’s unique internship program, Apprenticeships in Science and Engineering (ASE), pairs
            teens with industry mentors for a summer of on-the-job learning. Hundreds of motivated students apply
            for the program, so we designed a process that makes a multi-step application and screening process
            easy for applicants, and a portal for mentors to review mentors and rank applicants. Finally, the process
            has a step for Saturday Academy staff to complete approval and trigger a series of automated
            emails communication to the selected interns and mentors.
        </p>
        <p>
            While we’re proud of transforming Satturday Academy’s online presence and making everything smooth and
            easy for parents and students, the most transformative part of the solution
            is the real-time data flow between the website and the CRM, and the reporting capabilities that it unleashed
            for Saturday Academy. Leadership can now ask questions and gain insights instantly, such as seeing
            breakdown of financial aid relative to family demographics, intelligence that previously would either
            have days of data processing or have been entirely impossible.
        </p>
        """,
        'image': {
            'src' : 'website/images/case-studies/sa/solution@2x.png',
            'alt': 'A screenshot of a Saturday Academy application review page',
            'browser' : {
                'url' : 'saturdayacademy.org',
            },
        },
        # 'stat' : {
        #     'number': '$70k+',
        #     'label': 'Financial Aid<br>Automatically<br>Granted per Year',
        #     'summary': 'Why this metric is important and how Saturday Academy benefits directly or indirectly from it motes of rock and gas the ash of cosmic extraterrestrial alchemy bearable only through love.',
        # },
    }
    context['innovations'] = [
        {
            'title': 'Real-Time Class Registrations',
            'background': 'website/images/case-studies/sa/innov-slide-01@2x.jpg',
            'text': "A live class catalog syncs between the website and the Salesforce datastore, so parents "
                    "and students can see Saturday Academy’s classes and seating availability in real-time. "
                    "Parents can apply for and instantly receive financial aid, calculated "
                    "based on their adjusted gross income (AGI).",
            'action_text': '',
        },
        {
            'title': 'Salesforce Business Intelligence',
            'background': 'website/images/case-studies/sa/innov-slide-02@2x.jpg',
            'text': "Website interactions and class registration report to Salesforce "
                    "via a REST API, so Saturday Academy "
                    "can run reports in real-time to gain find out how classes are filling up, how finacial aid is "
                    "being distributed, and maintain a suite of live operational reports.",
            'action_text': '',
        },
        {
            'title': 'Data Migration',
            'background': 'website/images/case-studies/sa/innov-slide-03@2x.jpg',
            'text': "We wrote a migration script that processed over a decade’s worth of records from an Access "
                    "database and several spreadsheets, cleaning and consolidating a trove of legacy operational "
                    "data into Salesforce.",
            'action_text': '',
        }
    ]
    context['outcomes'] = [
        { 'title': 'Live', 'summary': 'Operational data for the first time' },
        { 'title': '0', 'summary': 'Paper registrations' },
        { 'title': '0', 'summary': 'Time processing financial aid', 'titleclass': ' rings--title--subtle' },
    ]

    context['cta_text'] = """
          <span class="footer--cta-intro--phrase">We helped Saturday Academy</span>
          <span class="footer--cta-intro--phrase">transform how they engage with families</span>
          <strong>What can we tranform for&nbsp;you?</strong>
    """


    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def browserconfig(request):
    response = render_to_response('browserconfig.xml')
    response['Content-Type'] = 'application/xml;'
    return response

def robots(request):
    sitemap_url = request.build_absolute_uri(reverse('sitemap'))
    response = render_to_response('robots.txt', {'sitemap_url': sitemap_url})
    response['Content-Type'] = 'text/plain'
    return response
