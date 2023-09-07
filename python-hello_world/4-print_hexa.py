def print_dec_hex(n):
  print('{:02d} {:02x}'.format(n, n))

for i in range(100):
  print_dec_hex(i)
