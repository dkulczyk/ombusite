from django.shortcuts import render

def home(request, context={}):
    context['title'] = "Web solutions for CMS, applications, and infrastructure"
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
    context['title'] = "Enterprise CMS, business applications, and infrastructure"
    context['services'] = [
        { 'title': 'Enterprise CMS', 'summary': 'We make content<br>manageable' },
        { 'title': 'Business Applications', 'summary': 'We make business<br>profitable' },
        { 'title': 'Infrastructure', 'summary': 'We make systems<br>reliable' },
    ]
    return render(request, 'services.html', context)

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions, consultations, and RFPs"
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Web design and development careers in Portland, Oregon"
    return render(request, 'careers.html', context)

# Work / Projects
# ##############################################################################

def project_occ(request, context={}):
    context['client'] = "Oregon Convention Center"
    context['title'] = "Project profile for Oregon Convention Center’s website redesign"
    context['visit_url'] = 'https://www.oregoncc.org/'
    context['visit_text'] = 'Visit Website'
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_occ.html'
    context['intro'] = '<h6>Making the world’s most useful convention center website</h6><p>The Oregon Convention Center is a prominent institution of the West Coast, one of only two LEED Platinum certified convention centers in the US. When the OCC approached OMBU, however, their website had two major failings: it looked woefully outdated and cheap, and the site’s navigation and content were messy and confusing.</p><p>The OCC engaged OMBU in a guided Discovery phase, to figure out how to organize, design, and build a web presence that communicated the OCC’s prestigious yet friendly brand and guide audiences to the information they need. </p><p>OMBU then took the information from Discovery and designed and built a sleek, modern, mobile-friendly and easy-to-navigate website that highlights the </p>'
    context['services'] = [ 'Technology Strategy', 'User Experience Design', 'Systems Integration', 'Development', 'Infrastructure' ]
    context['testimonial_image'] = 'website/images/project-images/occ/aerial-photo@2x.png'
    context['testimonial_quote'] = "The OCC website is our front door and delivers exactly what we are – a place where things happen, modern, exciting, sustainable and service oriented.  OMBU created a very successful site for us on time and on budget"
    context['testimonial_attribution'] = "Matt Pizzuti, Interim Executive Director"
    context['technologies'] = [ 'OMBU Core Drupal CMS', 'Responsive design', '60fps UI animations', 'Integration with EBMS event system', 'Apache Solr faceted search', 'Live chat', 'High-availability managed infrastructure' ]
    context['insights_content_template'] = 'content/project/insights/_occ.html'
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_kaufmanhall(request, context={}):
    context['client'] = "Kaufman Hall"
    context['title'] = "Project profile for Kaufman Hall’s website redesign"
    context['visit_url'] = 'https://www.kaufmanhall.com/'
    context['visit_text'] = 'Visit Website'
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_kaufmanhall.html'
    context['intro'] = '<h6>Powering the Enterprise</h6><p>Kaufman Hall is a management consulting and enterprise software company with clients around the globe. After expanding their business by acquiring the leading software provider in their field, Kaufman Hall needed a unified web presence with an enterprise content management system (CMS) to support their growth and thought leadership.</p><p>OMBU designed and built an enterprise CMS website featuring a modern design and powerful marketing tools. The site features a filterable resource center for white papers, case studies, webinars, and more, to prove Kaufman Hall’s thought leadership. Flexible layout tools mean the marketing team can spin up new landing pages, complete with lead capture, in minutes instead of weeks. Rich integration with Marketo and Salesforce allows the sales team to prospect and funnel attractive leads into their sales pipeline.</p>'
    context['services'] = [ 'User Experience Design', 'Visual Design', 'Drupal Enterprise CMS Development', 'Data Migration' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_stand(request, context={}):
    context['client'] = "Stand for Children"
    context['title'] = "Project profile for Stand for Children’s organizer app"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_stand.html'
    context['intro'] = '<h6>Empowering Community Organizers to Effect Change for Students</h6><p>Stand for Children reached out to OMBU to develop an iPad app with an ambitious goal: to transform the way Stand’s field organizers reach, manage, and activate their volunteer base across the nation.</p><p>OMBU’s Discovery determined that, rather than building an iPad-only app that would restrict the audience to these tablets, Stand would be better off with a mobile web app that would work on any device and platform. This early decision meant that, when Stand later switched it’s tablets from Apple to Microsoft, the app we built worked out- of-the-box and didn’t require additional investment.</p><p>The app integrates in real-time with Stand’s Salesforce CRM, which means that app data is always in sync with gift, membership development, and contact data that are critical for Stand’s daily operations.</p><p>The app was rolled out nationally and has become a critical tool for Stand’s efforts to drive parent engagement and improve outcomes for kids.</p>'
    context['services'] = [ 'Technology Strategy', 'Table Application Design', 'Application Development' ]
    context['technologies'] = [ 'Angular JavaScript Application', 'Real-time Salesforce Integration', 'Touch-centric UI' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_smithsonian(request, context={}):
    context['client'] = "Smithsonian Institute Lemelson Center"
    context['title'] = "Project profile for Smithsonian Institute Lemelson Center’s website design"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_smithsonian.html'
    context['intro'] = '<h6>An Innovative Website for the Museum of Innovation</h6><p>The Smithsonian Institute needed a website unique and advanced enough to represent their Lemelson Center for Invention and Innovation, and OMBU were thrilled to be tasked with this challenge. In addition to a quirky design that showcases the center’s bold, forward-thinking identity, the powerful Drupal website boasts features such as real-time faceted search, branded audio and video players, and fun on-page interactive elements to increase visitor engagement.</p><p>The Lemelson site integrates with other Smithsonian systems, such as an institution-wide calendaring solution, email marketing tools, and even an in-museum exhibit. These integrations make the site a  rst-class citizen in the Smithsonian ecosystem, and keep rich data  owing without staff intervention.</p>'
    context['visit_url'] = 'http://invention.si.edu/'
    context['visit_text'] = 'Visit Website'
    context['services'] = [ 'Technology Strategy', 'Enterprise CMS Architecture', 'Enterprise CMS Implementation', 'Archive Records Migration', 'Government Systems Integration', 'Training and Rollout' ]
    context['technologies'] = [ 'Enterprise Drupal CMS', 'Custom Video and Audio Players', 'Migration of 1700+ Archive Records', 'Apache Solr Faceted Search', 'Interactive Canvas Drawing Functionality', '“Surprise Me” Exploration Feature' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_nwcouncilrtf(request, context={}):
    context['client'] = "NW Council Regional Technical Forum"
    context['title'] = "Project profile for NW Council RTF’s website redesign"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_nw-council-rtf.html'
    context['intro'] = '<h6>Modernizing Interaction with Energy Efficiency Program Development</h6><p>OMBU designed and built the new Regional Technical Forum website for NWPCC. The new website serves a technical audience with a modern and task-oriented visual design, and supports content providers with enterprise CMS functions and integrations behind the scenes. For example, content editors can use assets stored in Box as if they were native files in the CMS.</p><p>NWPCC’s mission required transparency and public input. OMBU conceived and built a discussion component that can be placed anywhere on the new website to engage the public. OMBU is currently working with NWPCC to redesign their main council website.</p>'
    context['visit_url'] = 'https://rtf.nwcouncil.org/'
    context['visit_text'] = 'Visit Website'
    context['services'] = [ 'Technology Strategy', 'User Experience Design', 'Visual Design', 'Enterprise Drupal CMS', 'Accessibility Compliance Audit', 'Migration of Measures', 'Training' ]
    context['technologies'] = [ 'Enterprise Drupal CMS', 'Box Integration for CMS Asset Library', 'Searchable Measure List with Update History', 'Automated Content Migration Script' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_compliancenext(request, context={}):
    context['client'] = 'NAVEX Global <span class="widow-prevention">Compliance Next</span>'
    context['title'] = "Project profile for Compliance Next’s website design"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_compliance-next.html'
    context['intro'] = '<h6>A Community Platform for a Burgeoning New Industry</h6><p>OMBU built the world’s first community-driven compliance think tank for NAVEX Global. Compliance is an emerging and rapidly growing career field with limited resources for members. To help our client seize the opportunity,  OMBU launched Compliance Next in 5-months. The website features learning tracks and resources and is quickly evolving with features that allow peer-to-peer networking.</p>'
    context['visit_url'] = 'https://www.navexglobal.com/compliancenext/'
    context['visit_text'] = 'Visit Website'
    context['services'] = [ 'Services', 'Technology Strategy', 'Application Architecture', 'Application Development', 'Systems Integration' ]
    context['technologies'] = [ 'Django Community Application Platform' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_metro(request, context={}):
    context['client'] = "Oregon Metro"
    context['title'] = "Project profile for Oregon Metro’s website redesign"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_metro.html'
    context['intro'] = '<h6>Connecting Millions with Their Regional Government</h6><p>OMBU built a powerful and scalable enterprise Drupal platform for Metro to communicate its mission and services, and to provide online resources to its constituents such as the Find a Recycler search application. Using our rich and intuitive publishing tools, over 150 Metro staff from across the agency can draft, moderate, translate and approve content according to customizable permissions. Thanks to an agile process with predictable iterations, oregonmetro.gov launched on time, smoothly and has scaled gracefully .</p><p>Since launch, Metro has engaged OMBU for several follow-up projects, including a major new constituent engagement application, a map tool to solicit public comments on Metro projects, and enhancements to their news section.</p>'
    context['visit_url'] = 'https://www.oregonmetro.gov/'
    context['visit_text'] = 'Visit Website'
    context['services'] = [ 'Technology Strategy', 'Enterprise CMS Architecture', 'Drupal CMS Development', 'Government Systems Integration', 'Training & Rollout' ]
    context['technologies'] = [ 'Enterprise Drupal CMS', 'Publishing Moderation System', 'Translation/Localization for 13 Languages', 'Responsive Design', 'Rich Interactive Maps', 'Integration with Government Systems', 'Apache Solr Faceted Search', 'Searchable PDF Documents' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_metropcmt(request, context={}):
    context['client'] = "Oregon Metro Public Comment Map App"
    context['title'] = "Project profile for Oregon Metro PCMT’s web application design"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_metro-pcmt.html'
    context['intro'] = '<h6>Engaging the Public with Interactive Maps</h6><p>Metro engaged OMBU to design and implement a map-based public comment tool. Metro uses this tool to engage with the community on large transit planning projects, such as the Southwest Corridor and the Powell-Division Transit and Development Project.</p><p>OMBU’s web application allows Metro staff to design project plans and comment points on a modern mapping platform, and request comments from the public on routes and points through comment forms and rich media.</p>'
    # context['visit_url'] = 'http://oregonmetro.gov/swcorridormap'
    # context['visit_text'] = 'Visit Website'
    context['services'] = [ 'User Experience Design', 'Visual Design', 'Drupal Application Development', 'Interactive Map Application Development' ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_seri(request, context={}):
    context['client'] = "Sustainable Electronics Recycling International"
    context['title'] = "Project profile for Sustainable Electronics Recycling International’s website redesign"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_seri.html'
    # context['intro'] = ''
    context['visit_url'] = 'https://sustainableelectronics.org/'
    context['visit_text'] = 'Visit Website'
    # context['services'] = [ ]
    # context['technologies'] = [ ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_autodesk(request, context={}):
    context['client'] = "Autodesk ReCap"
    context['title'] = "Project profile for Autodesk ReCap’s website design"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_autodesk.html'
    # context['intro'] = ''
    # context['visit_url'] = ''
    # context['visit_text'] = ''
    # context['services'] = [ ]
    # context['technologies'] = [ ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

def project_uo(request, context={}):
    context['client'] = "University of Oregon Lundquist College of Business"
    context['title'] = "Project profile for University of Oregon Lundquist College of Business’s website design"
    context['hero_carousel_content_template'] = 'content/project/hero-carousels/_uo.html'
    # context['intro'] = ''
    context['visit_url'] = 'https://business.uoregon.edu/'
    context['visit_text'] = 'Visit Website'
    # context['services'] = [ ]
    # context['technologies'] = [ ]
    context['project_prev'] = { 'url': '#', 'name': 'Car Talk', 'cta': 'Don’t Drive Like My Brother' }
    context['project_next'] = { 'url': '#', 'name': 'Paramount Pictures', 'cta': 'Now Playing' }
    return render(request, 'project.html', context)

# Work / Case Studies
# ##############################################################################

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Case study for Northwest Power Pool’s learning management system"
    context['banner_image'] = "website/images/case-studies/nwpp/hero-tinted@2x.png"
    context['banner_title'] = "Modernized Power Utility Training"
    context['banner_subtitle']  = "Learning Management System"
    context['banner_position'] = '20% 40%'
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Northwest PowerPool (NWPP)</span> brings together 32 power utilities in eight US states and two Canadian provinces. OMBU designed a powerful centralized training platform so NWPP could help its member utilities keep up-to-date on mandated certifications and the latest trends, meaning greater safety, more engagement, and more benefit to the whole membership base and their customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/nwpp/testimonial-logo.png"
    context['testimonial_quote'] = "“Partnering with OMBU on this evolution of our platform was one of the best decisions I’ve ever made.”"
    context['testimonial_attribution_name'] = "David Pennington"
    context['testimonial_attribution_title'] = "Curriculum Developer, NWPP"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/nwpp/intro@2x.png',
            'alt': 'A screenshot of a source.training course video activity page',
            'browser' : {
                'url' : 'source.training',
            },
        },
        'skills': ["User Experience Design", "Python Application Development", "AWS Infrastructure", "Product Roadmap Planning"],
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
        'stat': {
            'number': '32',
            'label': 'Member<br>Utilities',
            'summary': 'Why member utilities are important and how they benefit directly or indirectly from modernized power utility training motes of rock and gas the ash of cosmic stellar extraterrestrial alchemy.',
        },
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
        'stat': {
            'number': '≥1200',
            'label': 'Utility<br>Operators<br>Served',
            'summary': 'Why utility operators are important and how they benefit directly or indirectly from modernized power utility training motes of rock and gas the ash of cosmic stellar alchemy.',
        }
    }
    context['innovations'] = [
        {
            'title': 'Drag & Drop Course Builder',
            'background': 'website/images/case-studies/nwpp/innov-slide-01@2x.png',
            'text': 'NWPP can drag-and-drop any assortment of videos, documentation, and quizzes together to quickly and easily create courses for utility workers to take.',
            'action_text': 'Watch Demo',
        },
        {
            'title': 'Powerful Digital Asset Management',
            'background': 'website/images/case-studies/nwpp/innov-slide-02@2x.png',
            'text': 'All media assets, such as videos, documents, and images are stored in a central asset library.<br><br>Videos integrate directly into the design and aesthetic of the site, a collaboration between NWPP’s production team and OMBU.',
            'action_text': 'Watch Demo',
        },
        {
            'title': 'High-Availability Infrastructure',
            'background': 'website/images/case-studies/nwpp/innov-slide-03@2x.png',
            'text': 'Because the LMS is a business critical application, it needed to be online at all times. To accomplish this, we designed a high-availability hosting system that keeps copies of the application in two datacenters. The system monitors for connectivity problems and automatically redirects traffic to the healthier data center.',
            'action_text': '',
        },
        {
            'title': 'Self-Service Team Management Panel',
            'background': 'website/images/case-studies/nwpp/innov-slide-04@2x.png',
            'text': 'To ensure strong adoption, we designed a system that decentralizes the task of managing utility teams and their training. NWPP can designate training coordinators at their member utilities, who then have tools to invite and monitor a handful to hundreds of individual operators as they progress through their training.<br><br>A convenient dashboard gives the training coordinators an overview of their team’s status, and they can then dig in to any operator’s individual progress.',
            'action_text': '',
        },
        {
            'title': 'xAPI Integration',
            'background': 'website/images/case-studies/nwpp/innov-slide-05@2x.png',
            'text': 'We built one of the first learning management systems featuring native real-time integration with a learning record store (LRS) using the emerging open standard experience API (xAPI, also called Tin Can), the modern replacement for the legacy SCORM protocol.<br><br>With the LRS data, NWPP can track every member’s progress, test results, and completion data, as well as see trends across all learners or insights about individual lessons.',
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
    context['cta_text'] = 'We helped Northwest PowerPool<br>modernize their power utility training.<br><strong>What can we modernize for you?</strong>'
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def casestudy_navex(request, context={}):
    context['client'] = "NAVEX Global"
    context['title'] = "Case study for NAVEX Global’s enterprise CMS"
    context['banner_image'] = "website/images/case-studies/navex/hero-tinted@2x.png"
    context['banner_title'] = "Enterprise CMS for the Global Ethics Leader"
    context['banner_position'] = '85% 40%'
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">NAVEX Global</span> was formed in 2012 to become the leader in the emerging field of Ethics & Compliance. They engaged OMBU with the mission to design and launch technology capable of not just keeping up, but accelerating, their meteoric rise.</p>"
    context['testimonial_image'] = "website/images/case-studies/navex/testimonial-logo.png"
    context['intro_testimonial_quote'] = "“Based on projects, the current uplift in high-value forms from the new pages will result in $4.6M in pipe and $1.4M in closed won business in the next 12 months!”"
    context['intro_testimonial_attribution_name'] = "Hillary Ervin"
    context['intro_testimonial_attribution_title'] = "Senior Director, Demand Generation & Sales Development Team"
    context['contributions'] = {
        'image': {
            'src' : 'website/images/case-studies/navex/intro@2x.png',
            'alt': 'A screenshot of the NAVEX Global home page',
            'browser' : {
                'url' : 'navexglobal.com',
            },
        },
        'skills': ["Technology Strategy", "Enterprise CMS", "Drupal CMS Development", "Marketo Integration", "AWS Migration", "AWS Infrastructure Management"],
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
            'title': 'Drag & Drop Course Builder',
            'background': 'website/images/case-studies/navex/innov-slide-01@2x.png',
            'text': 'The page builder feature enables marketers to create landing pages for new products and campaigns without coding or technical help. The page builder offers blocks, such as tailored lead-capture, video and other rich media that can be arranged and resized on-page to achieve the best layout for every situation and enable iterative optimization. Marketers can granularly customize the search engine optimization (SEO) at every content level to drive traffic into the sales funnel.',
            'action_text': '',
        },
        {
            'title': 'Localization',
            'background': 'website/images/case-studies/navex/innov-slide-02@2x.png',
            'text': 'NAVEX Global has customers in over 200 countries, so we built powerful localization functionality into their new site. NAVEX Global can easily customize products and messaging for individual geographies, launching with US, UK, and French content.<br><br>Each locale features fully customizable navigation and content, and the marketing team can quickly clone and adapt pages from one locale to another (e.g. clone a US page to the UK locale then tailor it for that geography).<br><br>For visitors, the experience is seamless, as the site automatically detects the user’s location and presents the appropriate targeted content.',
            'action_text': '',
        },
        {
            'title': 'Robust, Filterable Resource Center',
            'background': 'website/images/case-studies/navex/innov-slide-03@2x.png',
            'text': 'Potential customers are more likely to convert when they can see the expertise of a vendor, and so we built NAVEX Global a robust resource center to highlight their insights and demonstrate their thought leadership.<br><br>With robust resource media types, such as white paper PDFs, webinar videos, case studies, and blog posts, NAVEX Global’s team can reach prospects in a variety of forms.<br><br>Individual expert faces provide a personal connection with the content, and show the team behind the software connected directly with their thoughts.<br><br>NAVEX Global can offer premium content behind lead capture gating forms, customized for individual resources, and using progressive enhancement to intelligently and automatically grow lead profiles.',
            'action_text': '',
        },
        {
            'title': 'Marketo Marketing Automation',
            'background': 'website/images/case-studies/navex/innov-slide-04@2x.png',
            'text': 'We built custom integration with the Marketo marketing automation platform throughout NAVEX Global’s new site, to enable their marketing team to better capture new leads, gather insights about visitors, track customer value, and target content.<br><br>Potential customers gain access to key resources through Marketo-integrated gating forms, which we also connected with Marketo’s progressive form features, meaning that NAVEX Global can gather new information from visitors as they interact with the site.<br><br>Additionally, marketers can embed custom Marketo-integrated forms anywhere on the site, without any code. Building a custom lead-generation landing page takes a matter of minutes.',
            'action_text': '',
        },
        {
            'title': 'Scalable Application and Content Infrastructure',
            'background': 'website/images/case-studies/navex/innov-slide-05@2x.png',
            'text': 'To reach NAVEX Global’s worldwide audience quickly and reliably, we built a scalable AWS cloud infrastructure for the website application and content.<br><br>Dynamic computation is distributed across an auto-scaling fleet of application servers, with traffic managed by a load balancer. The infrastructure has full duplication between two data centers, with all resources ready fail-over to the backup in case of a data center outage.<br><br>Resources and assets, such as images, documents, and stylesheets, are served from a content delivery network, with leaf nodes close to users, for the fastest experience around the world.',
            'action_text': '',
        },
    ]
    context['outcomes'] = [
        { 'title': '< 4 <abbr title="minutes">min</abbr>', 'summary': 'Landing page launch', 'filled': 'true' },
        { 'title': '224', 'summary': 'White papers, eBooks, webinars' },
        { 'title': '448', 'summary': 'Expert blog posts' },
        { 'title': '2', 'summary': 'Top competitors acquired' },
        { 'title': '$4.6M', 'summary': 'Projected increase in pipeline due to launch' },
        { 'title': '$1.4M', 'summary': 'Projected increase in closed won business duet to launch' },
    ]
    context['outcome_conclusion'] = '<p>Galaxies encyclopaedia galactica, cosmos at the edge of forever the sky calls to us from which we spring Rig Veda Euclid made in the interiors of collapsing stars consciousness.</p>'
    context['cta_text'] = 'We helped NAVEX Global<br>modernize their website content.<br><strong>What can we modernize for you?</strong>'
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Case study for Saturday Academy’s class registration system"
    context['banner_image'] = "website/images/case-studies/sa/hero-tinted@2x.png"
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
        'stat': {
            'number': '5200+',
            'label': 'Registrations<br>per Year',
            'summary': 'Why this metric is important and how Saturday Academy benefits directly or indirectly from it motes of rock and gas the ash of cosmic extraterrestrial alchemy bearable only through love.',
        },
    }
    context['solution'] = {
        'body': '<p>OMBU implemented a rich CRM to serve as the canonical repository of data about families, classes, registrations, internships, and donors, built on Salesforce. By building on top of Salesforce, we were able to provide Saturday Academy with a leading CRM database platform, including using add-ons such as the Nonprofit Success Pack (NPSP) and data management tools. Additionally, Saturday Academy benefits from the knowledge and expertise of the huge number of other nonprofits who use Salesforce to run their organizations.</p><p>To reach parents, students, instructors, and mentors, we designed and built a fun, easy-to-use enterprise CMS website. Parents can set up their household information online, and register their children for any of Saturday Academy’s many classes quickly and easily, and even be granted auto-calculated financial aid to help make the classes accessible to all.</p><p>Saturday Academy’s unique internship program, Apprenticeships in Science and Engineering (ASE), pairs teens with industry mentors for a summer of on-the-job learning. Hundreds of motivated students apply for the program, so we designed a process that makes it easy to apply, as well as a portal for the mentors to rank applicants and a system for final approval and communication with selected interns.</p><p>While we’re proud of transforming Saturday Academy’s online presence and making everything smooth and easy for parents and students, the most transformative part of the solution we built for Saturday Academy is the real-time data flow and the accompanying reporting within the CRM. Leadership can now ask questions and gain insights instantly, such as seeing breakdown of financial aid relative to family demographics, intelligence that previously would either have days of data processing or have been entirely impossible.</p>',
        'image': {
            'src' : 'website/images/case-studies/sa/solution@2x.png',
            'alt': 'A screenshot of a Saturday Academy application review page',
            'browser' : {
                'url' : 'saturdayacademy.org',
            },
        },
        'stat' : {
            'number': '$70k+',
            'label': 'Financial Aid<br>Automatically<br>Granted per Year',
            'summary': 'Why this metric is important and how Saturday Academy benefits directly or indirectly from it motes of rock and gas the ash of cosmic extraterrestrial alchemy bearable only through love.',
        },
    }
    context['innovations'] = [
        {
            'title': 'Real-Time Class Registration System',
            'background': 'website/images/case-studies/sa/innov-slide-01@2x.png',
            'text': 'A live class catalog syncs between the website and the Salesforce datastore, meaning parents and students can see what classes Saturday Academy offers and, in real-time, seating availability.<br><br>Parents can manage their family’s information through a self-service household dashboard, and can even grant registration access to other household parents or guardians.<br><br>When it’s time to register, a parent can apply for and instantly receive financial aid, calculated based on their adjusted gross income (AGI) using a formula Saturday Academy can adjust over time.<br><br>Payment is processed immediately through Stripe’s API and is recorded within Salesforce, or, in the case of wait-list registrations, can be deferred and automatically charged if the student gets in.',
            'action_text': '',
        },
        {
            'title': 'Salesforce Business Datastore and Intelligence',
            'background': 'website/images/case-studies/sa/innov-slide-02@2x.png',
            'text': 'Since all registrations and interactions on the Saturday Academy speak to Salesforce in real-time via REST API, this means both systems are always in sync.<br><br>Real-time data, with customized data structures optimized for their business, means that Saturday Academy can run reports in real-time and gain insights in areas such as financials, demographics, and success metrics.',
            'action_text': '',
        },
        {
            'title': 'Data Migration',
            'background': 'website/images/case-studies/sa/innov-slide-03@2x.png',
            'text': 'Saturday Academy had over a decade of records of classes, students, and registrations stored in a number of homegrown Access databases and spreadsheets prior to launching the new system, so for archival and reporting purposes we built an automated migration system to bring the old records into the new system.<br><br>We also migrated donors and organizations from disparate, critical data for a nonprofit.<br><br>The migration meant that on launch day, we were able to automatically enable 10,592 website accounts for households, meaning those parents could log in on day 1 with their information and history already in place.',
            'action_text': '',
        },
        {
            'title': 'Enterprise CMS',
            'background': 'website/images/case-studies/sa/innov-slide-04@2x.png',
            'text': 'Since Saturday Academy is an organization that works with creative and inquisitive families, we designed and built a website that communicates that quirky, intelligent brand while maintaining a simple, easy-to-use interface for actions.<br><br>A mobile-responsive design means parents and students can learn about Saturday Academy’s offerings and register on any device.<br><br>A powerful enterprise CMS gives Saturday Academy’s marketing team the ability to quickly customize layouts with new page elements as their content needs change and the organization grows.',
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
    context['cta_text'] = 'We helped Saturday Academy<br>modernize their class registration system.<br><strong>What can we modernize for you?</strong>'
    # context['pdf_download'] = '/static/website/documents/case-studies/phytolacca-dioica.pdf'
    return render(request, 'case-study.html', context)
