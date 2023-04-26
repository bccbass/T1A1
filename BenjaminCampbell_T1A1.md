# Q1 

>Identify and explain common and important components and concepts of web development markup languages. 

Markup languages are essential to software development and can be found in many contexts. These range from simple readme documents to the HTML documents that define the structure and content of the web. While HTML is not the only web markup language (other notable examples include XML and XHTML) it is the most prevalent. $^1$


Broadly speaking, web markup languages have two important characteristics: they provide an annotated language that can be actionably parsed by web browsers and also maintain human readability. This results in a language that can provide vast amounts of information to a browser while retaining the ability to present its raw content meaningfully to the average human reader. $^2$ 


HTML (or hypertext markup language) was conceived and written by Tim Berners-Lee in 1990 as an integral language essential to the burgeoning World Wide Web.$^3$ Most notably its hypertext enables users to navigate seamlessly to linked pages and content via associated hyperlinks.  

After defining the document type that a browser can expect to render ( ```<!DOCTYPE html>```) we move to the two main structures of an html file, contained within the ```<html> </html>``` tags. These structures are the ```<head>``` and the ```<body>``` of the document. 
The head contains metadata for the browser such as the document title, linked stylesheets and javascript scripts (deferred), language, viewport settings and other linked resources such as frameworks, font libraries and icons. 

HTML markup utilizes tags to separate elements specific to rendering content by the browser but not intended to be seen by the end user. Tags are denoted by the ```<``` and ```> ```symbols. Most tags have opening and closing counterparts, using the  ```/``` character to denote a closing element (ie ```</TAG>```. The resulting tag structure generally takes this format: 
    ```<TAG>Content</TAG>```.


The body contains the content and structure that is intended to be seen by the end user. This content is laid out within different tags to indicate content type, meaning and provide further functionality. Some tag types include paragraphs, hyperlinks, ordered and unordered lists, buttons and forms. Some of these tags nest other specific tags to create more specialized and intricate structures. One example is that of an anchor tag ```<a></a>``` which accepts a url or file path to link content as a hyperlink. Another is a form which utilizes ``````<input>`````` tags that have a myriad of different definable input types, each with its own input fields and validation functionality. 


In more recent years HTML has seen a shift towards using semantic tags, moving away from the ubiquitous ```<div>``` and ```<span>``` tags from days of yore. Semantic tags are meant to convey meaning and intent (eg. ```<nav> <figure> <aside>```). One important benefit of semantic tags are their role in aiding users with accessibility issues using screen readers and other assistive technologies. Ultimately semantic tags provide the twofold benefit of creating more intelligible code and making the internet a more inclusive space for all.  


$^1$ Kyrnin, Jennifer. "What Are Markup Languages?" ThoughtCo, Jul. 31, 2021, thoughtco.com/what-are-markup-languages-3468655.


$^2$ “HTML Reference - HTML: Hypertext Markup Language: MDN.” HTML: HyperText Markup Language | MDN, https://developer.mozilla.org/en-US/docs/Web/HTML/Reference. 

$^3$ Craig, William. "History of the Internet", webfx, Aug. 31 2022,
https://www.webfx.com/blog/web-design/the-history-of-the-internet-in-a-nutshell/
 
<br />
<br />

# Q2

> Define the features of the following technologies that are essential in terms of the development of the internet: 
 >- packets 
 >- IP addresses (IPv4 and IPv6) 
 >- routers and routing 
 >- domains and DNS
>
> Explain how each technology has contributed to the development of the internet


Packet technology enables internet users to send vast amounts of data globally with limited interruptions and congestion. When sending large messages and files over networks congestion can occur as a result of routes being unavailable while the transfer is taking place.$^1$ This manifests either in subsequent data having to wait for its completion, or take significantly circuitous routes to reach its destination. This problem was ameliorated by implementing the use of data packets and packet switching. This technology breaks up large messages and files into smaller, more manageable packets, allowing them to travel more efficiently over multiple routes to end up at the same destination. To then reconstitute these packets the transfer relies on transfer protocol information (eg. UDP, TCP), which is included in the header of the transfer and requests a port to transfer the packets data to on arrival. UDP does not return a confirmation of receipt to the sender. This has the benefit of not taking up extra network bandwidth but the short coming of not notifying the sender as to whether the transfer was received successfully. When it is imperative that a package is received in whole TCP, or transmission control protocol is implemented instead. One main difference between TCP and UDP is that TCP sends an acknowledgment of receipt to its origin destination. Applications such as email and direct messaging implement TCP as it's imperative that the entire uncorrupted message is received and reconstituted, whereas scenarios in which speed trumps precision such as voice over internet programs (VoIP) and multiplayer games UDP is implemented as acknowledgement of receipt is less important than speed. In both scenarios the transfer is then validated with a checksum; the sum of all the data packets transferred, which is included in the transfer header, and then subsequently checked against the sum of the received packets. 

IP addresses were introduced in 1983 by the US Military's ARPANET as part of the tcp/ip protocol. They ensure every computer that is to be connected to a network is assigned a unique identifier. IP addresses facilitate tcp/ip packet transfers, ensuring disparate packets that have travelled over multiple routes end up at the intended destination where they are reassembled to their original state. IPv4 (or Internet Protocol Version 4) is the current version in use, but is reaching a point of inflection as the available pool of addresses is near exhausted. This is the result of the ubiquity of internet connected devices, not limited to computers, smart phones and tables but the vast amounts of Internet of Things(IoT) devices as well. The anticipated solution is the implementation of IPv6 which uses a 128bit address,  as opposed to IPv4's 32bit address structure. This creates a pool of 340 billion billion billion addresses, versus IPv4's comparatively paltry 4.3 billion addresses. However, the transition from IPv4 to IPv6 is complicated and requires many challenges to be met before it can successfully be implemented. $^2$

Routers are devices that act as connection points facilitating the sending and receiving of packets. Routers comprise both LANs(local area networks) and WANs(wide area networks), where they are sometimes referred to as nodes. $^3$  In a home a router serves to supply wifi internet to connected local devices. In a WAN routers are responsible for receiving and forwarding packets on their path to their final destination. Routing is organized by a routing table which proscribes the path a packet will travel on its way to its destination. This path can be either dynamic or static as well as have varying levels of security protocols and priority implemented. As the packet passes through each router its address is added to the packet to create a source route. This creates a 'travel log' and can be helpful in locating errors should they occur. 

 Website addresses are comprised of an IP address followed by a port number. 1984 saw an effort to make these addresses more human readable via the implementation of domains and the domain name system (DNS). Domains are what we recognize as modern Internet addresses such as facebook.com, whitehouse.gov and unitednations.org.  The DNS is a directory of servers in which all of the domain names are stored with their corresponding IP addresses. It is like the yellow pages of the Internet. $^4$ Every time a domain is requested to be served the browser makes a request to the DNS to direct the user to the associated stored ip address. This allows users to type a familiar name into a browser versus having to remember a 32bit IP address and port number. 


$^1$ History of the Internet, William Craig, 8/12/2022,
https://www.webfx.com/blog/web-design/the-history-of-the-internet-in-a-nutshell/

$^2$ “What Is ipv4?” BlueCat Networks, 31 Aug. 2022, https://bluecatnetworks.com/glossary/what-is-ipv4/.


$^3$ Network Infrastructur: Routers and routing: Computer Science Department, University of Cape Town https://www.cs.uct.ac.za/mit_notes/web_programming/html/ch07s05.html

$^4$ The Internet: Crash Course Computer Science #29 https://www.youtube.com/watch?time_continue=348&v=AEaKrq3SpW8&source_ve_path=MzY4NDIsMzY4NDIsMzY4NDI&feature=emb_logo  

<br />
<br />



 

# Q3

>Define the features of the following technologies that are essential in terms of the development of the internet: 
> - TCP 
> - HTTP and HTTPS 
> - web browsers (requests, rendering and developer tools) 

>Explain how each technology has contributed to the development of client and server communication over the internet (50 - 150 words for each technology)

### TCP

receive
 1974 a proposal was put forth to link a group of computers together in a decentralized network.To facilitate this 'inter-network' TCP, or transmission control protocol, was proposed as a way to regulate communication between machines.(1) TCP is a way to send and receive data securely and reliably over sometimes unreliable and unstable networks. (2) TCP uses TCP segments (or packets) to break up data and transfer over various routes. 
It also implements technologies to ensure secure connections, confirmation of segment receipt  and segment re-ordering when necessary: A three way handshake ensures secure communication, a header attached to the data payload enables checksum data validation, reordering, confirmation receipt of segments and more. TCP is responsible for creating reliable and stable channels over which network applications can communicate.  The most common use case of TCP relating to client/server communication can be found in the familiar act of browsing the web: HTTP, the protocol for requesting and receiving web pages and data, requires a reliable connection and thus is dependent on TCP to transfer its request/response pairs.(3) This relationship between HTTP and TCP forms the technological bedrock that facilitates the unfathomable numbers of client/server web interactions that occur daily. 

### HTTP and HTTPS
HTTP, or Hyper Text Transfer Protocol, is an extensible protocol that governs all exchanges of data on the web. (3) It is a client-server process and is always initiated by a client. This is a process that occurs anytime a website is queried; a tcp connection is established, a clients user-agent(typically a web browser) will send a get request for a specific URI or URL (a web address) and after passing through a number of proxies a server will deliver a response in the form of a status message and if successful will serve the requested resource. (4) HTTPS is HTTP with added security features. It implements Transport Layer Security (previously SSL) to encrypt and verify requests, creating a secure client-server interaction. HTTPS is crucial for users to safely access servers for banking, e-commerce, transferring sensitive medical as well as general web security and privacy. (5) HTTP requests occur every time a client attempts to access, edit or update a web resource. These take the forms of GET, POST and PATCH requests respectively and occur for every instance a user navigates to a web resource or requests to delete, create or alter a resource. An HTTP request occurs every time a user navigates to a website and its frequency and importance cannot be overstated with regard to client-server interaction. 

### Web Browsers and Developer Tools

Web browsers are applications that have a great deal of functionality, namely making client requests to servers using HTTP and rendering and displaying the server response. After a browser makes a request to a server and successfully receives a response it is then tasked with rendering the response. There are many elements a browser then interprets and renders: the content and structure provided in HTML documents, styling and layout from a CSS file, interpreting the logic supplied by a JavaScript file or embedded code as well as fetching and utilizing any linked resources including images, fonts, icons, videos and pdfs. Browsers will often supply a suite of developer tools that are invaluable when developing web sites and applications. They can display every element of a website including HTML, CSS, JavaScript as well as DOM, http status codes, network and session information. The importance of web browsers to modern client-server interactions is almost so gargantuan we take it for granted, like the air we breathe or the clean water that flows from our taps on demand. It provides great convenience, available on pretty almost any modern computing device, and is a far cry from the days of usenet, America Online, BBS and other antiquated means of accessing the internet to communicate with fellow humans from around the globe. 

  

(1) Craig, William. “The History of the Internet in a Nutshell.” WebFX, 12 Aug. 2022, https://www.webfx.com/blog/web-design/the-history-of-the-internet-in-a-nutshell/. 

(2) Sookocheff, Kevin. “How Does TCP Work?” Kevin Sookocheff (Alt + H), 15 May 2019, https://sookocheff.com/post/networking/how-does-tcp-work/.

(3) “An Overview of HTTP.” MDN, https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview. 

(4)  "MDN: A typical HTTP session." MDN,  https://developer.mozilla.org/en-US/docs/Web/HTTP/Session

(5) Why Is HTTP Not Secure? | HTTP vs. HTTPS . https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/. 


<br />
<br />


# Q4

> Identify THREE data structures used in the Python programming language and explain the reasons for using each.

### **List**
A list is a comma delimited collection of objects contained within square brackets: ```my_list = [1, 2, 3]```.(1) Its contents can be any data type and can be heterogeneous; multiple data types can be contained within the same list. ```my_list = [1, 2, 3, 'A', 3.14] ```. A list can even contain other lists or dictionaries: ```my_nested_list = [[1,2,3], [5,6,7]]```
It is indexed, has length and has a host of built-in methods accessible to alter or manipulate its contents. Lists are mutable, meaning their contents can be modified, reassigned and sorted. Additionally lists can have elements removed, inserted, concatenated and appended. They are also iterable, which means they can easily be used in loops:
```Python
my_list = [1, 2, 3]
for el in my_list:
    print(el)
```
Since a variable can only store one value at a time, a list is well suited to store collections of related(or unrelated) objects which can be accessed from the same variable. They can then be manipulated and acted upon relationally as a single data structure. One common use  case is utilizing a list to contain a collection of dictionaries:
```Python
People = [
{‘person1’: ‘Bobby’},
{‘person2’: ‘Jimmy’},
{‘person3’: ‘Jamey’}
]
```
This collection of people can now be iterated over and acted upon as a single data structure containing a group of related elements. 




### **Tuple**
A tuple is a comma delimited collection of elements contained within parentheses: 
```
my_tuple = (1, 2, 3, 'A', 'B', 'C')
```
It is extremely similar to a list with the main difference being that it is immutable; it cannot be altered, manipulated or have elements reordered, added or removed.(1) It is also indexed, has length and is iterable. 
Tuples are used when a list data structure is required but its contents are not intended to be altered. If a developer needs to manipulate a tuple there are built-in functions that help to facilitate this. The tuple() and list() functions serve to convert the passed in argument to their respective data types: 
```Python
print(list((1, 2, 3)))
``` 
would yield:
```
>>> [1, 2, 3]
```
To leave a list or tuple intact before manipulating its contents the ```copy()``` function can be called to duplicate it. This creates a completely new data instance with a unique reference ID from the original, which can then be converted to a list and mutated in any number of ways. (1)
A tuple is not only implemented to shield contents from alteration but also to signal to other developers the intent and spirit of its intent that the data should remain undisturbed: 
```Python
the_beatles = (‘John’, ‘Paul’, ‘George’, ‘Ringo’)
```


### **Dictionary**
A dictionary in Python is a collection of key/value pairs that are comma delimited and contained within curly braces:
```Python
person = {
'name': 'John',
'height': 190,
'age': 54
}
```
Dictionaries are unordered which means they cannot be accessed by index values, however they are iterable and later versions of Python will store the order in which their key/value pairs were originally formatted.(2) Dictionaries are particularly useful when modeling data structures on real life objects and people as seen in the previous example. Their paired values can be represented by any data types or structures available in the Python language. This gives dictionaries great flexibility and detail when modeling both abstract data and real life people, places and things. 



(1) Sweigart, Al. “Automate the Boring Stuff with Python: Dictionaries.” Automate the Boring Stuff with Python, https://automatetheboringstuff.com/2e/chapter5/. 

(2) Sweigart, Al. “Automate the Boring Stuff with Python: Lists.” Automate the Boring Stuff with Python, https://automatetheboringstuff.com/2e/chapter4/. 


<br />
<br />










 - 
