from django.shortcuts import render, render_to_response
from website.models.project import *

def home(request, context={}):
    context['title'] = "Web solutions for CMS, applications, and DevOps"
    context['meta_description'] = 'OMBU designs and builds the web’s best technology. Our clients come to us for three solution areas: content management, business applications, and DevOps.'
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
    context['title'] = "Case studies and project profiles for our web technology solutions"
    context['meta_description'] = 'OMBU’s portfolio of web technology case studies, project profiles, and clients.'
    return render(request, 'work.html', context)

def services(request, context={}):
    context['title'] = "Content Management, business applications, and DevOps"
    context['meta_description'] = 'OMBU designs and builds technology for visionaries.  We specialize in content management, business applications, and DevOps.'
    context['services'] = [
        { 'title': 'Content Management' },
        { 'title': 'Business Applications' },
        { 'title': 'Cloud Infrastructure' },
    ]
    return render(request, 'services.html', context)

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions, consultations, and RFPs"
    context['meta_description'] = 'Get in touch with OMBU.'
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
    context['project_next'] = kaufmanhall
    return render(request, 'project.html', context)

def project_kaufmanhall(request, context={}):
    context.update(kaufmanhall)
    context['project_prev'] = occ
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
    context['title'] = "Case study for Northwest Power Pool’s learning management system"
    context['meta_description'] = 'NWPP came to OMBU with a simple vision: Make federally-mandated power safety training easy and fun via an engaging video learning platform.'
    context['banner_image'] = "website/images/case-studies/nwpp/hero-tinted@2x.jpg"
    context['banner_title'] = "Modernized Power Utility Training"
    context['banner_subtitle']  = "Learning Management System"
    context['banner_position'] = '20% 40%'
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Northwest PowerPool (NWPP)</span> brings together 32 power utilities in eight US states and two Canadian provinces. OMBU designed a powerful centralized training platform so NWPP could help its member utilities keep up-to-date on mandated certifications and the latest trends, meaning greater safety, more engagement, and more benefit to the whole membership base and their customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/nwpp/testimonial-logo.png"
    context['testimonial_quote'] = "“Partnering with OMBU on this evolution of our platform was one of the best decisions I’ve ever made.”"
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
        'skills': ["User Experience Design", "Python Application Development", "AWS DevOps", "Product Roadmap Planning"],
    }
    context['visionary'] = {
        'body': '<p>NWPP came to us with a simple vision: <strong>Make federally-mandated power safety training easy and fun via an engaging video learning platform</strong>, so that employees of their member utilities would complete more trainings, engage more with the training material for better results, and ultimately create a safer and more productive world of power.</p><p>NWPP has trainers and video production talent in-house, so they wanted a technology partner who could come up with a learning system that would be a great platform for their training.</p>',
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
        'body': '<p>We built a modern, fun training platform targeted specifically for training utility workers, with integrated videos and interactive quizzes.</p><p>Powering this platform, we built a powerful yet easy-to-use Learning Management System (LMS) that lets the NWPP content team quickly put together new courses for their members in minutes.</p><p>Things like 3D models, skilled trainers, and fun easter eggs like blooper reels and jokes make the whole experience engaging</p><p>This platform integrates directly with industry-standard data systems, like the LRS/XAPI datastore and exports for federal compliance systems.</p><p>Ultimately, the most important feature is the fun and informative training materials that mean our client can increase education in an industry where knowledge and safety are critical.</p>',
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
            'background': 'website/images/case-studies/nwpp/innov-slide-01@2x.png',
            'text': 'NWPP can drag-and-drop any assortment of videos, documentation, and quizzes together to quickly and easily create courses for utility workers to&nbsp;take.',
            'action_text': '',
        },
        {
            'title': 'Powerful Digital Asset Management',
            'background': 'website/images/case-studies/nwpp/innov-slide-02@2x.png',
            'text': 'All media assets, such as videos, documents, and images are stored in a central asset library. Videos integrate directly into the design and aesthetic of the site, a collaboration between NWPP’s production team and&nbsp;OMBU.',
            'action_text': '',
        },
        {
            'title': 'High-Availability DevOps',
            'background': 'website/images/case-studies/nwpp/innov-slide-03@2x.png',
            'text': 'Because the LMS is a business critical application, it needed to be online at all times. To accomplish this, we designed a high-availability hosting system that keeps copies of the application in two datacenters. The system monitors for connectivity problems and automatically redirects traffic to the healthier data&nbsp;center.',
            'action_text': '',
        },
        {
            'title': 'Self-Service Team Management Panel',
            'background': 'website/images/case-studies/nwpp/innov-slide-04@2x.png',
            'text': 'To ensure strong adoption, we designed a system that decentralizes the task of managing utility teams and their training. NWPP can designate training coordinators at their member utilities, who then have tools to invite and monitor a handful to hundreds of individual operators as they progress through their&nbsp;training.',
            'action_text': '',
        },
        {
            'title': 'xAPI Integration',
            'background': 'website/images/case-studies/nwpp/innov-slide-05@2x.png',
            'text': 'We built one of the first learning management systems featuring native real-time integration with a learning record store (LRS) using the emerging open standard experience API (xAPI, also called Tin Can). With the LRS data, NWPP can track every member’s progress, test results, and completion data, as well as see trends across all learners or insights about individual&nbsp;lessons.',
            'action_text': '',
        },
    ]
    context['outcomes'] = [
        { 'title': '0.84<abbr title="seconds">s</abbr>', 'summary': 'Page loads' },
        { 'title': '99<sup>%</sup>', 'summary': 'Training completion' },
        { 'title': '23', 'summary': 'Fewer accidents per year'},
        { 'title': '4 <abbr title="minutes">min</abbr>', 'summary': 'New client onboarding' },
    ]
    context['outcome_conclusion'] = '<p>Galaxies encyclopaedia galactica, cosmos at the edge of forever the sky calls to us from which we spring Rig Veda Euclid made in the interiors of collapsing stars consciousness.</p>'
    context['cta_text'] = '<span class=\"footer--cta-intro--phrase\">We helped Northwest PowerPool</span> <span class=\"footer--cta-intro--phrase\">modernize their power utility training.</span> <strong>What can we modernize for&nbsp;you?</strong>'
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
                OMBU designed and implemented a website backed by a enterprise content management system (CMS) that 
                empowers NAVEX Global to 
                personally engage customers across their global markets.  Marketing teams are able to launch a rich 
                custom landing pages for new products and campaigns in minutes, with no IT involvement, allowing them to 
                iterate, test and optimize at breakthrough speeds. The campaigns support system integrations that allow
                marketing teams to track omni-channel campaign performance in Marketo and Salesforce. 
            </p>
            <p>
                The website features a resource center designed to position NAVEX as the global thought leader in
                ethics and compliance. The resource center publishes reports, guides, white papers, webinars and videos
                and is a key conversion point for new business, deeply integrated with Marketo's progressive 
                enhancement to intelligently and automatically grow lead&nbsp;profiles.
            </p>
            <p>
                While building the new website NAVEX had ambitious plans to expand to international markets, so we built 
                a backend with translation, URL and SEO functions to support any number of locales on day one. As NAVEX
                started opening offices in new markets, the website was ready to keep up and empower the local teams
                not only to translate content, but tailor the website experience and campaigns to local products and
                market conditions.
            </p>
        ''',
    }
    context['innovations'] = [
        {
            'title': 'Page Builder',
            'background': 'website/images/case-studies/navex/innov-slide-01@2x.png',
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
            'background': 'website/images/case-studies/navex/innov-slide-02@2x.png',
            'text': '''
                NAVEX Global has customers in over 200 countries, so we built powerful localization into the core of
                their content management system. NAVEX's  team can quickly launch locales, clone 
                pages between locales and translate any site content. For visitors, the experience is seamless, as the 
                site gently guides users to their relevant content.
            ''',

            'action_text': '',
        },
        {
            'title': 'Marketo Marketing Automation',
            'background': 'website/images/case-studies/navex/innov-slide-04@2x.png',
            'text': '''
                We built custom integration with the Marketo marketing automation platform at the core of NAVEX's
                website to empower their marketing teams to reach new new leads, gather insights about visitors and
                content performance, and run omni-channel campaigns. Using our solution, marketers can embed custom 
                Marketo forms on landing pages, without technical help, allowing them to launch campaigns in minutes.'
            ''',

            'action_text': '',
        },
        {
            'title': 'AWS infrastructure',
            'background': 'website/images/case-studies/navex/innov-slide-05@2x.png',
            'text': '''
                NAVEX Global website get's global traffic at large scale. When NAVEX is in the news or one of their
                resource center pieces goes viral, the site sees quick massive spikes in traffic. OMBU designed the
                CMS to leverage the best cloud technology available, such as load-balancing, auto-scaling, cross-region
                replication, and content delivery networks to make sure the site remains fast and available in under
                any condition.
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
    context['title'] = "Case study for Saturday Academy’s class registration system"
    context['meta_description'] = 'OMBU implemented a rich CRM for Saturday Academy to serve as the repository of data about families, classes, registrations, and more, built on Salesforce.'
    context['banner_image'] = "website/images/case-studies/sa/hero-tinted@2x.jpg"
    context['banner_title'] = "Engaging the Next Generation of Scientists, Engineers, and Artists"
    context['banner_subtitle'] = "Class Registration System"
    context['banner_position'] = '50% 30%'
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Saturday Academy</span> strives to engage all motivated young people in hands-on, in-depth learning by connecting them to community experts as educators and mentors by offering over 850 STEAM-curriculum classes per year. But registration was cumbersome for parents and data collection was poor and incomplete.</p><p>OMBU conducted an organization-wide survey of processes, workflows and technology usage and designed and built a nonprofit Salesforce CRM and integrated website that enables families to register to classes and engage with mentors, funneling data in real time into Salesforce for instant reporting and analysis. This IT revision transformed how Saturday Academy engages with its customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/sa/testimonial-logo.png"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/sa/intro@2x.png',
            'alt': 'A screenshot of a Saturday Academy course detail page',
            'browser' : {
                'url' : 'saturdayacademy.org',
            },
        },
        'skills': ["Technology Strategy", "User Experience Design", "Visual Design", "Salesforce CRM Development", "Drupal Application Development", "AWS Design & Implementation"],
    }
    context['visionary'] = {
        'body': '<p>Founded in 1983, Saturday Academy offers over 850 classes and camps per year and over 100 internships for students, with focus on STEAM education and an emphasis on engaging underprivileged students by offering over $70k per year in financial aid.</p><p>Saturday Academy’s unique model is to partner with community subject experts as teachers and mentors, such as practicing doctors, working scientists, and professional actors in the Portland metropolitan area and around Oregon.</p><p>Despite their growth and technology focus, Saturday Academy had been limping along with an old and creaky homegrown Access database and registration process that involved printouts and laborious manual staff interaction for every registration and application.</p><p>The vision: Saturday Academy needed a database of students and their families with a real-time integrated web registration system, so families can self-serve and SA can gain insights from data in real-time.</p>',
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
        'body': '<p>OMBU implemented a rich CRM to serve as the canonical repository of data about families, classes, registrations, internships, and donors, built on Salesforce. By building on top of Salesforce, we were able to provide Saturday Academy with a leading CRM database platform, including using add-ons such as the Nonprofit Success Pack (NPSP) and data management tools. Additionally, Saturday Academy benefits from the knowledge and expertise of the huge number of other nonprofits who use Salesforce to run their organizations.</p><p>To reach parents, students, instructors, and mentors, we designed and built a fun, easy-to-use Content Management website. Parents can set up their household information online, and register their children for any of Saturday Academy’s many classes quickly and easily, and even be granted auto-calculated financial aid to help make the classes accessible to all.</p><p>Saturday Academy’s unique internship program, Apprenticeships in Science and Engineering (ASE), pairs teens with industry mentors for a summer of on-the-job learning. Hundreds of motivated students apply for the program, so we designed a process that makes it easy to apply, as well as a portal for the mentors to rank applicants and a system for final approval and communication with selected interns.</p><p>While we’re proud of transforming Saturday Academy’s online presence and making everything smooth and easy for parents and students, the most transformative part of the solution we built for Saturday Academy is the real-time data flow and the accompanying reporting within the CRM. Leadership can now ask questions and gain insights instantly, such as seeing breakdown of financial aid relative to family demographics, intelligence that previously would either have days of data processing or have been entirely impossible.</p>',
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
            'title': 'Real-Time Class Registration System',
            'background': 'website/images/case-studies/sa/innov-slide-01@2x.png',
            'text': 'A live class catalog syncs between the website and the Salesforce datastore, so parents and students can see Saturday Academy’s classes and seating availability in real-time. When it’s time to register, a parent can apply for and instantly receive financial aid, calculated based on their adjusted gross income (AGI) using a formula Saturday Academy can adjust over time. Payment is processed immediately through Stripe’s API and is recorded within&nbsp;Salesforce.',
            'action_text': '',
        },
        {
            'title': 'Salesforce Business Datastore and Intelligence',
            'background': 'website/images/case-studies/sa/innov-slide-02@2x.png',
            'text': 'Since all registrations and interactions on the Saturday Academy speak to Salesforce in real-time via REST API, this means both systems are always in sync. Real-time data, with customized data structures optimized for their business, means that Saturday Academy can run reports in real-time and gain insights in areas such as financials, demographics, and success&nbsp;metrics.',
            'action_text': '',
        },
        {
            'title': 'Data Migration',
            'background': 'website/images/case-studies/sa/innov-slide-03@2x.png',
            'text': 'Saturday Academy had over a decade of records stored in disparate homegrown Access databases and spreadsheets prior to launching the new system. For archival and reporting purposes we built an automated migration system to bring those old records into the new system. On launch day, we were able to automatically enable 10,592 household accounts, allowing existing parents and students to immediately log in and see their legacy&nbsp;information.',
            'action_text': '',
        },
        {
            'title': 'Content Management',
            'background': 'website/images/case-studies/sa/innov-slide-04@2x.png',
            'text': 'Saturday Academy works with creative and inquisitive families, so we designed and built a website that communicates that quirky, intelligent brand while maintaining an easy-to-use, mobile-responsive interface. Powerful content management gives Saturday Academy’s marketing team the ability to quickly customize layouts with new page elements as their content needs change and the organization&nbsp;grows.',
            'action_text': '',
        },
    ]
    context['outcomes'] = [
        { 'title': 'Live', 'summary': 'Operational data for the first time' },
        { 'title': '0', 'summary': 'Registrations printed on paper' },
        { 'title': 'Realtime', 'summary': 'Class registration with instant financial aid calculation', 'titleclass': ' rings--title--subtle' },
        { 'title': '23<sup>%<sup>', 'summary': 'Increased engagement on mobile' },
        { 'title': '3,184', 'summary': 'Brand new registrants' },
    ]
    context['outcome_conclusion'] = '<p>Galaxies encyclopaedia galactica, cosmos at the edge of forever the sky calls to us from which we spring Rig Veda Euclid made in the interiors of collapsing stars consciousness.</p>'
    context['cta_text'] = '<span class=\"footer--cta-intro--phrase\">We helped Saturday Academy</span> <span class=\"footer--cta-intro--phrase\">modernize their class registration system.</span> <strong>What can we modernize for&nbsp;you?</strong>'
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def browserconfig(request):
    response = render_to_response('browserconfig.xml')
    response['Content-Type'] = 'application/xml;'
    return response
