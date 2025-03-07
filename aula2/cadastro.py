import banco

ze = banco.Banco("Saqua Eng Software", 1, 1, "Zé da manga", "38201948310")

zecove = banco.Banco("Inter", 1, 1006, "Zé das Coves", "00987465123")

print(ze)

print(zecove)

ze.definir_senha("admin01")
zecove.definir_senha("12345")

ze.deposito(5000)

ze.pix(zecove, 2000)

ze.saque("admin01", 2000)

ze.extrato()

zecove.extrato()