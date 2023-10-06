# Temporary readme

# Getting started on the backend project

The project is dockerized and all the necessary configurations for databases are set.

## Running the backend api

USE `docker-compose up --build` to build and run the container
USE `docker-compose up --build -d` to run the program in detach mode
for more info about docker use this video to get upto speed with it

- [Docker video](https://www.youtube.com/watch?v=0H2miBK_gAk&t=1580s)


`sudo docker exec -it ems254-mysql-1 mysql -u test_user -p` ---- accessing the mysql container

curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_JWT_TOKEN" -d '{
  "account_number": "RECEIVER_ACCOUNT_NUMBER",
  "amount": AMOUNT
}' http://localhost:5000/api/v1/views/transactions/transact


`curl -H "Authorization: Bearer YOUR_JWT_TOKEN" http://localhost:5000/api/v1/views/transactions/transactions`


`curl -H "Authorization: Bearer YOUR_JWT_TOKEN" http://localhost:5000/api/v1/views/transactions/transaction/TRANSACTION_ID`


`curl -X PATCH -H "Authorization: Bearer YOUR_JWT_TOKEN" http://localhost:5000/api/v1/views/transactions/approve/TRANSACTION_ID`

`curl -X PATCH -H "Authorization: Bearer YOUR_JWT_TOKEN" http://localhost:5000/api/v1/views/transactions/cancel/TRANSACTION_ID`


`curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "secretpassword", "first_name": "john", "last_name": "Doe", "phone_number": "12345678", "location": "london"}' "http://127.0.0.1:5000/api/v1/views/register"`

 `curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "secretpassword" }' "http://127.0.0.1:5000/api/v1/users/login"`

 `curl -X POST -H "Content-Type: application/json"   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU0MTk4MCwianRpIjoiMTdkNGNmMzItOTFjZS00NzE1LTg1MTgtNDA4ZTMxOWYxYWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQwZjk4YjQyLTU1ZDQtNDVkZS04ZjA3LWI2ODU2ZWU4MjlhMiIsIm5iZiI6MTY5NjU0MTk4MCwiZXhwIjoxNjk2NTQzNzgwfQ.KWesgBQcqXg_bJAQ1Co1soinhVjpr2AoxHxc-TUu15A"   -d '{"amount": 500}'   "http://127.0.0.1:5000/api/v1/transactions/deposit"`


mson@pc:~/ems253/EMS254$ curl -X POST http://localhost:5000/api/v1/transactions/transact   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU0NTE1NywianRpIjoiZmZmMjY0MjktNDE0MS00MjU1LWIwMjMtMWNmZmJmZmU3MDg2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQwZjk4YjQyLTU1ZDQtNDVkZS04ZjA3LWI2ODU2ZWU4MjlhMiIsIm5iZiI6MTY5NjU0NTE1NywiZXhwIjoxNjk2NTQ2OTU3fQ.2IUmI2O5GvLi-8O9BQj_2_HpLnGlmhj_5AYaQJKEnOI"   -H "Content-Type: application/json"   -d '{
    "account_number": "6201001120",
    "amount": 200
  }'
{
  "message": "transaction created successfully"
}

 curl -X GET http://localhost:5000/api/v1/users/profile -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU0MTk4MCwianRpIjoiMTdkNGNmMzItOTFjZS00NzE1LTg1MTgtNDA4ZTMxOWYxYWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQwZjk4YjQyLTU1ZDQtNDVkZS04ZjA3LWI2ODU2ZWU4MjlhMiIsIm5iZiI6MTY5NjU0MTk4MCwiZXhwIjoxNjk2NTQzNzgwfQ.KWesgBQcqXg_bJAQ1Co1soinhVjpr2AoxHxc-TUu15A"

 curl -X POST -H "Content-Type: application/json"   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU0NDA3OCwianRpIjoiYzEyZDcyMzYtOTUyMy00MDJjLWFjYWYtOTI4MDFiOTNkNzllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQwZjk4YjQyLTU1ZDQtNDVkZS04ZjA3LWI2ODU2ZWU4MjlhMiIsIm5iZiI6MTY5NjU0NDA3OCwiZXhwIjoxNjk2NTQ1ODc4fQ.fXmUDoIFrhEj32LUOZsz9J48TgLVLq48HDHAku_PhTY"   -d '{"amount": 500}'   "http://127.0.0.1:5000/api/v1/transactions/withdraw"


curl -X GET http://localhost:5000/api/v1/transactions/user_transactions   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU4MDk1NywianRpIjoiMzBmNDAyYWYtODFkMi00NmQ5LTk1NjYtMjA4OGJiOTExODhlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQwZjk4YjQyLTU1ZDQtNDVkZS04ZjA3LWI2ODU2ZWU4MjlhMiIsIm5iZiI6MTY5NjU4MDk1NywiZXhwIjoxNjk2NTgyNzU3fQ.cutdgTIKIRHhssyTMU0hsaZfpcSXH7ZlCvNnrPqfEoE"

curl -X GET http://localhost:5000/api/v1/transactions/transaction/5a785e59-dac6-437d-affe-25e2062ba119 -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU4MDk1NywianRpIjoiMzBmNDAyYWYtODFkMi00NmQ5LTk1NjYtMjA4OGJiOTExODhlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQwZjk4YjQyLTU1ZDQtNDVkZS04ZjA3LWI2ODU2ZWU4MjlhMiIsIm5iZiI6MTY5NjU4MDk1NywiZXhwIjoxNjk2NTgyNzU3fQ.cutdgTIKIRHhssyTMU0hsaZfpcSXH7ZlCvNnrPqfEoE"
