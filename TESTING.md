# Testing

### Testing was required as part of MS4

#### Responsive Testing

In testing my site for mobile responsiveness I was constantly checking the site using Chrome Dev Tools on the various screen resolutions on offer. I aimed to make the site responsive down as far  as a 280px screen which was achieved through the use of media queries.

friends and family members also tested the site out on their relevant devices and it all worked as expected.

Please see below for a list of all screen sizes that my site was found to be mobile responsive on:

* Galaxy Fold

![Galaxy Fold]()

* Moto G4

![Moto G4]()

* Iphone 4

![Iphone 4]()

* Galaxy s5

![Galaxy s5]()

* pixel 2

![pixel 2]()


* iphone 5

![iphone 5]()

* iphone 6

![iphone 6]()

* iphone 6 plus

![iphone 6 plus]()

* iphone x

![iphone x]()

* ipad

![ipad]()

* ipad pro

![ipad pro]()

* surface duo

![surface duo]()


### Lighthouse

* I ran my site throught Lighthouse which generated reports for mobile and desktop views.

* Initially, there were some issues regarding alt text of images but I made the changes necessary and please see below for the lightouse reports for both desktop and mobile.

* Desktop
    * ![lighthouse-desktop]()

* Mobile
    * ![lighthouse-mobile]()

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

![add-to-bag]()

* This worked, so I then went to the bag page and tried to edit the qty of the product in my bag.

![update-bag-page]()

* I also then tried to remove the item from my bag to test delete functionality.

![delete-bag-page]()

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


