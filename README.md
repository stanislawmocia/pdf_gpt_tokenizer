# PDF Token Counter
PDF Token Counter is a tool to count the tokens within PDF documents. You can use it to calculate the number of tokens in a given document and estimate the costs of analyzing tokens using various models like GPT-4 and GPT-3.5 Turbo.

## Installation
To install the required packages, make sure you have Python installed, and then follow the instructions below in the root directory of the project:
1. Create a virtual environment using the command:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
    - On Linux/Mac: 
    ```source venv/bin/activate```
    - On Windows:
    ```.\venv\Scripts\activate```
3. Install the required packages using the command:
    ```pip install -r requirements.txt```

## Usage
After installing the dependencies, you can run the program. During execution, you will be prompted to enter the path to the PDF file from which you want to count the tokens.

## How to Use
1. Open a terminal in the project folder.
2. Run the command `python3 main.py` (or the name of your script if it's different).
3. Enter the path to the PDF file when prompted.
4. The program will then output the token count and the input prices for different models. Here's an example of what the output might look like:

```
Number of tokens: 160349

Input price
GPT-3.5 Turbo 4K: 0.24 $
GPT-3.5 Turbo 16K: 0.48 $
GPT-4 : 4.81 $
```

## Support
If you need assistance, please create an issue in the repository or contact me directly.