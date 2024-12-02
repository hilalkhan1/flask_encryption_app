# **Encryption Web Application**

A simple yet powerful web application built with Flask that allows users to encrypt and decrypt text using various encryption algorithms. The application supports the following algorithms:

- **ROT-13**: A substitution cipher that replaces each letter with the 13th letter after it in the alphabet.
- **Caesar Cipher**: A substitution cipher that shifts characters by a user-specified number of positions.
- **Columnar Transposition**: A method of encryption where the plaintext is written in rows, and the columns are reordered based on a key.

## **Features**

- **User-Friendly Interface**: An intuitive web interface for selecting encryption algorithms and entering input text.
- **Multiple Encryption Modes**:
  - Encrypt or decrypt text using radio buttons for selecting the mode.
  - Supports keys for columnar transposition and shift values for Caesar cipher.
- **Real-Time Output**: Displays results immediately below the "Submit" button for ease of access.

## **Technologies Used**

- **Frontend**: HTML, CSS (for styling the form elements).
- **Backend**: Flask (Python framework for handling logic and server-side processing).

## **Installation**

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hilalkhan1/flask_encryption_app.git
   cd encryption-web-app
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   flask run
   ```
   Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## **Usage**

1. Select an encryption algorithm from the dropdown menu:
   - **ROT-13**
   - **Caesar Cipher**
   - **Columnar Transposition**

2. Choose an action:
   - **Encrypt**: Encode the text.
   - **Decrypt**: Decode the text.

3. Provide the necessary inputs:
   - **Text**: Input the text to encrypt or decrypt.
   - **Shift** (for Caesar): Specify the shift value for Caesar cipher.
   - **Key** (for Columnar): Provide a key for columnar transposition.

4. Click **Submit** and view the result displayed under the button.

## **Screenshots**

### Main Interface
![Main Interface](https://github.com/hilalkhan1/flask_encryption_app/interface.png)

## **Encryption Algorithms**

### 1. ROT-13
A substitution cipher where each letter is replaced with the letter 13 positions after it in the alphabet.

### 2. Caesar Cipher
A substitution cipher that shifts the letters of the plaintext by a specified number of positions. The shift can be positive (right) or negative (left).

### 3. Columnar Transposition
Rearranges the plaintext into columns based on a key, and the ciphertext is formed by reading the columns in the key's sorted order.