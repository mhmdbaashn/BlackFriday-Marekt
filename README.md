

<div align="center" >

<img src="https://github.com/user-attachments/assets/a622710e-da8e-4fe8-ad68-c7259cd6c763" width="800" height="500">

<br>

# [Live Project .. Click here](https://balckfriday-market-7b8127d54f29.herokuapp.com/)
</div>

<br>



<div align="center" width="50">

<img src="https://github.com/user-attachments/assets/79c197d5-8bbc-48cf-b5f1-17b408987f35"  width="300" height="300">

</div>


<div align="center" width="50">
<h1> Welcome to  BlackFriday Market </h1>

</div>

### BlackFriday Market  is an e-commerce platform designed to provide a seamless shopping experience for users during the Black Friday shopping season. The website allows users to browse, select, and purchase a wide range of products, benefiting from exclusive Black Friday discounts and offers. The platform includes key features like user sign-up, login, Add product, Update and delete your product.



# User Experience Design
***

 ## Table of Contents
  
   * Purpose and target audience
   * UX
   * Agile development
   * Features implemented
   * Features for future development
   * Technology used
   * Testing and validation
   * Bugs and issues
   * Deployment
   * Resources
   * Credits and acknowledgements


## Purpose and Target Audience:
 The project aims to provide an attractive and user-friendly platform for a wide demographic looking to shop efficiently during one of the biggest retail events of the year.

The target audience for BlackFriday Market consists of:
* **Online Shoppers:** Individuals who prefer shopping online, especially during high-demand sale events like Black Friday.
* **Bargain Hunters:** People looking to take advantage of sread me -pecial offers, discounts, and promotions typically available during Black Friday.
* **Tech-Savvy Consumers:** Those who are comfortable with navigating e-commerce platforms and expect a smooth, secure online shopping experience.
* **First-Time Online Shoppers:** Users who are new to online shopping and want a simple, easy-to-navigate platform for their first experience.





### Technology used

   * Django: Web framework for building the site.
   * Heroku: Platform for hosting and deployment.
   * HTML & CSS: For page structure and custom styling.
   * Bootstrap 5: Ensures responsive design.
   * Python: Backend logic and processing.
   * JavaScript: Additional functionality, like checking passwords to match during log in.
   * PostgreSQL: Relational database system.
   * Cloudinary: Image hosting service.
   * Font Awesome: Icons for UI enhancement.
   * Google Fonts: Custom typography.
   * GitHub: Source code repository and agile project methodology.
   * Git: Version control for code management.
   * Google Slack and Stack Overflow ChatGPT utilized for general research or solving a bug, information gathering, and various online tools. 
---

## Database Planning
------

### I used dbdiagram to create my database entity relationship diagrams. Below you can see how each model relates to each other.

<div align="center" >

<img src="https://github.com/user-attachments/assets/cc04888b-0132-4234-bc4d-7d058d2548ab" width="900" height="400">
</div>





### Wireframes
---
<br>
<div align="center" >
<img src="https://github.com/user-attachments/assets/f87bad8d-4566-4628-96c5-73241cbfa410" width="700" height="700">
<br>
<br>
<img src="https://github.com/user-attachments/assets/3caffa38-9c47-4955-aaec-74392e246f1d" width="700" height="700">
</div>



## Agile Development
---



## Kanban Board Overview
---





## User Stories Overview
***

## Features Implemented
***

### Home Page:
***
*   Products are displayed as cards.
*   Users can click on card button  to read the detail product.
*   Users can edit and delete their own products.
*   Users must be logged in to  edit own products.
*   Users must be logged in to delete their own products.
*   Users cannot delete or edit product by other users.

<img src="https://github.com/user-attachments/assets/a3d0e6d4-f477-47a6-bc63-eb7cf529b3e9" width="700" height="550">


### Footer/Nav Bar:
***
*   Navigation links facilitate easy navigation throughout the website.
*   Social media links direct users to virtual BlackFriday Market social media pages.

<img src="https://github.com/user-attachments/assets/47e1b1a8-f402-4d0c-b8da-2cdb62dae962" width="700" height="40">
<br>
<br>


<img src="https://github.com/user-attachments/assets/20496b01-8822-4e0c-b012-ab09b148dc96" width="700" height="40">



### Login Page:
***
*   Secure signup functionality allows users to register securely.
*   Successful login redirects users to the home page.

<img src="https://github.com/user-attachments/assets/589a46c5-7fa6-4a45-9ccf-341446cb97b3" width="700" height="400">



### Registration Page:
***

*    Secure login functionality allows users to log in securely.
*    Successful registration redirects users to the home page.

<img src="https://github.com/user-attachments/assets/c5260b25-760a-4d70-8e9c-724fdc815943" width="700" height="400">


### Logout Page:
***

*   Logout functionality allows users to sign out securely.
*   After successful logout, users are redirected to the home page.

<img src="https://github.com/user-attachments/assets/46607067-70c1-4a2d-9920-484cc5bc0b5d" width="700" height="400">

## Additional Security Features:
***

*  Prevention of brute force actions via URL.
*  Users are redirected to the sign-in page with an unauthorized action notification if they attempt unauthorized actions.
*  Prevention of users deleting other users' product.
*  Prevention of users editing other users' product.






## Deployment
---

Deployment Steps:
Creating the Heroku App

    Begin by signing up or logging in to Heroku.
    In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
    Choose a unique name for your project, like "Travelling Scribbles".
    Select the EU region.
    Click on "Create App".
    In the "Deploy" tab, choose GitHub as the deployment method.
    Connect your GitHub account and find/connect your GitHub repository.

Setting Up Environment Variables

    Create env.py in the top level of the Django app.
    Import os in env.py.
    Set up necessary environment variables in env.py, including the secret key and database URL.
    Update settings.py to use environment variables for secret key and database.
    Configure environment variables in the Heroku "Settings" tab under "Config Vars".
    Migrate the models to the new database connection in the terminal.
    Configure static files and templates directories in settings.py.
    Add Heroku to the ALLOWED_HOSTS list.

Creating Procfile and Pushing Changes

    Create a Procfile in the top level directory.
    Add the command to run the project in the Procfile.
    Add, commit, and push the changes to GitHub.

Heroku Deployment

    In Heroku, navigate to the Deployment tab and deploy the branch manually.
    Monitor the build logs for any errors.
    Upon successful deployment, Heroku will display a link to the live site.
    Make sure to resolve any deployment errors by adjusting the code as necessary.
