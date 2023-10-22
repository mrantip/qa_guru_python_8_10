from pages.registration_page import RegistrationPage


def test_demoga_fill_form(set_demoga):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Alesha')
    registration_page.fill_last_name('Bigd')
    registration_page.fill_email('mf666@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.fill_phone_number('0123456789')
    registration_page.choose_birtday(month='2', year='56', day='012')
    registration_page.choose_subject('Arts')
    registration_page.choose_hobby_1()
    registration_page.choose_hobby_2()
    registration_page.uppload_picture('ava.jpg')
    registration_page.fill_current_address('Heaven')
    registration_page.choose_state('Uttar Pradesh')
    registration_page.choose_city('Agra')
    registration_page.submit_form()

    # THEN
    registration_page.should_be_registered_form(
        'Alesha Bigd',
        'mf666@gmail.com',
        'Male',
        '0123456789',
        '12 February,1955',
        'Arts',
        'Sports, Reading',
        'ava.jpg',
        'Heaven',
        'Uttar Pradesh Agra'
    )
