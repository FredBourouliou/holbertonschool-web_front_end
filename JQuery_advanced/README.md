# jQuery Advanced

![Doctor Who](./ducktor_who.webp)

This project explores advanced jQuery concepts and techniques for DOM manipulation, AJAX requests, and dynamic web applications.

## Description

This project demonstrates proficiency in jQuery through a series of progressively complex tasks, from basic DOM manipulation to building a full-featured application with AJAX requests, pagination, and CRUD operations.

## Learning Objectives

- Load jQuery from a CDN
- Create and manipulate DOM elements using jQuery
- Modify element attributes, styles, and content
- Handle user events (clicks, form submissions)
- Perform AJAX requests (GET, POST, DELETE)
- Work with external APIs (Wikipedia)
- Build dynamic forms and tables
- Implement pagination
- Use jQuery effects (wrap/unwrap for loading states)
- Set up and interact with a local JSON server

## Technologies

- **jQuery 3.7.1**: JavaScript library for DOM manipulation and AJAX
- **json-server**: Mock REST API for testing
- **Wikipedia API**: External API for search functionality

## Project Structure

- `0-index.html` - Load jQuery from CDN
- `1-index.html` - Create DOM elements
- `2-index.html` - Create multiple DOM elements
- `3-index.html` - Chain DOM elements
- `4-index.html` - HTML function to replace content
- `5-index.html` - Click, CSS, and remove functions
- `6-index.html` - Val, before, and prepend functions
- `7-index.html` - Query Wikipedia API with AJAX GET
- `8-index.html` - Pagination implementation
- `9-index.html` - Wrap/unwrap for loading states
- `10-index.html` - GET request to local JSON server
- `11-index.html` - POST request to create data
- `12-index.html` - DELETE request to remove data
- `db.json` - Database file for json-server

## Setup

### Prerequisites

- Node.js and npm installed
- A modern web browser

### Installation

1. Clone the repository:
```bash
cd holbertonschool-web_front_end/JQuery_advanced
```

2. Install json-server:
```bash
npm install json-server
```

3. Start the JSON server (for tasks 10-12):
```bash
node_modules/.bin/json-server --watch db.json
```

The server will run on `http://localhost:3000`

## Usage

### Basic Tasks (0-9)

Simply open the HTML files in your browser:
```bash
open 0-index.html
```

### AJAX Tasks (10-12)

1. Start the JSON server first
2. Open the HTML file in your browser
3. The application will interact with the local API

## Features by Task

### Task 0: Load jQuery
- Load jQuery from CDN in the browser console
- Verify jQuery is loaded correctly

### Task 1: Creating a DOM Element
- Create and append paragraph elements using jQuery

### Task 2: Creating Multiple Elements
- Create complex nested DOM structures
- Build a table with multiple rows

### Task 3: Chain DOM Elements
- Use jQuery chaining for cleaner code
- Build structured HTML efficiently

### Task 4: HTML Function
- Replace table content dynamically
- Use `.html()` method

### Task 5: Click, CSS, and Remove
- Handle click events
- Apply CSS styling with jQuery
- Remove DOM elements dynamically

### Task 6: Val, Before, and Prepend
- Create interactive forms
- Get input values
- Add elements at different positions (before, prepend)
- Use nth-of-type selector

### Task 7: Wikipedia Search
- Query Wikipedia API
- Display search results dynamically
- Parse and render HTML snippets

### Task 8: Pagination
- Implement paginated results
- Calculate and display page numbers
- Navigate between pages with offset

### Task 9: Loading State
- Show loading indicator during API requests
- Use wrap/unwrap for visual feedback

### Task 10: GET Request
- Fetch data from local JSON server
- Display posts from database

### Task 11: POST Request
- Create form for new posts
- Send POST requests to API
- Add new records to database

### Task 12: DELETE Request
- Delete posts via API
- Remove elements from DOM
- Handle errors gracefully

## Key jQuery Methods Used

- **DOM Manipulation**: `.append()`, `.prepend()`, `.before()`, `.after()`, `.html()`, `.text()`
- **Selectors**: `.first()`, `.nth-of-type()`, `$('element')`
- **Events**: `.click()`, `.submit()`
- **AJAX**: `$.get()`, `$.post()`, `$.ajax()`
- **Effects**: `.wrap()`, `.unwrap()`
- **Styling**: `.css()`
- **Attributes**: `.attr()`, `.val()`
- **Traversal**: `.each()`
- **Removal**: `.remove()`

## API Endpoints (Tasks 10-12)

### Local JSON Server

- `GET /posts` - List all posts
- `POST /posts` - Create a new post
- `DELETE /posts/:id` - Delete a post by ID

### Wikipedia API

- Endpoint: `https://en.wikipedia.org/w/api.php`
- Action: `query`
- List: `search`
- Format: `json`

## Requirements

- Use jQuery 3.7.1 (slim or minified version as needed)
- Code must work in modern browsers
- No jQuery plugins allowed (only core jQuery)
- Follow proper JavaScript syntax and conventions

## Author

Frederic Bourouliou - Holberton School

## Repository

- **GitHub**: holbertonschool-web_front_end
- **Directory**: JQuery_advanced