# Q1 

>Identify and explain common and important components and concepts of web development markup languages. 

Markup languages are essential to software development and can be found in many contexts. These range from simple readme documents to the HTML documents that define the structure and content of the web. While HTML is not the only web markup language (other notable examples include XML and XHTML) it is the most prevalent. $^1$


Broadly speaking, web markup languages have two important characteristics: they provide an annotated language that can be actionably parsed by web browsers and also maintain human readability. This results in a language that can provide vast amounts of information to a browser while retaining the ability to present its raw content meaningfully to the average human reader. $^2$


HTML (or hypertext markup language) was conceived and written by Tim Berners-Lee in 1990 as an integral language essential to the burgeoning World Wide Web.$^3$ Most notably its hypertext enables users to navigate seamlessly to linked pages and content via associated hyperlinks.  

HTML markup utilizes tags to separate elements specific to rendering content by the browser but not intended to be seen by the end user. Tags are denoted by the ```<``` and ```> ```symbols. Most tags have opening and closing counterparts, using the  ```/``` character to denote a closing element (ie ```</TAG>```. The resulting tag structure generally takes this format: 
    ```<TAG>Content</TAG>```.


After defining the document type that a browser can expect to render ( ```<!DOCTYPE html>```) we move to the two main structures of an html file, contained within the ```<html> </html>``` tags. These structures are the ```<head>``` and the ```<body>``` of the document. 
The head contains metadata for the browser such as the document title, linked stylesheets and logic (deferred), language, viewport settings and other resources such as frameworks, font libraries and icons. 


The body contains the content and structure that is intended to be seen by the end user. This content is laid out within different tags to indicate content type, meaning and provide further functionality. Some tag types include paragraphs, hyperlinks, ordered and unordered lists, buttons and forms. Some of these tags nest other specific tags to create more specialized and intricate structures. For example, a form utilizes ``````<input>`````` tags which have a myriad of different definable input types, each with its own input fields and validation functionality. 


In more recent years HTML has seen a shift towards using semantic tags, moving away from the ubiquitous ```<div>``` and ```<span>``` from days of yore. Semantic tags are meant to convey meaning and intent (eg. ```<nav> <figure> <aside>```). One important benefit of semantic tags are their role in aiding users with accessibility issues using screen readers and other assistive technologies. Ultimately semantic tags provide the twofold benefit of creating more intelligible code and making the internet a more inclusive space for all.  


$^1$ Kyrnin, Jennifer. "What Are Markup Languages?" ThoughtCo, Jul. 31, 2021, thoughtco.com/what-are-markup-languages-3468655.


$^2$ MDN: HTML https://developer.mozilla.org/en-US/docs/Web/HTML#reference 

$^3$ Craig, William. "History of the Internet", webfx, Aug. 31 2022,
https://www.webfx.com/blog/web-design/the-history-of-the-internet-in-a-nutshell/