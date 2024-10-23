# Studio Booker

![AmIResponsive image of Studio Booker]()

## Introduction

The project is to build a website where you as a user can book a space in a local art studio. If the user doesn't visit the website with the goal to book a studio space right away, the website should work as an inspiration.

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
      - [Epic 3 - Development of user testimonials](#epic-3---development-of-user-testimonials)
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
    - [News page](#news-page)
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
      - [News page](#news-page-1)
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

One of the user goals is to be able to book __________. The user should also have a smooth experience with full CRUD (Create, Read, Update and Delete) accessibility to their bookings. The goal is also to view already created projects and to inspire the user.

### Site Owner Goals

The site owner goal is to facilitate the frictionless booking of studio spaces for local artists.

### User Stories

For the project, four different Epics were created. To them, a total of 13 user stories were created. To view all user stories, they are viewable at the [Projects board](). All user stories were assigned one of the following classes; Must have, Should have, Could have or Won't have. 

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

As a Site User I can easily view all available studios so that I can book a studio based on my availability

- Acceptance Criteria 1  
As a site user the booking page is visited displaying a list of available studios  
- Acceptance Criteria 2  
As a site user, the studios list includes crucial details, such as the studio's location, availability, description, etc.  

**User Story - Creating a new booking**

As a Site User I can book a studio so that I can secure my exclusive place

- Acceptance Criteria 1  
As a Site User I can visit the booking page and view a "Book" button next to / within my desired studio / time slot 
- Acceptance Criteria 2
As a Site User I can click the "Book" button and recieve confirmation of my choice of studio

**User Story - Viewing my bookings**

As a Site User I can view a list of my current bookings so that I can manage my schedule and review the studio I'm booked into

- Acceptance Criteria 1  
Given the user has a booked studio associate with their account, the user can view their currently booked studios  
- Acceptance Criteria 2  
Given the user has a booked studio associate with their account, they can view the details of any currently booked studios, including date, time, studio name, studio description

**User Story - Modifying an existing booking**

As a Site User / Admin I can change the date or details of my existing studio bookings so that I can adjust my schedule

- Acceptance Criteria 1  
Given the site user has an existing booking, they can modify their bookings via the 'My Bookings' page

**User Story - Cancelling a booking**

As a registered user I can cancel a booking if I can no longer attend so that I can manage my commitments and possibly allow others to book the now-available spot

- Acceptance Criteria 1  
Given the user has a booked course  
- Acceptance Criteria 2  
Given the user has a booked course 

**User Story - Implement modal pop-up confirmations for booking and booking changes**

As a site user I can receive immediate, clear confirmation requests in the form of modal pop-ups whenever I attempt to make any changes to my bookings so that instantly understand the impact of my actions

- Acceptance Criteria 1  
Given a user is on the booking or booking modification page when the user initiates a new booking or change to an existing booking, a modal pop-up should immediately appear, confirming the booking or change  
- Acceptance Criteria 2  
Given a modal pop-up is displayed to the user, if the user clicks confirm it will confirm the booking / change of booking with the user and update the relevant database models
- Acceptance Criteria 3  
Given a modal pop-up is displayed to the user when the user clicks the "Cancel" button the modal closes without making any modifications to the booking

#### Epic 3 - Developing User Testimonial functionality

As a site owner I can have a user-friendly testimonials section so that visitors can easily send feedback about their experiences if they've booked with Studio Booker before and can see the feedback of previous users

**User Story - Accessing the testimonial form**

As a site user I can easily find and access the testimonial form from any page on the website so that I am as encouraged to leave feedback as is possible

- Acceptance Criteria 1  
Given the user is anywhere at the website, a clear link to the testimonials page is available on every page, either in the navigation menu or footer  
- Acceptance Criteria 2  

**User Story - Submitting a testimonial**

As a site user I can submit a testimonial using the form so that I can communicate my with the studios and this website

- Acceptance Criteria 1  
Given the user has any feedback or experience booking with Studio Booker   
- Acceptance Criteria 2  

- Acceptance Criteria 3  


**User Story - Receive confirmation after sending testimonial form**

As a site user I can receive immediate confirmation that my testimonial has been sent successfully when I submit the form so that I am assured my testimonial has been received

- Acceptance Criteria 1  
I should see a confirmation message on the website indicating that my message has been sent successfully  

#### Epic 4 - Enhancing website aesthetics

As a website owner I would like to enhance the visual appeal and user experience of the website so that visitors are more engaged, find the website more trustworthy, and are encouraged to sign up using my service, due to its sleek presentation

**User Story - Implementing a responsive design**

As a site user I can easily navigate and view content so that I can use any device, whether it's a desktop, tablet, or smartphone

- Acceptance Criteria 1  
Given the user is visiting the site the website automatically adjusts its layout based on the screen size and orientation regardless of the device being used
- Acceptance Criteria 2  
Given the user is 
- Acceptance Criteria 3  
Given the user is  

**User Story - Using appealing fonts and color scheme**

As a site user I can visit the website with appealing fonts and a cohesive color scheme so that 

- Acceptance Criteria 1  
Given the user doesn't only use screen reader 
- Acceptance Criteria 2  
Given the user doesn't only use screen reader
- Acceptance Criteria 3  
Given the user doesn't only use screen reader


## Design

The design is aiming to be to be modern but easy to read. It should draw the attention to the websites core feature, the booking grid. 

### Color Scheme

The color scheme is set to  

### Typography

The typography was chosen to 

### Imagery

All the images are chosen to 

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

![ERD of Artist Model](docs/images/Artists_ERD.webp)

![ERD of Studio Model](docs/images/Studio_ERD.webp)

![ERD of Studio Model](docs/images/StudioBooking_ERD.webp)

## Features

### Header

#### Navigation bar

![Navigation bar as a not logged in user]()

.

#### Navigation bar (as a logged in user)

![Navigation bar as a logged in user]()

. 

#### Navigation bar (as a staff member or superuser)

![Navigation bar as a staff member or superuser]()

.

### Index page

#### Hero image

![Hero image at index page]()

.

#### Welcome text

![Welcome text at index page]()

.

#### Member benefits

![Benefits of becoming a member]()

. 

#### Sign up button

![Sign up button below member benefits]()

If the user is visiting the index page without being signed in, there is a sign up button below the member benefits. This is to make it easy for the user to sign up when they have read the fantastic benefits. 

#### Carousel

![Carousel of images]()

.

### About page

#### Profile image

![Profile image at the about page](d)

. 

#### About text

![A text about the owner and founder of ]()

.

#### Testimonial form

![The testimonial form at the about page]()

.

#### Testimonials Form

![The response after submitting the testimonials form]()

.

### Studios page

#### Studio Space Presentation

![The different studios are presented]()

The different are listed in a grid format and colour-coded using bootstrap's functionality.

#### Studio booking

![The booking section where the user can select which studio they are interested in]()

.

#### Booking pagination

![Pagination at booking page]()

.

#### Confirm booking modal

![Confirmation modal after a booking button in pressed]()

.

#### Double booked modal

![Modal to show that the user already has a booking at the chosen studio space]()

A double booking modal is triggered when the user tries to book a .

### Success page

#### Confirmation text

![Confirmation text after a successful booking]()

After a successful booking, a text that confirm the booking appears.

#### Navigation buttons

![Three navigation buttons; "View my bookings", "Home" and "Book another studio"]()

Under the confirmation text, three navigation buttons are visible; "View my bookings", "Home" and "Book another studio". On smaller devices, only "View my bookings" and "Book another studio" are visible. These buttons are there to make the user to stay at the website after a successful booking.

### My bookings page

#### No bookings - text

![The text on my booking page explains there is no bookings]()

When the user doesn't have any active bookings, a text informs the user about it. The text informs the user where they can find the booking page.

#### No bookings - button

![Button to direct the user to the booking page]()

.

#### Active bookings - text

![Text to notice the user that they have at least one active booking]()

When the user has at least one booking, 

#### Active bookings - booked studios

![The user bookings are presented]()

The user bookings are presented so that the booking that is next in time appears first. Each booked studio card has an Edit button and a Cancel button. When the Edit button is pressed, the user gets directed to the edit booking page. When the Cancel button is pressed, a confirmation modal is triggered. These two buttons allows the user to edit and delete the booked session if the user has to change their plans.

#### Active bookings pagination

![My bookings pagination]()

If the user has more than four active bookings, a pagination appears below the active bookings. This is to enhance the user experience, to make it easier for the user to see their active bookings.

#### Confirm cancellation modal

![Modal that the user gets to assure that they want to cancel their booking](doc/confirm-delete.webp)

When the user presses the Cancel button in their active bookings, a confirm cancellation modal is triggered. This is to make sure the user didn't press Cancel by mistake. The Confirm button in the modal is red to mark that if you press it, something that is irreversible will happen.

### Edit booking page

#### Available Studios

![All available studios presented as booking buttons]()

All available studios are presented in a  .

#### Available Studios Pagination

![Available Studios Pagination]()

If there are more than eight available studios to select from, pagination appears. This is to enhance the user experience, to avoid scrolling through a wall of available studios.

#### Confirm studio change modal

![Confirmation modal to ensure the user wants to change their studio booking]()

The confirmation modal ensures that the user wants to edit their booking to the selected .

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

### Footer

![Footer with developers name and year to the left and links to the Testimoial form and connecting Facebook, Instagram and Pinterest accounts]()

.

## Features to be Added

Several features can be added in the future.

- 

## Testing

### Validation of Code

#### HTML

![Screenshot of HTML validation of index page]()

All the pages were tested at the [W3C Markup Validation Service](). The index page validation is presented above, all the other validations are linked below.

- [About page](doc/)
- [Booking page]()
- [My bookings]()
- [News page]()
- [Edit booking]()
- [Success page]()
- [404 page]()
- [500 page]()

#### CSS

![Screenshot of CSS validation](doc/css-valid.webp)

The CSS code was tested at [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). It resulted in.

#### JavaScript

All JavaScript files were validated through [JSHint](https://jshint.com/). The validation rendered without errors. 


**Booking page**

![JavaScript validation of Booking page]()

**Edit booking page**

![JavaScript validation of Edit booking]()

**Delete booking**

![JavaScript validation of Delete booking]()

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

![Lighthouse test for desktop]()

The test for desktop resulted in __ in both performance and accessibility. It also resulted in __ in both best practice and SEO.

#### Mobile

![Lighthouse test for mobile](doc/lighthouse-mobile.webp)

The test for mobile resulted in __.

### Wave Webaim - accessibility testing

The accessibility test at [Wave Webaim](https://wave.webaim.org/) resulted without errors and contrast errors on all pages.

#### Index page

![Wave webaim test of index page]()

#### About page

![Wave webaim test of about page]()

#### Booking page

![Wave webaim test of about page]()

### Contrast Grid

The [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23CACACA%2C%20%20Background%20color%0D%0A%23353535%2C%20Text%0D%0A%23411919%2C%20Cancel%20btn%20-%20background%0D%0A%23FFFFFF%2C%20Cancel%2Fconfirm%2Fdelete%20btn%20-%20text%0D%0A%23193A18%2C%20Confirm%20btn%20-%20background%0D%0A%238d3838%2C%20Delete%20btn%20-%20background%0D%0A%23000000%2C%20Footer%20icons&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) resulted in only AAA results for the combination used on the webpage. The main combination throughout the page is #CACACA and #353535 which has a value of 7.4 (where the limit for AAA is 7+).

![Contrast Grid of the webpage]()

### Automated Testing

Automated testing is done for all three different apps (about, booking and testimonials). In total, 33 tests were made - 8 tests in about, 12 tests in booking and 13 tests in news.

![Automated tests for all apps]()

#### About

![Automated tests for about app]()

- [Test of forms.py]()
- [Test of views.py]()

#### Booking

![Automated tests for booking app]()

- [Test of models.py]()
- [Test of views.py]()

#### Testimonials

![Automated tests for news app]()

- [Tests of admin.py]()
- [Tests of models.py]()
- [Tests of views.py]()

### Manual Testing

Every page at the website has been manually tested. It is done in Google Chrome DevTools and on different devices. The devices used were one mobile phone, one laptop and one external screen:

- Fairphone 4 5G (1080 x 2400)
- Macbook Pro 2020 (1366 x 768)

#### Navigation bar

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Home link | When clicked, directs the user to the home page | Click at "Home" | Got directed to the home page | __ |
| About link | When clicked, directs the user to the about page | Click at "About" | Got directed to the about page | __ |
| Booking link | When clicked, directs the user to the booking page | Click at "Booking" | Got directed to the booking page | __ |
| Sign up link | When clicked, directs the user to the sign up page | Click at "Sign up" | Got directed to the sign up page | __ |
| Sign in link | When clicked, directs the user to the sign in page | Click at "Sign in" | Got directed to the sign in page | __ |
| News link not visible (signed out) | News link not visible as a signed out user | Sign out and inspect navigation bar | News link not visible | __ |
| News link not visible (signed in user - regular) | News link not visible as a signed in user (without staff or superuser credentials) | Sign in as a regular user, check navigation bar | News link not visible | __ |
| News link visible (signed in user - staff or superuser) | News link visible as a signed in user (with staff or superuser credentials) | Sign in as staff or superuser, check navigation bar | News link visible | __ |
| News link | When clicked, directs the signed in user (staff or superuser) to the news page | Sign in as a staff or superuser, click at "News" | Got directed to the news page | __ |
| My bookings link not visible | My bookings link not visible as a signed out user | Sign out and inspect navigation bar | My bookings link not visible | __ |
| Me bookings link visible | My bookings link visible as a signed in user | Sign in, check navigation bar | My bookings link visible | __ |
| Username showing (signed in user) | When the user is signed in, the username is presented as the link to my bookings | Sign in, check navigation bar | Username is showing | __ |
| My bookings link | When clicked, directs the signed in user to my bookings page | Click at username | Got directed to the my bookings page | __ |
| Sign out link | When clicked, directs the user to the sign out page | Click at "Sign out" | Got directed to the sign out page | __ |

#### Index page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The index page was responsive and changed depending on screen size | __ |
| "Check out available studios" button | Directs the user to the Booking page | Click at the "Check out available studios" button | Got directed to the Booking page | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Sign up button visible (not signed in) | The sign up button below member benefits is visible when the user isn't signed in | Sign out and check below member benefits | Sign up button is visible | __ |
| Sign up button not visible (signed in) | The sign up button below member benefits is not visible when the user is signed in | Sign in and check below member benefits | Sign up button isn't visible | __ |
| Text at image carousel | The text at the image carousel is readable | Read the text at all Bootstrap breakpoints | The text is readable | __ |
| Start image in carousel | Start image is always the one with "Fancy some inspiration" text | Browse through the image carousel and leave it at different images before refreshing the page | The carousel always begins at "Fancy some inspiration" image | __ |
| Image carousel never stops | The carousel doesn't stop, when all images are showed it starts over again | Browse through all images at both directions | When the last image is shown, the first image appears when the next arrow is pressed | __ | 

#### About page
		
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The about page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| __ form validation | A message appears if the user doesn't fill out all fields | Fill out all fields except one, let all different fields (First name, Last name, Email and Message) be the empty field one by one | A message appears when a field is left empty | __ |
| testimoial form response | Response appears, confirming to the user that the form has been sent | Fill out the form with valid input and press Submit | The testimoial form changed into a message confirming that the message has been sent | __ |
| Testimonial form message recieved | The submitted form is sent to selected inbox in Mailtrap | Fill out the form with valid input and press Submit, log in to Mailtrap and view selected inbox | The message from the testimonial form are sent to Mailtrap | __ |

#### Booking page
		
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The booking page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Read more button | The text about the stuido expands and shows more text when the "Read more" button is pressed | Press "Read more" in the studio card | The text expanded and showed more text | __ |
| Read less button | The expanded text about Perler beads studio goes back to "normal" when the "Read less" button is pressed | Press "Read less" in the studio card | The text collapsed and went back to normal | __ |
| Booking buttons - trigger modal | When a booking button is pressed, a confirmation modal is triggered | Click all booking buttons | All booking buttons triggered a confirmation modal | __ |
| Confirmation modal - X | When the X at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press X | The modal closed without making any booking | __ |
| Confirmation modal - Close | When the "Close" button at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press "Close" | The modal closed without making any booking | __ |
| Confirmation modal - outside modal | When the user clicks anywhere outside of the confirmation modal, it is closed without making any booking | Trigger confirmation modal, click somewhere outside of the modal | The modal closed without making any booking | __ |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, a booking is made | Press "Confirm", check "My bookings" if a booking has been made | A booking was made | __ |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, the user gets redirected to Success page | Press "Confirm" | The user got directed to the Success page | __ |
| Pagination | When it is more than 20 studios, pagination appears | Scroll down below active bookings buttons | After eight bookings, pagination buttons appears | __ |
| Pagination - stay at bookings buttons section | When you change between the pages of active booking buttons, you come to the top of the booking buttons | Change page using pagination | When next button is pressed, the second page is showed and scrolled to the top of booking buttons | __ |
| Double booking modal | When a user tries to book a studio session they already has a booking at, a Booking notice modal is triggered | Try to book a studio where an active booking already exists | A modal is triggered when the user tries to double book | __ |
| Double booking modal - X | When the X at the double booking modal is pressed, the modal is closed without making any booking | Trigger double booking modal, press X | The modal closed without making any booking | __ |
| Double booking modal - Close | When the "Close" button at the double booking modal is pressed, the modal is closed without making any booking | Trigger double booking modal, press "Close" | The modal closed without making any booking | __ |

#### Success page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| View my bookings button | The "View my bookings" button directs the user to My bookings page | Click at "View my bookings" button | The user got directed to the My bookings page | __ |
| Book another studio button | The "Book another studio" button directs the user to Bookings page - booking buttons section | Click at "Book another studio" | The user got directed to the Booking page, booking buttons section | __ |
| Home button - not visible | On devices smaller than 768px (breakpoint below medium in Bootstrap), the "Home" button is not visible | Select breakpoint smaller than medium and view the page | The "Home" button is not visible | __ |
| Home button - visible | On devices with 768px or larger (breakpoint medium or larger in Bootstrap), the "Home" button is visible | Select medium breakpoint and view the page | The "Home" button is visible | __ |

#### My bookings page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Username in text | In the first sentence, the username is presented | Sign in and compare the username with the presented name | The username and the presented name is equal | __ |
| Active bookings | All of the user's active bookings are presented | Compare active bookings in the admin panel to the presented active bookings | The active bookings are the same in the admin panel as presented at My bookings page | __ |
| Edit button | When the "Edit" button is pressed, the user gets directed to Edit booking page | Press "Edit" button | The user got directed to Edit booking page | __ |
| Cancel button | When the "Cancel" button is pressed, a confirmation modal is triggered | Press "Cancel" button | A confirmation modal is triggered | __ |
| Confirmation modal - X | When the X at the confirmation modal is pressed, the modal is closed without cancelling the booking | Trigger confirmation modal, press X | The modal closed without cancelling the booking | __ |
| Confirmation modal - Close | When the "Close" button at the confirmation modal is pressed, the modal is closed without cancelling the booking | Trigger confirmation modal, press "Close" | The modal closed without cancelling the booking | __ |
| Confirmation modal - outside modal | When the user click anywhere outside of the confirmation modal, it is closed without cancelling the booking | Trigger confirmation modal, click somewhere outside of the modal | The modal closed without cancelling the booking | __ |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, the booking is cancelled | Trigger confirmat modal, press "Confirm", check "My bookings" if the booking has been cancelled | The booking was cancelled | __ |
| Available spots increase | When a booking is cancelled, available spots are increased by one | Check available spots at an already booked studio, cancel the booking and check available spots again | Available spots increased by one | __ |
| Pagination | When it is more than 12 upcoming studio, pagination appears | Scroll down below my bookings buttons | After four bookings, pagination buttons appears | __ |
| No bookings - text | A text about no bookings were found appears at the top of the page | Cancel all the user's bookings | No bookings were found text appeared | __ |
| No bookings - Take me there button | The "Take me there" button directs the user to booking page | Click at "Take me there" button | The user got directed to booking page | __ |

#### Edit booking page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Available studios | Only sessions where the user doesn't already have an active booking is shown | Compare upcoming studio availability, the user's active bookings and the available sessions in edit booking | Only sessions where the user doesn't have an active booking are visible | __ |
| Booking buttons - trigger modal | When a booking button is pressed, a confirmation modal is triggered | Click all booking buttons | All booking buttons triggered a confirmation modal | __ |
| Confirmation modal - X | When the X at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press X | The modal closed without making any booking | __ |
| Confirmation modal - Close | When the "Close" button at the confirmation modal is pressed, the modal is closed without making any booking | Trigger confirmation modal, press "Close" | The modal closed without making any booking | __ |
| Confirmation modal - outside modal | When the user click anywhere outside of the confirmation modal, it is closed without making any booking | Trigger confirmation modal, click somewhere outside of the modal | The modal closed without making any booking | __ |
| Confirmation modal - Confirm | When the "Confirm" button is pressed, the existing booking is changed to the selected studio session | Trigger confirmation modal, press "Confirm", check "My bookings" if the booking has been changed | The booking was changed | __ |
| Available spots - increase | In the session the user cancel their booking, available spots increases by one | Check available spots at the session, edit the booking, check available spots again | Available spots increased by one | __ |
| Available spots - decrease | The available spots in the new session the user chooses, decreases by one | Check available spots at the session, edit the booking, check available spots again | Available spots decreased by one | __ |
| Pagination | When it is more than 20 available studios, pagination appears | Scroll down below active bookings buttons | After eight bookings, pagination buttons appears | __ |

#### Testimonials page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Color change - every other | Every other news have dark backgrounds, every other light backgrounds | Scroll through the news | Every other news has dark background, every other news has light background | __ |

#### Sign up page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| All fields required | An error message appears when the user tries to sign up but leaves one field empty | Leave one field empty one by one and try to Sign Up | An error message appeared when a field was left empty | __ |
| Redirected | When the "Sign Up" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign up, fill out all required fields, press "Sign Up" button | The user got redirected to Booking page | __ |

#### Sign in page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| All fields required | An error message appears when the user tries to sign in but leaves one field empty | Leave one field empty one by one and try to Sign In | An error message appeared when a field was left empty | __ |
| Sign In button | When the "Sign In" button is pressed, the user gets signed in | Click at "Sign In" button | The user gets signed in | __ |
| Redirected | When the "Sign In" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign in, press "Sign In" button | The user got redirected to Booking page | __ |

#### Sign out page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Sign Out button | When the "Sign Out" button is pressed, the user gets signed out | Click at "Sign Out" button | The user gets signed out | __ |
| Redirected | When the "Sign Out" button is pressed, the user gets redirected to the page they visited before | Visit Booking page, click Sign out, press "Sign Out" button | The user got redirected to Booking page | __ |

#### 404 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Return to stability button | When "Return to stability" button is pressed, the user gets directed to the home page | Click at "Return to stability" button | The user got directed to the home page | __ |

#### 500 page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | __ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Link to homepage | When the link to the homepage is clicked, the user gets directed to the homepage | Click at homepage link | The user got directed to the homepage | __ |
| Link to testimoial form | When the link to the testimoial form is clicked, the user gets directed to the testimoial form | Click at the link to the testimoial form | The user got directed to the testimoial form | __ | 

#### Footer

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The footer changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The footer was responsive and changed depending on screen size | ___ |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | __ |
| Link to testimonial form | When the pencil icon is clicked, the user gets directed to the testimonial form | Click at the icon | The user got directed to the testimonial form | __ |
| Link to Facebook | When the Facebook icon is clicked, the user gets directed to Facebook which opens in a new tab | Click at the Facebook icon | The user got directed to Facebook which opens in a new tab | __ |
| Link to Instagram | When the Instagram icon is clicked, the user gets directed to Instagram which opens in a new tab | Click at the Instagram icon | The user got directed to Instagram which opens in a new tab | __ |
| Link to Pinterest | When the Pinterest icon is clicked, the user gets directed to Pinterest which opens in a new tab | Click at the Pinterest icon | The user got directed to Pinterest which opens in a new tab | __ |

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

A big thanks to my mentor Ronan McLeland for feedback and direction throughout!

[Back to top](#studiobooker)