# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest
from io import StringIO
import sys

from src.white_box import *


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

class TestWhiteBoxHomework(unittest.TestCase):
    """
    White-box unittest class (Homework).
    """

    # 1
    def test_check_number_status_positive(self):
        """
        Checks the number status is positive.
        """
        self.assertEqual(check_number_status(5), "Positive")
    
    def test_check_number_status_negative(self):
        """
        Checks the number status is negative.
        """
        self.assertEqual(check_number_status(-5), "Negative")
    
    def test_check_number_status_zero(self):
        """
        Checks the number status is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    # 2
    def test_validate_password_length(self):
        """
        Checks the password length is valid.
        """
        self.assertFalse(validate_password("123456"))
    
    def test_validate_password_uppercase(self):
        """
        Checks the password has at least one uppercase letter.
        """
        self.assertFalse(validate_password("12345678"))
    
    def test_validate_password_lowercase(self):
        """
        Checks the password has at least one lowercase letter.
        """
        self.assertFalse(validate_password("12345678A"))
    
    def test_validate_password_digit(self):
        """
        Checks the password has at least one digit.
        """
        self.assertFalse(validate_password("ABCDEFGHabc"))
    
    def test_validate_password_special_character(self):
        """
        Checks the password has at least one special character.
        """
        self.assertFalse(validate_password("ABCDEFGHabc123"))
    
    def test_validate_password_valid(self):
        """
        Checks the password is valid.
        """
        self.assertTrue(validate_password("ABCDEFGHabc123!"))
    
    # 3
    def test_calculate_total_discount_smaller_than_100(self):
        """
        Checks the total discount is smaller than 100.
        """
        self.assertEqual(calculate_total_discount(90), 0)
    
    def test_calculate_total_discount_between_100_and_500(self):
        """
        Checks the total discount is between 100 and 500.
        """
        self.assertEqual(calculate_total_discount(300), 30)
    
    def test_calculate_total_discount_greater_than_500(self):
        """
        Checks the total discount is greater than 500.
        """
        self.assertEqual(calculate_total_discount(600), 120)
    
    # 4
    def test_calculate_order_total(self):
        """
        Checks the order total is calculated correctly.
        """
        items = [
            {"quantity": 3, "price": 10}, 
            {"quantity": 7, "price": 20},
            {"quantity": 11, "price": 30},
        ]
        self.assertEqual(calculate_order_total(items), 460)
    
    # 5
    def test_calculate_items_shipping_cost_standard_low_weight(self):
        """
        Checks the shipping cost for standard delivery with low weight.
        """
        items = [
            {"weight": 1},
            {"weight": 2}
        ]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)
    
    def test_calculate_items_shipping_cost_express_low_weight(self):
        """
        Checks the shipping cost for express delivery with low weight.
        """
        items = [
            {"weight": 1},
            {"weight": 2}
        ]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)
    
    def test_calculate_items_shipping_cost_standard_mid_weight(self):
        """
        Checks the shipping cost for standard delivery with mid weight.
        """
        items = [
            {"weight": 3},
            {"weight": 4}
        ]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)
    
    def test_calculate_items_shipping_cost_express_mid_weight(self):
        """
        Checks the shipping cost for express delivery with mid weight.
        """
        items = [
            {"weight": 3},
            {"weight": 4}
        ]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)
    
    def test_calculate_items_shipping_cost_standard_high_weight(self):
        """
        Checks the shipping cost for standard delivery with high weight.
        """
        items = [
            {"weight": 5},
            {"weight": 6}
        ]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)
    
    def test_calculate_items_shipping_cost_express_high_weight(self):
        """
        Checks the shipping cost for express delivery with high weight.
        """
        items = [
            {"weight": 5},
            {"weight": 6}
        ]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)
    
    # 6
    def test_validate_login_small_username(self):
        """
        Checks the username is too small.
        """
        self.assertEqual(validate_login("a", "12345678"), "Login Failed")
    
    def test_validate_login_big_username(self):
        """
        Checks the username is too big.
        """
        self.assertEqual(validate_login("123456789012345678901","12345678"), "Login Failed")
    
    def test_validate_login_small_password(self):
        """
        Checks the password is too small.
        """
        self.assertEqual(validate_login("12345678", "a"), "Login Failed")
    
    def test_validate_login_big_password(self):
        """
        Checks the password is too big.
        """
        self.assertEqual(validate_login("12345678", "123456789012345678901"), "Login Failed")
    
    def test_validate_login_valid(self):
        """
        Checks the login is valid.
        """
        self.assertEqual(validate_login("12345678", "12345678"), "Login Successful")
    
    # 7
    def test_verify_age_small(self):
        """
        Checks the age is too small.
        """
        self.assertEqual(verify_age(17), "Not Eligible")
    
    def test_verify_age_big(self):
        """
        Checks the age is too big.
        """
        self.assertEqual(verify_age(71), "Not Eligible")
    
    def test_verify_age_eligible(self):
        """
        Checks the age is eligible.
        """
        self.assertEqual(verify_age(25), "Eligible")
    
    # 8
    def test_categorize_product_category_a(self):
        """
        Checks the product category is A.
        """
        self.assertEqual(categorize_product(20), "Category A")
    
    def test_categorize_product_category_b(self):
        """
        Checks the product category is B.
        """
        self.assertEqual(categorize_product(70), "Category B")
    
    def test_categorize_product_category_c(self):
        """
        Checks the product category is C.
        """
        self.assertEqual(categorize_product(150), "Category C")
    
    def test_categorize_product_category_d(self):
        """
        Checks the product category is D.
        """
        self.assertEqual(categorize_product(300), "Category D")
    
    # 9
    def test_validate_email_invalid_len_email(self):
        """
        Checks the email length is invalid.
        """
        self.assertEqual(validate_email("a@b"), "Invalid Email")
    
    def test_validate_email_invalid_at(self):
        """
        Checks the email has no @.
        """
        self.assertEqual(validate_email("abaacom"), "Invalid Email")
    
    def test_validate_email_invalid_dot(self):
        """
        Checks the email has no dot.
        """
        self.assertEqual(validate_email("a@bcom"), "Invalid Email")

    
    def test_validate_email_valid(self):
        """
        Checks the email is valid.
        """
        self.assertEqual(validate_email("abco@gcom.com"), "Valid Email")
    
    # 10
    def test_celsius_to_fahrenheit_valid(self):
        """
        Checks the conversion from Celsius to Fahrenheit is valid.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)
    
    def test_celsius_to_fahrenheit_invalid(self):
        """
        Out of the scope.
        """
        self.assertEqual(celsius_to_fahrenheit(-500), "Invalid Temperature")
    
    # 11
    def test_validate_credit_card_invalid_len(self):
        """
        Checks the credit card length is invalid.
        """
        self.assertEqual(validate_credit_card("1234567890"), "Invalid Card")
    
    def test_validate_credit_card_invalid_is_digit(self):
        """
        Checks the credit card has non-digit characters.
        """
        self.assertEqual(validate_credit_card("1234567890123a"), "Invalid Card")
    
    def test_validate_credit_card_valid(self):
        """
        Checks the credit card is valid.
        """
        self.assertEqual(validate_credit_card("12345678901234"), "Valid Card")
    
    # 12
    def test_validate_date_invalid_year(self):
        """
        Checks the year is invalid.
        """
        self.assertEqual(validate_date(2200, 2, 29), "Invalid Date")
    
    def test_validate_date_invalid_month(self):
        """
        Checks the month is invalid.
        """
        self.assertEqual(validate_date(2020, 13, 29), "Invalid Date")
    
    def test_validate_date_invalid_day(self):
        """
        Checks the day is invalid.
        """
        self.assertEqual(validate_date(2020, 2, 35), "Invalid Date")
    
    def test_validate_date_valid(self):
        """
        Checks the date is valid.
        """
        self.assertEqual(validate_date(2020, 2, 29), "Valid Date")
    
    # 13
    def test_check_flight_eligibility_invalid_age_and_no_frequent_flyer(self):
        """
        Checks the age is invalid and the user is not a frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
    
    def test_check_flight_eligibility_valid_age(self):
        """
        Checks the age is valid.
        """
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")
    
    def test_check_flight_eligibility_frequent_flyer(self):
        """
        Checks the user is a frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
    
    # 14
    def test_validate_url_invalid_len(self):
        """
        Checks the URL length is invalid.
        """
        self.assertEqual(validate_url("abcde" * 100), "Invalid URL")
    
    def test_validate_url_invalid_start(self):
        """
        Checks the URL doesn't start with http:// or https://.
        """
        self.assertEqual(validate_url("abcde.com"), "Invalid URL")
    
    def test_validate_url_valid(self):
        """
        Checks the URL is valid.
        """
        self.assertEqual(validate_url("https://www.google.com"), "Valid URL")
    
    # 15
    def test_calculate_quantity_discount_no_discount(self):
        """
        Checks the quantity discount is 0.
        """
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
    
    def test_calculate_quantity_discount_5_percent(self):
        """
        Checks the quantity discount is 5%.
        """
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")
    
    def test_calculate_quantity_discount_10_percent(self):
        """
        Checks the quantity discount is 10%.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
    
    # 16
    def test_check_file_size_invalid(self):
        """
        Checks the file size is invalid.
        """
        self.assertEqual(check_file_size(1048576+1), "Invalid File Size")
    
    def test_check_file_size_valid(self):
        """
        Checks the file size is valid.
        """
        self.assertEqual(check_file_size(10), "Valid File Size")
    
    # 17
    def test_check_loan_eligibility_low_income(self):
        """
        Checks the income is low.
        """
        self.assertEqual(check_loan_eligibility(10000, 1000), "Not Eligible")
    
    def test_check_loan_eligibility_good_income_and_good_credit(self):
        """
        Checks the income is good and the credit is good.
        """
        self.assertEqual(check_loan_eligibility(50000, 1000), "Standard Loan")
    
    def test_check_loan_eligibility_good_income_and_bad_credit(self):
        """
        Checks the income is good and the credit is bad.
        """
        self.assertEqual(check_loan_eligibility(50000, 500), "Secured Loan")
    
    def test_check_loan_eligibility_high_income_and_good_credit(self):
        """
        Checks the income is high and the credit is good.
        """
        self.assertEqual(check_loan_eligibility(100000, 1000), "Premium Loan")
    
    def test_check_loan_eligibility_high_income_and_bad_credit(self):
        """
        Checks the income is high and the credit is bad.
        """
        self.assertEqual(check_loan_eligibility(100000, 500), "Standard Loan")
    
    # 18
    def test_calculate_shipping_cost_low_price(self):
        """
        Checks the shipping cost for low price.
        """
        self.assertEqual(calculate_shipping_cost(1, 1, 1, 1), 5)
    
    def test_calculate_shipping_cost_mid_price(self):
        """
        Checks the shipping cost for mid price.
        """
        self.assertEqual(calculate_shipping_cost(4, 15, 15, 15), 10)
    
    def test_calculate_shipping_cost_high_price(self):
        """
        Checks the shipping cost for high price.
        """
        self.assertEqual(calculate_shipping_cost(10, 300, 300, 300), 20)
    
    # 19
    def test_grade_quiz_pass(self):
        """
        Checks the quiz is passed.
        """
        self.assertEqual(grade_quiz(8, 1), "Pass")
    
    def test_grade_quiz_conditional_pass(self):
        """
        Checks the quiz is conditionally passed.
        """
        self.assertEqual(grade_quiz(6, 1), "Conditional Pass")
    
    def test_grade_quiz_fail(self):
        """
        Checks the quiz is failed.
        """
        self.assertEqual(grade_quiz(4, 1), "Fail")
    
    # 20
    def test_authenticate_user_admin(self):
        """
        Checks the user is an admin.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")
    
    def test_authenticate_user_user(self):
        """
        Checks the user is a regular user.
        """
        self.assertEqual(authenticate_user("12345678", "12345678"), "User")
    
    def test_authenticate_user_invalid(self):
        """
        Checks the user is invalid.
        """
        self.assertEqual(authenticate_user("admin", "admin"), "Invalid")
    
    # 21
    def test_get_weather_advisory_high(self):
        """
        Checks the weather advisory is high.
        """
        self.assertEqual(get_weather_advisory(35, 80), "High Temperature and Humidity. Stay Hydrated.")
    
    def test_get_weather_advisory_low(self):
        """
        Checks the weather advisory is low.
        """
        self.assertEqual(get_weather_advisory(-20, 50), "Low Temperature. Bundle Up!")
    
    def test_get_weather_advisory_normal(self):
        """
        Checks the weather advisory is normal.
        """
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

# 22 
class TestVendingMachine(unittest.TestCase):
    """
    VendingMachine unittest class.
    """

    def setUp(self):
        """
        Set up for each test.
        """
        self.vending_machine = VendingMachine()

    def test_initial_state(self):
        """
        Test the initial state of the vending machine.
        """
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_insert_coin(self):
        """
        Test inserting a coin when the machine is ready.
        """
        response = self.vending_machine.insert_coin()
        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(response, "Coin Inserted. Select your drink.")

    def test_invalid_insert_coin(self):
        """
        Test inserting a coin when the machine is not in the ready state.
        """
        # First insert a coin to change the state to "Dispensing"
        self.vending_machine.insert_coin()

        # Try inserting another coin, which should return an invalid operation
        response = self.vending_machine.insert_coin()
        self.assertEqual(response, "Invalid operation in current state.")
        self.assertEqual(self.vending_machine.state, "Dispensing")

    def test_select_drink(self):
        """
        Test selecting a drink after inserting a coin.
        """
        # Insert a coin first to change the state
        self.vending_machine.insert_coin()

        # Now select a drink
        response = self.vending_machine.select_drink()
        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(response, "Drink Dispensed. Thank you!")

    def test_invalid_select_drink(self):
        """
        Test selecting a drink when the machine is in the 'Ready' state.
        """
        response = self.vending_machine.select_drink()
        self.assertEqual(response, "Invalid operation in current state.")
        self.assertEqual(self.vending_machine.state, "Ready")

# 23
class TestTrafficLight(unittest.TestCase):
    """
    TrafficLight unittest class.
    """

    def setUp(self):
        """
        Set up for each test.
        """
        self.traffic_light = TrafficLight()

    def test_initial_state(self):
        """
        Test the initial state of the traffic light.
        """
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_change_state_from_red_to_green(self):
        """
        Test changing state from 'Red' to 'Green'.
        """
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

    def test_change_state_from_green_to_yellow(self):
        """
        Test changing state from 'Green' to 'Yellow'.
        """
        # First change to 'Green'
        self.traffic_light.change_state()
        # Now change to 'Yellow'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

    def test_change_state_from_yellow_to_red(self):
        """
        Test changing state from 'Yellow' to 'Red'.
        """
        # First go through 'Green' and 'Yellow'
        self.traffic_light.change_state()  # Red -> Green
        self.traffic_light.change_state()  # Green -> Yellow
        self.traffic_light.change_state()  # Yellow -> Red
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_full_cycle(self):
        """
        Test the full cycle of the traffic light.
        """
        # Initial state should be 'Red'
        self.assertEqual(self.traffic_light.get_current_state(), "Red")
        
        # Change to 'Green'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

        # Change to 'Yellow'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

        # Change to 'Red'
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

# 24
class TestUserAuthentication(unittest.TestCase):

    def setUp(self):
        self.auth = UserAuthentication()

    def test_initial_state(self):
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_success(self):
        result = self.auth.login()
        self.assertEqual(self.auth.state, "Logged In")
        self.assertEqual(result, "Login successful")

    def test_login_invalid(self):
        self.auth.login()  # Log in first
        result = self.auth.login()
        self.assertEqual(result, "Invalid operation in current state")

    def test_logout_success(self):
        self.auth.login()  # Log in first
        result = self.auth.logout()
        self.assertEqual(self.auth.state, "Logged Out")
        self.assertEqual(result, "Logout successful")

    def test_logout_invalid(self):
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")

# 25
class TestDocumentEditingSystem(unittest.TestCase):

    def setUp(self):
        self.doc_system = DocumentEditingSystem()

    def test_initial_state(self):
        self.assertEqual(self.doc_system.state, "Editing")

    def test_save_document_success(self):
        result = self.doc_system.save_document()
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(result, "Document saved successfully")

    def test_save_document_invalid(self):
        self.doc_system.save_document()  # Save first
        result = self.doc_system.save_document()
        self.assertEqual(result, "Invalid operation in current state")

    def test_edit_document_success(self):
        self.doc_system.save_document()  # Save first
        result = self.doc_system.edit_document()
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(result, "Editing resumed")

    def test_edit_document_invalid(self):
        result = self.doc_system.edit_document()
        self.assertEqual(result, "Invalid operation in current state")

# 26
class TestElevatorSystem(unittest.TestCase):

    def setUp(self):
        self.elevator = ElevatorSystem()

    def test_initial_state(self):
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_success(self):
        result = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(result, "Elevator moving up")

    def test_move_up_invalid(self):
        self.elevator.move_up()  # Move up first
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")

    def test_move_down_success(self):
        result = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(result, "Elevator moving down")

    def test_move_down_invalid(self):
        self.elevator.move_down()  # Move down first
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")

    def test_stop_success_from_moving_up(self):
        self.elevator.move_up()  # Move up first
        result = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(result, "Elevator stopped")

    def test_stop_success_from_moving_down(self):
        self.elevator.move_down()  # Move down first
        result = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(result, "Elevator stopped")

    def test_stop_invalid(self):
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")

# 27
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("12345", 1000.0)

    def test_initial_state(self):
        self.assertEqual(self.account.account_number, "12345")
        self.assertEqual(self.account.balance, 1000.0)

    def test_view_account(self):
        # Capture the printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.account.view_account()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        
        expected = "The account 12345 has a balance of 1000.0"
        self.assertEqual(output, expected)

# 28
class TestShoppingSystem(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Mouse", 20)
        self.cart = ShoppingCart()

    def test_product_creation(self):
        self.assertEqual(self.product1.name, "Laptop")
        self.assertEqual(self.product1.price, 1000)

    def test_add_product(self):
        self.cart.add_product(self.product1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)
        
        # Test adding same product increases quantity
        self.cart.add_product(self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_remove_product(self):
        # Add products first
        self.cart.add_product(self.product1, 2)
        
        # Remove one
        self.cart.remove_product(self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)
        
        # Remove remaining
        self.cart.remove_product(self.product1)
        self.assertEqual(len(self.cart.items), 0)

    def test_checkout(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2, 2)
        
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.cart.checkout()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        
        self.assertIn("Total: $1040", output)
        self.assertIn("Checkout completed", output)