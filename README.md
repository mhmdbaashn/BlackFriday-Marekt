

<div align="center" >

<img src="https://github.com/user-attachments/assets/a622710e-da8e-4fe8-ad68-c7259cd6c763" width="800" height="500">

<br>

# [Live Project .. BlackFriday Market](https://balckfriday-market-7b8127d54f29.herokuapp.com/)
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
 ***
  
 1. [UX](#ux)

 2. [Agile Development](#agile-development)

 3. [Features Implemented](#features-implemented)  

 4. [Features Left to Implement](#features-left-to-implement)  

 5. [Technology Used](#technology-used) 

 6. [Testing](#testing-and-validation)  

 7. [Bugs](#known-bugs)  

 8. [Deployment](#deployment)

 9. [Resources](#resources)  

 10. [Credits and Acknowledgements](#credits-and-acknowledgements)



## Purpose and Target Audience:
 The project aims to provide an attractive and user-friendly platform for a wide demographic looking to shop efficiently during one of the biggest retail events of the year.

The target audience for BlackFriday Market consists of:
* **Online Shoppers:** Individuals who prefer shopping online, especially during high-demand sale events like Black Friday.
* **Bargain Hunters:** People looking to take advantage of sread me -pecial offers, discounts, and promotions typically available during Black Friday.
* **Tech-Savvy Consumers:** Those who are comfortable with navigating e-commerce platforms and expect a smooth, secure online shopping experience.
* **First-Time Online Shoppers:** Users who are new to online shopping and want a simple, easy-to-navigate platform for their first experience.





### Technology used
***

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
#### During the development of the BlackFriday Market website, I implemented an Agile methodology and utilised a Kanban board on GitHub linked to my repository.


## Kanban Board Overview
---

<img src="https://github.com/user-attachments/assets/0c7ee2ee-88f6-4994-8aba-4193889e15a9" width="700" height="500">




## User Stories Overview
***
1. Title: Registration (Sign Up).
   * AC1 Given an email a user can register an account.
   * AC2 Then the user can log in.
   * AC3 When the user is logged in they can add his products.

2. Title: Hero Section
   *  AC1 A hero Image with welcoming message .
   *  AC2 The call-to-action button redirects to the registration page.


3. Title: Navigation
   * AC1 When clicking the index link, the user is always taken to the landing page.
   * AC2  When clicking the Registration link, the user is always taken to the registration page.
   * AC3 When clicking the Log In link, the user is taken to the login page.
   * AC4 When clicking the Log Out link, the user is taken to the log out page.

4. Title: Footer

5. Title: Product Management .
   * AC1 Given a logged in user, they can create a product.
   * AC2 Given a logged in user, they can read a product .
   * AC3 Given a logged in user, they can update a product.
   * AC4 Given a logged in user, they can delete a product.

6. Title: Log in 

   * AC1 login form with fields for username and password is available.
   * AC2 The form displays error messages for incorrect credentials.
   * AC3 Successful login redirects to the user's dashboard with a welcome message.




## Features Implemented
***
### Home Page:
***
*   Users can  displayed as cards.
*   Users can sign up throug hero section or from navbar.


<img src="https://github.com/user-attachments/assets/a3d0e6d4-f477-47a6-bc63-eb7cf529b3e9" width="700" height="550">


### All Products :
***
*  It shows all products in our site. 


<img src="https://github.com/user-attachments/assets/896912c6-1bc7-4f1e-91d2-1986764f0f3a" width="700" height="550">


### Add Product : 
***
*  It asks to complete fields like : Title, Description, Price , Price descount and Seller


<img src="https://github.com/user-attachments/assets/4af48bc0-5aa2-4986-8d31-1cfea4f6692e" width="700" height="550">

### Detail Product
***
*  Users can edit and delete their own products.
*  Users must be logged in to edit own products.
*  Users must be logged in to delete their own products.
*  Users cannot delete or edit product by other users.


<img src="https://github.com/user-attachments/assets/102d1e1b-314d-4de9-8e67-7924565c42c6" width="700" height="550">


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


### Technology used
***

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
   * Goog


## Testing and validation 


## CSS
***
* I used the [ CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) Validator to check my CSS script by Direct Input. I found no errors! There are 1 warning.

<img src="https://github.com/user-attachments/assets/2853269d-ebb7-44a3-8b11-521d8bac4d0d" width="500" height="300">

## HTML
***

* I used the  [W3C](https://validator.w3.org/) HTML Validator to check the HTML on each of my site pages by Direct Input. I have resolved the necessary errors (extra tags and correcting how width is set in an img tag). However there are some error messages remaning which are due to the content being created using Django Summernote editor in the admin panel.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/504a42c1-a0bd-40c2-bb0c-b157ce1ae61e" width="500" height="300">| Pass |
| All Products  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/791f897e-b9b1-470d-b53c-8eedf7a8eb53" width="500" height="300">| Pass |
| Add Product  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/c30caac7-1455-4697-8e40-4d3a8d3e4de4" width="500" height="300">| Pass |
| Product  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/9382b40f-b8e6-4832-8ae9-5769a70d1a2a" width="500" height="300">| Pass |
| Sign Up  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/9ef1b5dc-e6a1-4a25-ac72-c370517c43ae" width="500" height="300">| 4 errors |
| Sign In  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/27195422-ae57-4414-9143-1802fd9f2a4a" width="500" height="300">| Pass |
| Logout  |  [W3C](https://validator.w3.org/)| <img src="https://github.com/user-attachments/assets/b76ff352-eba5-4551-8497-d147d7c3087f" width="500" height="300">| Pass |


## Python
***

* I have used the recommended [PEP8 CI](https://pep8ci.herokuapp.com/)  Python Linter to validate all of my Python files.

| Page | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| forms.py  |  [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py)| <img src="https://github.com/user-attachments/assets/b9595aca-d08b-4802-b9bd-d7fbce2b0d87" width="500" height="300">| Pass |
| settings.py  |  [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py)| <img src="https://github.com/user-attachments/assets/4369f69a-c141-45bc-9e11-7279d0920b04" width="500" height="300">| Pass |
| views.py |  [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py)| <img src="https://github.com/user-attachments/assets/3306e1dd-b184-4edd-a0ca-a23e8b24264b" width="500" height="300">|Pass |
| urls.py  |  [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py)| <img src="https://github.com/user-attachments/assets/e05252d0-aa1b-41d5-bf7a-1881ca2f81b7" width="500" height="300">| Pass |
| models.py  |  [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py)| <img src="https://github.com/user-attachments/assets/cdf29738-6962-4e7d-80b4-df4904dbd300" width="500" height="300">| Pass |





#### [ Back to Top ](#table-of-contents)

## Testing and Validation
### Manual Testing Results


### Home Page 

| Test | Result |
| --- | --- |
| Products displayed as cards | Pass |
| Redirect after successful login | Pass |
| User must be logged in to add/edit/delete product | Pass |
| Ability to click on a product card | Pass |
| Edit and delete product functionality | Pass |
| Prevention of editing other users' product | Pass |
| Prevention of deleting other users' product | Pass |


### Footer/Navbar 

| Test | Result | 
| --- | --- |
| Navigation links functionality | Pass |
| Social media links functionality | Pass |  


### Login Page 

| Test | Result |
| --- | --- |
| Secure login functionality | Pass |
| Redirect after successful login | Pass |



### Registration Page  

| Test | Result |
| --- | --- |
| Secure signup functionality | Pass |
| Redirect after successful registration | Pass |


### Logout Page 


| Test | Result |
| --- | --- |
| Logout functionality` | Pass |
| Redirect after successful logout | Pass |




###  Security

| Test | Result |
| --- | --- |
| Prevention of brute force actions via URL | Pass |
| Redirect to sign-in page after attempted unauthorized action | Pass |



#### [ Back to Top ](#table-of-contents)

## Deployment
---

#### Deployment Steps:
#### Creating the Heroku App

* Begin by signing up or logging in to Heroku.
* In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
* Choose a unique name for your project, like "Travelling Scribbles".
* Select the EU region.
* Click on "Create App".
* In the "Deploy" tab, choose GitHub as the deployment method.
* Connect your GitHub account and find/connect your GitHub repository.

#### Setting Up Environment Variables

*    Create env.py in the top level of the Django app.
*    Import os in env.py.
*    Set up necessary environment variables in env.py, including the secret key and database URL.
*    Update settings.py to use environment variables for secret key and database.
*    Configure environment variables in the Heroku "Settings" tab under "Config Vars".
*    Migrate the models to the new database connection in the terminal.
*    Configure static files and templates directories in settings.py.
*    Add Heroku to the ALLOWED_HOSTS list.

#### Creating Procfile and Pushing Changes

*    Create a Procfile in the top level directory.
*    Add the command to run the project in the Procfile.
*    Add, commit, and push the changes to GitHub.

#### Heroku Deployment

*    In Heroku, navigate to the Deployment tab and deploy the branch manually.
*    Monitor the build logs for any errors.
*    Upon successful deployment, Heroku will display a link to the live site.
*    Make sure to resolve any deployment errors by adjusting the code as necessary.

#### [ Back to Top ](#table-of-contents)


## Resources
***

## Credits and Acknowledgements
***




