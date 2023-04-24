# import web driver
from selenium import webdriver
from Keys import password as pass1
import time

def scrape_all(url):
    # specifies the path to the chromedriver.exe
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('chromedriver',chrome_options=options)

    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.linkedin.com')
    time.sleep(1)

    # locate email form by_class_name
    username = driver.find_element_by_id('session_key')

    # send_keys() to simulate key strokes
    username.send_keys('gabriel.cuchacovich@gmail.com')

    # locate password form by_class_name
    password = driver.find_element_by_id('session_password')

    # send_keys() to simulate key strokes
    password.send_keys(pass1)

    # locate submit button by_class_name
    log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

    # .click() to mimic button click
    log_in_button.click()

    try:
        # locate Skip button by_class_name
        skip_button = driver.find_element_by_class_name('secondary-action-new')

        # .click() to mimic button click
        skip_button.click()
    except:
        print('No skip button')

    # Visit profile
    driver.get(url)
    time.sleep(1)

    # Contactos
    contactos = driver.find_elements_by_class_name('t-16.t-black.t-normal')[1].text

    # Ubicación
    ubicacion = driver.find_elements_by_class_name('t-16.t-black.t-normal')[0].text

    # Name
    nombre = driver.find_element_by_class_name('inline.t-24.t-black.t-normal.break-words').text

    # Foto Cara
    cara = driver.find_element_by_class_name('pv-top-card__photo.presence-entity__image').get_attribute("src")
    # sin foto: data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7

    # Foto Fondo
    fondo = ''
    try:
        fondo = driver.find_element_by_class_name('profile-background-image__image').get_attribute("src")
        print(fondo)
    except:
        fondo = ''

    # Cargo
    cargo = driver.find_element_by_class_name('mt1.t-18.t-black.t-normal.break-words').text

    # Último Empleo
    ultimo_empleo = driver.find_elements_by_class_name('text-align-left.ml2.t-14.t-black.t-bold')[0].text

    # Último Estudio
    ultimo_estudio = driver.find_elements_by_class_name('text-align-left.ml2.t-14.t-black.t-bold')[1].text

    # Extracto
    extracto_texto = ''
    try:
        driver.find_element_by_id('line-clamp-show-more-button').click()
        extracto = driver.find_elements_by_class_name('lt-line-clamp__raw-line')
        for i in range(len(extracto)):
            extracto_texto = extracto_texto + extracto[i].text
        print(extracto_texto)
    except:
        print('Sin ver mas')
        extracto = driver.find_elements_by_class_name('lt-line-clamp__line')
        if len(extracto)==0:
            print('Sin extracto')
    
    return [nombre, contactos, ubicacion, cara, fondo, cargo, ultimo_empleo, ultimo_estudio, extracto_texto]

if __name__ == "__main__":
    print(scrape_all())
