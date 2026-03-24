# Online Food Ordering System using Basic HTTP Server

## Abstract
The Online Food Ordering System using a Basic HTTP Server is a simple web-based application developed to demonstrate the basic concepts of web technologies and client-server communication. The main aim of this project is to create a basic HTTP server that can host and deliver static web pages through a web browser. Users can view available food items, select their preferred dishes, and simulate placing an order through a simple web interface.

In this system, the HTTP server receives requests from the client and responds by sending the appropriate HTML pages with CSS styling. The project includes multiple webpages such as a homepage, a food menu page, and an order page. It also demonstrates HTTP response codes like 200 OK for successful requests and 404 Not Found for invalid pages, helping to understand how web servers and web communication work.

## Tools and Technologies Used
- Programming Language: Python
- Web Technologies: HTML, CSS
- Server Technology: Python HTTP Server (`http.server` module)
- Development Environment: Visual Studio Code
- Web Browser: Google Chrome / Microsoft Edge
- Operating System: Windows

## Project Structure
```
mini_project_1/
|-- server.py
|-- README.md
`-- static/
    |-- index.html
    |-- menu.html
    |-- order.html
    |-- 404.html
    `-- styles.css
```

## How to Run
1. Open terminal in this project folder.
2. Run:
   ```bash
   python server.py
   ```
3. Open browser and visit:
   - `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/home` (Homepage)
   - `http://127.0.0.1:8000/menu` (Menu page)
   - `http://127.0.0.1:8000/order` (Order page)
   - `http://127.0.0.1:8000/invalid` (Shows custom 404 page)

## HTTP Response Demonstration
- Valid pages return: `200 OK`
- Invalid pages return: `404 Not Found`
