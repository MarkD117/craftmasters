# Craft Masters

Welcome to Craft Masters, a vibrant online community where woodworking enthusiasts of all skill levels come together to celebrate the artistry of woodcraft. The Craft Masters blog is a dedicated space for passionate individuals to showcase their woodworking projects, share insights, and inspire fellow craftsmen. 

Whether you're a seasoned woodworker with years of experience or a newcomer eager to explore the world of woodworking, Craft Masters is your haven. Join in on this creative journey, where each project is a masterpiece and every craftsperson is a master in their own right. Let the sawdust fly and the creativity flourish – welcome to Craft Masters, where the beauty of woodworking knows no bounds.

The live project can be accessed [here]()

![Screenshot](documentation/)

## Index – Table of Contents

* [UI/UX](#uiux)
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
    <img src="documentation/"/>
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



## Database Structure

During the planning stages of this project, [Lucid Chart](https://www.lucidchart.com/) was used to design the initial structure of the database in order to plan the data storage and relationships of site.

As of right now, the 'project_images CloudinaryField' was removed from the model. The original intent with this entry was to display more images of the project in the created blog; however, with the addition of the summernote editor, users can upload images directly into the content field, therefore making it redundant.

This field, could be re-added in the future to allow a collage of project images to be shown of the project altogether, yet, this is something that will be explored further in the future features section of this README.

![Screenshot](documentation/initial-model-plan.png)

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