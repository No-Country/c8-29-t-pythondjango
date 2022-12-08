import time
from automation import Automation


ciudades = ["Azcapotzalco, CDMX","Buenos aires", "San Miguel de Tucumán", "Salta", "Santa Fe", "Corrientes", "Mar de Plata",]


for ciudad in ciudades:
    automation = Automation()
    automation.search_job("java", f"{ciudad}")
    automation.extract_data("java", f"{ciudad}")
    automation = Automation()
    automation.search_job("python", f"{ciudad}")
    automation.extract_data("python", f"{ciudad}")
    automation = Automation()
    automation.search_job("javascript", f"{ciudad}")
    automation.extract_data("javascript", f"{ciudad}")
    automation = Automation()
    automation.search_job("ux", f" {ciudad}")
    automation.extract_data("ux", f"{ciudad}")




automation.extract_data()

