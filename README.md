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

--------------------------------------------------------------

**Checkout Confirmation**

![Checkout confirmation](docs/features/other/checkout-confirm.png)

- Once the user submits an order successfully, they are shown a confirmation page containing their order details, delivery and billing information.
- **Email**: A confirmation of their order is also sent to their email address containing their order details.
- **Order number**: The order number provided is unique to that particular order so it can be easily and uniquely referenced later if needed.
- **Continue Shopping**: If the user wishes to continue shopping for more products, they can use the button provided to be redirected to the products page.

<br>

![Checkout success message](docs/features/other/checkout-success.png)

- In addition to the order confirmation provided above, and the email the user received, they are also shown a success message in the top right hand corner just to give them the extra confidence that their order was successfully submitted.

**Login page**

![Login page](docs/features/other/login.png)

- The login page is where the user is able to login to their pre-registered account. If the user doesn't have an account already, they are able to register for one using the link provided. They can also reset their password if they can't remember it.

**Sign up page**

![Sign up page](docs/features/other/signup.png)

- The sign up page is where the user is able to create an account. Users must enter matching email addresses and passwords as part of the validation. The site will also inform them if they try to use a username which is already in use. If the user tries to signup for an account using an email address which is already in the database, an email will be sent to that email address to inform the person who has access to it, in case someone it trying to commit fraud.

**Password reset page**

![Password reset page](docs/features/other/password-reset.png)

- This page allows the user to reset their password if they have forgotten it, so the user doesn't have to sign up for another account if they've just forgotten their password.

**Change password page**

![Change password page](docs/features/other/change-password.png)

- This page allows the logged in user to change their password if they wish. This is useful if they believe someone is trying to get access to their account and personal information.

**Add a product**

![Add product](docs/features/other/add-product.png)

- This page is only accessible by the superuser, so customers without permission are not able to access this page via the product detail page or by entering the /products/add/ into the URL bar.
- Here, the superuser can add products to the store, selecting all of the relevant product details without having to access the admin panel.

**Edit product**

![Edit product](docs/features/other/edit-product.png)

- This page is only accessible by the superuser, so customers without permission are not able to access this page via the product detail page or by entering the /products/edit/ into the URL bar.
- Here, the superuser can edit existing products in the store.

**Profile page**

![Profile page](docs/features/other/profile-page.png)

- This is the users profile page. Here they can update their personal information.
- Users can also view their past order history. By clicking on the shortened version of their order number, they are taken to a page showing their full order details in case they need to look back on what they ordered.

**Contact page**

![Contact page](docs/features/other/contact-page.png)

- The contact page is where the user can find multiple ways of contacting the store.
- **Contact form**: The contact form allows the user a way of submitting a message to the store for a response. It requires a name, email, subject and enquiry message and once submitted, the form is sent to the In Home team's email address so they can assist the customer. If the user is already logged in, their email address is automatically entered for them.
- **Contact details**: The contact page also features the company contact details, in case the user wishes to contact the store directly.

## **Future Enhancements**

Some possible enhancements which could be applied in the future include:

- A section in the users profile which displays any previous reviews they have left for products, with the option to update or delete them directly from their profile.
- A featured product section above the footer which shows on any page of the site, so the store can promote the most popular products, or products they wish to push at any given time.
- A social account login feature, so the user can login to the website using their social media account rather than an email
- A special offers section for any discounted products or special deals available
- A 'You may also like...' section at the bottom of each product which shows products the user may be interested in based on what they are currently viewing
- A 'Suggested for you' section on the users profile page which suggests products they may wish to purchase based on their previous order history
- A newsletter signup, so the store can market their products and special offers directly to interested users.
- Product images could be converted to WebP format to allow faster page loading





