## Horizontally scaleable Socket IO server with Flask and RabbitMQ

### Implemented
* Flask server with Socket IO

* Docker containers for the following:
    * Nginx Webserver (running on http://localhost)
    * HAProxy Loadbalancer for the api (running on http://localhost:8080)
    * 3 Flask instances (running on http://localhost:5000, http://localhost:5000, http://localhost:5000)
Note: Flask also serves the same html file as nginx at http://localhost:[5000 | 5001 | 5002]/chat
### Not Implemented
*RabbitMQ for inter api communication

*Socket IO comms with multiple clients


### Current State
   * Rest calls from any served client to all flask instances and HAProxy 
   * Socket connection to the same flask instance. (haproxy socket connection fails). This means that a socket connection from http://localhost:5000/chat works for this endpoint http://localhost:5000/ and not for any other instances eg 5001, 5002.
     The socket connection fails if using a different instance, or nginx served ui, or calls to haproxy load balancer.
     
     The Issue: 
     ```
     Access to XMLHttpRequest at 'http://localhost:5001/socket.io/?EIO=3&transport=polling&t=NIc_l1B' from origin 'http://localhost:5000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
          index.js:83 GET http://localhost:5001/socket.io/?EIO=3&transport=polling&t=NIc_l1B net::ERR_FAILED
     ```
     This falsely appears as cors issue but cors has been enabled on the flask server and rest calls work fine, its just the socket connection
     
 ### Expected behaviour
 
 I want to be able to establish socket connection to any of the instances from any other instance and ultimately, 
 the client should only send request to the haproxy load balancer, and it should forward the request to one of the instances and successfully establich a socket connection.
 
 Note: The haproxy load balancer works perfectly for rest calls 
 
 
 ### How to run
 
* You need to have docker installed
* If you want to test python code locally, activate the env thats located at (`./env/Scripts/activate`)
* To run everything on Docker, Navigate to the root and execute `docker-compose up --build`


### References:

https://www.youtube.com/watch?v=gzIcGhJC8hA

https://www.youtube.com/watch?v=9sAg7RooEDc