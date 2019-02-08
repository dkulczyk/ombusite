from django.shortcuts import render, render_to_response
from django.core import urlresolvers
from website.models.project import *

def home(request, context={}):
    context['title'] = "Web solutions for CMS, applications, and DevOps"
    return render(request, 'home.html', context)

def about(request, context={}):
    context['title'] = "The web technology agency for visionaries"
    return render(request, 'about.html', context)

def kitchensink(request, context={}):
    context['title'] = "Kitchen Sink"
    return render(request, 'kitchen_sink.html', context)

def work(request, context={}):
    context['title'] = "Case studies and project profiles for our web technology solutions"
    return render(request, 'work.html', context)

def services(request, context={}):
    context['title'] = "Content Management, business applications, and DevOps"
    context['services'] = [
        { 'title': 'Content Management', 'summary': 'We make content<br>manageable' },
        { 'title': 'Business Applications', 'summary': 'We make business<br>profitable' },
        { 'title': 'DevOps', 'summary': 'We make systems<br>reliable' },
    ]
    return render(request, 'services.html', context)

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions, consultations, and RFPs"
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Web design and development careers in Portland, Oregon"
    return render(request, 'careers.html', context)

def pagenotfound(request, context={}):
    context['title'] = "Page not found"
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

def project_seri(request, context={}):
    context.update(seri)
    return render(request, 'project.html', context)

def project_autodesk(request, context={}):
    context.update(autodesk)
    return render(request, 'project.html', context)

def project_uo(request, context={}):
    context.update(uo)
    return render(request, 'project.html', context)

# Work / Case Studies
# ##############################################################################

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Case study for Northwest Power Pool’s learning management system"
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
    context['title'] = "Case study for NAVEX Global’s Content Management"
    context['banner_image'] = "website/images/case-studies/navex/hero-tinted@2x.jpg"
    context['banner_title'] = "Content Management for the Global Ethics Leader"
    context['banner_position'] = '85% 40%'
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">NAVEX Global</span> was formed in 2012 to become the leader in the emerging field of Ethics & Compliance. They engaged OMBU with the mission to design and launch technology capable of not just keeping up, but accelerating, their meteoric rise.</p>"
    context['testimonial_image'] = "website/images/case-studies/navex/testimonial-logo.png"
    context['intro_testimonial_quote'] = "“Based on projects, the current uplift in high-value forms from the new pages will result in $4.6M in pipe and $1.4M in closed won business in the next 12 months!”"
    context['intro_testimonial_attribution_name'] = "Hillary E."
    context['intro_testimonial_attribution_title'] = "Demand Generation Manager, NAVEX Global"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/navex/intro@2x.png',
            'alt': 'A screenshot of the NAVEX Global home page',
            'browser' : {
                'url' : 'navexglobal.com',
            },
        },
        'skills': ["Technology Strategy", "Content Management", "Drupal CMS Development", "Marketo Integration", "AWS Migration", "AWS DevOps Management"],
    }
    context['visionary'] = {
        'body': '<p>Facing explosive growth and with a clientele featuring most Fortune 500 companies in more than 200 countries, NAVEX Global needed rock solid, cutting-edge web marketing technology capable of supporting smooth collaboration among distributed teams and rapidly changing business.</p>',
        'image': {
            'src' : 'website/images/case-studies/navex/visionary@2x.png',
            'alt': 'A screenshot of the NAVEX Global blog',
            'browser' : {
                'url' : 'navexglobal.com/blog',
            },
        },
    }
    context['solution'] = {
        'body': '<p>OMBU designed and launched an enterprise content management system (CMS) that empowers NAVEX Global to personally engage customers across their global markets.  Marketing teams are able to launch a rich custom landing page for new products and campaigns in minutes, with no IT involvement, allowing them to iterate, test and optimize at breakthrough speeds.</p><p>The website features a rich resource center that asserts NAVEX Global’s leadership in the field and is a key conversion point for new business. To further project NAVEX Global’s thought leadership, OMBU transformed an existing blog into a multi-channel publication that quickly became an industry must-read.</p><p>To allow NAVEX Global to personally reach their global markets, we built a localization framework that empowers marketing teams launch locales as the company grows and tailor content and offerings specific market conditions.</p>',
    }
    context['innovations'] = [
        {
            'title': 'Page Builder',
            'background': 'website/images/case-studies/navex/innov-slide-01@2x.png',
            'text': 'The page builder feature enables marketers to create landing pages for new products and campaigns without coding or technical help. The page builder offers blocks, such as tailored lead-capture, video and other rich media that can be arranged and resized on-page to achieve the best layout for every situation and enable iterative optimization. Marketers can granularly customize the search engine optimization (SEO) at every content level to drive traffic into the sales funnel.',
            'action_text': '',
        },
        {
            'title': 'Localization',
            'background': 'website/images/case-studies/navex/innov-slide-02@2x.png',
            'text': 'NAVEX Global has customers in over 200 countries, so we built powerful localization functionality into their new site.  Our solutiom enables the marketing team to quickly clone, translate, and adapt pages from one locale to another. For visitors, the experience is seamless, as the site automatically detects the user’s location and presents the appropriate targeted&nbsp;content.',
            'action_text': '',
        },
        {
            'title': 'Robust, Filterable Resource Center',
            'background': 'website/images/case-studies/navex/innov-slide-03@2x.png',
            'text': 'Potential customers are more likely to convert when they can see the expertise of a vendor, and so we built NAVEX Global a robust resource center to demonstrate their thought leadership through white papers, webinar videos, case studies, and other content types. NAVEX Global can offer premium content behind lead capture gating forms, customized for individual resources, and using progressive enhancement to intelligently and automatically grow lead&nbsp;profiles.',
            'action_text': '',
        },
        {
            'title': 'Marketo Marketing Automation',
            'background': 'website/images/case-studies/navex/innov-slide-04@2x.png',
            'text': 'We built custom integration with the Marketo marketing automation platform throughout NAVEX Global’s new site, to enable their marketing team to better capture new leads, gather insights about visitors, track customer value, and target content.  Using our solution, marketers can embed custom Marketo-integrated forms anywhere on the site, without any code. Building a custom lead-generation landing page takes a matter of&nbsp;minutes.',
            'action_text': '',
        },
        {
            'title': 'Scalable Application and Content DevOps',
            'background': 'website/images/case-studies/navex/innov-slide-05@2x.png',
            'text': 'To reach NAVEX Global’s worldwide audience quickly and reliably, we built a scalable AWS cloud DevOps solution. Dynamic computation is distributed across an auto-scaling fleet of application servers with full failover redudancy in case of a data center outage. Images, documents, and stylesheets, are served from a content delivery network, with leaf nodes close to users, for the fastest experience around the&nbsp;world.',
            'action_text': '',
        },
    ]
    context['outcomes'] = [
        { 'title': '< 4 <abbr title="minutes">min</abbr>', 'summary': 'Landing page launch' },
        { 'title': '224', 'summary': 'White papers, eBooks, webinars' },
        { 'title': '448', 'summary': 'Expert blog posts' },
        { 'title': '2', 'summary': 'Top competitors acquired' },
        { 'title': '$4.6M', 'summary': 'Projected increase in pipeline due to launch' },
        { 'title': '$1.4M', 'summary': 'Projected increase in closed won business duet to launch' },
    ]
    context['outcome_conclusion'] = '<p>Galaxies encyclopaedia galactica, cosmos at the edge of forever the sky calls to us from which we spring Rig Veda Euclid made in the interiors of collapsing stars consciousness.</p>'
    context['cta_text'] = '<span class=\"footer--cta-intro--phrase\">We helped NAVEX Global</span> <span class=\"footer--cta-intro--phrase\">modernize their website content.</span> <strong>What can we modernize for&nbsp;you?</strong>'
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Case study for Saturday Academy’s class registration system"
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
