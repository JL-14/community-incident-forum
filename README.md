# The Reigate Community Issues and Incidents Forum

![Front page](documentation/README_images/front-page.jpg)

Live version: [Reigate Community Issues and Incidents Forum](https://)

Repository: [GitHub repository](https://github.com/JL-14/community-incident-forum)

The app is developed by [Jorgen Lovbakke](https://github.com/JL-14)

## About the Reigate Community Issues and Incidents Forum

The Reigate Community Issues and Incidents Forum is a platform designed to provide residents and visitors to Reigate
with up-to-date information about what is happening in their local area. The website pulls together information and
updates from official sources (such as local authorities, police, schools) about events, incidents, road closures,
works, etc, and information from residents and visitors about things they have seen or experienced, such as issues
affecting traffic, roads, fly-tipping, anti-social behaviour, and other things that affect day-to-day lives in Reigate.

Prior to the launch of the Reigate Community Issues and Incidents Forum information about the local area and issues
affecting everything from transport and planned road closures to the walk in and out of the town centre was not
available in any one place. Furthermore, there was no forum for sharing local occurrences and concerns that may have an
impact on other residents and visitors. The Reigate Community Issues and Incidents Forum thus brings together this
information in one place, enabling residents to be aware of any issues and make informed decisions about their daily
lives.

The Reigate Community Issues and Incidents Forum is designed to be informative, up-to-date, interactive, and
user-friendly for residents and visitors alike.

## UX Design

### Strategy

The site has been developed for use by residents and visitors to Reigate (but is easily adaptable to other towns and
cities). The main goal of the site is to provide a forum for sharing information about issues and incidents residents
and visitors have experienced, which alongside information from the authorities, will ensure that users know what is
happening in their local area. This has been achieved by the use of a simple and intuitive interface where the
information takes centre-stage. 

The site has additional functionalities, such as the ability to register and log in securely in order to comment and 
provide updates on reports, as well as edit comments and updates. The site is managed by administrative superusers who
review and approve content before it is posted on the site.

### Target audience

The target audience for site can be divided into:

* Residents: The core audience for the site are the residents of Reigate and its immediate surroundings.
* Visitors: To a lesser extent than for residents, the site will also be of use to visitors to the town and commuters,
enabling informed decision-making about travel, routes, accommodation, activities, etc.
* Local authorities: Through the provision of user-generated information about issues in the local area, local
authorities will be able to see hazards and issues that may not have been reported to them.

### User Stories

#### First-time user

As a first-time visitor to the site, I want to:
* see an informative front page, so that I clearly understand what the site is about
* easily be able to navigate through the app using intuitive links, so that I can easily find what I am looking for
* see all the reported issues and incidents in a list, so that I can find any that are relevant to me
* be able to click on any report listed, so that I can get more detail where available
* be able to see any images of the issue or incident, to give me a clear sense of what and where it is
* I want to be able to easily register for the site, so that I can make full use of the comment/ update function

#### Frequent user

As a frequent user of the site, I want to:
* easily be able to log in, so that I can use comment and update functionality
* be able to comment and post updates on reports I see on the site, so that I can provide other users with the latest
information
* be able to have images uploaded on the site when alerting users to new issues and incidents, so that I can clearly
show the issue I am referring to
* be able to edit or delete comments and updates I post, so that I am in control of the content I post on the site
* be able to easily contact the forum owners and administrators, so that I can submit new reports or let them have any
comments or suggestions I may have

#### Admin user
As an admin user, I want to:
* be able to easily manage both the front- and back-end of the site, so that I can make any changes necessary
* be able to moderate content through having new reports go through me and comments approved by me before posting, so
that I have overall control over the site
* be able to monitor usage of the site in terms of visits, so that I can make decisions about
whether to further promote the site
* be able to see a list of registered users, so that I can see who is posting and what they are posting
* be alerted to new submissions through a dedicated e-mail for new reports, so that I can act swiftly when receiving
new content

## Technologies used

### Languages
* HTML for the site content
* CSS for site design and layout
* JavaScript for user interaction on the site for automatically (specifically for the edit and delete capabilities)
* Python as back-end programming language
* PostgreSQL for relational database management.

### Frameworks
* Bootstrap as front-end CSS framework for modern responsiveness and pre-built components, with
- Summernote as Bootstrap tool for managing the appearance and functionality of the administrative parts of the site
* Django as Python framework for the site, with
- Crispy Forms as Django framework for managing the appearance and functionality of the comment form

### Databases and storage
* [ElephantSQL](https://www.elephantsql.com/) as Postgres database (please note that ElephantSQL will cease operations in January 2025)
* Cloudinary for static file storage

### Integrated Development Environment (IDE)
* VS Code used as main coding environment
* GitPod used as backup IDE

### Version control and Deployment
* Git for version control
* GitHub for the online repository
* Heroku used for hosting the deployed app

### Other tools
#### Wireframes
- Balsamiq for the creation of wireframes for the site
- 
#### Agile working tools
* GitHub Projects used to manage the Agile working approach for the project

#### Entity Relationship Diagram (ERD)
* Lucidchart for the creation of the ERD


## App design

### Colour scheme
The colour scheme for the site has been chosen to convey a degree of seriousness, reflecting that the site is
concerned with issues and incidents affecting the lives of residents and visitors in Reigate.

The colours used are:
* Header and footer: Black (#212529) with Grey font (#aeaea7)

* Background: Light grey (#f9fafc) with black font (#212529)

* Floating heading container (hex #445261, with 0.9 opaqueness)

* Author banner in report list: Green (#188181) with white font (#ffffff)

* Font for individual report titles: Red (#e84610)


### Typography

### Imagery




## Features

### Home page

### Report List page

### Report details page

### Contact Us page





![Wireframe 1](/assets/images/ciif-wireframe-1.png)
![Wireframe 2](/assets/images/ciif-wireframe-2.png)
![Wireframe 3](/assets/images/ciif-wireframe-3.png)
![Wireframe 4](/assets/images/ciif-wireframe-4.png)
![Wireframe 5](/assets/images/ciif-wireframe-5.png)
![Wireframe 6](/assets/images/ciif-wireframe-6.png)
![Wireframe 7](/assets/images/ciif-wireframe-7.png)