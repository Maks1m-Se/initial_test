# Python Dash Application

This is a Python Dash application that includes the following components:

- `.git`: Configuration files for Git
- `.vscode`: Configuration files for Visual Studio Code.
- `assets`: Contains a `style.css` file for styling the application.
- `components`: Houses files for the dashboard components, such as dropdown menus and layout modules.
- `data`: Contains code for handling data.
- `env_initial_dash`: The folder for the virtual environment.
- `main.py`: The main Python script for your Dash application.
- `.gitignore`: Specifies which files and directories should be ignored by Git.

## Installation

To set up and run the application, follow these steps:

1. Clone this repository.
2. Create a virtual environment in the `env_initial_dash` folder.
3. Activate the virtual environment.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Run the application using `python main.py`.

## Explanations

# main.py

The Main file does the following things:
- loads all the nessecar libraries and
- reads the data
- initializes the Dash class
- creates the layout from the components\layout.py module
- starts the server and hosts the Dash application

# components

- each component has a render function
- inside the render function the entire structure of Divs and other html elements, that are needed for that particular component are constructed
- each render function receives the application and returns an html.Div object
- each render function utilizes a callback function to enable connection to the graph

## Usage

This section should describe how to use your Python Dash application, including any specific commands or options to run the dashboard.

## Contributing

## License

## Contact

## Acknowledgments

## Frequently Asked Questions (FAQ)

## Troubleshooting

## Changelog

## Examples


