#Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classe (opicional)
class Teste_Produtos():

        # 2.1 - Atributos
        url = "https://www.saucedemo.com/"                                    #endereço do site alvo

        # 2.2 Funcoes e métodos
        def setup_method(self, method):                                  # metodo de inicialização dos testes
            self.driver = webdriver.Chrome()                        # instancia o objeto do selenium webdriver como chrome
            self.driver.implicitly_wait(10)                             # define o tempo de espera padrao por elementos em 10 segundos  

        def teardown_method(self, method):                      # metodo de finalização dos testes
                self.driver.quit()                            # emcerra / destroi o objeto do selenium webdriver da memoria, precisa do recuo (tab)

        def test_selecionar_produto(self):                 # metodo de teste
                self.driver.get(self.url)                             # abrir o site
                self.driver.find_element(By.ID, "user-name").send_keys("standard_user") #escreve no campo user-name
                self.driver.find_element(By.NAME, "password").send_keys("secret_sauce") #escreve a senha

                                              