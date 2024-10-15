# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

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
        self.assertFalse(validate_login("a", "12345678"))
    
    def test_validate_login_big_username(self):
        """
        Checks the username is too big.
        """
        self.assertFalse(validate_login("123456789012345678901","12345678"))
    
    def test_validate_login_small_password(self):
        """
        Checks the password is too small.
        """
        self.assertFalse(validate_login("12345678", "a"))
    
    def test_validate_login_big_password(self):
        """
        Checks the password is too big.
        """
        self.assertFalse(validate_login("12345678", "123456789012345678901"))
    
    def test_validate_login_valid(self):
        """
        Checks the login is valid.
        """
        self.assertTrue(validate_login("12345678", "12345678"))
    
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
        self.assertFalse(validate_email("a@b"))
    
    def test_validate_email_invalid_at(self):
        """
        Checks the email has no @.
        """
        self.assertFalse(validate_email("abaacom"))
    
    def test_validate_email_invalid_dot(self):
        """
        Checks the email has no dot.
        """
        self.assertFalse(validate_email("a@bcom"))
    
    def test_validate_email_valid(self):
        """
        Checks the email is valid.
        """
        self.assertTrue(validate_email("abco@gcom.com"))
    
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
        self.assertEqual(validate_date(2020, 2, 30), "Invalid Date")
    
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
        self.assertEqual(check_loan_eligibility(100000, 500), "Secured Loan")
    
    # 18