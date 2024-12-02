class EncryptionAlgorithms:
    @staticmethod
    def rot13(text):
        """
        Encrypt and decrypt using ROT-13 (same logic for both).
        
        ROT-13 shifts each alphabetic character by 13 positions in the alphabet.
        The operation is symmetric: applying it twice results in the original text.
        """
        result = []  # Initialize an empty list to store the result.
        for char in text:
            if 'a' <= char <= 'z':  # Check if the character is a lowercase letter.
                # Shift the character by 13 positions within 'a' to 'z'.
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':  # Check if the character is an uppercase letter.
                # Shift the character by 13 positions within 'A' to 'Z'.
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                # For non-alphabetic characters, add them unchanged.
                result.append(char)
        return ''.join(result)  # Combine the list into a single string and return.

    @staticmethod
    def caesar_encrypt(text, shift):
        """
        Encrypt text using Caesar cipher.

        The Caesar cipher shifts each alphabetic character by a given number of positions.
        """
        result = []  # Initialize an empty list to store the result.
        for char in text:
            if 'a' <= char <= 'z':  # Check if the character is a lowercase letter.
                # Shift the character by 'shift' positions within 'a' to 'z'.
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':  # Check if the character is an uppercase letter.
                # Shift the character by 'shift' positions within 'A' to 'Z'.
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                # For non-alphabetic characters, add them unchanged.
                result.append(char)
        return ''.join(result)  # Combine the list into a single string and return.

    @staticmethod
    def caesar_decrypt(text, shift):
        """
        Decrypt text using Caesar cipher.

        Decryption reverses the shift by applying a negative shift.
        """
        # Reuse the encryption method with a negative shift to reverse the encryption.
        return EncryptionAlgorithms.caesar_encrypt(text, -shift)

    @staticmethod
    def columnar_encrypt(text, key):
        """
        Encrypt text using columnar transposition.

        The key determines the order in which columns are read to form the ciphertext.
        """
        key_order = sorted(list(key))  # Get the sorted order of the key characters.
        # Initialize columns for each character in the sorted key.
        columns = {char: [] for char in key_order}
        for i, char in enumerate(text):
            # Distribute characters into columns based on the cyclic key order.
            columns[key[i % len(key)]].append(char)
        # Read columns in the sorted order of the key and combine into ciphertext.
        return ''.join(''.join(columns[char]) for char in key_order)

    @staticmethod
    def columnar_decrypt(text, key):
        """
        Decrypt text using columnar transposition.

        The key is used to reconstruct the columns and retrieve the original text.
        """
        n_cols = len(key)  # Number of columns, equal to the length of the key.
        n_rows = len(text) // n_cols  # Calculate the number of complete rows.
        extra_chars = len(text) % n_cols  # Determine extra characters in incomplete rows.

        columns = {}  # Initialize dictionary to store columns.
        start_idx = 0  # Index to keep track of the start of each column in the text.

        # Fill the columns by iterating over the sorted key.
        for char in sorted(key):
            # Determine the size of the current column.
            col_size = n_rows + (1 if key.index(char) < extra_chars else 0)
            # Extract the substring for the current column.
            columns[char] = text[start_idx:start_idx + col_size]
            # Update the start index for the next column.
            start_idx += col_size

        result = []  # Initialize an empty list to store the reconstructed text.
        # Iterate row by row to retrieve characters from columns in the original key order.
        for i in range(n_rows + 1):
            for char in key:
                if i < len(columns[char]):  # Ensure the character exists in the current column.
                    result.append(columns[char][i])
        return ''.join(result)  # Combine the list into a single string and return.
