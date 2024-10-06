# GIF Grid Splitter

GIF Grid Splitter is a web application that allows users to upload a GIF file and split it into a grid of smaller GIFs. This project uses Flask for the backend and Tailwind CSS for the frontend styling.

## Setup and Running Instructions

1. Clone the repository:

   ```
   git clone https://github.com/rodrigoochoam/gif-grid-splitter.git
   cd gif-grid-splitter
   ```

2. Create and activate a virtual environment:

   - On Windows:
     ```
     python -m venv grid_env
     grid_env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     python3 -m venv grid_env
     source grid_env/bin/activate
     ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   or

   ```
   pip3 install -r requirements.txt
   ```

4. Run the Flask application:

   ```
   flask run
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Dependencies and Libraries Used

- Flask: Web framework for Python
- Pillow (PIL): Python Imaging Library for image processing
- Tailwind CSS: Utility-first CSS framework (loaded via CDN)

## Approach and Challenges

### Approach

1. Frontend:

   - Created a simple and intuitive user interface using HTML and Tailwind CSS.
   - Implemented client-side validation for input fields.
   - Added a loading spinner to indicate processing status.

2. Backend:

   - Used Flask to handle file uploads and serve the web pages.
   - Implemented GIF processing logic using the Pillow library.
   - Split the GIF into a grid of smaller GIFs based on user input.

3. Integration:
   - Connected the frontend and backend to create a seamless user experience.
   - Used Flask's templating engine to dynamically generate the result page.

### Challenges Faced

1. GIF Processing: Handling animated GIFs and preserving their animation in the split output required careful implementation.

2. Performance: Processing large GIFs can be time-consuming. Future improvements could include asynchronous processing or progress indicators for larger files.

3. Error Handling: Implementing robust error handling for various edge cases, such as invalid file types or processing failures, was crucial for a smooth user experience.

4. Responsive Design: Ensuring the application works well on different screen sizes while maintaining the grid layout of the split GIFs presented some CSS challenges.

## Future Improvements

- Implement asynchronous processing for large GIFs
- Add more customization options (e.g., output size, frame rate adjustment)
- Improve error handling and user feedback
- Optimize performance for faster processing of large GIFs
