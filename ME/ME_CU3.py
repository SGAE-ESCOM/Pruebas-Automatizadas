import unittest
from selenium import webdriver
import time


#Clase para Editar de grupos.
class Editar:
	def __init__(self, driver):
		self.driver = driver

	#Caso de Indice Evaluación 
	def editar_grupo(self):
		button = self.driver.find_element_by_name('btnActualizar')
		button.click()
		#Editar ventana emergente 
		programa = ['','Machine Learning']
		inp = self.driver.find_elements_by_class_name('mat-input-element')
		for i in range(0,len(programa)):
			inp[i].clear()
			inp[i].send_keys(programa[i])
		time.sleep(4)
		self.driver.find_element_by_name('btnModalActualiza').click()
		time.sleep(4)

		def buscar(self):
			buscar = self.driver.find_element_by_id('txtBuscar')
			buscar.send_keys("Learning")
			time.sleep(3)
			buscar.clear()

		def elminar(self):
			self.driver.find_element_by_name('btnEliminar').click()
			time.sleep(2)
			self.driver.find_elements_by_name('btnConfiramar')
			time.sleep(2)
			self.driver.find_elements_by_class_name('swal2-confirm.mat-button.mat-button-base.mat-danger')[0].click()
			time.sleep(2)
			self.driver.find_elements_by_class_name('swal2-confirm.mat-button.mat-button-base.mat-info')[0].click()
			self.driver.refresh()
			time.sleep(2)

			

		buscar(self)
		elminar(self)
		self.driver.back()
		time.sleep(2)
		print("... Test Case 'Editar Grupo' Successful ...")
		print("==============================================")

