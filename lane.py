passou_de_ano = input ("você passou de ano? (sim/não):").strip().lower()
passou_no_vestibular = input("você passou no vstibular?) (sim/não):").strip().lower()

if passou_de_ano == "sim":
     if passou_no_vestibular == "sim":
        print("começarei a faculdade no próximo ano.")
     else:    
        print ("vou precisar tentar o vestinular novamente.") 

else:
    print ("preciso estudar mais para passar de ano.")    