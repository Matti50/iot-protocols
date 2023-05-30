curl -i -X POST "http://localhost:8086/write?db=matias_cicchitti" -d "clima,localidad=La_Plata,mota=1 temp=10"
curl -i -X POST "http://localhost:8086/write?db=matias_cicchitti" -d "clima,localidad=La_Plata,mota=1 temp=11"
curl -i -X POST "http://localhost:8086/write?db=matias_cicchitti" -d "clima,localidad=Berazategui,mota=2 temp=13"
curl -i -X POST "http://localhost:8086/write?db=matias_cicchitti" -d "clima,localidad=Quilmes,mota=4 temp=12"