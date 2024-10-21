## **Shelly's Corner**

## **Site Overview**

Shally's Corner is an online e-commerce store selling different book genres. Users are able to browse and purchase books directly through the website, make an account to keep track of their order history, leave reviews for products they have purchased and contact the company for an inquiry via a contact form.


[View the deployed project here](https://shellys-corner-5b60b12a8abf.herokuapp.com/)

![Application shown on multiple devices]()

- [**Shelly's Corner**](#shellys-corner)
- [**Site Overview**](#site-overview)
- [**Table of contents**](#table-of-contents)
- [**Planning stage**](#planning-stage)
  - [**Target Audiences**](#target-audiences)
  - [**User Stories**](#user-stories)
  - [**Site Aims**](#site-aims)
  - [**Database Schema**](#database-schema)
  - [**Wireframes**](#wireframes)
  - [**Color Scheme**](#color-scheme)
- [**Typography**](#typography)
- [**Features**](#features)
- [**Future Enhancements**](#future-enhancements)
- [**Testing Phase**](#testing-phase)
  - [**Responsiveness**](#responsiveness)
  - [**Functionality**](#functionality)
  - [**Validators**](#validators)
  - [**Testing user stories**](#testing-user-stories)
- [**Bugs**](#bugs)
- [**Deployment**](#deployment)
- [**Tech**](#tech)
- [**Credits**](#credits)
  - [**Honourable mentions**](#honourable-mentions)
  - [**Media**](#media)

## **Planning stage**

### **Target Audiences**

- Users that want buy a book.
- Users in need of book to study.
- Users in need of book as a gift for a friend or relative.

### **User Stories**

**As a new user, I want to**:

1. Immediately understand the site's purpose
2. Easily navigate the website
3. Browse all available products
4. Filter products to quickly find what I need
5. Search for products
6. Contact the company for help or advice
7. Purchase products without registering for an account
8. Browse product reviews left by other users
9. Stay informed on actions I take throughout the website
10. Receive confirmation of my order
11. Access the site on any device
12. Create and log into an account

**As a registered user, I want to**:

13. View my profile page
14. View my previous order history
15. View and update my personal information
16. Create reviews for products I have purchased
17. View reviews for products I have purchased
18. Update reviews for products I have purchased
19. Delete reviews for products I have purchased
20. Change my password
21. Make purchases without filling in my personal information each time
22. Logout of my account

**As an admin, I want to**:

23. Add new products to the store
24. Update existing products
25. Delete existing products
26. Delete existing reviews

### **Site Aims**

- Provide a simple and responsive online shop for quick book purchases.
- Allow account registration to manage past orders, personal data and reviews.
- Offer clear feedback on user actions, confirming successes and alerting to issues.
- Implement a contact form for customer assistance and support.

### **Database Schema**

Many thanks to [Draw SQL](https://drawsql.app/) for assisting me with my database schema. This really helped me to visualise how the tables would be set up and where each table connects.

![Database Schema](docs/schema/dbschemanew2.png)

### **Wireframes**

The original wireframes for the main pages of the store can be found below. During development, a few decisions were made to change the original structure.

<br>

<details>
<summary>Home Page</summary>
<br>
<img alt="Home Page Wireframe" src="docs/wireframes/home-wf.png">
</details>
<br>

<details>
<summary>Profile Page</summary>
<br>
<img alt="Profile Page Wireframe" src="docs/wireframes/user-profile-wf.png">
</details>
<br>

<details>
<summary>Contact Page</summary>
<br>
<img alt="Contact Page Wireframe" src="docs/wireframes/contact-us-wf.png">
</details>
<br>

<details>
<summary>Products Page</summary>
<br>
<img alt="Products Page Wireframe" src="docs/wireframes/products-wf.png">
</details>
<br>

<details>
<summary>Product Detail Page</summary>
<br>
<img alt="Product Detail Page Wireframe" src="docs/wireframes/product-details-wf.png">
</details>
<br>

<details>
<summary>Shopping Bag</summary>
<br>
<img alt="Shopping Bag Wireframe" src="docs/wireframes/shopping-cart-wf.png">
</details>
<br>

<details>
<summary>Checkout Page</summary>
<br>
<img alt="Checkout Page Wireframe" src="docs/wireframes/checkout-wf.png">
</details>
<br>

<details>
<summary>Order Confirmation Page</summary>
<br>
<img alt="Order Confirmation Page Wireframe" src="docs/wireframes/order-conf-wf.png">
</details>

### **Color Scheme**

- Navy: #0D1B2A
- Blue: #415A77
- Black: #000
- White: #fff
- Grey: #d5d5d5 (used when hovering navigation links)

The [WCAG Color Contrast Checker](https://accessibleweb.com/color-contrast-checker/) was used to ensure that any navy/blue and white/grey combinations were suitable for use. All results passed except the small text in the AAA test for the blue/grey combination, however after a discussion with my mentor we agreed this was OK as the criteria for the AAA testing is incredibly high and almost never passes.

![Color contrast](docs/color/navy-white-color-check.png)

![Color contrast](docs/color/blue-white-color-check.png)

![Color contrast](docs/color/blue-grey-color-check.png)

## **Typography**

I decided to import and use the Outfit font using Google Fonts for the store, with Helvetica and sans-serif acting as the back up fonts should the Outfit import fail.

## **Features**

### **Features common to all pages**

**Navigation**

![Navigation](docs/features/all_pages/navbar.png)

- **Search bar**: Users can quickly search for products. If the search bar is empty but the user clicks the search button, they receive a message informing them that no search term was entered. The search function finds results matching the product name or description, maximizing the chances of finding what's needed.
- **Logo**: The Shelly's Corner logo was designed to be instantly recognizable as that of a home goods store. Clicking on the logo returns you to the main page.
- **My Account**: The options in the "My Account" dropdown menu vary based on the user's login status and whether they are a superuser. Non-authenticated users will see options to register and log in. Authenticated users will see their profile and an option to log out. Superusers will also have the option to add new products.
- **Shopping Bag**: The shopping bag displays the current total of purchases and, when clicked, takes the user to the shopping bag page.
- **Main nav links**: The blue navigation bar contains the main links for efficiently exploring the site. A "Home" button is included to return to the homepage from any point on the site. To find products, users can browse by category or use the complete list, with or without sorting options.
- **Free delivery banner**: A banner constantly informs the user of the minimum spend required for free shipping. This encourages increasing purchases if close to the free shipping threshold.

<br>

**Mobile Navigation**

![Mobile navigation](docs/features/all_pages/navbar-mobile.png)

- **Burger icon**: On smaller devices, the main navigation bar is hidden within the burger icon positioned on the left.
- **Search**: The search functionality operates identically across all devices. However, on more compact screens, the search bar appears as a dropdown menu that activates when clicking on the designated button, thus enhancing the user experience.
- **Other links**: The other interactive elements, such as the logo, access to personal account, and shopping cart, maintain the same functionality as described earlier, adapting to the device's layout.

<br>

**Footer**

![Footer](docs/features/all_pages/footer.png)

- **Quick links**: Quick links are provided at the bottom of the page, allowing users to rapidly access their desired products.
- **Contact Us**: The store's address, phone number, and email address are visible on all pages, enabling users to easily and directly get in touch with the store.
- **Social Media Links**: Links to the store's social media profiles are available for users who wish to follow it on platforms such as Facebook, Instagram, YouTube.
<br>

**Messages**

![Messages](docs/features/all_pages/messages.png)

- This box appears when a message is sent to the user to inform them about the success or failure of an action they have performed on the website.
- **Success message**: This is displayed when the user has successfully completed an action, such as adding an item to their cart, placing an order, submitting a contact form inquiry, or logging in/out. If the user has items in their cart, they will also see a link to proceed to checkout. Additionally, if they haven't spent enough for free shipping, they are informed about how much more they need to spend to reach the threshold.
- **Warning message**: This appears when it not necessary to warn the user about an action they've taken on the site.
- **Info message**: This is shown when the user needs to receive information about an action they've performed on the site.
- **Error message**: This is displayed to inform the user of an error related to an action they've taken.
### **Other Features**

**Home Page**

![Home hero section](docs/features/other/home-hero-section.png)

-This is one of the first elements the user will notice upon entering the site. The text and main image help to immediately understand the website's purpose. A "Shop Now" button is present to allow users to start shopping quickly and easily, directing them to the all products page. 

<br>

![Home categories section](docs/features/other/home-categories.png)

- To provide a more specific understanding of the store's offerings, categories are neatly presented right after, enabling users to immediately begin shopping by category if they already know which area of their home they wish to furnish.
**Products page**

![Products page](docs/features/other/products-page-2.png)

- **Sorting**: Users can sort products on any page using various parameters. When sorting by rating, products with a score are displayed first, followed by those without a current rating.
- **Product layout**: On wider screens, the site maximizes width by showing 4 products per row. The number of products per row decreases as the screen/device size reduces. Even on small devices, two products are placed side by side to prevent users from having to scroll excessively to view all products. All details remain clearly visible even with two products per row.
- **Rating**: The product score (if available) is calculated as an average of all review ratings submitted for that product to date.
- **Link to product**: When hovering over the product image, name, or price, these elements are underlined to clearly indicate to the user that clicking will open the product page. When hovering over the category, only this is underlined, linking to the relevant category page.

**Product detail page**

![Product detail page](docs/features/other/product-detail.png)

- **Image**: Clicking on the image opens a new tab with an enlarged version of the product.
- **Price**: TThe product price is clearly highlighted, allowing users to quickly assess the affordability of the purchase.
- **Category**: The product category is indicated with a relevant icon. Clicking on it takes the user to the category page to explore similar products.
- **Rating**: The product rating, if available, is visible both here and on the products page.
- **Edit/Delete product**: Administrators have access to buttons to edit or delete products directly from the site. Deletion requires confirmation via a modal window to prevent accidental removals.
- **Description**: Provides additional details about the product, complementing the information already present in the name.
- **Quantity select**: Users can select a quantity between 1 and 99. The system automatically prevents the input of out-of-range values, both through buttons and manual entry. If the total quantity in the cart exceeds 99, the user is informed that the maximum allowed value will be set.
- **Buttons**: Options are available to return to the products page or add the item to the cart. Adding to the cart generates a confirmation message for the user.

**Reviews (Product detail page)**

![Product review form](docs/features/other/review-form.png)

- Authenticated users have access to a form for leaving reviews on products listed on the website. They can input their feedback and assign a rating to the product, then submit the review which will be visible to all other users. The form can only be submitted if both feedback and a rating have been entered; otherwise, a pop-up notifies the user to complete both fields before proceeding.
- If a user has already reviewed the product in question, submitting a new form will update their existing review. This option is provided in case the user has changed their opinion about the product. Additionally, it prevents a dissatisfied customer from leaving multiple negative reviews, which would unfairly affect the overall product rating.
- For non-authenticated users, the form is not visible. Instead, a message is displayed inviting them to log in or register to leave a review, with direct links to the login and registration pages to facilitate the process.
- Once submitted, the review is displayed in the list below the form (further details on this aspect will be provided later).

<br>

![Product review list](docs/features/other/review-list-2.png)

- All submitted reviews are displayed in the list below the form, visible to all users. To optimise space and organize them neatly, they are stored within a Bootstrap accordion.
- Users who have left a review have the option to delete it if they wish. Additionally, the superuser has the authority to remove any review present on the site, for example in case of inappropriate language. When a user selects the delete option, a confirmation prompt appears to prevent accidental deletions.
- In the absence of reviews, the list is not shown, and a message appears instead, informing that no reviews have been submitted yet.

**Shopping bag**

![Shopping bag](docs/features/other/shopping-bag-2.png)

- The shopping bag page displays the items that the user has added while browsing the site. If the cart is empty, a message is shown along with a button to return to shopping.
- **Quantity / Update**: Users can modify the quantity of each item in the cart and update the total. Controls are in place to limit the quantity between 1 and 99, with informative messages for invalid attempts.
- **Remove item**: It's possible to completely remove items from the bag.
- **Product image**: Product images are clickable to return to the product page.
- **Subtotal**: The subtotal for each product updates automatically when the quantity is modified.
- **Free delivery threshold**: If the amount is below the £100 threshold for free shipping, a message appears indicating how much more is needed to reach it.
- **Buttons**:  Buttons are available to continue shopping or proceed to checkout.

**Checkout**

![Checkout form](docs/features/other/checkout-form-new.png)

- The payment form contains all the necessary details required from the user to process their order, including full name, email address, and delivery information.
- **Save info**: A checkbox is available, offering users the option to save their information to their profile. By choosing this option, their details will be automatically pre-filled for their next order. Users can update this information on their profile page if they wish. If the user is not logged in, a message is displayed prompting them to log in or register to save their information.
- **Stripe**: The store uses Stripe to process payments. When the button to complete the order is clicked, a loading animation appears until the processing is complete, aiming to prevent users from leaving the page during the payment process. A brief notice is shown to the user informing them of the amount that will be charged to their card.

<br>

![Checkout summary](docs/features/other/checkout-summary.png)

- On the payment page, the user is presented with a summary of their order, to ensure they are fully aware of what they are about to purchase. If they notice an error at this point, the user has the option to go back and modify the contents of their cart before finalizing the order and proceeding with payment.

**Checkout Confirmation**

![Checkout confirmation](docs/features/other/checkout-confirm.png)

- After the user successfully completes an order, a confirmation page is displayed containing the order details, delivery and billing information.
- **Email**: An order confirmation is also sent to the user's email address, including the complete purchase details.
- **Order number**: A unique order number is provided for that specific transaction, allowing easy and exclusive reference to the order in the future if needed.
- **Continue Shopping**: If the user wishes to purchase more products, they can use the designated button to be redirected to the products page.

<br>

![Checkout success message](docs/features/other/checkout-success.png)

- n addition to the order confirmation provided above and the email received by the user, a success message is also displayed in the top right corner, specifically to give them extra assurance that their order has been successfully submitted.

**Login page**

![Login page](docs/features/other/login.png)

- The access page is where users can authenticate themselves into their pre-registered account. If a user doesn't have an account yet, they have the option to create one using the provided link. Additionally, they can reset their password in case they have forgotten it.

**Sign up page**

![Sign up page](docs/features/other/signup.png)

- The registration page allows users to create an account. As part of the validation process, users must enter matching email addresses and passwords. The site will also notify them if they attempt to use a username that is already taken. If a user tries to sign up using an email address already in the database, an email will be sent to that address to inform the person who has access to it, in case someone is attempting to commit fraud.

**Password reset page**

![Password reset page](docs/features/other/password-reset.png)

- This page allows users to reset their password if they've forgotten it, eliminating the need to create a new account just because they can't remember their password.

**Change password page**

![Change password page](docs/features/other/change-password.png)

- This page allows the logged in user to change their password if they wish. This is useful if they believe someone is trying to get access to their account and personal information.

**Add a product**

![Add product](docs/features/other/add-product.png)

- This page is accessible only to the administrator, therefore customers without authorization cannot access it either from the product details page or by entering /products/add/ in the address bar.
- In this section, the administrator can add products to the store, selecting all relevant details without having to access the administration panel.

**Edit product**

![Edit product](docs/features/other/edit-product.png)

- This page is accessible only to the system administrator, therefore customers without authorization cannot access it either through the product details page or by entering /products/edit/ in the address bar.
- In this section, the administrator has the ability to modify existing products in the store.

**Profile page**

![Profile page](docs/features/other/profile-page.png)

- This is the user's profile page. Here they can update their personal details.
- Users can also view their previous order history. By clicking on the abbreviated version of their order number, they are directed to a page displaying the full order details, in case they need to review what they purchased.

**Contact page**

![Contact page](docs/features/other/contact-page.png)

- The contact page is where users can find various methods to communicate with the store.
- **Contact form**: The contact form provides users with a way to send a message to the store and receive a response. It requires a name, email, subject, and message text. Once submitted, the form is sent to the In Home team's email address, allowing them to assist the customer. If the user is already logged in, their email address is automatically filled in.
- **Contact details**: The contact page also includes the company's contact details, in case the user wishes to reach out to the store directly.

## **Future Enhancements**

Some potential improvements that could be implemented in the future include:

- A section in the user profile that displays previous reviews left for products, with the option to edit or delete them directly from the profile
- A featured products section above the footer visible on every page of the site, allowing the store to promote the most popular items or those they wish to push at any given time.
- A social account login feature, enabling users to log in to the site using their social media profile instead of an email.
- A special offers section for any discounted products or available promotions.
- A "You might also like..." section at the bottom of each product page showing items potentially interesting to the user based on what they are currently viewing.
- A "Recommended for you" section on the user profile page suggesting products that might interest them based on their previous order history.
- A newsletter subscription, so the store can promote its products and special offers directly to interested users.
- Product images could be converted to WebP format to enable faster page loading.

## **Testing Phase**

### **Responsiveness**

Responsiveness was checked and worked as intended with the following browsers and screen sizes:

- Extra Large (27" Mac Desktop):

  - Chrome
  - Safari
  - Firefox

- Large (15" MacBook Pro Laptop):

  - Chrome
  - Firefox
  - Safari

- Medium (10.9" iPad):

  - Chrome
  - Safari
  - Firefox

- Small (6" iPhone 13):

  - Chrome
  - Safari
  - Firefox

DevTools was also used to check the responsiveness at various screen sizes and devices from the list of devices available. All were fully responsive and caused no issues, including the smallest device available in the list which was a Galaxy Z Fold 5.

### **Functionality**
                                                                                                                                      
| Function                                             | Expectation                                                                                                                                           | Pass? |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **Navigation**                                           |                                                                                                                                                       |       |
| Search Bar (with search criteria)                    | On submit, redirect to products page showing products with names or descriptions matching users criteria                                               | Yes   |
| Search Bar (no search criteria)                      | On submit, user is informed they submitted an empty search                                                                                            | Yes   |
| Logo                                                 | On click, redirect to home page                                                                                                                        | Yes   |
| My Account (logged out user)                         | On click, dropdown appears with register and login links. 'Register' directs  to the sign up page, 'Login'   to login page.                             | Yes   |
| My Account (logged in user)                          | On click, dropdown appears with profile and logout links. 'My Profile' directs to users profile page, 'Logout'  to logout confirm page.                 | Yes   |
| My Account (logged in superuser)                     | On click, superuser has same options as above plus 'Add a product' which directs them to the add product page.                                          | Yes   |
| Shopping Bag                                         | On click, takes user to the shopping bag page.                                                                                                         | Yes   |
| Shopping Bag Total                                   | Default value shown is £0.00 unless user has items in their shopping bag, in which case amount shown should reflect the bag total.                      | Yes   |
| Home Nav Link                                        | On click, takes user to the home page.                                                                                                                 | Yes   |
| All Products Nav Link                                | On click, dropdown appears with relevant options, all linking to their relevant pages.                                                                 | Yes   |
| Kitchen Nav Link                                     | On click, dropdown appears with relevant options, all linking to their relevant pages.                                                                 | Yes   |
| Living Room Nav Link                                 | On click, dropdown appears with relevant options, all linking to their relevant pages.                                                                 | Yes   |
| Bedroom Nav Link                                     | On click, dropdown appears with relevant options, all linking to their relevant pages.                                                                 | Yes   |
| Bathroom Nav Link                                    | On click, dropdown appears with relevant options, all linking to their relevant pages.                                                                 | Yes   |
| Contact Nav Link                                     | On click, takes user to the contact page.                                                                                                               | Yes   |
| **Footer**                                               |                                                                                                                                                       |       |
| Quick Links                                          | On click, each link takes the user to the relevant page.                                                                                               | Yes   |
| Telephone Number                                     | On click, the site attempts to start a phone call direct to the store.                                                                                  | Yes   |
| Email                                                | On click,  the store attempts to start an email direct to the store via the users default email provider.                                               | Yes   |
| Social Media Links                                   | On click, user is directed to the relevant social media platform.                                                                                      | Yes   |
| **Home Page**                                            |                                                                                                                                                       |       |
| Shop Now                                             | On click, takes user to the all products page.                                                                                                         | Yes   |
| Kitchen Category Image                               | On click (on the image or the button), takes user to the kitchen products page.                                                                        | Yes   |
| Living Room Category Image                           | On click (on the image or the button), takes user to the living room products page.                                                                    | Yes   |
| Bedroom Category Image                               | On click (on the image or the button), takes user to the bedroom products page.                                                                        | Yes   |
| Bathroom Category Image                              | On click (on the image or the button), takes user to the bathroom products page.                                                                       | Yes   |
| **Products Page**                                        |                                                                                                                                                       |       |
| Link to product detail                               | For each product shown, the product image, name and price all link to that products detail page.                                                       | Yes   |
| Link to category                                     | For each product shown, the products category shown links to the category that product belongs to.                                                     | Yes   |
| Sorting by price                                     | Sorting  low to high displays the products in ascending order by price, and high to low in descending order.                                           | Yes   |
| Sorting by name                                      | Sorting  A-Z displays the products in alphabetical order by name, and Z-A in the reverse order.                                                        | Yes   |
| Sorting by rating                                    | Sorting  low to high displays the products in ascending order by rating, and high to low in descending order. Products with  ratings are always displayed first. | Yes   |
| Sorting by category                                  | Sorting  A-Z displays the products in alphabetical order by category, and Z-A in the reverse order.                                                    | Yes   |
| Products Home                                        | On click, products Home link directs the user to the all products page                                                                                 | Yes   |
| Products total                                       | Total number of products matches total number actually shown on page                                                                                   | Yes   |
| Products (search query)                              | When user is taken to the products page from a search query, page confirms how many products were found based on their search criteria.                 | Yes   |
| **Product Detail Page**                                  |                                                                                                                                                       |       |
| Image                                                | On click, image opens in a new tab                                                                                                                     | Yes   |
| Category                                             | On click, user is directed to the category in which the product belongs to                                                                             | Yes   |
| Edit (superuser only)                                | When superuser is logged in, edit link is shown which directs superuser to the edit product page                                                       | Yes   |
| Delete (superuser only)                              | When superuser is logged in, delete link is shown which prompts the delete product modal. The delete button deletes the product                        | Yes   |
| Quantity Decrease (-)                                | On click, quantity is reduced by 1 (unless quantity is already 1, then decrease button is disabled)                                                    | Yes   |
| Quantity Increase (+)                                | On click, quantity is increased by 1 (unless quantity is 99, then increase button is disabled)                                                         | Yes   |
| Quantity input, manual entry                         | If a quantity below 1 or above 99 is manually entered, user is told to enter a valid quantity when attempting to add the product to the bag             | Yes   |
| Keep shopping                                        | On click, user is directed to the all products page                                                                                                    | Yes   |
| Add to bag (product not already in bag)              | On click, product is added to the users shopping bag in the desired quantity, with success message confirming the action and a button to proceed to the checkout. Bag total to update at top of page | Yes   |
| Add to bag (product already in bag)                  | If product already in users bag and a further quantity is added making the new quantity above 99, bag quantity is set to 99 and user is informed. Otherwise, update bag quantity & total accordingly. | Yes   |
| Product Review Form (logged in user)                 | For logged in users, product review form to be displayed and only submitted when feedback is entered and a rating is selected.                          | Yes   |
| Product Review Form (user not logged in)             | Form is hidden and prompt for user to either login or register for an account is displayed.                                                            | Yes   |
| Product Review Form Submission                       | On submit (provided validation criteria is met), review is added to the reviews accordion style list below.                                             | Yes   |
| Product reviews                                      | If no reviews have been submitted for that product yet, message is displayed to that effect. Otherwise, reviews are stacked in a collapsable list.     | Yes   |
| Product reviews, delete                              | When viewing a review, if it belongs to the logged in user or a superuser is logged in, delete button appears which prompts the delete review modal. Clicking the modals delete button deletes the review. | Yes   |
| **Shopping Bag page**                                    |                                                                                                                                                       |       |
| No products                                          | If no products are currently in the shopping bag, user is informed their bag is empty and provided with a keep shopping button which directs them to the all products page. | Yes   |
| Products in bag                                      | If products are in the shopping bag, each products image, name, price, quantity and subtotal is shown                                                  | Yes   |
| Product image                                        | Product image directs user to that particular product                                                                                                  | Yes   |
| Update quantity (outside of 1-99 range)              | Update quantity to include same validation checks as on the product detail page to ensure quantity is always between 1 and 99. Message appear to inform the user if they try to go outside of the range | Yes   |
| Update quantity (inside of 1-99 range)               | On click, quantity, subtotal, bag total and grand total to be updated accordingly. Delivery total to be updated if under free delivery threshold        | Yes   |
| Remove                                               | On click, product is removed from the bag. Bag total and grand total updated accordingly (or revert to no products in bag message if last product is removed). If now below free delivery threshold, delivery total updated accordingly. | Yes   |
| Keep shopping                                        | On click, direct user to all products page                                                                                                             | Yes   |
| Secure checkout                                      | On click, direct user to checkout page                                                                                                                 | Yes   |
| **Checkout page**                                        |                                                                                                                                                       |       |
| Pre filled details                                   | If user is logged in and profile information is saved, customers details are pre-filled accordingly.                                                   | Yes   |
| Save delivery information (logged in user)           | If user is logged in, checkbox to save delivery information is shown. Once order is placed, delivery information on profile page is updated.            | Yes   |
| Save delivery information (user not logged in)       | If user is logged is not logged in, prompt to login or register appears taking them to the relevant pages.                                              | Yes   |
| Adjust bag                                           | On click, direct user back to the shopping bag                                                                                                          | Yes   |
| Charge warning                                       | Red warning message for charge amount to match the grand total on same page.                                                                           | Yes   |
| Product image                                        | Product image in order summary to link to product page                                                                                                 | Yes   |
| Complete order                                       | On click, loading spinner appears while order is processed. If order is successful, direct user to order confirmation page and success message appears. Clear shopping bag and reset bag total to £0.00 | Yes   |
| Complete order continued                             | With successful order, if user is logged in, add order to order history on profile page and sent confirmation of order to users email address           | Yes   |
| **Order confirmation page**                              |                                                                                                                                                       |       |
| Order details                                        | All order details shown to match those that were entered originally. Unique order number assigned to the order                                         | Yes   |
| Missed something                                     | Missed something button to direct user to all products page                                                                                            | Yes   |
| **Profile page**                                         |                                                                                                                                                       |       |
| Delivery information                                 | If user has previously saved delivery info via checkout page or previously saved via profile page, details are pre-populated.                          | Yes   |
| Change password                                      | On click, direct user to change password page                                                                                                          | Yes   |
| Update information                                   | On click, update any changed details in form above                                                                                                     | Yes   |
| Order history                                        | All previous orders to be displayed, with order number acting as a link to order page. When clicked, message to appear informing user they are viewing an existing order | Yes   |
| **Logout Page**                                          |                                                                                                                                                       |       |
| Cancel                                               | On click, directs user to Home page and user is not logged out                                                                                         | Yes   |
| Sign out                                             | On click, logs the user out, message appears to confirm and user is directed to the home page                                                          | Yes   |
| **Sign Up/Register Page**                                |                                                                                                                                                       |       |
| Sign in link                                         | On click, directs user to login page                                                                                                                   | Yes   |
| Email validation                                     | On submit/sign up, if email address doesn’t match email address confirmation field, user is informed must retry with correct details                   | Yes   |
| Username validation                                  | On submit/sign up, if username already exists, user is informed to make another choice                                                                 | Yes   |
| Password validation                                  | On submit/sign up, if passwords don't match or meet the minimum criteria, user is informed with instructions as to what they must do to meet criteria  | Yes   |
| Back to login                                        | On click, directs user to login page                                                                                                                   | Yes   |
| Sign up                                              | On click, if all validation checks pass, user is sent an email to confirm their email address and registration. Once confirmed, account is created and user can login. | Yes   |
| Sign up (email already registered)                   | As above, but email to user mentions that someone has tried to create an account using their email, but an account already exists.                     | Yes   |
| **Login page**                                           |                                                                                                                                                       |       |
| Signup link                                          | On click, directs user to sign up/register page                                                                                                        | Yes   |
| Home button                                          | On click, directs user to the home page                                                                                                                | Yes   |
| Sign in                                              | On click, if username/email and password match a users details stored in database, log the user in with success message                               | Yes   |
| Forgot password                                      | On click, directs user to reset password page                                                                                                          | Yes   |
| **Change password page**                                 |                                                                                                                                                       |       |
| Back to login                                        | On click, directs user to login page                                                                                                                   | Yes   |
| Change password                                      | On click, update the users password if current password matches current password currently stored in database and new password and new password (again) both match | Yes   |
| **Reset password page**                                  |                                                                                                                                                       |       |
| Back to login                                        | On click, directs user to login page                                                                                                                   | Yes   |
| Reset my password                                    | On click, send password reset email to users email                                                                                                     | Yes   |
| **Contact page**                                         |                                                                                                                                                       |       |
| Contact form                                         | If user is logged in, email is pre-populated. On submit, if all fields are completed and match validation criteria, user is directed to home page and shown success message. Contact form is sent to In Home email address for a response | Yes   |
| **Add product page (superuser only)**                    |                                                                                                                                                       |       |
| Select image                                         | On click, opens image select window on users device. When image is selected and confirmed, message appears to user to let them know what the image will be set to. | Yes   |
| Cancel                                               | On click, direct user to all products page                                                                                                             | Yes   |
| Add product                                          | On click, provided required fields are completed/entered, add new product to store                                                                     | Yes   |
| Access                                               | If any user other than the superuser attempts to access the add product page, they are informed they can't access it                                    | Yes   |
| **Edit product page (superuser only)**                   |                                                                                                                                                       |       |
| On load                                              | Info message to inform superuser what product they are editing                                                                                        | Yes   |
| Pre-filled details                                   | Existing product details pre-filled in relevant fields                                                                                                 | Yes   |
| Select image                                         | On click, opens image select window on users device. When image is selected and confirmed, message appears to user to let them know what the image will be set to. | Yes   |
| Remove image                                         | On submit (update), if ticked, image is removed from the product                                                                                       | Yes   |
| Cancel                                               | On click, direct user to all products page                                                                                                             | Yes   |
| Update product                                       | On click, provided required fields are completed/entered, update existing product details                                                              | Yes   |
| Access                                               | If any user other than the superuser attempts to access the edit product page, they are infomred they can't access it                                   | Yes   |
| **404 page not found**                                   |                                                                                                                                                       |       |
| Page not found                                       | For any 404 page not found errors, direct user to custom 404 error page                                                                                | Yes   |
| **500 error page**                                       |                                                                                                                                                       |       |
| 500 server error page                                | For any 500 server errors, direct user to custom 500 error page                                                                                        | Yes   |