import PyPDF2
import tiktoken

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("p50k_base") # Its for [gpt-4, gpt-3.5-turbo, text-embedding-ada-002] models
    num_tokens = len(encoding.encode(string))
    return num_tokens

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

pdf_path = input("PDF path: ")
text_from_pdf = extract_text_from_pdf(pdf_path)
tokens_count = num_tokens_from_string(text_from_pdf)

price_per_1k_tokens_gpt4 = 0.03
price_per_1k_tokens_gpt3_5_turbo_4K = 0.0015
price_per_1k_tokens_gpt3_5_turbo_16K = 0.003

price_gpt4 = (tokens_count / 1000) * price_per_1k_tokens_gpt4
price_gpt3_5_turbo_4K = (tokens_count / 1000) * price_per_1k_tokens_gpt3_5_turbo_4K
price_gpt3_5_turbo_16K = (tokens_count / 1000) * price_per_1k_tokens_gpt3_5_turbo_16K

print(f"Number of tokens: {tokens_count}\n")
print("Input price")
print(f"GPT-3.5 Turbo 4K: {price_gpt3_5_turbo_4K:.2f} $")
print(f"GPT-3.5 Turbo 16K: {price_gpt3_5_turbo_16K:.2f} $")
print(f"GPT-4 : {price_gpt4:.2f} $")