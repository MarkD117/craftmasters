# Craft Masters

Welcome to Craft Masters, a vibrant online community where woodworking enthusiasts of all skill levels come together to celebrate the artistry of woodcraft. The Craft Masters blog is a dedicated space for passionate individuals to showcase their woodworking projects, share insights, and inspire fellow craftsmen. 

Whether you're a seasoned woodworker with years of experience or a newcomer eager to explore the world of woodworking, Craft Masters is your haven. Join in on this creative journey, where each project is a masterpiece and every craftsperson is a master in their own right. Let the sawdust fly and the creativity flourish – welcome to Craft Masters, where the beauty of woodworking knows no bounds.

The live project can be accessed [here]()

![Screenshot](documentation/)

## Index – Table of Contents

* [UI/UX](#uiux)
* [Agile Development](#agile-development)
* [User Stories](#user-stories)
* [Database Structure](#database-structure)
* [Wireframes](#wireframes)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Bug Fixes](#bug-fixes)
* [Known Bugs](#known-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## UI/UX

### Design Overview
The main goal of the site is to allow users to upload their own opinions and projects to a blog site for other people with the same interests. Inspiring conversation and interaction about all things to do with wood working. The website was designed to be intuitive and easy to navigate providing feedback to the user in the form of on screen messages. Projects are promoted on almost every page of the site encouraging user to click and see more. Everything on the site should be easy to find and self-explanatory providing a good user experience.

### Colour Scheme
Initially, I didn't want the colour scheme to be too outlandish as I didn't want it to take away from the main content of the site, which are the project articles. For this reason, I decided to use quite mellow colours throughout the site. Generally I used a 'Seasalt' white for the site background and for any text elements on a darker background. An 'Eerie Black' Colour was used for the nav bar and footer to emphasise a harsh contrast between the site body and nav/footer. 

A 'Tomato' red/orange was used for the site buttons and links as I felt an orange colour worked well with the theme of wood, being a lighter variation of brown. Most text elements on the site are in a 'Jet' grey colour as I feel it complements well against the seasalt background and is easier on the eyes compared to plain white & black. I also ued a 'Kelly Green' colour for the 'NEW' label on the site home page.

[Coolors.co](https://coolors.co/) was used to generate the images of the colour palettes below.

#### Site Colour Pallet

<p align="center">
    <img src="documentation/site-colour-pallet.png"/>
</p>

- `#252525` used for nav bar & footer.
- `#F26749` used for buttons & links.
- `#D12600` used for hover effects.
- `#155724` used for button text.
- `#D4EDDA` used for button background.
- `#C3E6CB` used for button border.

### Fonts & Icons

- The 'Poppins' font was used for all text on the site. 

This font was sourced from [Google Fonts](https://fonts.google.com/).

- Heart icon used for the like button.
- Comments icon was used for the comments.
- Envelope icon used for email contact info.
- Phone icon used for phone contact info.

Icons sourced from [Font Awesome](https://fontawesome.com/).

## Agile Development

This project was launched alongside a GitHub Projects Page in order to measure and manage the anticipated workload. The goal was to outline my projected workload, list the epics, and then break them down into user stories or bite-sized tasks to work on in order to complete the site on time.

To see the project Kanban please click [here](https://github.com/users/MarkD117/projects/6).

At the initial planning stages, I planned each page individually listing the requirements and features I wanted to include. From these page plans, I created the user stories. The user stories were implemented in such a way that the core functionality of the site works seamlessly. This was mainly centered around the projects being created and displaying correctly.

On each user story, acceptance criteria was added along with tasks. Once a task was completed, the appropriate box would be ticked and if all parts of the user story were completed and the acceptance criteria was met, the user story was moved from **In Progress** to **Completed**.

#### User stories

####  Completed User Stories

Click on a user story below to be directed to the Kanban project to examine any of the additional details of the user stories. If the specific story does not appear automatically, please click on it from the project page for more details.

 1. [USER STORY: Landing Page](https://github.com/MarkD117/craftmasters/issues/1)
 2. [USER STORY: View Projects Page](https://github.com/MarkD117/craftmasters/issues/2)
 3. [USER STORY: View Project Post Info](https://github.com/MarkD117/craftmasters/issues/3)
 4. [USER STORY: Site Pagination](https://github.com/MarkD117/craftmasters/issues/4)
 5. [USER STORY: Open a post](https://github.com/MarkD117/craftmasters/issues/5)
 6. [USER STORY: Comment on a post](https://github.com/MarkD117/craftmasters/issues/6)
 7. [USER STORY: Like / Unlike](https://github.com/MarkD117/craftmasters/issues/8)
 8. [USER STORY: Register an account](https://github.com/MarkD117/craftmasters/issues/9)
 9. [USER STORY: Login / Logout](https://github.com/MarkD117/craftmasters/issues/10)
 10. [USER STORY: Selectable Categories](https://github.com/MarkD117/craftmasters/issues/12)
 11. [USER STORY: CRUD own project posts](https://github.com/MarkD117/craftmasters/issues/13)
 12. [USER STORY: Create Drafts](https://github.com/MarkD117/craftmasters/issues/15)
 13. [USER STORY: Manage all posts](https://github.com/MarkD117/craftmasters/issues/16)
 14. [USER STORY: Approve Comments](https://github.com/MarkD117/craftmasters/issues/17)
 15. [USER STORY: View Comments](https://github.com/MarkD117/craftmasters/issues/18)
 16. [USER STORY: Manage Categories](https://github.com/MarkD117/craftmasters/issues/22)
 

####  Incompleted User Stories

The following user stories have not been completed as they were deemed unnecessary for the core functionality of the site; however, they are possible features to implement in the future. 

 1. [USER STORY: Contact Creator](https://github.com/MarkD117/craftmasters/issues/7)
 2. [USER STORY: Search Function](https://github.com/MarkD117/craftmasters/issues/11)
 3. [USER STORY: Create Drafts](https://github.com/MarkD117/craftmasters/issues/14)
 4. [USER STORY: View Profile](https://github.com/MarkD117/craftmasters/issues/19)
 5. [USER STORY: View own likes posts](https://github.com/MarkD117/craftmasters/issues/20)
 6. [USER STORY: Set up profile image and bio](https://github.com/MarkD117/craftmasters/issues/21)

## Database Structure

During the planning stages of this project, [Lucid Chart](https://www.lucidchart.com/) was used to design the initial structure of the database in order to plan the data storage and relationships of site.

As of right now, the 'project_images CloudinaryField' was removed from the model. The original intent with this entry was to display more images of the project in the created blog; however, with the addition of the summernote editor, users can upload images directly into the content field, therefore making it redundant.

This field, could be re-added in the future to allow a collage of project images to be shown of the project altogether, yet, this is something that will be explored further in the future features section of this README.

<p align="center">
    <img src="documentation/initial-model-plan.png"/>
</p>

## Wireframes

During the planning stages, I  created wireframes for all pages of the site. [Balsamiq](https://balsamiq.com/wireframes) was used to design the digital wireframes. All wireframes can be seen below.

### Home Page Wireframes

<details>
<summary>Click to see the Home Page Wireframes</summary>

| Type | Image |
| --- | --- |
| Desktop | ![screenshot](documentation/wireframes/home-page-desktop.png) |
| Mobile | ![screenshot](documentation/wireframes/home-page-mobile.png) |

</details>

### Project & Categories Pages Wireframes

<details>
<summary>Click to see the Projects & Category Pages Wireframes</summary>

| Type | Image |
| --- | --- |
| Desktop | ![screenshot](documentation/wireframes/projects-categories-pages-desktop.png) |
| Mobile | ![screenshot](documentation/wireframes/projects-categories-pages-mobile.png) |

</details>

### Project Detail Page Wireframes

<details>
<summary>Click to see Project Detail Page Wireframes</summary>

| Type | Image |
| --- | --- |
| Desktop | ![screenshot](documentation/wireframes/project-detail-page-desktop.png) |
| Mobile | ![screenshot](documentation/wireframes/project-detail-page-mobile.png) |

</details>

### Add Project Page Wireframes

<details>
<summary>Click to see the Add Project Page Wireframes</summary>

| Type | Image |
| --- | --- |
| Desktop | ![screenshot](documentation/wireframes/add-project-page-desktop.png) |
| Mobile | ![screenshot](documentation/wireframes/add-project-page-mobile.png) |

</details>

## Features

### Navigation Menu

The Craft Masters site is a multi page site. All pages are accessible from the nav bar located at the top of the site. The nav bar was built with bootstrap and customised to fit the needs of the site. The nav menu is fully responsive to both mobile and desktop layouts.

- Desktop

<p align="center">
    <img src="documentation/insert"/>
</p>

- Mobile

<p align="center">
    <img src="documentation/insert"/>
</p>

### Site Footer

The site footer was built to provide the user with more information as well as to add functionality to the website. It includes a small snippet about the site, navigation links, and contant information. The footer is also completely responsive to mobile and desktop layouts

- Desktop

<p align="center">
    <img src="documentation/insert"/>
</p>

- Mobile

<p align="center">
    <img src="documentation/insert"/>
</p>

### **Home Page**

### Hero Image

Below the nav bar is a large darkened image of a woodworking workshop to gently and immediately introduce the user to the purpose of the site. The hero image, also displays the name of the site.

<p align="center">
    <img src="documentation/insert"/>
</p>

### About Section

The about section of the home page, is a small introduction into what the site is, informing the user if the site is for them. It also serves as a warm welcome to the blog if the user decides to continue.

<p align="center">
    <img src="documentation/insert"/>
</p>

### Lastest Projects

Below the about section are the lastest projects. In this section, any new posts will automatically be pushed to the front home page, allowing new posts to gain traction easily and reach new audiences. Each project card will be tagged with a 'NEW' label directing site users attention to the content. This also encourages bloggers to post new projects consistantly to be seen immediately on the first page of the site. There is also a clickable link that will bring the user to the projects page.

<p align="center">
    <img src="documentation/insert"/>
</p>