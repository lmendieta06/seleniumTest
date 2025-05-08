from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time

# Función para hacer la escritura más lenta (simulando escritura humana)
def slow_type(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)  # Pausa entre cada carácter

# 1. Iniciar la sesión
print("Iniciando el navegador Chrome...")
driver = webdriver.Chrome()

# Maximizar la ventana para mejor visualización
driver.maximize_window()

try:
    # 2. Realizar acción en el navegador
    print("Navegando al formulario web de Selenium...")
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(1)  # Pausa después de cargar la página
    
    # 3. Solicitar información del navegador
    title = driver.title
    print(f"Título de la página: {title}")
    time.sleep(0.5)  # Pequeña pausa
    
    # 4. Establecer estrategia de espera
    print("Configurando espera implícita...")
    driver.implicitly_wait(0.5)
    
    # 5. Encontrar elementos
    print("Localizando elementos del formulario...")
    text_box = driver.find_element(by=By.NAME, value="my-text")
    password = driver.find_element(by=By.NAME, value="my-password")
    textarea = driver.find_element(by=By.NAME, value="my-textarea")
    dropdown = driver.find_element(by=By.NAME, value="my-select")
    checkbox = driver.find_element(by=By.NAME, value="my-check")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    time.sleep(1)  # Pausa después de identificar elementos
    
    # 6. Realizar acciones en los elementos (más lentamente)
    print("Interactuando con los elementos...")
    
    # Haciendo scroll para visualizar mejor los elementos
    driver.execute_script("arguments[0].scrollIntoView();", text_box)
    time.sleep(0.5)
    
    # Usar escritura lenta para el campo de texto
    print("Escribiendo en el campo de texto...")
    text_box.click()
    time.sleep(0.5)
    slow_type(text_box, "Ejemplo Selenium", 0.1)
    time.sleep(1)
    
    # Escribir la contraseña lentamente
    print("Escribiendo en el campo de contraseña...")
    password.click()
    time.sleep(0.5)
    slow_type(password, "password123", 0.1)
    time.sleep(1)
    
    # Escribir en el área de texto lentamente
    print("Escribiendo en el área de texto...")
    textarea.click()
    time.sleep(0.5)
    slow_type(textarea, "Este es un ejemplo práctico de automatización con Selenium", 0.05)
    time.sleep(1)
    
    # Seleccionar del dropdown
    print("Seleccionando una opción del menú desplegable...")
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(0.5)
    dropdown.click()
    time.sleep(1)
    dropdown_option = driver.find_element(by=By.CSS_SELECTOR, value="option[value='2']")
    dropdown_option.click()
    time.sleep(1)
    
    # Marcar la casilla
    print("Marcando la casilla de verificación...")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(0.5)
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(1)
    
    # Tomar una captura antes de enviar
    print("Tomando captura de pantalla del formulario completado...")
    driver.save_screenshot("formulario_completado.png")
    time.sleep(1)
    
    # Desplazarse hasta el botón de enviar
    print("Preparándose para enviar el formulario...")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(1)
    
    # Enviar el formulario
    print("Enviando el formulario...")
    submit_button.click()
    
    # Esperar a que se cargue la respuesta (tiempo más largo para visualización)
    print("Esperando la respuesta...")
    time.sleep(3)  
    
    # 7. Solicitar información del elemento
    print("Verificando el mensaje de confirmación...")
    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    print(f"Mensaje recibido: {text}")
    time.sleep(1)
    
    # Tomar captura del resultado
    driver.save_screenshot("formulario_enviado.png")
    print("Capturas guardadas como 'formulario_completado.png' y 'formulario_enviado.png'")
    time.sleep(1)
    
    # Verificar si el mensaje es el esperado
    if "Received" in text:
        print("¡Prueba exitosa! El formulario se envió correctamente.")
    else:
        print("La prueba falló. No se recibió el mensaje esperado.")
    
    # Pausa final para ver el resultado
    print("Manteniendo abierto el navegador para ver el resultado...")
    time.sleep(2)

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # 8. Finalizar la sesión
    print("Finalizando la sesión y cerrando el navegador...")
    driver.quit()
    print("Prueba completada.")