import codecs

def decrypt(ciphertexts):
  cipher_xor = hex(int(ciphertexts[1], 16) ^ int(ciphertexts[2], 16))[2:]
  print(cipher_xor)
  for word in [b" the ", b" this ", b" you ", b' is ', b' can ', b' that ']:
    print(word)
    encoded_word = codecs.encode(word,"hex")
    index = 0
    while index < len(cipher_xor)-len(encoded_word):
      drag = hex(int(cipher_xor[index:index+len(encoded_word)],16) ^ int(encoded_word,16))[2:]
      # print(drag)
      if len(drag)%2!=0:
        drag = drag + "0"
      print(str(codecs.decode(drag,"hex")) + str(index//2))
      index+=2
    print("")

  key_5_10 = hex(int(ciphertexts[1][10:20], 16) ^ int(codecs.encode(b' can ',"hex"), 16))
  print(key_5_10)
  print(str(codecs.decode(key_5_10[2:],"hex")))
  print("")

  for ciphertext in ciphertexts:
    region_decode = hex(int(ciphertext[10:20],16) ^ int(key_5_10,16))[2:]
    print(str(codecs.decode(region_decode,"hex")))

  key_4_11 = hex(int(ciphertexts[5][8:22], 16) ^ int(codecs.encode(b' would ',"hex"), 16))
  print(key_4_11)
  print(str(codecs.decode(key_4_11[2:],"hex")))
  print("")

  for ciphertext in ciphertexts:
    region_decode = hex(int(ciphertext[8:22],16) ^ int(key_4_11,16))[2:]
    print(str(codecs.decode(region_decode,"hex")))

  key_3_11 = hex(int(ciphertexts[10][6:22], 16) ^ int(codecs.encode(b' we are ',"hex"), 16))
  print(key_3_11)
  print(str(codecs.decode(key_3_11[2:],"hex")))
  print("")

  for ciphertext in ciphertexts:
    region_decode = hex(int(ciphertext[6:22],16) ^ int(key_3_11,16))[2:]
    print(str(codecs.decode(region_decode,"hex")))

  key_0_16 = hex(int(ciphertexts[0][0:32], 16) ^ int(codecs.encode(b'Testing testing ',"hex"), 16))
  print(key_0_16)
  print(str(codecs.decode(key_0_16[2:],"hex")))
  print("")

  for ciphertext in ciphertexts:
    region_decode = hex(int(ciphertext[0:32],16) ^ int(key_0_16,16))[2:]
    print(str(codecs.decode(region_decode,"hex")))

  key_0_33 = hex(int(ciphertexts[0][0:66], 16) ^ int(codecs.encode(b'Testing testing can you read this',"hex"), 16))
  print(key_0_33)
  print(str(codecs.decode(key_0_33[2:],"hex")))
  print("")

  for ciphertext in ciphertexts:
    region_decode = hex(int(ciphertext[0:66],16) ^ int(key_0_33,16))[2:]
    print(str(codecs.decode(region_decode,"hex")))

  print("")

  english_key = "TheQuickBrownFoxJumpsOverLazyDog!"
  hex_key = hex(int(codecs.encode(b'TheQuickBrownFoxJumpsOverLazyDog!', "hex"),16))
  print(hex_key)
  print(str(codecs.decode(hex_key[2:],"hex")))

  for ciphertext in ciphertexts:
    # print(ciphertext)
    # print(str(codecs.decode(ciphertext,"hex")))
    region_decode = hex(int(ciphertext,16) ^ int(hex_key,16))[2:]
    print(str(codecs.decode(region_decode,"hex")))
  
  return english_key


ciphertexts = ["000d16251c07044b36171c0307280858291403500a2003450029001e5930070e52",
              "0d0d15713c49000a2c521d120f224f0125004d00163d100011380d0359330a0b4d",
              "151f00221a04064b2d1c0a571a2f021d6a050c145326054505231311102a084701",
              "0d091c71020c4308231c4f1a0f2d0a582c0003501c29562b1b2f0e09592a001001",
              "1d480d3e050c43052d521c031b220a163e550e111d6f04001328410e112d1c4701",
              "00000425551e0c1e2e164f150b661e0d2301085016221404003e00090a2d010001",
              "181d063a1c051a4b0d263f5707354f082f070b15103b1a1c523f04190b211b4701",
              "1001013f01492d02211d1c571d2716583e1d0802166f0104016c005a1a251b0449",
              "19091c3310491a0e365226570a2f0b163e551d110a6f171106290f0e102b014701",
              "030d45221d06160726521d120f2a03016a190403072a1845062341341027001401",
              "1a090d71020c430a30174f13012f011f6a02081c1f6f010c06240e0f0d64070e4c"]

print(decrypt(ciphertexts))