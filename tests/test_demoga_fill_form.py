from data.users import User
from pages.registration_page import RegistrationPage


def test_demoga_fill_form(set_demoga):
    # GIVEN
    registration_page = RegistrationPage()
    student = User(first_name='Alesha', last_name='Bigd', email='mf666@gmail.com', gender='Male',
                   phone_number='0123456789',
                   month_of_birth='2', year_of_birth='56', day_of_birth='012', subject='Arts',
                   hobby='Sports, Reading', picture='ava.jpg', current_address='Heaven', state='Uttar Pradesh',
                   city='Agra')

    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.should_be_registered_form(student)
