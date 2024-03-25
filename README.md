# FRIDAYPROJECT6

## FILE DESCRIPTION

### gridSignUp.py: 
+ Main Window:
1. Created using tk.Tk() from the Tkinter library.
2. Title set to "Calculator".
+ Entry Box:
1. Created with tk.Entry() to display numbers and calculations.
2. Configured with a width of 20 and no border.
3. Disabled to prevent user input.
4. Text color in disabled state is black, background color is white.
+ Button Definitions:
1. Button texts organized into rows in a list of tuples.
2. Each tuple represents a row of buttons on the calculator.
+ Button Creation:
1. Frames created for each row of buttons.
2. Buttons created with tk.Button() for each row.
3. Texts assigned according to button definitions.
4. Configured with a specific font and command (though command doesn't implement functionality).
5. Buttons packed into frames with padding, frames packed into main window.
+ Main Event Loop:
1. Started using root.mainloop().
2. Allows the GUI to be displayed and interacted with by the user.

### packCalculator.py:
+ Main Window Creation:
1. The code initializes the main window of the calculator GUI using tk.Tk().
2. The title of the window is set to "Calculator".
+ Entry Box Creation:
1. An entry box is created to display numbers and calculations.
2. Configured with a width of 20 and no border.
3. The entry box is in a disabled state to prevent user input.
4. Text color in disabled state is set to black, and the background color is white.
5. Positioned with some vertical padding within the main window.
+ Button Definitions:
1. Buttons are organized into rows, defined as tuples in a list.
2. Each tuple represents a row of buttons on the calculator.
+ Button Creation:
1. For each row of button definitions, a frame is created to contain the buttons.
2. Buttons are created with text according to the button definitions.
3. Configured with a specific font and command (although the command doesn't perform any functionality).
4. Buttons are packed into their respective frames with padding, and frames are packed into the main window.
+ Main Event Loop:
1. The main event loop is started using root.mainloop(), allowing the GUI to be displayed and interacted with.

### placeLogin.py: 
+ Main Window Creation:
1. A main window is created using tk.Tk().
2. The title of the window is set to "Login" using root.title("Login").
+ Login Function:
1. The login() function retrieves the username and password entered by the user from usernameEntry and passwordEntry respectively.
2. It then prints the username and password to the console.
+ Entry Widgets:
1. Entry widgets are created to allow the user to input their username and password.
2. The usernameEntry and passwordEntry widgets are created using tk.Entry(root) and positioned at specific coordinates within the window using place() method.
+ Label Widgets:
1. Label widgets are created to provide visual labels for the username and password entry fields.
2. The usernameLabel and passwordLabel widgets are created using tk.Label(root, text="Username:") and tk.Label(root, *text="Password:") respectively. They are positioned using the place() method.
+ Login Button:
1. A login button is created using tk.Button(root, text="Login", command=login).
2. The command parameter specifies that the login() function should be called when the button is clicked.
3. The button is positioned using the place() method.
+ Main Event Loop:
1. The root.mainloop() function starts the Tkinter event loop, allowing the GUI to be displayed and interacted with by the user.
