# DIVISOR DE RANGES

num_puzzle = 68
num_divisao = 10

ini_range = int('0x80000000000000000', 16)
end_range = int('0xfffffffffffffffff', 16) # 68 | 80000000000000000 : fffffffffffffffff

tamanho_slot = (end_range - ini_range) // num_divisao
print(f"Puzzle numero: {num_puzzle}")
print(f"Range inicial: {ini_range:,} | {ini_range:x}")
print(f"Range   final: {end_range:,} | {end_range:x}")
print(f"Total de chaves: {end_range - ini_range:,}")
print(f"\nChaves por slot: {tamanho_slot:,}")


# Calculate and print ranges
current_start = ini_range
for i in range(num_divisao):
  current_end = current_start + tamanho_slot
  if i == num_divisao -1:
    current_end = end_range
  print(f"\nSlot {i+1}:")
  print(f"  Ini (INT): {current_start} | Ini (HEX): {hex(current_start)}")
  print(f"  Fim (INT): {current_end} | Fim (HEX): {hex(current_end)}")
  current_start = current_end
