from qa_form_test.pages.form_page import FormPage
import time


def test_submit_form(driver):
    form = FormPage(driver)
    form.load()
    form.fill_first_name("John")
    form.fill_last_name("Doe")
    form.select_gender("Male")
    form.fill_mobile_number("1234567890")
    form.select_date_of_birth(month="May", year="1995", day="15")
    form.select_subject("Maths")
    form.select_hobby("Music")
    form.upload_file("sample.png")
    form.select_state("NCR")
    form.select_city("Delhi")
    form.submit_form()

    # Validate confirmation modal
    time.sleep(2)
    assert "Thanks for submitting the form" in driver.page_source