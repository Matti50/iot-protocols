curl -i -X POST "http://localhost:8086/query" -d "q=create database matias_cicchitti"
curl -i -X POST "http://localhost:8086/write?db=matias_cicchitti" -d "climate,localidad=test,mota=99 temp=10"