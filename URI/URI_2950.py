dados = input()
distance, d_sauron, d_saruman = dados.split()
icm = float(distance)/(float(d_sauron) + float(d_saruman))
print("%.2f"%icm)
