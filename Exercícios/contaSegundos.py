segundosCliente = int(input("Por favor, entre com o número de segundos que deseja converter: "))

segundosDados = segundosCliente/86400

dias = segundosCliente//86400

segundosDados = segundosCliente%86400

horas = segundosDados//3600

segundosDados = segundosDados%3600

minutos = segundosDados//60

segundos = segundosDados%60


print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")