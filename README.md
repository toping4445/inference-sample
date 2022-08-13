## 1. 서버에서 Git pull
```shell
git clone https://github.com/toping4445/inference-sample.git
```
## 2.도커 빌드 
```shell
docker-compuse build ml-inference
```
## 3.컨테이너 실행
```shell
docker-compose up -d
```
## 4.API test
### ping
```shell
curl -X GET http://localhost:5004/ping
```
### predict
```shell
curl -X POST -H "Content-Type:application/json" --data '{data}' localhost:5002/predict
```
