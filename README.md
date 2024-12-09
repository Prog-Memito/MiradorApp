<!-- 
POST
http://127.0.0.1:5000/gastos/generar

{ "mes": 10, "año": 2024, "monto_base": 50000 }

POST
http://127.0.0.1:5000/gastos/pagar

{ "departamento": "100", "periodo": "2024-10", "fecha_pago": "2024-11-03" }

GET
http://127.0.0.1:5000/gastos/pendientes?mes=10&año=2024

RECUERDA QUE EN LOS PENDINTES CAMBIAR EL MES Y EL AÑO  -->