#bài 02
def caesar_encrypt_char(ch, shift):
  if 'A' <= ch <= 'Z':
    base = ord('A')
    return chr((ord(ch) - base + shift) % 26 + base)
  elif 'a' <= ch <= 'z':
    base = ord('a')
    return chr((ord(ch) - base + shift) % 26 + base)
  return ch

def caesar_decrypt_char(ch, shift):
 return caesar_encrypt_char(ch, -shift)
def caesar_encrypt(text, shift):
    encrypted_chars = [caesar_encrypt_char(ch, shift) for ch in text]
    return "".join(encrypted_chars)
def caesar_decrypt(ciphertext, shift):
    print(f"Shift để giải mã = {shift} (tức dịch ngược bằng {-shift})")
    plain_chars = []
    for idx, ch in enumerate(ciphertext):
        dec = caesar_decrypt_char(ch, shift)
        print(f"pos {idx:02d}: '{ch}' -> '{dec}'")
        plain_chars.append(dec)
    plain_text = "".join(plain_chars)
    print("\nBản rõ cuối:", plain_text)
    return plain_text
  # thực thi
ciphertext = "MJQQT, BTWQI!"
print("Bản mã:", ciphertext, "\n")
plaintext = caesar_decrypt(ciphertext, 5)