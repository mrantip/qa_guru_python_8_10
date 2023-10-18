from selene import browser, have, be


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self):
        browser.element('#firstName').type('Alesha')

    def fill_last_name(self):
        browser.element('#lastName').type('Bigd')

    def fill_email(self):
        browser.element('#userEmail').click().type('mf666@gmail.com')

    def choose_gender(self):
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    def fill_phone_number(self):
        browser.element('#userNumber').type('0123456789')

    def choose_birtday(self):
        # browser.element('#dateOfBirthInput').click()
        # browser.element('.react-datepicker__month-select').click().element('option[value="1"]').click()
        # browser.element('.react-datepicker__year-select').click().element('option[value="1955"]').click()
        # browser.element('.react-datepicker__day--012').click()

        browser.element('#dateOfBirthInput').click()
        # browser.element('.react-datepicker__month-select').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({month})').should(be.visible).click()
        # browser.element('.react-datepicker__year-select').should(be.visible).click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({year})').should(be.visible).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{day}').should(be.visible).click()

    def choose_subject(self):
        browser.element("#subjectsInput").type("Arts").press_enter()

    def choose_hobby_1(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def choose_hobby_2(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def choose_hobby_3(self):
        browser.element('[for="hobbies-checkbox-3"]').click()

    def uppload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resourses/ava.jpg'))

    def fill_current_address(self):
        browser.element('#currentAddress').type('Heaven')

    def choose_state(self):
        browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
