print()
print('ĆWICZENIE – Cena brutto')
print()

# Mamy kilka produktów i chcemy obliczyć ich cenę brutto przy zadanej stawce podatku.

tax_rate = 0.23
item1_netto_price = 100
item2_netto_price = 345
item3_netto_price = 30.50

print('Produkt 1:', item1_netto_price, 'zł (cena netto)')
print('Produkt 2:', item2_netto_price, 'zł (cena netto)')
print('Produkt 3:', item3_netto_price, 'zł (cena netto)')
print()

print('Produkt 1:', item1_netto_price + (item1_netto_price * tax_rate), 'zł (cena brutto)')
print('Produkt 2:', item2_netto_price + (item2_netto_price * tax_rate), 'zł (cena brutto)')
print('Produkt 3:', item3_netto_price + (item3_netto_price * tax_rate), 'zł (cena brutto)')
print()
# lub
print('Produkt 1:', 100 + (100 * 0.23), 'zł (cena brutto)')
print('Produkt 2:', 345 + (345 * 0.23), 'zł (cena brutto)')
print('Produkt 3:', 30.50 + (30.50 * 0.23), 'zł (cena brutto)')

print()
print('--------------------------------------------------------------------')
print()
