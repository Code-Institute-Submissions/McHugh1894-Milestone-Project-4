# Testing

### Testing was required as part of MS4

#### Responsive Testing

In testing my site for mobile responsiveness I was constantly checking the site using Chrome Dev Tools on the various screen resolutions on offer. I aimed to make the site responsive down as far  as a 280px screen which was achieved through the use of media queries.

friends and family members also tested the site out on their relevant devices and it all worked as expected.

Please see below for a list of all screen sizes that my site was found to be mobile responsive on:

* Moto G4

![Moto G4](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/screenshot.png)

* Galaxy s5

![Galaxy s5](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/screenshot2.png)


* iphone x

![iphone x](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/screenshot3.png)

* ipad

![ipad](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/screenshot4.png)

* surface duo

![surface duo](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/screenshot5.png)


### Lighthouse

* I ran my site throught Lighthouse which generated reports for mobile and desktop views.

* Initially, there were some issues regarding alt text of images but I made the changes necessary and please see below for the lightouse reports for both desktop and mobile.

* Desktop
    * ![lighthouse-desktop](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/lighthouse-desktop.png)

* Mobile
    * ![lighthouse-mobile](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/lighthouse-mobile.png)

### Code validation

#### HTML

* I used W3C Markup validation for my HTML validation and my code passed this test.

![html validation]()

#### CSS

* I used W3C Markup validation for my CSS validation and my code passed this test.

![css validation]()

#### JavaScript

* I used jshint validation for my JavaScript validation and my code passed this test.

![JavaScript validation]()

#### Python

* I used pep8 validation for my Python validation and my code passed this test.

![python validation]()

### Manual Testing of site

* The functionality of the site was manually tested to ensure that all worked as expected.

#### Bag App Functionality

* to test the bag, I navigated to the products page, clicked on a product and chose "add to bag"

![add-to-bag](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/add-to-bag.png)

* This worked, so I then went to the bag page and tried to edit the qty of the product in my bag.

![update-bag-page](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/edit-quantity.png)

* I also then tried to remove the item from my bag to test delete functionality.

![delete-bag-page](https://github.com/McHugh1894/Milestone-Project-4/blob/main/media/README-Images/TESTING-Images/remove-from-bag.png)

#### Checkout App Functionality

* In order to test checkout functionality of the site, I first added an item to my bag and proceeded to secure checkout.

![secure-checkout]()

* Then proceeded to the checkout page and fill in the orderform using stripe.

![orderform]()

* When the order was successful I was redirected to the checkout success page with a summary of my order information

![order success]()

* I then checked my email to ensure I received a confirmation email.

![order-confirmation-email]()

* Then i logged into stripe to ensure payment was successful, which it was as seen below.

![stripe confirmation]()

* I also checked in the admin section of the website to ensure the orderform was created. as seen below it was successful.

![admin-order-confirmation]()

#### Products App Functionality

* To test product app functionality, I first had to login as an admin user. To add a product, I clicked on my account at the top of the page and clicked on the product management dropdown.

![product-mgmt]()

* I arrived on the add product page to an empty product item form which I filled in to add a new item to the database.

![add-product-form]()

* Product got added successfully

![successfully-aded-product]()

* Only admin users will be able to edit and delete products, which can be seen below.

![add-edit-btns]()

* Then I tried to edit the item by clicking edit, This brought me to the edit product page which allowed me to edit the product

![edit-product-page]()

![edit-confirmation]()

* Finally, I attempted to delete my product from the site, delete confirmation should appear before product gets deleted

![delete-product-modal]()

![delete-confirmation]()

#### Blog Functionality

* I needed to login as an admin user to test the blog functionality.

* I navigated to the blog page and clicked on the add blog post button only visible to admin users.

![add-blog-post-btn]()

* I was then taken to the add blog post page where i added a new blog post in the form provided.

![add-blog-post-page]()

![add-post-confirmation]()

* I then clicked on the edit button to edit the blog post and was taken to the edit blog post page.

![edit-blog-post-page]()

![edit-post-successful]()

* Then I tried to delete the blog post, delete confirmation appearing first however. and confirmation of deletion

![delete blog modal]()

![blog-post-deleted]()

* I then tried to leave a comment on a blog post, all users have this functionality by clicking on the blog post and scrolling to the comments section at the bottom of the page.

![add-comment]()

* I then deleted the comment so to test the delete comment is working sufficiently.

![delete-comment-modal]()

![delete-comment]()

#### contact us Functionality

* To test thye contact form I navigated to the contact us page in the nav bar 

![contact-us-page]()

* I filled in the contact form and clicked the submit button to send the form.

![contact-us-confirmation]()

![contact-us-admin]()

#### Profiles Functionality

* To test profiles I needed to be logged in.

* to test profiles functionality, I clicked on my account and clicked my profile.

* I made sure any previous orders were displayed on the right and default customer information was displayed in the form oif the user chose to save their information.

![profile-page]()

#### Form Functionality

* All forms have been checked to ensure incorrect or blank inputs give errors to the user if aa blank field is empty.

![invalid-forms]()

### issues/Bugs during development

* Navbar placement

    * In testing my site using Google Chrome tools I saw that when the search bar icon was clicked the search bar drop down veered offscreen.

    * I spent a large amount of time trying to understand why this was happening, I tried everything that I could think of and use a vast array of channels e.g Slack, stack overflow etc.

    * I eventually, figured out the issue was that the dropdown menu was using position: absolute which I eventually saw using Google Chrome dev tools, to fix the issue and make the navbar responsive I added the below css class to the dropdown menu.
        ```
            .menu-position-mobile{
                left: 0;
            }
        ```

* Quantity of products in bag app

    * I noticed in the bag app that the user could enter a quantity of the product for under 1 and click update, the website would crash to a 500 error.

    * To fix this I spent a large amount of time trying to understand why this was happening in the first place. I spent time on stack overflow and googling up possible solutions but nothing seemed to work, I went on the slack channels and eventually I found an adequate solution.

    * The solution is below. I didn't want the site to crash for the user if they put in a number below one, If they have the product in the bag then the minimun quantity therefoire has to be one so I added "or 1" to where the function looks for the quantity of items so that the site won't crash and they will have at least one quantity of the item in the bag in case of mistakes, accidents etc.
        ``` quantity = int(request.POST.get('quantity') or 1) ```

* Test Error

    * When I first started to create and run the unit tests for my project I ran into an error regarding the tests module.

    * I spent a lot of time researching this error and It was eventually found that I had not deleted the tests.py file before I ran the tests, My tests are stored in the tests folder for each app and django was trying to run tests from the empty tests.py file.

    * [here](https://stackoverflow.com/questions/37525075/what-does-tests-module-incorrectly-imported-mean) is where I found my solution to the problem.

* Styling issues

    * There were a lot of styling issues I found whilst attempting to change the styling of some of my elements in chrome dev tools.

    * Buttons were turning white on click, when image files were added the site was turning unresponsive on mobile devices etc.

    * To fix the styling and coloring issues I had to use !important to override the bootstrap elements in certain places. To stop the filename from veering offscreen and turning my site unresponsive on mobile I added the text-break class to the paragraph element that held the filename.

* Migrations files - lines too long

    * In testing my python code in Gitpod I used the below command.
        ``` python3 -m flake8 ```
    
    * Issues were found regarding line length of python code in the migrations folder, I was unsure about whether or not this code should be validated and fixed. I asked in the #full-stack-frameworks-channel on Slack about what the best course of action would be. I was informed by Gaff the Channel Lead that as I did not write this code myself that I should not make any changes to the migrations files in question. So I heeded his advice and did not make the changes.

* Add/edit Blog posts

    * In testing, I realised at the very last second that the filename was not being displayed underneath the input area.

    * I ran into this bug very very late and unfortunately I could not offer a solution or find an answer as to why, The images can be uploaded and changed but The filename is not displaying where I wanted it to display.

* Shopping Bag Page

    * Shopping bag page is not mobile responsive, I tried many different ways to make it validate in accordance to the boutique ado shopping bag page but the reality is I could not do it in such a way that validated the html code and made it mobile responsive, which is a shame. I didn't spot the error with validation until very late in the game and unfortunately I did not get sufficient time to fix the error. Its not mobile responsive which is horrible considering everything else is.


## User Story Testing

#### User Story 1

* I want to be able to quickly view the products that the site is selling.

##### Action

* The user will see and be made aware what the site is about and selling via homepage imagery, header cta and navigation links. Navigate to the homepage or by using the navbar to move across the site.

##### Expectation

* The site makes it very clear straight away to the user what the site sells and also clear navigation to understand the categories of products for sale on the site and a clear and visible CTA on the homepage header which makes it clear what I want the user to do.

##### Result

* The homepage background image makes it clear what the store is about and what we sell. The navigation is clear and intuitive with the categories of products shown and dropdown menus ti show the various categories of items on the site. The Header Cts stands out and is easy to read so makes it clear to the user whjat they need to do.

* homepage background image
    ![home-back-image]()

* Navigation
    ![navbar]()

* homepage CTA
    ![home-cta]()

#### User Story 2

* I want to be able to easily navigate throughout the site.

##### Action

* User clicks on the navbar toggler button on mobile view at the op of the page to open the menu or on deskyop sees the navbar displayed at the top of every page.

##### Expectation

* The user can quickly and intuitvely navigate throughout the site and see that once they add a product to their bag the bag item in the navbar changes color to gold to indicate they have an item in their bag. The user should also be aware that by clicking on the My Account link on the navbar they get the option to be taken to their profile to see their default delivery information and a logout option so to allow th user to logout of the site regardl;ess of whatever page they are on.

##### Result

* The user is able to navigate through the site using the navbar, the user can also move to their bag page and complete their purchase by choosing the bag icon in the navbar once an item has been added. The user is also able and understanding of using the searchbar to search for products that they wish to know more about on the site. Overall, the user has a good understanding of where they are and where they want to go.

* Navbar
    ![navbar]()

* searchbar + bag
    ![searchbar-and-bag]()

* bag with items
    ![bag-with-items]()

* my account options
    ![my-account-options]()

#### User Story 3

* I want to be able to find out more information about the company and see if they have a social media presence.

##### Action

* User clicks on the social media links in the footer in order to see the social profiles of company and find out more information about company. Also, clicks on contact us and sends a message if there's more they need to know

##### Expectation

* The user travels to the social media sites of the company by following the links in the footer. The user navigates to the contact us page and sends a message to the company, they are then informed of successful sending of message.

##### Result

* The user sees and navigates to the social media sites of the company and finds out the information they need about the company. The user successfully manages to send their message to the site using the contact us page and gets confirmation of successful delivery of message.

* Footer with socials
    ![footer]()

* contact us page
    ![contact-us]()

* contact us successful
    ![contact-us-successful]()

#### User Story 4

* I want to be able to contact the company.

##### Action

* The user clicks on contact us in the navbar and is taken to the contact us page where they can contact the store.

##### Expectation

* The user recognizes and follows the navigation to the contact us page where they fill in the contact form and submit. No errors in the form and all fields entered.

##### Result

* The user successfully fills in all relevant information in the form and successfully sends the message to the site.

* message successful
    ![contact-us-successful]()

* ensure form is valid
    ![form-validation-error]()

#### User Story 5

* I would like to be able to search for a specific item using the search bar.

##### Action

* user clicks on the searchbar in the navbar and types in whatever they are looking for and submits their search.

##### Expectation

* A result of the search will appear on the page below with information on the search query the user has provided.

##### Result

* The user enters a search term related to an item/s on the site and the search returns items for the user. If an item is not entyered before submitting an error appears on screen to the user asking them to enter a search and if the user enters a search term not related to an item on site then a message appears informing them that no such product is in the database.

* searchbar
    ![searchbar]()

* searchbar invalid
    ![searchbar-invalid]()

* search results
    ![search-results]()

* no results
    ![no-results]()

#### User Story 6

* I want to be able to search the site based on the different categories.

##### Action

* User clicks on one of the categories in the navbar and a list of subcategories appears below.

##### Expectation

* The User clicks on one of the links in the searchbar which will display to the user a list of subcategories below the navbar. The user can then click on the subcategory to show all results of products on the site related to that particular subcategory.

##### Result

* The user successfully manages to search for products on the site using the list of subcategories in the navbar dropdown menus.

* category dropdowns
    ![category]()

* products related to category search
    ![category-search]()

#### User Story 7

* I want to be able to see all product details before I choose to buy the item

##### Action

* User navigates to products page and clicks on a product and is taken to the product details page displaying all information relevant to the product.

##### Expectation

* The user finds the product they want and clicks on it, navigates to the product details page for that particular product and all the relevant product information is displayed for the user. They then either add product to their shopping bag or return to the products page.

##### Result

* The user successfully manages to navigate to the product details page and can see all the relevant product information displayed before the user decides whether or not to buy the product. They can then choose to add product to their bag or they can return to shopping by clicking on the buttons on the product details page. if they choose to add to their bad a notification message appears to inform them the product has been added to their bag.

* product details page
    ![product-details-page]()
* product details CTAs
    ![product details ctas]()

* add product to bag notification
    ![add-product-notification]()

#### User Story 8

* I want to be able to sort the items based on their price.

##### Action

* User navigates to the all products page under the shop dropdown menu. There, they click the select input and choose either price low to high or price high to low.

##### Expectation

* The user navigates to the products page and filters the products based on their price.

##### Result

* The user successfully manages to filter the products on the site based on their price.

* select input
    ![select-input]()

* filtered results
    ![filtered-results]()

#### User Story 9

* I want to be able to see products price and sizes if they have any.

##### Action

* User navigates to the product details page of their choosing. There the user is able to see the products price and if it has sizes a sizes select input will be visible.

##### Expectation

* The user can see the price of the item on the product details page and the select input for items which have sizes.

##### Result

* The user can view the products prices on all products page and if the user clicks on an item and is taken to product details page the price remains visible. The size select input will only be visible on product details page if an item has different sizes.

* prices all products
    ![prices-all-products]()

* prices product details
    ![prices-product-details]()

* size selector
    ![size-selector]()

#### User Story 10

* I want to be able to add items to my shopping bag

##### Action

* User navigates to the product details page and clicks add to bag, product gets added to shopping bag

##### Expectation

* When the add to bag button is selected the product gets added to the users shopping bag

##### Result

* The user successfully adds items to their shopping bag and total cost gets displayed in the navbar underneath the bag icon.

* add to bag button
    ![add-to-bag-button])

* bag in navbar with total cost displayed
    ![bag in navbar]()

#### User Story 11

* I would like to be notified when I add items to bag or interact with the site functionality.

##### Action

* User interacts with the site in some respect and they get notified of the interaction. e.g adding a product to the bag

##### Expectation

* User interacts with the site and they receive a notification from the site of the interaction.

##### Result

* User successfully is notified of an interaction with the site. These interactions also come in form of alerts and warnings like invalid forms too

* notification of interaction
    ![notification-of-interaction]()

* warning message
    ![searchbar-invalid]()  

#### User Story 12

* I want to be able to edit my shopping bag.

##### Action

* User moves along the checkout process and goes to the bag page where they can update the quantity of each individual item and remove an item entirely from their bag.

##### Expectation

* The user can easily update the quantity of items in their bag and remoive items entirely from their bag.

##### Result

* The user changes the quantity number in the input, clicks update and the bag gets updated with the new information. If the user clicks on remove then that item will be removed from their bag entirely and they will be informed.

* edit shopping bag
    ![bag page]()

* update quantity
    ![update-quantity]()

* remove item from bag
    ![remove-from-bag]()

#### User Story 13

* I want the checkout process to be quick and painless.

##### Action

* User clicks on secure checkout on bag page, they then land on the checkout page where they fill out the form and submit their order.

##### Expectation

* The user follows the instructions, fills out the form, enters their correct order details, completes their order. Then they get redirected to checkout success page with details of their order and they receive a confiormation email.

##### Result

* The user fills in the order form correctly and is valid, completes their order, redirects to checkout success page with order details and then the user receives a confirmation email.

* secure checkout button - bag page
    ![secure-checkout-button]()

* secure checkout button - toast-success
    ![secure-checkout-button-toast]()

* Order form
    ![orderform]()

* checkout success page
    ![checkout-success-page]()

* Order confirmation email
    ![order-confirmation-email]()

#### User Story 14

* I want to receive confirmation of my order.

##### Action

* Once a user completes an order and payment a confirmation email will be sent to them

##### Expectation

* A user completes the checkout process for their order, they complete the payment, the order is accepted and a confirmation email will automatically be sent to them with their order details.

##### Result

* Once a user completes the checkout process, and they check their email account they will see a confirmation email that was sent automatically to them upon order completion and this email contains all relevant information related to their order.

* Order confirmation email
    ![order-confirmation-email])

#### User Story 15

* I want to be able to see previous order details.

##### Action

* User navigates to their profile page where they see previous orders and click on the information to see the details from their previous orders.

##### Expectation

* once the user clicks on the order number from a previous order they are taken to a page which displays all the relevant information from their previous order.

##### Result

* User successfully finds previous orders and can find all relevant information from those orders.

* Previous order
    ![previous-order]()

#### User Story 16

* I want my details to be saved to my account for faster purchases in future.

##### Action

* User goes through the checkout process to the checkout page, they fill out the order form and, if they are signed in they can check the save info button below the form or, if they are not signed in then the option to create an account or login to save info will appear.

##### Expectation

* When the user completes the checkout process, submits the order form and they then navigate to their profile page they will see the form prefilled with their saved orderform information.

##### Result

* User successfully saves their information to their account which will automatically be prefilled in future order forms for that user.

* Save info button
    ![save-info-btn]()

* not logged in user
    ![user-not-logged-in]()

* Profile with default saved information
    ![default-info]()

* Prefilled future order forms
    ![prefilled-info])

## Site Goal Testing

#### Site Goal 1

* I want to be able to add, edit and delete products, blog posts and the ability to delete comments from blog posts easily.

##### Action

* site admin have full CRUD ability over all things on the site. Admin can add, edit and delete products on the site or in the backend as they are set up as superusers, they can also edit and delete reviews that users have left, they can delete comments left by any user on the site and they can add edit and delete blog posts either on the site frontend or backend.

##### Expectation

* Site Admin have the ability to have full control over the site and when logged in as superusers, they can see additional functionality on the front end and see add and edit buttons that normal users can't see. This is mainly for safety reasons on the site.

##### Result

* Site Admin/Superusers have full CRUD functionality on the site and the ability and awareness to make use of the fuctionality on the site frontend and backend.

* edit and delete buttons on site for admin users
    ![edit-delete-btns]()

* delete comment button
    ![delete-comment-button]()

* Admin Backend
    ![admin-backend]()

* add blog post button
    ![add-blog-btn]()

* Delete Product Modal
    ![delete-product-modal]( )

#### Site Goal 2

* I want to be able to increase organic visitors to the site using SEO friendly blog posts.

##### Action

* Admin users can create blog posts rich with SEO friendly terms and phrases which increases organic traffic to the site.

##### Expectation

* The site sees an increase in visitors to the site from search engines like google who rank the site blog posts highly due to the SEO terms and searches from users.

##### Result

* Admin users add blog posts to the site which sees interactivity in the comments section by users and an increase in organic traffic to the site which leads to an increase in sales.

* add blog post
    ![add-blog-post]()

* comments section
    ![comments section]()

#### Site Goal 3

* I want an admin section of the site and to make administration tasks simpler.

##### Action

* Site owners/Admin are able and aware of how to access the backend of the site to make for easier administration tasks. I also want a place to see any customer messages

##### Expectation

* Admin users can easily access the backend and carry out their duties. They can also see any customer messages in the contact us table

##### Result

* Admin users have a much simpler task of doing administration duties than by doing it on the front end

* Admin Backend
    ![admin-backend]()

* contacts table under home heading
    ![contact-us]()

* customer messages
    ![customer-messages]()

#### Site Goal 4

* I want customers to have a relaxed and trouble free time on the site.

##### Action

* Customers should be able to flow through the site and navigate easily achieving their goal on the site.

##### Expectation

* That customers enjoy their time on the site and are able to interact with the site and make purchases where necessary.

##### Result

* From speaking with family members and friends who I asked to test out the site, I have received good feedback with regards to the working and functionality of the site, the navigation and the checkout process of the site. I am happy with my feedback.

#### Site Goal 5

* I want the site to be fully mobile responsive.

##### Action

* The site reacts to changes to screen size changes and remains consistent throughout.

##### Expectation

* The site remains consistent and functionality remains the same throughout the site

##### Result

* Please see above for the responsiveness testing of the site.    





