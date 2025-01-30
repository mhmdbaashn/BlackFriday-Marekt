

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

 7. [Deployment](#deployment)

 8. [Credits and Acknowledgements](#credits-and-acknowledgements)



# UX 
***

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
#### During the development of the BlackFriday Market website, I implemented an Agile methodology and I applied MoSCoW Prioritization to effectively classify tasks based on their importance and urgency. Asutilised a Kanban board on GitHub linked to my repository. 


## MoSCoW Prioritization

* **Must Have**
* **Should Have**
* **Could Have**
* **Won't Have**

## Kanban Board Overview
---

* **To do:** This column contains user stories that are ready for development.
* **In Progress:** This column tracks user stories currently being worked on.
* **Done:** This column holds all the tasks that have been successfully completed.

<img src="https://github.com/user-attachments/assets/a80102d8-ee80-40a0-b021-98baf3cf0a05" width="700" height="500">


## Design Choices:
***
### ***Color our scheme:***

#### Colors ( white and black  ) are chosen for a clean and simple website design that keeps the focus on the content.

### ***Typography:***
***
#### The following font was chosen for a clean and modern look that is both readable and minimal.

#### Poppins', sans-serif;


## Epic, Milestons and User Stories Overview
***
### Epic 1 : Authentication System
* User Story: Design Navbar 
"As a guest, I want to see a homepage with clear information about the store."
* User Stor : Home Page 

### Epic 2 : User Interface (UI)
* User Story : Sign Up "As a guest, I want to be able to create a new account so I can use the site."
* User Story: Login
"As a user, I want to be able to log in using my email and password."* User Stor : Design Navbar
* User Story: Logout
"As a logged-in user, I want to be able to log out of my account."

### Epic 3 : Product Management (CRUD)
* User Story : Add Product
"As an admin or Seller, I want to be able to add a new product to the store."
* User Story : Edit Product
"As an admin or Seller, I want to be able to edit a product’s details."
* User Story : Delete Product
"As an admin or Seller, I want to be able to delete a product."

### Epic 4 : Impoving User Experience (UX)

* User Story : Prevent Negative Values in Price Input 
 As a user, I want to be prevented from entering negative values for product price and discount price, So that I ensure valid pricing information is entered.
* User Story :  negative values and notification
I want to receive a notification if I enter a negative value for the product price.
* User Story : Validate Discount Price Compared to Product Price 
As a user, I want to show an error message if the discount price is greater than or equal to the original product price,
So that the discount makes logical sense.
* User Story : Display Featured Products Section on Homepage
I want to see a "Featured Products" section on the homepage, So that I can quickly discover special or recommended products.
* User Story : Display Banners on Homepage for Promotions or Offers 
As a user, I want to see promotional banners on the homepage, so that I can be informed about ongoing offers and discounts.

### Epic 5 : Adding New Features (Review Rating and commets on Products)
* User Story : Express about the products by rating review and adding comments.
I want to express my interest in a product by rating review or adding comment so I can value product that I used it .







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

## Future Features
***
1.  **Shopping Cart** :
      *  Display Products in Cart, Total Price Calculation, Payment and Shipping Options and Guest or Registered Checkout.

2. **Checkout Process** :
      * Support Multiple Payment Methods, Payment Security and Payment Confirmation.


## Testing and validation 

## Lighthouse Audit:
***
#### I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

###  On Desktop

#### Home
<img src="https://github.com/user-attachments/assets/e561abe6-bad1-4fcf-9490-412902cb5406" width="600" height="300">

#### All Products
<img src="https://github.com/user-attachments/assets/d79312b8-6af5-43a3-af0c-7b8fe9e68447" width="600" height="300">

#### Add Product
<img src="https://github.com/user-attachments/assets/f3d640f6-8207-498d-b259-9adfcf84424a" width="600" height="300">

###  On Mobile

#### Home
<img src="https://github.com/user-attachments/assets/f6152237-dd50-43f0-b887-2b467449a939" width="800" height="200">

#### All Products
<img src="https://github.com/user-attachments/assets/9e8c1509-7df1-448f-93a5-2c2206463c01" width="800" height="200">

#### Add Product
<img src="https://github.com/user-attachments/assets/61233fa1-428c-438e-8421-71e885bd8346" width="800" height="200">


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

| Test | ACTION | EXPECTATION | RESULT |
| --- | --- | --- | --- |
| Navbar logo Link | Logo link clicked | When click on it goes to the home page | Worked as expected |
| Navbar Home Links | Home link clicked | When click on it goes to the home page | Worked as expected |
| Navbar Login Link | Login link clicked | Get taken to sign in page | Worked as expected |
| Redirect after successful login | After Sign in Process | When click on it goes to all products page | Worked as expected |
| Navbar Sign Up Link | Sign Up link clicked | Get taken to Sign Up page | Worked as expected |
| Navbar logout Link | logout link clicked | Get taken to Sign Out page | Worked as expected |
| Redirect after successful logout | After Sign out Process | When click on it goes to  homepage page | Worked as expected |
| Navbar Add Product | Add Product link clicked | Get taken to add product page | Worked as expected |
| Edit and delete product functionality |  links clicked(dosen't apperar to any user expect the product woner ) | When click on it goes to  Edit or Delete page | Worked as expected |
| Navbar All Products | All Products link clicked | Get taken to All products page | Worked as expected |
| Social media links functionality | Social media links clicked | Get taken to Social media pages | Worked as expected |



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


## Credits and Acknowledgements
***


*  Code Institute LMS Content: For providing the educational materials that guided my learning process.
*  Course Facilitators: Special thanks to  David Calikes for his support and guidance.
*  Slack and Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.
*  A special thanks to all the other indivudals in our cohort for their continuous support throughout the course.
*  The added Photo and products details were taken from the Shein Website.
*  Boostrap Icons was used for icons and the fonts used were derived from Google Fonts.
*  Wireframes, logo and flowcharts were created using balsamiq Wireframes.



