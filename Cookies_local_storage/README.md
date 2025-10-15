# 🦆 Cookies and Local Storage 🦆

This project contains exercises for learning how to use cookies, local storage, and session storage in web applications.

🦆 Happy coding with ducks! 🦆

## 🦆 Project Structure

- `package.json` - Node.js package configuration with webpack dependencies
- `webpack.config.js` - Webpack configuration for development server
- `src/index.js` - Empty file (required by webpack)
- HTML files for each task (one duck for each! 🦆):
  - `0-index.html` - Basic cookie creation
  - `1-index.html` - Cookie with expiration date and path
  - `2-index.html` - Reading cookies
  - `3-index.html` - Delete cookies and mini login application
  - `4-index.html` - Using js-cookie library
  - `5-index.html` - Local storage shopping cart
  - `6-index.html` - Session storage shopping cart
  - `7-index.html` - Advanced session storage cart with quantities

## 🦆 Setup

1. Install dependencies (the ducks need their tools! 🦆):
```bash
npm install
```

2. Start the development server:
```bash
npm start
```

3. Access the pages at:
- http://localhost:8080/0-index.html
- http://localhost:8080/1-index.html
- http://localhost:8080/2-index.html
- http://localhost:8080/3-index.html
- http://localhost:8080/4-index.html
- http://localhost:8080/5-index.html
- http://localhost:8080/6-index.html
- http://localhost:8080/7-index.html

## 🦆 Tasks

### 0. Create basic cookie 🍪🦆
Create a basic HTML page with:
- Two text inputs (firstname and email)
- "Log me in" button to set cookies
- "Show the cookies" button to display cookies

### 1. Create cookie with expiration date and specific path
Modify cookies to expire in 10 days with specific path.

### 2. Read cookie
Create a `getCookie` function to read specific cookies by name.

### 3. Delete cookie and mini application
Create a mini login application with:
- Login form
- Welcome message with logout functionality
- Cookie deletion on logout

### 4. Use js-cookie
Replace vanilla JavaScript cookie functions with js-cookie library.

### 5. Local storage 🦆
Create a shopping cart using local storage:
- Display available items (maybe add some rubber ducks? 🦆)
- Add items to cart (persists across browser sessions)
- Show cart count on page load

### 6. Session storage
Same as task 5 but using session storage (only persists for current session).

### 7. Advanced use of web storage
Advanced shopping cart with:
- Item quantities
- Remove individual items
- Clear entire cart
- Real-time cart updates

## 🦆 Requirements

- All code must be written in vanilla JavaScript
- No external dependencies except webpack-dev-server and js-cookie (for task 4)
- All files must end with a new line
- Browser must support Web Storage API
- Ducks are mandatory! 🦆🦆🦆

---

Made with 🦆 and ❤️ by duck lovers!
