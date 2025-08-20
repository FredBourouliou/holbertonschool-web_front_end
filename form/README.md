# HTML5 Forms Project

## Description
This project focuses on creating modern, accessible, and user-friendly HTML5 forms using only HTML and CSS. The project demonstrates various form elements, validation techniques, and styling approaches without relying on any external libraries or frameworks.

## Learning Objectives
By the end of this project, you will be able to:

- Create HTML5 forms with semantic markup
- Choose the appropriate input types for different data requirements
- Implement form field constraints using regular expressions
- Style form inputs to indicate invalid, valid, and required states
- Build a functional comment form
- Create a simple and effective search form
- Develop usable and accessible forms following best practices

## Requirements
- All files must end with a new line
- A README.md file at the root of the project folder is mandatory
- No external libraries allowed (No NodeJS, React, VueJS, Bootstrap, etc.)
- Website must be built with only HTML/CSS
- HTML and CSS must render correctly on Chrome 78 or higher

## Project Structure

### HTML Files
- `00-article.html` - Base article page template
- `01-article.html` - Article with basic comment structure
- `02-article.html` - Article with fieldsets and form groups
- `03-article.html` - Article with labels and input containers
- `04-article.html` - Article with complete form inputs
- `05-article.html` - Article with help messages
- `06-article.html` - Article with error handling
- `07-article.html` - Article with search form

### CSS Files
- `00-styles.css` - Base styles
- `01-styles.css` - Styles with comment section
- `02-styles.css` - Styles with fieldset layout
- `03-styles.css` - Styles with label formatting
- `04-styles.css` - Styles with input field design
- `05-styles.css` - Styles with help text
- `06-styles.css` - Styles with validation states
- `07-styles.css` - Styles with search form

## Features Implemented

### 1. Comment Form
- Personal information section (First Name, Last Name, Email)
- Comment section (Title, Comment text)
- Form validation with visual feedback
- Accessible form structure with proper labels

### 2. Form Validation
- HTML5 pattern attributes for input validation
- Regular expressions for:
  - Names: `[A-Za-zÀ-ž\s]{3,}` (minimum 3 characters, letters and spaces)
  - Email: `[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$`
  - Title: `[A-Za-zÀ-ž\s]{4,}` (minimum 4 characters)
- Visual indicators for valid/invalid states
- Required field validation

### 3. Search Form
- Expandable search interface
- Smooth animations and transitions
- Icon-based search button
- Responsive design

### 4. Accessibility Features
- Semantic HTML5 elements
- Proper label associations
- ARIA labels where appropriate
- Keyboard navigation support
- Screen reader friendly markup
- Visually hidden helper text

### 5. CSS Styling
- Custom properties (CSS variables) for consistent theming
- Flexbox layouts for responsive design
- Form validation states (valid/invalid indicators)
- Hover and focus states
- Smooth transitions and animations

## Browser Compatibility
This project has been tested and optimized for:
- Chrome 78+
- Modern browsers supporting HTML5 and CSS3

## Usage
1. Open any of the HTML files in a web browser
2. Navigate to the comment section at the bottom of the article
3. Fill in the form fields with appropriate data
4. Visual feedback will indicate valid/invalid inputs
5. The search form can be accessed in the navigation menu

## Best Practices Applied
- Progressive enhancement approach
- Mobile-first responsive design
- Semantic HTML markup
- CSS organization and modularity
- Form validation without JavaScript
- Accessibility standards compliance

## Author
Holberton School Student Project

## License
This project is part of the Holberton School curriculum.