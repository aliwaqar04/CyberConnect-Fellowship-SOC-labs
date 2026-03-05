# Introductory Networking

This lab introduced the basic concepts of computer networking and how devices communicate with each other over a network. Understanding these fundamentals is important before moving into traffic analysis and security monitoring which are core tasks in a SOC environment.

## Topics Covered

IP addressing  
Ports and common services  
TCP and UDP  
Packets and data transmission  
Basic client server communication

## Key Concepts

IP Address  
Every device connected to a network has an IP address. It acts as the identity of the device so that data can be sent to the correct destination.

Ports  
Ports allow multiple services to run on the same system. For example web servers usually run on port 80 for HTTP and port 443 for HTTPS.

TCP vs UDP  
TCP is connection oriented and ensures reliable data delivery. UDP is faster but does not guarantee delivery of packets.

Packets  
Data sent across a network is broken into smaller units called packets. Each packet contains header information and the actual data being transmitted.

## Example

When a user opens a website in a browser, the browser sends a request to the server using HTTP or HTTPS. The request travels across the network in packets. The server processes the request and sends a response back to the client.

## Screenshots

Screenshots from the completed tasks and room progress are stored in the screenshots folder.

Example location

../../screenshots/introductory-networking/

## Notes

This room helped build a basic understanding of how networks operate. These concepts are essential for later topics such as packet analysis, intrusion detection and network monitoring.