# JavaScript Advanced

![Amazing Duck](amazing_duck2.png)

## Description
This project explores advanced JavaScript concepts including closures, lexical scoping, callbacks, and the execution stack. Through practical exercises, you'll learn how JavaScript manages scope, creates private methods, and handles asynchronous operations.

## Learning Objectives
By completing this project, you will understand:
- What is lexical scoping in JavaScript
- What is closure in JavaScript
- How to use closure
- How to chain different closures
- How to simulate private methods with Closure
- The execution stack order with JavaScript
- How to use binding
- How to use callbacks

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `.js` extension

## Project Structure
```
Javascript_advanced/
├── 0-welcome.js
├── 1-nested_functions.js
├── 2-function_me.js
├── 3-classrooms.js
├── 4-math.js
├── 5-mode.js
├── 6-hogwarts.js
├── 7-timeout.js
├── 8-payments.js
├── 9-prime.js
├── 10-prime.js
├── 11-prime.js
├── 12-room_area.js
├── 13-bind_user.js
├── 14-wikipedia.js
├── 100-stock.js
└── README.md
```

## Tasks Overview

### 0. Lexical scoping and welcome message
Introduction to lexical scoping with nested functions accessing parent scope variables.

### 1. Closure Scope Chain
Demonstrates how nested functions create a scope chain, accessing variables from multiple parent scopes.

### 2. Closure
Creating functions that return other functions, maintaining access to their creation context.

### 3. Closure and loops
Using closures with loops to create multiple functions with their own private state.

### 4. Complex Closure
Higher-order functions that create mathematical operations through closures.

### 5. Changing DOM with closure
Using closures to create theme switchers that modify page styles.

### 6. Private methods with closure
Simulating private variables and methods in JavaScript using closures.

### 7. Stack order and setTimeout
Understanding JavaScript's execution stack and how `setTimeout` affects execution order.

### 8. Stack order in functions
Exploring synchronous function execution and call stack behavior.

### 9. Prime numbers & timing execution
Performance measurement using the Performance API.

### 10. Execution stack & timing execution
Measuring execution time for repeated operations.

### 11. Changing stack order using setTimeout
Using `setTimeout` to defer execution and understand event loop behavior.

### 12. Binding
Understanding function binding and the `this` context.

### 13. Binding + Closure
Combining binding with closures for complex function behaviors.

### 14. Simple callback
Implementing callbacks with AJAX requests using XMLHttpRequest.

### 15. Multiple callbacks (Advanced)
Managing multiple callback scenarios for success and error handling.

## Usage Examples

### Running a file in the browser console:
```javascript
// Copy and paste the content of any .js file into the browser console
// For example, for 0-welcome.js:
welcome('Holberton', 'School'); // Will display: Welcome Holberton School!
```

### Testing closure behavior:
```javascript
// From 2-function_me.js
const guillaume = welcomeMessage('Guillaume');
guillaume(); // Alert: Welcome Guillaume
```

### Testing DOM manipulation (5-mode.js):
1. Create an HTML file
2. Include the script: `<script src="5-mode.js"></script>`
3. Click the buttons to change themes

## Key Concepts

### Lexical Scoping
Variables are accessible within the scope where they are defined and in all nested scopes.

### Closures
Functions that maintain access to variables from their outer (enclosing) scope even after the outer function has returned.

### Execution Stack
JavaScript executes code in a single-threaded manner, using a call stack to manage function execution order.

### Event Loop
Asynchronous operations are handled through the event loop, which processes callbacks after the main execution stack is empty.

### Function Binding
The `bind()` method creates a new function with a permanently bound `this` context.

## Testing
To test any of the JavaScript files:
1. Open your browser's developer console
2. Copy and paste the code from the desired file
3. Execute the test cases as described in each task

## License
This project is part of the Holberton School curriculum.