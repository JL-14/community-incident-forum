# The Reigate Community Issues and Incidents Forum

![Front page](documentation/images/front-page.png)

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

## Future Development

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

## Features
The following is a description of the features and functionality of the site. Please see the [testing](Testing) section for details of all aspects of functionality.

### Navbar
The navbar is fixed in place, and appears on all pages. It features the site logo ('Reigate Community Issues and Incidents') in the top left corner (which also serves as a link to the Home page), and navigation links next to the logo. The navigation links are a dark orange to set them apart from the logo and tagline, and will take the user to the Home page, the Report List page, and the Contact Us page. On first arriving at the site, there is an option to Register as a new user of the site, which opens a registration form which creates a new account. There is also an option to Log In (for existing users), which opens the login page where username and password allows the user to log in. There is a red box to the right of the screen which informs visitors that 'You are not logged in', which changes to a green box to inform users that 'You are logged in as (username)' once logged in. These boxes stay visible throughout the site. Finally, on the right hand side of the screen, there is a tagline which reads 'a community forum for issues and incidents in Reigate'.

![Navbar image](documentation/images/navbar-image.png)

### Footer
The Footer is at the bottom of the screen, and is reached by scrolling down. At the centre of the Footer there is a copyright message ('Copyright Jorgen Lovbakke 2024') and an option to 'Follow us' with icons linking to Facebook, Twitter/ X, Instagram, and YouTube.

### Home page
The Home page introduces the site, including the rationale and instructions on how to use the site and contact the developer. There is a section with highlighted text (bold in red) emphasising to visitors that the site is not linked to the emergency services or official local government channels, and that in the case of an emergency they should phone 999.

### Report List page
The Report List page lists the posts on the site, ordered chronologically by the date and time of the issue or incident reported. The posts have an image (relevant to the post if the person reporting it has supplied an image, or a placeholder image -the main image for the site), a banner with the username of the person who reported it, and the title and date of time of the issue that was reported. There are a maximum of 6 reports listed on a page, with Next and Back buttons at the bottom of the page for accessing more reports. The user can click on any report to see the full details of the issue or incident in question.

### Report details page
On the Report Details page the title, author, and date and time of the issue or incident are set out next to the image supplied by the person making the report (or the placeholder image if no image was provided). The detailed content of the report is then set out below the image and title. Below the contents there is space for comments and/ or updates, which can be provided by registered users who are logged in by clicking the 'Add a Comment' button (which is only visible to logged in users). The comment section has full CRUD functionality (enabling users to Create comments, Read the comments, Update comments, and Delete comments) giving users full control over content they post to the site. To prevent erroneous or misleading information from being posted, comments will appear as shaded until approved by a user with administrative privileges. Feedback boxes appear when comments are submitted (saying that 'The comment is awaiting approval' or 'There was an error submitting, please try again'). Users who have submitted comments have the option of editing or deleting their comments through buttons to 'Delete' and 'Edit' underneath their comments (not for comments submitted by other users). For users who wish to delete their comments or updates, a box asks them to confirm that they want to delete the comment as this action cannot be undone, before a box appears confirming that 'Comment has been successfully deleted'. Users who wish to edit their comment or update are taken back to the Add a Comment form, where the original comment appears (to facilitate editing). On submitting the updated comment, a box appears to confirm that the comment has been updated, although the comment is shaded out and showing as awaiting approval so that the moderator can approve (or not) the updated comment. 

### Contact Us page
The Contact Us page has information on how to contact the forum, whether to to provide information about a new issue or incident, or to provide comments or suggestions. For new content, there is a link to a dedicated e-mail address ('report@reigatecommunityforum.co.uk') and instructions on what content needs to be included for a report to be created. Using an email-based submission process, the forum moderators have access to the submitters e-mail address for questions, queries, or missing information. There is a separate e-mail address for questions or suggestions for the moderators and developer ('info@reigatecommunityforum.co.uk').

## App design

### Colour scheme
The colour scheme for the site has been chosen to convey a degree of seriousness, reflecting that the site is
concerned with issues and incidents affecting the lives of residents and visitors in Reigate.

The colours used are:
#### Home page
* Header and footer: Black (#212529) with Grey font (#aeaea7)
* Background: Light grey (#f9fafc) with black font (#212529)
* Floating heading container (hex #445261, with 0.9 opaqueness)
![Front Page palette](documentation/images/front-page-palette.png)

#### Report List page
* Author banner in report list: Green (#188181) with white font (#ffffff)
* Font for individual report titles: Red (#e84610)
![Report List palette](documentation/images/report-list-palette.png)

### Typography
The font type used for the site is Lato, which is clearly defined and carries an appropriate degree of gravity and
urgency for the site.
![Lato font example](documentation/images/lato-font-outline.png)

### Imagery
The main image and placeholder for the site shows the junction between Bell Street and High Street in Reigate, with the
old Town Hall tower in the background. The photo was taken by Joanne Lovbakke.
![Main image](documentation/images/rcii-main-image.jpg)

Additional images are submitted by users (relevant to the issue or incident) or provided by the relevant local
authority, and uploaded by admin to the Cloudinary storage facility for static files.

### Wireframes
The wireframes for the site were developed using [Balsamiq](https://balsamiq.com/) software.

![Wireframe 1](/documentation/images/wireframe1-home.png)
![Wireframe 2](/documentation/images/wireframe2-reportlist.png)
![Wireframe 3](/documentation/images/wireframe3-reportdetail.png)
![Wireframe 4](/documentation/images/wireframe4-addcomment.png)
![Wireframe 5](/documentation/images/wireframe5-contact.png)


## Agile Methodology
An Agile methodology was adopted from start to finish for the development of the site. GitHub Project Management was used to manage the project, which facilitated the move from the aspirational initial design to the minimum viable product over the course of the work, moving the User Stories labeled as 'Nice to have' into the column for Future Deployments. 

### GitHub Project Management
![](/documentation/images/github-project-board-1.png)
![](/documentation/images/github-project-board-2.png)

All User Stories were assigned labels of 'Must Have', 'Could Have', or 'Nice to Have'. The final product consists of the 'Must Have' User Stories, with two 'Could Have' User Stories and four additional 'Nice to Have' User Stories which could be accommodated within the project life.

![](/documentation/images/github-project-board-labels.png)


## Information Architecture

### Database
The database used for the project is PostgreSQL, hosted by [ElephantSQL](https://www.elephantsql.com/). SQLite was used as backup database, and for automated Django testing purposes.

### Entity-Relationship Diagram
[](/documentation/images/ciif-erd.png)

### Data Modelling

#### Issue Model
This is the data model for issues and incidents used in the database.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| user | user | ForeignKey | User, on_delete=models.CASCADE |
| phone | phone | CharField | max_length=12, blank=True |
| issue_type | issue_type | CharField | max_length=50, choices=ISSUE_TYPE_CHOICES |
| created_on | created_on | DateTimeField | auto_now_add=True |
| updated_on | updated_on | DateTimeField | auto_now_add=True |
| date_of_issue | date_of_issue | DateTimeField | - |
| issue_title | issue_title | CharField | max_length=80, blank=False |
| slug | slug | SlugField | max_length=200, unique=True, blank=True |
| issue_content | issue_content | CharField | max_length=1500 |
| issue_location | issue_location | CharField | max_length=100, blank=False |
| is_urgent | is_urgent | CharField | max_length=13, choices=URGENT_CHOICES |
| featured_image | featured_image | CloudinaryField | 'image', default='placeholder' |
| dept_notified | dept_notified | ManyToManyField | DeptNotified, blank=True |
| notes_about_notifications | notes_about_notifications | TextField | max_length=200, blank=True |
| status | status | CharField | max_length=20, choices=STATUS_CHOICES |
| approved | approved | CharField | max_length=20, choices=APPROVED_CHOICES |

Choices models:
ISSUE_TYPE_CHOICES = (
    (ASB, 'Anti-social behaviour'),
    (ROADS, 'Road issues'),
    (TRAFFIC, 'Traffic issues'),
    (PAVEMENTS, 'Pavement-related issues'),
    (PUBLIC_SPACES_MAINTENANCE, 'Issues with maintenance of public spaces'),
    (RUBBISH, 'Rubbish-related issues'),
    (FLY_TIPPING, 'Fly-tipping'),
)

URGENT_CHOICES = (
    (IS_URGENT, 'Needs urgent attention, potential danger'),
    (IS_NOT_URGENT, 'Not an urgent or high risk issue'),
)

STATUS_CHOICES = (
    (RESOLVED, 'Resolved'),
    (UNRESOLVED, 'Not resolved'),
)

APPROVED_CHOICES = (
    (APPROVED, 'Approved'),
    (REJECTED, 'Rejected'),
    (PENDING, 'Pending Review'),
)

#### Comment Model

Data model for users to leave comments or provide updates when logged in. 

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| comment_issue  | comment_issue  | ForeignKey | Issue, on_delete=models.CASCADE, related_name="comments" |
| comment_author | comment_author | ForeignKey | User, on_delete=models.CASCADE, related_name="commenter" |
| comment_content | comment_content | TextField | - |
| created_on | created_on | DateTimeField | auto_now_add=True |
| approved | approved | BooleanField | default=False |

#### Department Notified Model

Data model for departments the user has notified about the issue or incident. 

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| dept_notified | dept_notified | CharField | max_length=50, choices=DEPARTMENT_CHOICES |

Choices model:
DEPARTMENT_CHOICES = (
    (RBC, 'Reigate and Banstead Council'),
    (SCC, 'Surrey County Council'),
    (SP, 'Surrey Police'),
)

#### UserAccount Model
Data model for additional information about the user, such as postcode (to provide contextual information about the user who is reporting the issue or incident). *This model is not used in the MVP version of the database*

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| user          | user          | OneToOneField | User, on_delete=models.CASCADE |
| postcode | postcode | CharField    | max_length=8 |

## Testing


## Deployment

- The programme was deployed to [Heroku](https://dashboard.heroku.com/apps/community-incident-forum).
- The programme can be reached by the [link](https://community-incident-forum-75e7791f6b68.herokuapp.com/)

### Deploying the project as an application running locally:

  1. This project requires you to have Python installed on your local PC:
  [Python](https://www.python.org/downloads/)

  2. You will also need pip installed to allow the installation of modules the application uses.
  [PIP](https://pypi.org/project/pip/)

  3. Create a local copy of the GitHub repository by following one of the two processes below:

    - Download ZIP file:
        1. Go to the [GitHub Repo page](https://github.com/JL-14/community-incident-forum).
        2. Click the Code button and download the ZIP file containing the project.
        3. Extract the ZIP file to a location on your PC.

    - Clone the repository:
        1. Open a folder on your computer with the terminal.
        2. Run the following command
        - `git clone https://github.com/JL-14/community-incident-forum.git`

    - Alternatively, if using Gitpod, you can use the link below to create your own workspace using this repository.

    [Open in Gitpod](https://jl14-communityinciden-u2yc7ql938w.ws.codeinstitute-ide.net/)

  4. Install Python module dependencies:
     
    1. Navigate to the folder 'community-incident-forum' by executing the command:
            - `cd /workspace/community-incident-forum`
    2. Run the command pip install -r requirements.txt
            - `pip3 install -r requirements.txt`

### Deploying the project to Heroku to be run as a web application:
1. Clone the repository:
    1. Open a folder on your computer with the terminal.

    2. Run the following command
        - `git clone https://github.com/JL-14/community-incident-forum.git`

2. Create your own GitHub repository to host the code.

    1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

    2. Push the files to your repository with the following command:
        - `git push`

3. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).

4. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

    1. Go to the Deploy tab:

    2. Link your GitHub account and connect the application to the repository you created.

    3. Go to the Settings tab:

    4. Click "Add buildpack":

    5. Add the Python and Node.js buildpacks in the following order:

    6. Click "Reveal Config Vars."

    7. Add 1 new Config Vars:
        - Key: PORT Value: 8000
        - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

    8. Go back to the Deploy tab:

    9. Click "Deploy Branch":

        - Wait for the completion of the deployment.

    10. Click "Open app" to launch the application inside a web page.

---

## Credits


### Content and Images


## Acknowledgements




