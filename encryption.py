class EncryptionAlgorithms:
    @staticmethod
    def rot13(text):
        """Encrypt and decrypt using ROT-13 (same logic for both)."""
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def caesar_encrypt(text, shift):
        """Encrypt text using Caesar cipher."""
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def caesar_decrypt(text, shift):
        """Decrypt text using Caesar cipher."""
        return EncryptionAlgorithms.caesar_encrypt(text, -shift)

    @staticmethod
    def columnar_encrypt(text, key):
        """Encrypt text using columnar transposition."""
        key_order = sorted(list(key))
        columns = {char: [] for char in key_order}
        for i, char in enumerate(text):
            columns[key[i % len(key)]].append(char)
        return ''.join(''.join(columns[char]) for char in key_order)

    @staticmethod
    def columnar_decrypt(text, key):
        """Decrypt text using columnar transposition."""
        n_cols = len(key)
        n_rows = len(text) // n_cols
        extra_chars = len(text) % n_cols

        columns = {}
        start_idx = 0
        for char in sorted(key):
            col_size = n_rows + (1 if key.index(char) < extra_chars else 0)
            columns[char] = text[start_idx:start_idx + col_size]
            start_idx += col_size

        result = []
        for i in range(n_rows + 1):
            for char in key:
                if i < len(columns[char]):
                    result.append(columns[char][i])
        return ''.join(result)
