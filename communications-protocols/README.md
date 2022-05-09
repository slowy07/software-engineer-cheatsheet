## what happens when you type urlin the web browser

a url many contain a request to html, image file or any other type


1. If the content of the typed URL is in the cache and fresh, then display the content.
2. Else find the IP address for the domain so that a TCP connection can be set up. Browser does a DNS lookup.
3. Browser needs to know the IP address for a URL so that it can set up a TCP connection. This is why browser needs DNS service. The browser first looks for URL-IP mapping browser cache, then in OS cache. If all caches are empty, then it makes a recursive query to the local DNS server. The local DNS server provides the IP address.
4. Browser sets up a TCP connection using three-way handshake.
5. Browser sends a HTTP request.
6. Server has a web server like Apache, IIS running that handles incoming HTTP request and sends an HTTP response.
7. Browser receives the HTTP response and renders the content.


## how many layers are in OSI reference model

OSI reference model: OSI reference model is an ISO standard which defines a networking framework for implementing the protocols in seven layers. These seven layers can be grouped into three categories:
1. network layer: layer 1, layer 2, layer 3 are the network layers.
2. transport layer: layer 4 is a transport layer.
3. application layer. layer 5, layer 6, 7 are the application layers.

### data link layer
- it is used for transferring the data from one node to another node.
- it receives the data from the network layer and converts the data into data frames and then attach the pyhsicals address to these frames which are sent to the physical layer.
- it enables the error-free transfer of data from one node to another node.
