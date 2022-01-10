from django.test import TestCase
from .models import Embarque
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create your tests here.

class UnitTestCase(TestCase):

    def setUp(self):
        User=get_user_model()
        self.user = User.objects.create_superuser(
            username="adminTest",
            password="1234",
            email="admintest@example.com")
        self.credentials={"username":"adminTest","password":"1234"}

    def test_login(self):
        response = self.client.post(reverse("login"),self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class FunctionalTestCase(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True #activa el navegador de manera invisible
        options.add_argument("--window-size=1920, 1080")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_home(self):
        self.driver.get('http://localhost:8000')
        self.assertEqual(self.driver.title, "Gestor Embarques App")
        assert 'Bienvenido al Sistema de Embarques'



class TestLoginUsuario(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = False #activa el navegador de manera invisible
        options.add_argument("--window-size=1920, 1080")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()
     
    def test_loginUsuario(self):
        self.driver.get("http://127.0.0.1:8000/login/?next=/")
        self.driver.set_window_size(1476, 1040)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("paanc")
        self.driver.find_element(By.ID, "id_password").send_keys("testing321")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.get("http://127.0.0.1:8000/logout")
  

#No esta funcionando, se cae en la linea 127. Hay que rehacerlo

class TestLoginUsuarioaPerfil(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = False #activa el navegador de manera invisible
        options.add_argument("--window-size=1920, 1080")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()
  
    def test_loginhomeahistorial(self):
        self.driver.get("http://127.0.0.1:8000/login/")
        self.driver.set_window_size(1920, 1040)
        self.driver.find_element(By.ID, "id_username").send_keys("paanc")
        self.driver.find_element(By.ID, "id_password").send_keys("testing321")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, "img").click()
        self.driver.get("http://127.0.0.1:8000/logout")

class TestLoginPerfilLogout(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = False #activa el navegador de manera invisible
        options.add_argument("--window-size=1920, 1080")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_loginperfilhomelogout(self):
        self.driver.get("http://127.0.0.1:8000/login/?next=/")
        self.driver.set_window_size(1920, 1040)
        self.driver.find_element(By.ID, "id_username").send_keys("paanc")
        self.driver.find_element(By.ID, "id_password").send_keys("testing321")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.ID, "user").click()
        self.driver.find_element(By.CSS_SELECTOR, "a > img").click()

    


