# Function to change the value of the firstName parameter in the request body
def get_user_body(first_name):
    # Copy the dictionary with the request body from the data file to the variable current_body
    current_body = data.user_body.copy()
    # Change the value of the firstName parameter
    current_body["firstName"] = first_name
    # Return a new dictionary with the required firstName value
    return current_body

# Function to test positive cases


def positive_assert(first_name):
    # The updated request body is saved in the variable user_body
    user_body = get_user_body(first_name)
    # The result of the request to create a new user or user is saved in the variable response
    user_response = sender_stand_request.post_new_user(user_body)

    # Check if the status code is 201
    assert user_response.status_code == 201
    # Check that the authToken field is in the response body and contains a value
    assert user_response.json()["authToken"] != ""

    # Check if the user or user exists and is unique
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

# Function to test negative cases for errors related to characters
def negative_assert_symbol(first_name):
    # The updated request body is saved in the variable user_body
    user_body = get_user_body(first_name)

    # The result of the request is saved in the variable response
    response = sender_stand_request.post_new_user(user_body)

    # Check if the status code is 400
    assert response.status_code == 400

    # Check that the code attribute in the response body is 400
    assert response.json()["code"] == 400
    # Check the message attribute in the response body
    assert response.json()["message"] == "The name you entered is incorrect. " \
                                         "Names can only contain Latin characters, " \
                                         "names must have at least 2 characters and no more than 15 characters"

# Function to test negative cases when the error is "Not all required parameters were sent"
def negative_assert_no_firstname(user_body):
    # The result of the request is saved in the variable response
    response = sender_stand_request.post_new_user(user_body)

    # Check if the status code is 400
    assert response.status_code == 400

    # Check that the code attribute in the response body is 400
    assert response.json()["code"] == 400
    # Check the message attribute in the response body
    assert response.json()["message"] == "Not all required parameters were sent"

# Test 1. User or user created successfully. The firstName parameter contains 2 characters
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Test 2. User or user created successfully. The firstName parameter contains 15 characters
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Test 3. Error. The firstName parameter contains 1 character
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Test 4. Error. The firstName parameter contains 16 characters
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Test 5. User or user created successfully. The firstName parameter contains Latin characters
def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")

# Test 6. Error. The firstName parameter contains a string of special characters
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

# Test 7. Error. The firstName parameter contains a string of digits
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# Test 8. Error. The firstName parameter is missing in the request
def test_create_user_no_first_name_get_error_response():
    # The dictionary with the request body is copied from the data file to the variable user_body
    user_body = data.user_body.copy()
    # The firstName parameter is removed from the request
    user_body.pop("firstName")
    # Check the response
    negative_assert_no_firstname(user_body)

# Test 9. Error. The firstName parameter contains an empty string
def test_create_user_empty_first_name_get_error_response():
    # The updated request body is saved in the variable user_body
    user_body = get_user_body("")
    # Check the response
    negative_assert_no_firstname(user_body)

# Test 10. Error. The type of the firstName parameter: number
def test_create_user_number_type_first_name_get_error_response():
    # The updated request body is saved in the variable user_body
    user_body = get_user_body(12)
    # The result of the request to create a new user or user is saved in the variable response
    response = sender_stand_request.post_new_user(user_body)

    # Check the status code of the response
    assert response.status_code == 400
#
#This code has been updated with proper commenting. Comments should be clear and concise. Stay focused, as this is very important for your career.