# Al Zebra: AI-Powered Maths Tutor for Kids

![Alt text](<AL ZEBRA.png>)

Al Zebra is an AI-powered maths tutor designed to provide interactive learning experiences for kids. It helps kids with mathematics by posing problems of increasing complexity based on their previous responses, verifying their answers, and providing step-by-step explanations for correct solutions.

## Features

- Intelligent progression of problem complexity based on learner performance
- Explanation of correct answers in a step-by-step manner
- Interactive and engaging learning experience

## Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/moreshk/alzebra.git
    cd alzebra
    ```

2. Install the necessary dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:

    ```sh
    python server.py
    ```

Then, open your web browser and navigate to `localhost:5000`.

## Usage

Start by inputting your message to Al Zebra in the provided text box. Al Zebra will then respond with a mathematical problem. Enter your answer in the text box and Al Zebra will validate it, providing a step-by-step explanation if the answer is incorrect.

## Tech Stack

- Flask: Web server
- OpenAI: AI model
- LangChain: Library for chaining different language models
- Bootstrap: Front-end component library

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
