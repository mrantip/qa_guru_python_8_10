import resource

from selene import browser, have, be


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').click().type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.phone_number)
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({user.month_of_birth})').click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({user.year_of_birth})').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{user.day_of_birth}').click()
        browser.element("#subjectsInput").type(user.subject).press_enter()
        if 'Sports' in user.hobby:
            browser.element('label[for=hobbies-checkbox-1]').click()
        if 'Reading' in user.hobby:
            browser.element('label[for=hobbies-checkbox-2]').click()
        if 'Music' in user.hobby:
            browser.element('label[for=hobbies-checkbox-3]').click()
        browser.element('#uploadPicture').type(resource.path(user.picture))
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').execute_script('element.click()')

    def should_be_registered_form(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f"{user.day_of_birth.replace('0', '')} "
            f"{user.month_of_birth.replace('2', 'February')},"
            f"{user.year_of_birth.replace('56', '1955')}",
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.state} {user.city}'
        ))
