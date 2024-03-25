#FRIDAYPROJECT6

##FILE DESCRIPTION

###gridSignUp.py: 
Main Window:
*Created using tk.Tk() from the Tkinter library.
*Title set to "Calculator".
Entry Box:
*Created with tk.Entry() to display numbers and calculations.
*Configured with a width of 20 and no border.
*Disabled to prevent user input.
*Text color in disabled state is black, background color is white.
*Button Definitions:
*Button texts organized into rows in a list of tuples.
*Each tuple represents a row of buttons on the calculator.
Button Creation:
*Frames created for each row of buttons.
*Buttons created with tk.Button() for each row.
*Texts assigned according to button definitions.
*Configured with a specific font and command (though command doesn't implement functionality).
*Buttons packed into frames with padding, frames packed into main window.
*Main Event Loop:
*Started using root.mainloop().
*Allows the GUI to be displayed and interacted with by the user.

###packCalculator.py:
Main Window Creation:
*The code initializes the main window of the calculator GUI using tk.Tk().
*The title of the window is set to "Calculator".
Entry Box Creation:
*An entry box is created to display numbers and calculations.
*Configured with a width of 20 and no border.
*The entry box is in a disabled state to prevent user input.
*Text color in disabled state is set to black, and the background color is white.
*Positioned with some vertical padding within the main window.
Button Definitions:
*Buttons are organized into rows, defined as tuples in a list.
*Each tuple represents a row of buttons on the calculator.
*Button Creation:
*For each row of button definitions, a frame is created to contain the buttons.
*Buttons are created with text according to the button definitions.
*Configured with a specific font and command (although the command doesn't perform any functionality).
*Buttons are packed into their respective frames with padding, and frames are packed into the main window.
Main Event Loop:
*The main event loop is started using root.mainloop(), allowing the GUI to be displayed and interacted with.

###placeLogin.py: 
Main Window Creation:
*A main window is created using tk.Tk().
*The title of the window is set to "Login" using root.title("Login").
Login Function:
*The login() function retrieves the username and password entered by the user from usernameEntry and passwordEntry respectively.
*It then prints the username and password to the console.
Entry Widgets:
*Entry widgets are created to allow the user to input their username and password.
*The usernameEntry and passwordEntry widgets are created using tk.Entry(root) and positioned at specific coordinates *within the window using place() method.
Label Widgets:
*Label widgets are created to provide visual labels for the username and password entry fields.
*The usernameLabel and passwordLabel widgets are created using tk.Label(root, text="Username:") and tk.Label(root, *text="Password:") respectively. They are positioned using the place() method.
Login Button:
*A login button is created using tk.Button(root, text="Login", command=login).
*The command parameter specifies that the login() function should be called when the button is clicked.
*The button is positioned using the place() method.
Main Event Loop:
*The root.mainloop() function starts the Tkinter event loop, allowing the GUI to be displayed and interacted with by the user.
