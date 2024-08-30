-- Distinctiveness and Complexity --

/admin_login can be logged into using:
super
password123

This is a web based welcomebook for a family member's AirBnb Guesthouse. The goal of the project was to create a web based welcomebook for their guests. As the host doesn't live near the AirBnb year round, the web-based welcomebook would allow the host to make updates remotely, without having to make physical changes to a traditional welcomebook.

However, the host doesn't know how to code, and therefore wouldn't be able to update the welcomebook without the help of someone who does - which can be time consuming and costly. So, the challenge of the project was to create a simple and easy to use interface that would allow the host to create, update, and delete content from the welcomebook as desired without needing to know anything about web development.

I started the project in Figma and began designing the welcomebook based on research on what welcomebooks should include and what guests use welcomebooks for. The host also wanted to include an About the house section for any guests interested in how the house was built and the reason behind the design decisions. I narrowed the contents of the welcomebook down to:
- About the house
- Essential information
- Places to eat
- Things to do
- Emergency contacts
- House rules

My goal was to provide the host with enough flexibility to write, edit, arrange and delete their own content for the welcomebook but to limit customization in terms of layout and design to prevent the host from getting bogged down with design decisions.

There were two distinct features I had never programmed before:
1. A sorting feature that allowed the host to re-order the contents of the welcomebook by dragging and dropping an existing element, then clicking a save button.
2. Implementing a rich text editor that allowed the host to write and format their own "About the House" page without needing to know HTML. This was important to the host because they wanted the flexibility of writing their own article with different links. Using a rich text editor, the host would be able to write their article as if writing a Word document, which would then be converted to HTML and appear to guests how the host intended.

I used two JavaScript libraries to accomplish the implementation of these features. Sortable.js for the sorting feature, and Quill for the rich text editor feature.

I created a sortable list using the Sortable object and passing in the container div for my list items to the create method. To allow the user to save the positions of the list items I added an event listener to the save button, and within the callback function, added all the id's of the list items to an array using the forEach() method that I then sent to my 'edit_position' view through a POST request using fetch(). This way I've effectively created a snapshot of the order that the list item's were in at the time the user clicked the save button. The forEach() method loops over the node list of list items returned by queryselectorAll from top down in the DOM, therefore, the first list item's id is stored as the 0th index of my positions array. In my edit_position view, I used python's enumerate() function to add an index to each list item id. I then looped over the object returned by the enumerate() function and assigned the index to the item's position model value and saved the model. Within the models that I wanted to be sortable, I was able to order them using the Meta class and setting the ordering value to the position field.

For the implementation of the rich text editor feature I chose Quill. Using the Quill documentation I set up the required script and style tags in my layout.html header and wrote the required initializing function in my JavaScript file. The challenge was figuring out how to send what the user had typed into the quill editor to Django in order to store what the user had written as HTML. I would then use this HTML to display to guests. After reading Quill's documentation further it turned out to be as simple as calling the getSemanticHTML() method on the quill object, storing it in a variable and stringifying it, then sending that variable to Django through a post request. I was then able to render the html content saved in the About model using {{ about.html_content | safe }} in my template.

Aside from the new features I implemented, the rest of the project consisted of letting the user create, update, and delete information for the welcomebook. However, if there was ever the need to create a new page and a new model for that page, I wanted the process of adding a new page to be as easy as just writing the HTML for said page. I did this by adding a 'type' data attribute to my HTML elements which corresponded to which model they were apart of. I then used this 'type' data attribute in a majority of my JavaScript and Django view functions to communicate which model was to be created, updated, or deleted. This allowed me to, for example, write one function each for JavaScript and Django to edit items across different models. Now if there's ever a need to create a new page that takes data from a new model I don't need to worry about writing new JavaScript and Django functions for the new page/model specifically.


-- Contents of files I created --

static/app/assets: svgs for icons used in index

static/app/css: scss and css files

static/app/js: JavaScript files

templates/app: HTML templates

admin.py: admin interface configuration

forms.py: Django forms created using the corresponding models. The forms used to allow users to upload images to certain models.

models.py: Django models for all of the data I wanted to allow the host to share to guests in the welcomebook.

urls.py: All of the routes for the view functions. Routes for admin only pages, user/guest pages, and API routes.

media: This is the directory where the user uploaded images are stored.

requirements.txt: made using pip freeze > requirements.txt, a txt file including all of the dependencies for the project.

