from django.shortcuts import render

def home(request, context={}):
    context['title'] = "Web solutions for CMS, applications, infrastructure, and tech strategy"
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

def project(request, context={}):
    context['title'] = "Oregon Convention Center"
    return render(request, 'project.html', context)

def services(request, context={}):
    context['title'] = "Enterprise CMS, business applications, infrastructure, and technology strategy"
    return render(request, 'services.html', context)

def contact(request, context={}):
    context['title'] = "Contact OMBU for web technology solutions, consultations, and RFPs"
    return render(request, 'contact.html', context)

def careers(request, context={}):
    context['title'] = "Web design and development careers in Portland, Oregon"
    return render(request, 'careers.html', context)

# Work / Case Studies
# ##############################################################################

def casestudy_nwpp(request, context={}):
    context['client'] = "Northwest PowerPool"
    context['title'] = "Case study for Northwest Power Pool’s learning management system"
    context['banner_image'] = "website/images/case-studies/nwpp/banner.png"
    context['banner_title'] = "Modernized Power Utility Training"
    context['banner_subtitle']  = "Learning Management System"
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Northwest PowerPool (NWPP)</span> brings together 32 power utilities in eight US states and two Canadian provinces. OMBU designed a powerful centralized training platform so NWPP could help its member utilities keep up-to-date on mandated certifications and the latest trends, meaning greater safety, more engagement, and more benefit to the whole membership base and their customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/nwpp/testimonial-logo.png"
    context['testimonial_quote'] = "“Partnering with OMBU on this evolution of our platform was one of the best decisions I’ve ever made.”"
    context['testimonial_attribution_name'] = "David Pennington"
    context['testimonial_attribution_title'] = "Curriculum Developer, NWPP"
    context['contribution_video'] = 'website/videos/sample.mp4'
    context['contribution_skills'] = ["User Experience Design", "Python Application Development", "AWS Infrastructure", "Product Roadmap Planning"]
    context['visionary_body'] = "<p>NWPP came to us with a simple vision: <strong>Make federally-mandated power safety training easy and fun via an engaging video learning platform</strong>, so that employees of their member utilities would complete more trainings, engage more with the training material for better results, and ultimately create a safer and more productive world of power.</p><p>NWPP has trainers and video production talent in-house, so they wanted a technology partner who could come up with a learning system that would be a great platform for their training.</p>"
    context['visionary_video'] = "website/videos/sample.mp4"
    context['solution_body'] = "<p>We built a modern, fun training platform targeted specifically for training utility workers, with integrated videos and interactive quizzes.</p><p>Powering this platform, we built a powerful yet easy-to-use Learning Management System (LMS) that lets the NWPP content team quickly put together new courses for their members in minutes.</p><p>Things like 3D models, skilled trainers, and fun easter eggs like blooper reels and jokes make the whole experience engaging</p><p>This platform integrates directly with industry-standard data systems, like the LRS/XAPI datastore and exports for federal compliance systems.</p><p>Ultimately, the most important feature is the fun and informative training materials that mean our client can increase education in an industry where knowledge and safety are critical.</p>"
    context['solution_video'] = "website/videos/sample.mp4"
    return render(request, 'case-study.html', context)

def casestudy_navex(request, context={}):
    context['client'] = "NAVEX Global"
    context['title'] = "Case study for NAVEX Global’s enterprise CMS"
    context['banner_image'] = "website/images/case-studies/navex/banner.png"
    context['banner_title'] = "Enterprise CMS for the Global Ethics Leader"
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">NAVEX Global</span> was formed in 2012 to become the leader in the emerging field of Ethics & Compliance. They engaged OMBU with the mission to design and launch technology capable of not just keeping up, but accelerating, their meteoric rise.</p>"
    context['testimonial_image'] = "website/images/case-studies/navex/testimonial-logo.png"
    context['intro_testimonial_quote'] = "“Based on projects, the current uplift in high-value forms from the new pages will result in $4.6M in pipe and $1.4M in closed won business in the next 12 months!”"
    context['intro_testimonial_attribution_name'] = "Hillary Ervin"
    context['intro_testimonial_attribution_title'] = "Senior Director, Demand Generation & Sales Development Team"
    context['contribution_video'] = 'website/videos/sample.mp4'
    context['contribution_skills'] = ["Technology Strategy", "Enterprise CMS", "Drupal CMS Development", "Marketo Integration", "AWS Migration", "AWS Infrastructure Management"]
    context['visionary_body'] = "<p>Facing explosive growth and with a clientele featuring most Fortune 500 companies in more than 200 countries, NAVEX Global needed rock solid, cutting-edge web marketing technology capable of supporting smooth collaboration among distributed teams and rapidly changing business.</p>"
    context['visionary_video'] = "website/videos/sample.mp4"
    context['solution_body'] = "<p>OMBU designed and launched an enterprise content management system (CMS) that empowers NAVEX Global to personally engage customers across their global markets.  Marketing teams are able to launch a rich custom landing page for new products and campaigns in minutes, with no IT involvement, allowing them to iterate, test and optimize at breakthrough speeds.</p><p>The website features a rich resource center that asserts NAVEX Global’s leadership in the field and is a key conversion point for new business. To further project NAVEX Global’s thought leadership, OMBU transformed an existing blog into a multi-channel publication that quickly became an industry must-read.</p><p>To allow NAVEX Global to personally reach their global markets, we built a localization framework that empowers marketing teams launch locales as the company grows and tailor content and offerings specific market conditions.</p>"
    context['solution_video'] = "website/videos/sample.mp4"
    return render(request, 'case-study.html', context)

def casestudy_sa(request, context={}):
    context['client'] = "Saturday Academy"
    context['title'] = "Case study for Saturday Academy’s class registration system"
    context['banner_image'] = "website/images/case-studies/sa/banner.png"
    context['banner_title'] = "Engaging the Next Generation of Scientists, Engineers, and Artists"
    context['banner_subtitle'] = "Class Registration System"
    context['intro_text'] = "<p><span class=\"cs-intro--emphasis\">Saturday Academy</span> strives to engage all motivated young people in hands-on, in-depth learning by connecting them to community experts as educators and mentors by offering over 850 STEAM-curriculum classes per year. But registration was cumbersome for parents and data collection was poor and incomplete.</p><p>  OMBU conducted an organization-wide survey of processes, workflows and technology usage and designed and built a nonprofit Salesforce CRM and integrated website that enables families to register to classes and engage with mentors, funneling data in real time into Salesforce for instant reporting and analysis. This IT revision transformed how Saturday Academy engages with its customers.</p>"
    context['testimonial_image'] = "website/images/case-studies/sa/testimonial-logo.png"
    context['contribution_video'] = 'website/videos/sample.mp4'
    context['contribution_skills'] = ["Technology Strategy", "User Experience Design", "Visual Design", "Salesforce CRM Development", "Drupal Application Development", "AWS Design & Implementation"]
    context['visionary_body'] = "<p>Founded in 1983, Saturday Academy offers over 850 classes and camps per year and over 100 internships for students, with focus on STEAM education and an emphasis on engaging underprivileged students by offering over $70k per year in financial aid.</p><p>Saturday Academy’s unique model is to partner with community subject experts as teachers and mentors, such as practicing doctors, working scientists, and professional actors in the Portland metropolitan area and around Oregon.</p><p>Despite their growth and technology focus, Saturday Academy had been limping along with an old and creaky homegrown Access database and registration process that involved printouts and laborious manual staff interaction for every registration and application.</p><p>The vision: Saturday Academy needed a database of students and their families with a real-time integrated web registration system, so families can self-serve and SA can gain insights from data in real-time.</p>"
    context['visionary_video'] = "website/videos/sample.mp4"
    context['solution_body'] = "<p>OMBU implemented a rich CRM to serve as the canonical repository of data about families, classes, registrations, internships, and donors, built on Salesforce. By building on top of Salesforce, we were able to provide Saturday Academy with a leading CRM database platform, including using add-ons such as the Nonprofit Success Pack (NPSP) and data management tools. Additionally, Saturday Academy benefits from the knowledge and expertise of the huge number of other nonprofits who use Salesforce to run their organizations.</p><p>To reach parents, students, instructors, and mentors, we designed and built a fun, easy-to-use enterprise CMS website. Parents can set up their household information online, and register their children for any of Saturday Academy’s many classes quickly and easily, and even be granted auto-calculated financial aid to help make the classes accessible to all.</p><p>Saturday Academy’s unique internship program, Apprenticeships in Science and Engineering (ASE), pairs teens with industry mentors for a summer of on-the-job learning. Hundreds of motivated students apply for the program, so we designed a process that makes it easy to apply, as well as a portal for the mentors to rank applicants and a system for final approval and communication with selected interns.</p><p>While we’re proud of transforming Saturday Academy’s online presence and making everything smooth and easy for parents and students, the most transformative part of the solution we built for Saturday Academy is the real-time data flow and the accompanying reporting within the CRM. Leadership can now ask questions and gain insights instantly, such as seeing breakdown of financial aid relative to family demographics, intelligence that previously would either have days of data processing or have been entirely impossible.</p>"
    context['solution_video'] = "website/videos/sample.mp4"
    return render(request, 'case-study.html', context)
