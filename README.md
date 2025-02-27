# Studio Booker

![AmIResponsive image of Studio Booker]()

## Introduction

The project is to build a website where you as a user can book a space in a local art studio. If the user doesn't visit the website with the goal to book a studio space right away, the website should work as an inspiration.

The basic functionality of the website is outlined in the image below:

![Flowchart of Studio Booker Functionality](https://res.cloudinary.com/drkz6okfn/image/upload/v1737359270/Site_Functionality_FlowChart_lcd3gi.png)

## Table of Contents

- [Studio Booker](#studiobooker)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
      - [Epic 1 - User account creation process](#epic-1---user-account-creation-process)
      - [Epic 2 - Development of a studio booking system](#epic-2---development-of-a-course-booking-system)
      - [Epic 3 - Development of Studio Blog](#epic-3---development-of-user-testimonials)
      - [Epic 4 - Enhancing website aesthetics](#epic-4---enhancing-website-aesthetics)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
      - [Index page](#index-page)
      - [About page](#about-page)
      - [Booking page](#booking-page)
      - [My bookings page](#my-bookings-page)
      - [Success page](#success-page)
      - [Edit booking page](#edit-booking-page)
      - [Sign up page](#sign-up-page)
      - [Sign in page](#sign-in-page)
      - [Sign out page](#sign-out-page)
      - [404 page](#404-page)
      - [500 page](#500-page)
    - [Entity Relationship Diagram - ERD](#entity-relationship-diagram---erd)
  - [Features](#features)
    - [Header](#header)
      - [Navigation bar](#navigation-bar)
      - [Navigation bar (as a logged in user)](#navigation-bar-as-a-logged-in-user)
      - [Navigation bar (as a staff member or superuser)](#navigation-bar-as-a-staff-member-or-superuser)
    - [Index page](#index-page-1)
      - [Hero image](#hero-image)
      - [Welcome text](#welcome-text)
      - [Member benefits](#member-benefits)
      - [Sign up button](#sign-up-button)
      - [Carousel](#carousel)
    - [About page](#about-page-1)
      - [Profile image](#profile-image)
      - [About text](#about-text)
      - [Testimonial form](#testimonial-form)
      - [Testimonial form response](#testimonial-form-response)
    - [Booking page](#booking-page-1)
      - [Studio presentation](#studio-presentation)
      - [Studio booking](#studio-booking)
      - [Booking pagination](#booking-pagination)
      - [Confirm booking modal](#confirm-booking-modal)
      - [Double booked modal](#double-booked-modal)
    - [Success page](#success-page-1)
      - [Confirmation text](#confirmation-text)
      - [Navigation buttons](#navigation-buttons)
    - [My bookings page](#my-bookings-page-1)
      - [No bookings - text](#no-bookings---text)
      - [No bookings - button](#no-bookings---button)
      - [Active bookings - text](#active-bookings---text)
      - [Active bookings - booked studios](#active-bookings---booked-studios)
      - [Active bookings pagination](#active-bookings-pagination)
      - [Confirm cancellation modal](#confirm-cancellation-modal)
    - [Edit booking page](#edit-booking-page-1)
      - [Available studios](#available-studios)
      - [Available studios pagination](#available-studios-pagination)
      - [Confirm studio change modal](#confirm-studio-change-modal)
    - [Blog page](#blog-page)
    - [Sign up page](#sign-up-page-1)
    - [Sign in page](#sign-in-page-1)
    - [Sign out page](#sign-out-page-1)
    - [404 page](#404-page-1)
      - [404 page text](#404-page-text)
      - [404 page button](#404-page-button)
    - [500 page](#500-page-1)
      - [500 page text](#500-page-text)
      - [500 page tips](#500-page-tips)
    - [Footer](#footer)
  - [Features to be Added](#features-to-be-added)
  - [Testing](#testing)
    - [Validation of Code](#validation-of-code)
      - [HTML](#html)
      - [CSS](#css)
      - [JavaScript](#javascript)
      - [Python](#python)
    - [Lighthouse](#lighthouse)
      - [Desktop](#desktop)
      - [Mobile](#mobile)
    - [Wave Webaim - accessibility testing](#wave-webaim---accessibility-testing)
      - [Index page](#index-page-2)
      - [About page](#about-page-2)
      - [Booking page](#booking-page-2)
    - [Contrast Grid](#contrast-grid)
    - [Automated Testing](#automated-testing)
      - [About](#about)
      - [Booking](#booking)
      - [News](#news)
    - [Manual Testing](#manual-testing)
      - [Navigation bar](#navigation-bar-1)
      - [Index page](#index-page-3)
      - [About page](#about-page-3)
      - [Booking page](#booking-page-3)
      - [Success page](#success-page-2)
      - [My bookings page](#my-bookings-page-2)
      - [Edit booking page](#edit-booking-page-2)
      - [Blog page](#blog-page-1)
      - [Sign up page](#sign-up-page-2)
      - [Sign in page](#sign-in-page-2)
      - [Sign out page](#sign-out-page-2)
      - [404 page](#404-page-2)
      - [500 page](#500-page-2)
      - [Footer](#footer-1)
    - [Bugs](#bugs)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
    - [Fork repository in GitHub](#fork-repository-in-github)
    - [Clone repository in GitHub](#clone-repository-in-github)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
    - [Libraries used](#libraries-used)
    - [Used resources](#used-resources)
    - [Images](#images)
  - [Acknowledgements](#acknowledgements)

## User Experience

### User Goals

One of the user goals is to be able to book an art studio space. The user should also have a smooth experience with full CRUD (Create, Read, Update and Delete) accessibility to their bookings. The goal is also to view already created projects and to inspire the user.

### Site Owner Goals

The site owner goal is to facilitate the frictionless booking of studio spaces for local artists.

### User Stories

For the project, four different Epics were created. To them, a total of 13 user stories were created. To view all user stories, they are viewable at the [Projects board](https://github.com/users/l3wk3m/projects/4). All user stories were assigned one of the following classes; Must have, Should have, Could have or Won't have. 

The following user stories were completed within the first release of Studio Booker.

#### Epic 1 - User account creation process

As a site owner, I would like to create a sign-up process that is intuitive and gets the user able to book studio spaces as soon as possible.

**User Story - Accessing the sign-up page**

As a site user I can easily find and access the sign-up page from the homepage so that I can create an account without confusion or unnecessary delays

- Acceptance Criteria 1  
Given the user is not signed up, the sign-up button will be easy to find.
- Acceptance Criteria 2  
Given a user is not signed up, clicking the sign-up button takes them to the sign up page.

**User Story - Filling in the sign-up form**

As a site user I can enter my personal details into a sign-up form so that I can register for a new account

- Acceptance Criteria 1  
Given the user doesn't have an account, when the user is filling out the sign up form the form includes fields for necessary information (e.g., email, password, confirmation of password)  
- Acceptance Criteria 2  
Given the user doesn't have an account, when the user is filling out the sign up form the form has input validation (e.g., email format)

#### Epic 2 - Development of a studio booking system

As a site owner I would like to have a comprehensive booking system so that users can effortlessly create, read, update and delete bookings.

**User Story - Viewing available studios**

As a Site User I can easily view all current studios so that I can book a studio based on my availability

- Acceptance Criteria 1  
As a site user the booking page is visited displaying a list of available studios  
- Acceptance Criteria 2  
As a site user, the studios list includes crucial details, such as the studio's location, availability, description, etc.  

**User Story - Creating a new booking**

As a Site User I can book a studio so that I can secure my exclusive place

- Acceptance Criteria 1  
As a Site User I can visit the stuio page and view a list of available dates next to / within my desired studio / time slot 
- Acceptance Criteria 2
As a Site User I can click submit my date and time selection for the given studio and recieve confirmation of my choice of studio

**User Story - Viewing my bookings**

As a Site User I can view a list of my current bookings so that I can manage my schedule and review the studio I'm booked into

- Acceptance Criteria 1  
Given the user has a booked studio associate with their account, the user can view their currently booked studios  
- Acceptance Criteria 2  
Given the user has a booked studio associate with their account, they can view the details of any currently booked studios, including date, time, studio name, studio description

**User Story - Modifying an existing booking**

As a Site User / Admin I can change the date or details of my existing studio bookings so that I can adjust my schedule (given the booking is more than 24 hours away)

- Acceptance Criteria 1  
Given the site user has an existing booking, they can modify their bookings via the 'User Panel' page

**User Story - Cancelling a booking**

As a registered user I can cancel a booking if I can no longer attend so that I can manage my commitments and possibly allow others to book the now-available spot

- Acceptance Criteria 1  
Given the user has a booked course  
- Acceptance Criteria 2  
Given the user has a booked course 

#### Epic 3 - Developing Blog functionality

As a site owner I can have a user-friendly blog section so that visitors can easily keep up with the goings on of the different studios and our plans for the future.

**User Story - Accessing the Blog**

As a site user I can easily find and access all of the blog posts, as well as click into each of the posts for expanded details

- Acceptance Criteria 1  
Given the user is anywhere at the website, a clear link to the blog page is available on every page, either in the navigation menu or footer  

**User Story - Submitting a blog post**

As a site superuser I can submit a blog post which will be viewable by site users on the blog page

- Acceptance Criteria 1  
Given the user visits the website in any capacity (no login / registration required) they will be able to view the blog posts of the studio owners

**User Story - Editing Blog Posts**

As a site superuser I can edit details of a post I have published via a clickable link on the post's details page, giving the superuser CRUD capabilities of the blog model

- Acceptance Criteria 1  
I should see a link to an Edit Post page on the post details page if logged in as a superuser
- Acceptance Criteria 2
Any edits I make and submit should edit all the relevant fields of that Blog entry in the blog model  

#### Epic 4 - Enhancing website aesthetics

As a website owner I would like to enhance the visual appeal and user experience of the website so that visitors are more engaged, find the website more trustworthy, and are encouraged to sign up using my service, due to its sleek presentation

**User Story - Implementing a responsive design**

As a site user I can easily navigate and view content so that I can use any device, whether it's a desktop, tablet, or smartphone

- Acceptance Criteria 1  
Given the user is visiting the site the website automatically adjusts its layout based on the screen size and orientation regardless of the device being used

**User Story - Using appealing fonts and color scheme**

As a site user I can visit the website with appealing fonts and a cohesive color scheme so that I'm encouraged to use the service again

- Acceptance Criteria 1  
Given the user doesn't only use screen reader the soft pastel green visuals will create a cohesive visual language evenly applied across the website
- Acceptance Criteria 2  
Given the user doesn't only use screen reader, the user will be able to notice consistency in the art design of the website


## Design

The design is aiming to be to be modern but easy to read. It should draw the attention to the websites core feature, the booking grid. 

### Color Scheme

The color scheme is set to a soft pastel green palette to complement the art work generated for each of the studio images

### Typography

The typography was chosen to 

### Imagery

All the images are chosen to be cartoonish, artful and appealing

### Wireframes

#### Index page

![Wireframe of index page]()

#### About page

![Wireframe of about page]()

#### Booking page

![Wireframe of booking page]()

#### My bookings page

![Wireframe of my bookings page]()

#### Success page

![Wireframe of success page]()

#### Edit booking page

![Wireframe of edit booking page]()

#### Sign up page

![Wireframe of sign up page]()

#### Sign in page

![Wireframe of sign in page]()

#### Sign out page

![Wireframe of sign out page]()

#### 404 page

![Wireframe of 404 page]()

#### 500 page

![Wireframe of 500 page]()

### Entity Relationship Diagram - ERD

Three different models were used in the making of the website.

Their collective ERD is displayed below.

![ERD of Studio Booker Website](https://res.cloudinary.com/drkz6okfn/image/upload/v1737357952/StudioBooker_ERD_mkmviw.png)

## Features

### Index page

#### Hero image

![Hero image at index page](https://res.cloudinary.com/drkz6okfn/image/upload/v1737362710/StudioBooker_HeroImage_odvzk5.webp)
. 

#### Sign up button

![Sign up button below member benefits]()

If the user is visiting the index page without being signed in, there is a sign up button below the member benefits. This is to make it easy for the user to sign up when they have read the fantastic benefits. 

### Blog page

#### Blog text

![A text about the owner and founder of ]()

.

#### Blog

![The Blog page with a list of posts]()

.

### Studios page

#### Studio Space Presentation

![The different studios are presented]()

The different are listed in a grid format and colour-coded using bootstrap's functionality.

#### Studio booking

![The booking section where the user can select which studio they are interested in]()

.

### Success page

#### Confirmation text

![Confirmation text after a successful booking]()

After a successful booking, a text that confirm the booking appears.

#### Navigation buttons

![Three navigation buttons; "View my bookings", "Home" and "Book another studio"]()

Under the confirmation text, three navigation buttons are visible; "View my bookings", "Home" and "Book another studio". On smaller devices, only "View my bookings" and "Book another studio" are visible. These buttons are there to make the user to stay at the website after a successful booking.

### User Panel - the my bookings page

#### No bookings - text

![The text on my booking page explains there is no bookings]()

When the user doesn't have any active bookings, a text informs the user about it. The text informs the user where they can find the booking page.
.

#### Active bookings - text

![Text to notice the user that they have at least one active booking]()

When the user has at least one booking, the details of that booking will appear, along with an option to edit that booking

#### Active bookings - booked studios

![The user bookings are presented]()

The user bookings are presented so that the superuser has access to a list of all booked studios at which times and by who. This was they can plan studio maintenance accordingly.

### Edit booking page

#### Select a New Date

![A user can see the list of available dates for the studio they have booked from the dropdown]()

All available dates are presented for each weekday across the next 14 days. Unavailable / booked dates will not appear in the dropdown.

#### Select a New Timeslot

![Available Timeslots]()

The user can see the list of available remaining timeslots for the studio and date they have chosen. Unavailble / booked options will not appear on the dropdown.

### Sign up page

![Sign up page with fields for email, username, password and password again]()

The sign up page have fields where the user is required to fill out email, username, password and password again. This to make sure the user doesn't get a typo in the password and to ensure the user register a way to contact them.

### Sign in page

![Sign in page with fields for email and password]()

The sign in page allows the user who already has an account to sign in. This to make the user experience smoother where they don't have to fill out their email every time they want to make a booking. It is also an advantage that the user can see all their bookings.

### Sign out page

![Sign out page with a confirmation button]()

The sign out page allows the user to sign out to ensure no one else can edit the users booking. The sign out button ensures the user really wanted to sign out and didn't press on Sign out by mistake.

### 404 page

#### 404 page text

![Text provided when a 404 page is rendered]()

The text explains to the user in a fun way that the page they are looking for doesn't exist. It points the user in the direction of heading back to the homepage to give it a new try.

#### 404 page button

![Button which takes the user to the homepage]()

The button below the 404 text directs the user back to the homepage. This allows the user to give it a new shot to find the page they were looking for.

### 500 page

#### 500 page text

![Screenshot of the text at the 500 page]()

The text at the 500 page explains to the user that the server isn't working as intended. This is to make sure the user knows what is happening.

#### 500 page tips

![The tips of what to do when a 500 page is rendered]()

The tips suggests to the user what they can do; refresh the page or go back to the homepage. The suggestion about going back to the homepage is provided with a link to the homepage.

## Features to be Added

Several features can be added in the future.

- I would add a CRUD feature for the Blog so that a superuser could create a blogpost from the superuser panel
- I would also make it so that the superuser panel allows them to cancel other users' bookings in case they're informally informed of such changes.

## Testing

### Validation of Code

#### HTML

![Screenshot of HTML validation of index page]()

All the pages were tested at the [W3C Markup Validation Service](https://res.cloudinary.com/drkz6okfn/image/upload/v1737374005/html_validation_fnxidt.png)

#### CSS

![Screenshot of CSS validation](https://res.cloudinary.com/drkz6okfn/image/upload/v1737373716/css_validation_vdtu6p.png)

The CSS code was tested at [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). It resulted in.

![CSS Validator Test]()

#### Python

All Python files have been validated through [CI Python Linter](https://pep8ci.herokuapp.com/) to make sure the code meets the standards of PEP8. The validation resulted without errors.

**Bookings - views.py**

![Python validation of views.py in bookings]()

**About - views.py**

![Python validation of views.py in about]()

**News - views.py**

![Python validation of views.py in news]()

- [Python validation of models.py in bookings]()
- [Python validation of admin.py in news]()
- [Python validation of models.py in news]()

### Lighthouse

Tests in Lighthouse were performed for both desktop and mobile.

#### Desktop

![Lighthouse test for desktop](https://res.cloudinary.com/drkz6okfn/image/upload/v1737373197/Desktop_Lighthouse_fmagrj.png)

The test for desktop resulted in 100 in both best practices and accessibility. It also resulted in 82 in both performance and SEO.

### Wave Webaim - accessibility testing

The accessibility test at [Wave Webaim](https://wave.webaim.org/) resulted with two contrast errors.

#### Index page

![Wave webaim test of index page](https://res.cloudinary.com/drkz6okfn/image/upload/v1737373450/WebAim_jjilpy.png)

#### Booking page

![Wave webaim test of about page](https://res.cloudinary.com/drkz6okfn/image/upload/v1737373556/bookings_webaim_gr5thg.png)

### Manual Testing

Every page at the website has been manually tested. It is done in Google Chrome DevTools and on different devices. The devices used were one mobile phone, one laptop and one external screen:

- Fairphone 4 5G (1080 x 2400)
- Macbook Pro 2020 (1366 x 768)

#### Navigation bar

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Home link | When clicked, directs the user to the home page | Click at "Home" | Got directed to the home page | Pass |
| Blog link | When clicked, directs the user to the blog page | Click at "Blog" | Got directed to the blog page | Pass |
| Booking link | When clicked, directs the user to the booking page | Click at "Booking" | Got directed to the booking page | Pass |
| Sign up link | When clicked, directs the user to the sign up page | Click at "Sign up" | Got directed to the sign up page | Pass |
| Sign in link | When clicked, directs the user to the sign in page | Click at "Sign in" | Got directed to the sign in page | Pass |
| Sing in link not visible (signed out) | Sing in link not visible as a signed out user | Sign out and inspect navigation bar | Sign In link not visible | Pass |
| My bookings link not visible | My bookings link not visible as a signed out user | Sign out and inspect navigation bar | My bookings link not visible | Fail |
| Me bookings link visible | My bookings link visible as a signed in user | Sign in, check navigation bar | My bookings link visible | Fail |
| Username showing (signed in user) | When the user is signed in, the username is presented as the link to my bookings | Sign in, check navigation bar | Username is showing | Pass |
| My bookings link | When clicked, directs the signed in user to my bookings page | Click at username | Got directed to the my bookings page | Pass |
| Sign out link | When clicked, directs the user to the sign out page | Click at "Sign out" | Got directed to the sign out page | Pass |

#### Index page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The index page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Sign up button visible (not signed in) | The sign up button below member benefits is visible when the user isn't signed in | Sign out and check below member benefits | Sign up button is visible | Pass |
| Sign up button not visible (signed in) | The sign up button below member benefits is not visible when the user is signed in | Sign in and check below member benefits | Sign up button isn't visible | Pass |

#### Blog page
		
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The about page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Blog form validation | A message appears if the user doesn't fill out all fields | Fill out all fields except one, let all different fields (First name, Last name, Email and Message) be the empty field one by one | A message appears when a field is left empty | Fail |

#### Booking page
		
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The booking page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Read more button | The text about the stuido expands and shows more text when the "Read more" button is pressed | Press "Read more" in the studio card | The text expanded and showed more text | Fail |
| Read less button | The expanded text about Perler beads studio goes back to "normal" when the "Read less" button is pressed | Press "Read less" in the studio card | The text collapsed and went back to normal | Fail |
| Double booking notification | When a user tries to book a studio session they already has a booking at, a Booking notice modal is triggered | Try to book a studio where an active booking already exists | A modal is triggered when the user tries to double book | Fail |

#### Success page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| View my bookings button | The "View my bookings (user panel)" button directs the user to My bookings page | Click at "View my bookings" button | The user got directed to the My bookings page | Pass |
| Book another studio button | The "Book another studio" button directs the user to Bookings page - booking buttons section | Click at "Book another studio" | The user got directed to the Booking page, booking buttons section | Pass |
| Home button - not visible | On devices smaller than 768px (breakpoint below medium in Bootstrap), the "Home" button is not visible | Select breakpoint smaller than medium and view the page | The "Home" button is not visible | Fail |
| Home button - visible | On devices with 768px or larger (breakpoint medium or larger in Bootstrap), the "Home" button is visible | Select medium breakpoint and view the page | The "Home" button is visible | Pass |

#### My bookings page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Username in text | In the first sentence, the username is presented | Sign in and compare the username with the presented name | The username and the presented name is equal | Fail |
| Active bookings | All of the user's active bookings are presented | Compare active bookings in the admin panel to the presented active bookings | The active bookings are the same in the admin panel as presented at My bookings page | __ |
| Edit button | When the "Edit" button is pressed, the user gets directed to Edit booking page | Press "Edit" button | The user got directed to Edit booking page | Pass |
| Available spots increase | When a booking is cancelled, available spots are increased by one | Check available spots at an already booked studio, cancel the booking and check available spots again | Available spots increased by one | __ |
| Pagination | When it is more than 12 upcoming studio, pagination appears | Scroll down below my bookings buttons | After four bookings, pagination buttons appears | Pass |
| No bookings - text | A text about no bookings were found appears at the top of the page | Cancel all the user's bookings | No bookings were found text appeared | Fail |
| No bookings - Take me there button | The "Take me there" button directs the user to booking page | Click at "Take me there" button | The user got directed to booking page | __ |

#### Edit booking page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Available studios | Only sessions where the user doesn't already have an active booking is shown | Compare upcoming studio availability, the user's active bookings and the available sessions in edit booking | Only sessions where the user doesn't have an active booking are visible | Pass |
| Booking buttons - trigger modal | When a booking button is pressed, a confirmation modal is triggered | Click all booking buttons | All booking buttons triggered a confirmation modal | __ |
| Available spots - increase | In the session the user cancel their booking, available spots increases by one | Check available spots at the session, edit the booking, check available spots again | Available spots increased by one | Pass |
| Available spots - decrease | The available spots in the new session the user chooses, decreases by one | Check available spots at the session, edit the booking, check available spots again | Available spots decreased by one | Pass |
| Pagination | When it is more than 20 available studios, pagination appears | Scroll down below active bookings buttons | After eight bookings, pagination buttons appears | Fail |

#### Sign up page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to sign up but leaves one field empty | Leave one field empty one by one and try to Sign Up | An error message appeared when a field was left empty | Fail |
| Redirected | When the "Sign Up" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign up, fill out all required fields, press "Sign Up" button | The user got redirected to Booking page | Pass |

#### Sign in page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to sign in but leaves one field empty | Leave one field empty one by one and try to Sign In | An error message appeared when a field was left empty | Pass |
| Sign In button | When the "Sign In" button is pressed, the user gets signed in | Click at "Sign In" button | The user gets signed in | Pass |
| Redirected | When the "Sign In" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign in, press "Sign In" button | The user got redirected to Booking page | Fail |

#### Sign out page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Sign Out button | When the "Sign Out" button is pressed, the user gets signed out | Click at "Sign Out" button | The user gets signed out | Pass |
| Redirected | When the "Sign Out" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign out, press "Sign Out" button | The user got redirected to Booking page | Pass |

#### 404 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Return to stability button | When "Return to stability" button is pressed, the user gets directed to the home page | Click at "Return to stability" button | The user got directed to the home page | Pass |

#### 500 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Link to homepage | When the link to the homepage is clicked, the user gets directed to the homepage | Click at homepage link | The user got directed to the homepage | __ |

### Bugs

During the testing several bugs have been discovered. No bugs were left unfixed.

When  

## Technologies Used

The repository is created from [Code Institutes Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template) through [GitHub](https://github.com/). The Project board is created at [GitHub](https://github.com/). The code is written in [Gitpod](https://www.gitpod.io/) and deployed at [Heroku](https://www.heroku.com/). The wireframes are created in [Balsamiq](https://balsamiq.com/) and the ERD's are created in [Google Spreadsheet](https://docs.google.com/spreadsheets/).

The code languages used in this project are HTML, CSS, JavaScript and Python. The main frameworks used are Django and Bootstrap.

## Deployment

### Fork repository in GitHub

- Open the chosen repository in GitHub 
- Click on the "Fork" button
- A copy of the repository is now located in your own account

### Clone repository in GitHub

- Open the chosen repository in GitHub 
- Click on "Code" button
- Copy the URL
- Open your command line interface
- Navigate to the directory you want to clone the repository to
- Use 'git clone', followed by the earlier copied URL
- Move into the newly created directory
- Install the dependencies using 'pip install -r requirements.txt'
- Run the application with 'python manage.py runserver'

### Deployment to Heroku

- Open Heroku and log in
- Click on "New" and choose the option "Create new app"
- Choose an app name and which region (Europe or United States) you are located in
- Press "Create app"
- When the app is created, choose the Settings tab
- Under "Config Vars", press "Reveal Config Vars"
- In keys, write DATABASE_URL
- In value, insert the url to the database
- Press "Add"
- Under "Buildpacks", press "Add buildpack"
- Choose "Python", press "Add buildpack"
- Change tab to the Deploy tab
- Choose deploy method - GitHub
- Search for the correct repository name at your connected GitHub account
- Press "Connect"
- Under "Manual deploy", choose which branch to deploy and press "Deploy Branch"

Link to deployed website: <https://_____.herokuapp.com/>

## Credits

### Libraries used

| Library | Functionality |
| ------------------- | --------------------------------- |
| django-allauth | Used for authentication, registration and account management |
| django-summernote | Integrated editor in djangos admin panel |
| gunicorn | Used to run Python web applications |
| oauthlib | Used to implement OAuth functionality |
| sendgrid | For interacting with the SendGrid email service |
| urllib3 | Used to make HTTP requests |
| whitenoise | Simplifies static file serving for Python web apps |

### Used resources

| Page | Used for |
| --------------| ----------------- |
| [Djecrety](https://djecrety.ir/) | Generate a secret key |
| [Frida Wikell](https://github.com/FridaWikell/frisa-booking) | For the ReadMe format |
| [Font Awesome](https://fontawesome.com/) | All icons at the website |
| [W3Schools](https://www.w3schools.com/howto/howto_js_read_more.asp) | Base for read more/read less buttons |
| [django](https://docs.djangoproject.com/) | Knowledge about django |
| [Emojipedia](https://emojipedia.org/) | Select emojis |
https://learndjango.com/tutorials/django-testing-tutorial
| [Learn Django](https://learndjango.com/tutorials/django-testing-tutorial) | Learn Django's page on testing |

### Images

| Page | Used for |
| ------------- | --------------- |
| [Vecteezy](https://www.vecteezy.com/photo/_) | Background image at 500 page, from [_](https://www.vecteezy.com/members/_) |
| [BeFunky](https://www.befunky.com/) | Edit and resize images |
| [Pixelied](https://pixelied.com/convert) | Convert images to webp |
| [TinyPNG](https://tinypng.com/) | Compress images |

All other photos are taken by the website creator, [Luke Maycock](https://github.com/l3wk3m).

## Acknowledgements

Logic for bookings views and function was inspired by:
[Clinic Booker](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)

My blog app was worked up when doing the Django Girls tutorial upon recommendation from my mentor
[Django Girls](https://djangogirls.org/en/)

Custom user model setup was taken from
[Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)

A big thanks to my mentor Ronan McLeland for feedback and direction throughout!

[Back to top](#studiobooker)