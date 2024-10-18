# GOOGLE CHROME BROWSER ------------------------------------------------------------------------------------------------

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Initialize the Chrome Webdriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.maximize_window()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# NEGATIVE TEST ON LOGIN PAGE ON GOOGLE CHROME BROWSER ------------------------------------------------------------------------------------------

EMAIL_ADDRESS = driver.find_element(By.CSS_SELECTOR,
                                    '#email')
EMAIL_ADDRESS.send_keys("martha12345")
time.sleep(2)

PASSWORD = driver.find_element(By.CSS_SELECTOR,
                               '#password')
PASSWORD.send_keys("asdfghjkl123")
time.sleep(2)

SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#submit')
SUBMIT_BUTTON.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# DELETE INVALID CREDENTIALS ON LOGIN PAGE------------------------------------------------------------------

EMAIL_ADDRESS = driver.find_element(By.CSS_SELECTOR,
                                    '#email')
EMAIL_ADDRESS.clear()
time.sleep(2)

PASSWORD = driver.find_element(By.CSS_SELECTOR,
                               '#password')
PASSWORD.clear()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# ADD CONTACT --- 1 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------

NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                         '#add-contact')
NEW_CONTACT_BUTTON.click()
time.sleep(2)

FIRST_NAME_1 = driver.find_element(By.CSS_SELECTOR,
                                   '#firstName')
FIRST_NAME_1.send_keys("hello")
time.sleep(2)

# LAST_NAME_1 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_1.send_keys("1")
# time.sleep(2)
#
# DATE_OF_BIRTH_1 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_1.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_1 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_1.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_1 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_1.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_1 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_1.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_1 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_1.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_1 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_1.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_1 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_1.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_1 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_1.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_1 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_1.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 2 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_2 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_2.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_2 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_2.send_keys("2")
# time.sleep(2)
#
# DATE_OF_BIRTH_2 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_2.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_2 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_2.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_2 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_2.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_2 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_2.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_2 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_2.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_2 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_2.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_2 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_2.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_2 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_2.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_2 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_2.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 3 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_3 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_3.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_3 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_3.send_keys("3")
# time.sleep(2)
#
# DATE_OF_BIRTH_3 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_3.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_3 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_3.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_3 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_3.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_3 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_3.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_3 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_3.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_3 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_3.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_3 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_3.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_3 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_3.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_3 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_3.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 4 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_4 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_4.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_4 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_4.send_keys("4")
# time.sleep(2)
#
# DATE_OF_BIRTH_4 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_4.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_4 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_4.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_4 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_4.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_4 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_4.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_4 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_4.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_4 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_4.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_4 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_4.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_4 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_4.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_4 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_4.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 5 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_5 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_5.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_5 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_5.send_keys("5")
# time.sleep(2)
#
# DATE_OF_BIRTH_5 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_5.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_5 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_5.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_5 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_5.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_5 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_5.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_5 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_5.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_5 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_5.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_5 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_5.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_5 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_5.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_5 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_5.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 6 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_6 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_6.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_6 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_6.send_keys("6")
# time.sleep(2)
#
# DATE_OF_BIRTH_6 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_6.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_6 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_6.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_6 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_6.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_6 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_6.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_6 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_6.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_6 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_6.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_6 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_6.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_6 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_6.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_6 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_6.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 7 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_7 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_7.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_7 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_7.send_keys("7")
# time.sleep(2)
#
# DATE_OF_BIRTH_7 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_7.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_7 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_7.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_7 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_7.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_7 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_7.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_7 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_7.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_7 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_7.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_7 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_7.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_7 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_7.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_7 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_7.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 8 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_8 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_8.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_8 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_8.send_keys("8")
# time.sleep(2)
#
# DATE_OF_BIRTH_8 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_8.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_8 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_8.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_8 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_8.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_8 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_8.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_8 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_8.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_8 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_8.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_8 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_8.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_8 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_8.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_8 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_8.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 9 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_9 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_9.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_9 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_9.send_keys("9")
# time.sleep(2)
#
# DATE_OF_BIRTH_9 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_9.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_9 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_9.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_9 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_9.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_9 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_9.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_9 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_9.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_9 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_9.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_9 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_9.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_9 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_9.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_9 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_9.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 10 ON GOOGLE CHROME BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_10 = driver.find_element(By.CSS_SELECTOR,
#                                     '#firstName')
# FIRST_NAME_10.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_10 = driver.find_element(By.CSS_SELECTOR,
#                                    '#lastName')
# LAST_NAME_10.send_keys("10")
# time.sleep(2)
#
# DATE_OF_BIRTH_10 = driver.find_element(By.CSS_SELECTOR,
#                                        '#birthdate')
# DATE_OF_BIRTH_10.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_10 = driver.find_element(By.CSS_SELECTOR,
#                                        '#email')
# EMAIL_ADDRESS_10.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_10 = driver.find_element(By.CSS_SELECTOR,
#                                       '#phone')
# PHONE_NUMBER_10.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_10 = driver.find_element(By.CSS_SELECTOR,
#                                           '#street1')
# STREET_ADDRESS_1_10.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_10 = driver.find_element(By.CSS_SELECTOR,
#                                           '#street2')
# STREET_ADDRESS_2_10.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_10 = driver.find_element(By.CSS_SELECTOR,
#                               '#city')
# CITY_10.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_10 = driver.find_element(By.CSS_SELECTOR,
#                                         '#stateProvince')
# STATE_PROVINCE_10.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_10 = driver.find_element(By.CSS_SELECTOR,
#                                      '#postalCode')
# POSTAL_CODE_10.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_10 = driver.find_element(By.CSS_SELECTOR,
#                                  '#country')
# COUNTRY_10.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)

# LOG-OUT BUTTON ON GOOGLE CHROME BROWSER ---------------------------------------------------------------------------------------
LOGOUT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#logout')
LOGOUT_BUTTON.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# CLOSE THE BROWSER ON GOOGLE CHROME BROWSER -----------------------------------------------------------------------------------
driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# MICROSOFT EDGE BROWSER -----------------------------------------------------------------------------------------------

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# INITIALIZE THE MICROSOFT EDGE WEBDRIVER USING WEBDRIVER MANAGER ------------------------------------------------------
driver = webdriver.Edge()

# OPEN THE WEBSITE -----------------------------------------------------------------------------------------------------
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------
# NEGATIVE TEST ON LOGIN PAGE ON MICROSOFT EDGE BROWSER ------------------------------------------------------------------------------------------
EMAIL_ADDRESS = driver.find_element(By.CSS_SELECTOR,
                                    '#email')
EMAIL_ADDRESS.send_keys("martha12345")
time.sleep(2)

PASSWORD = driver.find_element(By.CSS_SELECTOR,
                               '#password')
PASSWORD.send_keys("asdfghjkl123")
time.sleep(2)

SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#submit')
SUBMIT_BUTTON.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# DELETE INVALID CREDENTIALS ON LOGIN PAGE------------------------------------------------------------------

EMAIL_ADDRESS = driver.find_element(By.CSS_SELECTOR,
                                    '#email')
EMAIL_ADDRESS.clear()
time.sleep(2)

PASSWORD = driver.find_element(By.CSS_SELECTOR,
                               '#password')
PASSWORD.clear()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# ADD CONTACT --- 1 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------

NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                         '#add-contact')
NEW_CONTACT_BUTTON.click()
time.sleep(2)

FIRST_NAME_1 = driver.find_element(By.CSS_SELECTOR,
                                   '#firstName')
FIRST_NAME_1.send_keys("hello")
time.sleep(2)

LAST_NAME_1 = driver.find_element(By.CSS_SELECTOR,
                                  '#lastName')
LAST_NAME_1.send_keys("1")
time.sleep(2)

DATE_OF_BIRTH_1 = driver.find_element(By.CSS_SELECTOR,
                                      '#birthdate')
DATE_OF_BIRTH_1.send_keys("2024-10-11")
time.sleep(2)

EMAIL_ADDRESS_1 = driver.find_element(By.CSS_SELECTOR,
                                      '#email')
EMAIL_ADDRESS_1.send_keys("test123@gmail.com")
time.sleep(2)

PHONE_NUMBER_1 = driver.find_element(By.CSS_SELECTOR,
                                     '#phone')
PHONE_NUMBER_1.send_keys("1234567890")
time.sleep(2)

STREET_ADDRESS_1_1 = driver.find_element(By.CSS_SELECTOR,
                                         '#street1')
STREET_ADDRESS_1_1.send_keys("1, Mainland street")
time.sleep(2)

STREET_ADDRESS_2_1 = driver.find_element(By.CSS_SELECTOR,
                                         '#street2')
STREET_ADDRESS_2_1.send_keys("2, Mainland street")
time.sleep(2)

CITY_1 = driver.find_element(By.CSS_SELECTOR,
                             '#city')
CITY_1.send_keys("Mainland")
time.sleep(2)

STATE_PROVINCE_1 = driver.find_element(By.CSS_SELECTOR,
                                       '#stateProvince')
STATE_PROVINCE_1.send_keys("Lagos")
time.sleep(2)

POSTAL_CODE_1 = driver.find_element(By.CSS_SELECTOR,
                                    '#postalCode')
POSTAL_CODE_1.send_keys("12345")
time.sleep(2)

COUNTRY_1 = driver.find_element(By.CSS_SELECTOR,
                                '#country')
COUNTRY_1.send_keys("Nigeria")
time.sleep(2)

SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#submit')
SUBMIT_BUTTON.click()
time.sleep(2)

# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 2 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_2 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_2.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_2 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_2.send_keys("2")
# time.sleep(2)
#
# DATE_OF_BIRTH_2 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_2.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_2 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_2.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_2 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_2.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_2 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_2.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_2 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_2.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_2 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_2.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_2 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_2.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_2 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_2.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_2 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_2.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 3 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_3 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_3.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_3 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_3.send_keys("3")
# time.sleep(2)
#
# DATE_OF_BIRTH_3 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_3.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_3 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_3.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_3 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_3.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_3 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_3.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_3 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_3.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_3 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_3.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_3 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_3.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_3 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_3.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_3 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_3.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 4 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_4 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_4.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_4 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_4.send_keys("4")
# time.sleep(2)
#
# DATE_OF_BIRTH_4 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_4.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_4 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_4.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_4 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_4.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_4 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_4.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_4 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_4.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_4 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_4.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_4 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_4.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_4 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_4.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_4 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_4.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 5 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_5 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_5.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_5 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_5.send_keys("5")
# time.sleep(2)
#
# DATE_OF_BIRTH_5 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_5.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_5 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_5.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_5 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_5.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_5 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_5.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_5 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_5.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_5 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_5.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_5 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_5.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_5 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_5.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_5 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_5.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 6 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_6 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_6.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_6 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_6.send_keys("6")
# time.sleep(2)
#
# DATE_OF_BIRTH_6 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_6.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_6 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_6.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_6 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_6.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_6 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_6.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_6 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_6.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_6 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_6.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_6 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_6.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_6 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_6.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_6 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_6.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 7 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_7 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_7.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_7 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_7.send_keys("7")
# time.sleep(2)
#
# DATE_OF_BIRTH_7 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_7.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_7 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_7.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_7 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_7.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_7 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_7.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_7 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_7.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_7 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_7.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_7 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_7.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_7 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_7.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_7 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_7.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 8 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_8 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_8.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_8 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_8.send_keys("8")
# time.sleep(2)
#
# DATE_OF_BIRTH_8 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_8.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_8 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_8.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_8 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_8.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_8 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_8.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_8 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_8.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_8 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_8.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_8 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_8.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_8 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_8.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_8 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_8.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 9 --- ON MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_9 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_9.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_9 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_9.send_keys("9")
# time.sleep(2)
#
# DATE_OF_BIRTH_9 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_9.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_9 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_9.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_9 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_9.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_9 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_9.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_9 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_9.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_9 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_9.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_9 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_9.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_9 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_9.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_9 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_9.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 10 --- ON MICROSOFT EDGE BROWSER----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_10 = driver.find_element(By.CSS_SELECTOR,
#                                     '#firstName')
# FIRST_NAME_10.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_10 = driver.find_element(By.CSS_SELECTOR,
#                                    '#lastName')
# LAST_NAME_10.send_keys("10")
# time.sleep(2)
#
# DATE_OF_BIRTH_10 = driver.find_element(By.CSS_SELECTOR,
#                                        '#birthdate')
# DATE_OF_BIRTH_10.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_10 = driver.find_element(By.CSS_SELECTOR,
#                                        '#email')
# EMAIL_ADDRESS_10.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_10 = driver.find_element(By.CSS_SELECTOR,
#                                       '#phone')
# PHONE_NUMBER_10.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_10 = driver.find_element(By.CSS_SELECTOR,
#                                           '#street1')
# STREET_ADDRESS_1_10.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_10 = driver.find_element(By.CSS_SELECTOR,
#                                           '#street2')
# STREET_ADDRESS_2_10.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_10 = driver.find_element(By.CSS_SELECTOR,
#                               '#city')
# CITY_10.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_10 = driver.find_element(By.CSS_SELECTOR,
#                                         '#stateProvince')
# STATE_PROVINCE_10.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_10 = driver.find_element(By.CSS_SELECTOR,
#                                      '#postalCode')
# POSTAL_CODE_10.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_10 = driver.find_element(By.CSS_SELECTOR,
#                                  '#country')
# COUNTRY_10.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)

# LOG-OUT BUTTON ON MICROSOFT EDGE BROWSER ---------------------------------------------------------------------------------------
LOGOUT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#logout')
LOGOUT_BUTTON.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# CLOSE THE MICROSOFT EDGE BROWSER ----------------------------------------------------------------------------------
driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# INITIALIZE
# Initialize the Chrome Webdriver using WebDriver manager
driver = webdriver.Firefox()

# Open a website
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------
# NEGATIVE TEST ON LOGIN PAGE ON MOZILLA FIREFOX ------------------------------------------------------------------------------------------
EMAIL_ADDRESS = driver.find_element(By.CSS_SELECTOR,
                                    '#email')
EMAIL_ADDRESS.send_keys("martha12345")
time.sleep(2)

PASSWORD = driver.find_element(By.CSS_SELECTOR,
                               '#password')
PASSWORD.send_keys("asdfghjkl123")
time.sleep(2)

SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#submit')
SUBMIT_BUTTON.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# DELETE INVALID CREDENTIALS ON LOGIN PAGE ------------------------------------------------------------------

EMAIL_ADDRESS = driver.find_element(By.CSS_SELECTOR,
                                    '#email')
EMAIL_ADDRESS.clear()
time.sleep(2)

PASSWORD = driver.find_element(By.CSS_SELECTOR,
                               '#password')
PASSWORD.clear()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# ADD CONTACT --- 1 --- ON MOZILLA FIREFOX BROWSER----------------------------------------------------------------------------------------------

NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                         '#add-contact')
NEW_CONTACT_BUTTON.click()
time.sleep(2)

FIRST_NAME_1 = driver.find_element(By.CSS_SELECTOR,
                                   '#firstName')
FIRST_NAME_1.send_keys("hello")
time.sleep(2)

LAST_NAME_1 = driver.find_element(By.CSS_SELECTOR,
                                  '#lastName')
LAST_NAME_1.send_keys("1")
time.sleep(2)

DATE_OF_BIRTH_1 = driver.find_element(By.CSS_SELECTOR,
                                      '#birthdate')
DATE_OF_BIRTH_1.send_keys("2024-10-11")
time.sleep(2)

EMAIL_ADDRESS_1 = driver.find_element(By.CSS_SELECTOR,
                                      '#email')
EMAIL_ADDRESS_1.send_keys("test123@gmail.com")
time.sleep(2)

PHONE_NUMBER_1 = driver.find_element(By.CSS_SELECTOR,
                                     '#phone')
PHONE_NUMBER_1.send_keys("1234567890")
time.sleep(2)

STREET_ADDRESS_1_1 = driver.find_element(By.CSS_SELECTOR,
                                         '#street1')
STREET_ADDRESS_1_1.send_keys("1, Mainland street")
time.sleep(2)

STREET_ADDRESS_2_1 = driver.find_element(By.CSS_SELECTOR,
                                         '#street2')
STREET_ADDRESS_2_1.send_keys("2, Mainland street")
time.sleep(2)

CITY_1 = driver.find_element(By.CSS_SELECTOR,
                             '#city')
CITY_1.send_keys("Mainland")
time.sleep(2)

STATE_PROVINCE_1 = driver.find_element(By.CSS_SELECTOR,
                                       '#stateProvince')
STATE_PROVINCE_1.send_keys("Lagos")
time.sleep(2)

POSTAL_CODE_1 = driver.find_element(By.CSS_SELECTOR,
                                    '#postalCode')
POSTAL_CODE_1.send_keys("12345")
time.sleep(2)

COUNTRY_1 = driver.find_element(By.CSS_SELECTOR,
                                '#country')
COUNTRY_1.send_keys("Nigeria")
time.sleep(2)

SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#submit')
SUBMIT_BUTTON.click()
time.sleep(2)

# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 2 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_2 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_2.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_2 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_2.send_keys("2")
# time.sleep(2)
#
# DATE_OF_BIRTH_2 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_2.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_2 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_2.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_2 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_2.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_2 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_2.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_2 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_2.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_2 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_2.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_2 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_2.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_2 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_2.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_2 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_2.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 3 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_3 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_3.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_3 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_3.send_keys("3")
# time.sleep(2)
#
# DATE_OF_BIRTH_3 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_3.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_3 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_3.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_3 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_3.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_3 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_3.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_3 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_3.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_3 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_3.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_3 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_3.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_3 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_3.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_3 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_3.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 4 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_4 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_4.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_4 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_4.send_keys("4")
# time.sleep(2)
#
# DATE_OF_BIRTH_4 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_4.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_4 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_4.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_4 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_4.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_4 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_4.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_4 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_4.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_4 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_4.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_4 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_4.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_4 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_4.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_4 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_4.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 5 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_5 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_5.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_5 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_5.send_keys("5")
# time.sleep(2)
#
# DATE_OF_BIRTH_5 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_5.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_5 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_5.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_5 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_5.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_5 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_5.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_5 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_5.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_5 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_5.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_5 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_5.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_5 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_5.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_5 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_5.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 6 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_6 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_6.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_6 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_6.send_keys("6")
# time.sleep(2)
#
# DATE_OF_BIRTH_6 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_6.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_6 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_6.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_6 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_6.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_6 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_6.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_6 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_6.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_6 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_6.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_6 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_6.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_6 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_6.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_6 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_6.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 7 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_7 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_7.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_7 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_7.send_keys("7")
# time.sleep(2)
#
# DATE_OF_BIRTH_7 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_7.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_7 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_7.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_7 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_7.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_7 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_7.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_7 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_7.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_7 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_7.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_7 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_7.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_7 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_7.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_7 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_7.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 8 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_8 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_8.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_8 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_8.send_keys("8")
# time.sleep(2)
#
# DATE_OF_BIRTH_8 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_8.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_8 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_8.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_8 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_8.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_8 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_8.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_8 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_8.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_8 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_8.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_8 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_8.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_8 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_8.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_8 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_8.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 9 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_9 = driver.find_element(By.CSS_SELECTOR,
#                                    '#firstName')
# FIRST_NAME_9.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_9 = driver.find_element(By.CSS_SELECTOR,
#                                   '#lastName')
# LAST_NAME_9.send_keys("9")
# time.sleep(2)
#
# DATE_OF_BIRTH_9 = driver.find_element(By.CSS_SELECTOR,
#                                       '#birthdate')
# DATE_OF_BIRTH_9.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_9 = driver.find_element(By.CSS_SELECTOR,
#                                       '#email')
# EMAIL_ADDRESS_9.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_9 = driver.find_element(By.CSS_SELECTOR,
#                                      '#phone')
# PHONE_NUMBER_9.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_9 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street1')
# STREET_ADDRESS_1_9.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_9 = driver.find_element(By.CSS_SELECTOR,
#                                          '#street2')
# STREET_ADDRESS_2_9.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_9 = driver.find_element(By.CSS_SELECTOR,
#                              '#city')
# CITY_9.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_9 = driver.find_element(By.CSS_SELECTOR,
#                                        '#stateProvince')
# STATE_PROVINCE_9.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_9 = driver.find_element(By.CSS_SELECTOR,
#                                     '#postalCode')
# POSTAL_CODE_9.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_9 = driver.find_element(By.CSS_SELECTOR,
#                                 '#country')
# COUNTRY_9.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)
#
# # ----------------------------------------------------------------------------------------------------------------------
# # ADD CONTACT --- 10 --- ON MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
#
# NEW_CONTACT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                          '#add-contact')
# NEW_CONTACT_BUTTON.click()
# time.sleep(2)
#
# FIRST_NAME_10 = driver.find_element(By.CSS_SELECTOR,
#                                     '#firstName')
# FIRST_NAME_10.send_keys("hello")
# time.sleep(2)
#
# LAST_NAME_10 = driver.find_element(By.CSS_SELECTOR,
#                                    '#lastName')
# LAST_NAME_10.send_keys("10")
# time.sleep(2)
#
# DATE_OF_BIRTH_10 = driver.find_element(By.CSS_SELECTOR,
#                                        '#birthdate')
# DATE_OF_BIRTH_10.send_keys("2024-10-11")
# time.sleep(2)
#
# EMAIL_ADDRESS_10 = driver.find_element(By.CSS_SELECTOR,
#                                        '#email')
# EMAIL_ADDRESS_10.send_keys("test123@gmail.com")
# time.sleep(2)
#
# PHONE_NUMBER_10 = driver.find_element(By.CSS_SELECTOR,
#                                       '#phone')
# PHONE_NUMBER_10.send_keys("1234567890")
# time.sleep(2)
#
# STREET_ADDRESS_1_10 = driver.find_element(By.CSS_SELECTOR,
#                                           '#street1')
# STREET_ADDRESS_1_10.send_keys("1, Mainland street")
# time.sleep(2)
#
# STREET_ADDRESS_2_10 = driver.find_element(By.CSS_SELECTOR,
#                                           '#street2')
# STREET_ADDRESS_2_10.send_keys("2, Mainland street")
# time.sleep(2)
#
# CITY_10 = driver.find_element(By.CSS_SELECTOR,
#                               '#city')
# CITY_10.send_keys("Mainland")
# time.sleep(2)
#
# STATE_PROVINCE_10 = driver.find_element(By.CSS_SELECTOR,
#                                         '#stateProvince')
# STATE_PROVINCE_10.send_keys("Lagos")
# time.sleep(2)
#
# POSTAL_CODE_10 = driver.find_element(By.CSS_SELECTOR,
#                                      '#postalCode')
# POSTAL_CODE_10.send_keys("12345")
# time.sleep(2)
#
# COUNTRY_10 = driver.find_element(By.CSS_SELECTOR,
#                                  '#country')
# COUNTRY_10.send_keys("Nigeria")
# time.sleep(2)
#
# SUBMIT_BUTTON = driver.find_element(By.CSS_SELECTOR,
#                                     '#submit')
# SUBMIT_BUTTON.click()
# time.sleep(2)

# LOG-OUT BUTTON OF THE APPLICATION ON MOZILLA FIREFOX BROWSER---------------------------------------------------------------------------------------
LOGOUT_BUTTON = driver.find_element(By.CSS_SELECTOR,
                                    '#logout')
LOGOUT_BUTTON.click()
time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------
# CLOSE MOZILLA FIREFOX BROWSER----------------------------------------------------------------------------------
driver.quit()
