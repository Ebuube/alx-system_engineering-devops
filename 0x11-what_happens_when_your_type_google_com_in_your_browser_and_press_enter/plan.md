# PLAN
* Introduction: How do web browsers interact with users and the servers
* Brief narration:
	* browser makes resolves domain name to IP address of server
	* if content is static: web server hosted on the remote server returns the needed resource
	* if dynamic: the web server makes request to the application server
	* If database is needed: application server makes request to database server
	* Now, everything is combined together to form an appropriate response to the browser
	* The packages are sent to the browser and the browser renders the content to the user
	* browsing continues

## Proper explanation
* DNS request
* TCP/IP communication and port
* Firewall -> restriction of access to some content
* HTTPS/SSL -> Secure Socket Layer and certificates
* Load-balancer -> meaning, algorithms, benefits, disadvantes
* Web server -> To server static content
* Application server -> To run business logic
* Database and database server
* Best combination for the three servers on the physical server
