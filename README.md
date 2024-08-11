--- SORTABLE FUNCTION FOR HOUSE RULES PAGE --

use sortable js library to create sortable list of rules on front end.
sortable list will be in a form that when the user clicks submit will
iterate over the list and take the ID of each rule and add it to an array
that will be sent through a POST request to the backend
the server will take the array of rules and enumerate it using enumerate()
then using the object returned by the enumerate() function, the "position"
value of each house_rule model will be updated with it's corresponding enumeration value