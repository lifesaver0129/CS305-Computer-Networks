# CS305 Computer Networks
Personal repo for SUSTech course CS305 Computer Networks

## Labs
* Lab02:
    - Create a class, and initialize following methods:
        + Add the students' name and ID
        + Find name by ID
        + Arrange students according to ID then print out
    - Create a subclass, rewrite arrangement method in another way
* Lab05 Task1:
    - In this assignment, you will develop a simple Web server in Python that is capable of processing only one request. Specifically, your Web server will
        + (i) create a connection socket when contacted by a client (browser);
        + (ii) receive the HTTP request from this connection;
        + (iii) parse the request to determine the specific file being requested;
        + (iv) get the requested file from the server’s file system;
        + (v) create an HTTP response message consisting of the requested file preceded by header lines; and
        + (vi) send the response over the TCP connection to the requesting browser.
    - If a browser requests a file that is not present in your server, your server should return a “404 Not Found” error message. In the companion Web site, we provide the skeleton code for your server. Your job is to complete the code, run your server, and then test your server by sending requests from browsers running on different hosts. If you run your server on a host that already has a Web server running on it, then you should use a different port than port 80 for your Web server
* Lab05 Task2:
    - Deploy a chatting program
    - The message and sender can be recognized inreal time
    - Client to client is a plus
    - GUI is a plus
* Grading for Lab05:
    ![](lab05/grading.gif)
* Lab11:
    - Achieve djikstra algorithm

## Project : Network Measurement and Analysis
In this project, you are required to use all kinds of tracing tools to measure the network performance of our network in campus. You are required to measure both the wireless network and wired network.

You need to measure various metrics of the network, e.g. end-to-end throughput, network delay, signal strength e.t.c. and capture necessary packets to infer the network topology and network configuration.

By measuring our network, you need to point out the problems of our campus network, and propose techniques to solve these problems. It would be better if you really solve some of the problems by reconfiguring the network (maybe you need to contact the network administrator for authority).

For optional topics, you are required to analyze one of the following three problems: 1) The enabling techniques of the Wall. You are required to analyze the performance and enabling techniques of the wall, which prevent you from visiting some of the oversea websites, by tracing the packets go through the network. You'd better propose several schemes to overcome it. 2) security problems in Internet, e.g. how https, ftps, ssl or other mechanisms with security implemented. 3) CDN network. By tracing the real traffic in the network, analyze how CDN network works, where is the CDN servers deployed, and how does their load balancing algorithm works.

Submission:
1) Technical report. including your findings, your analysis procedure and your proposals for network improvement.
2) presentation slides.
3) Source code for tracing traffics, original measurement data and code for network improvement.

