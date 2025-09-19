#Bài 03
def caesar_shift_text(text, shift):
  return ''.join(caesar_encrypt_char(ch, shift) for ch in text)
  ciphertext = "YMJ VZNHP GWTBS KTC OZRUX TAJW YMJ QFED ITL"
  print("Bản mã đầu vào:",ciphertext, "\n")

  #Từ vựng thường xuất hiện trong tiếng anh
  common_words = ["THE", "AND" , "TO","OF","IS","THAT","FOR"]
  candidates =[]
  for s in range(26):
    text_decrypted = caesar_shift_text(ciphertext,-s)
    upper = ""+ text_decrypted.upper()+""
    score = sum(1 for w in common_words if w in upper)
    candidates.append((s,score,text_decrypted))
    print(f"Shift {s:02d} -> {text_decrypted} [score={score}]")
  # sắp xếp
  best= candidates_sorted[0]
  print("\nGợi ý tốt nhất theo heuristic (nhiều từ phổ biển xuaasrt hiện nhất):")
  print(f"Shift = {best[0]:02d}, score = {best[1]},plaintext candidate:\n  {best[2]}")