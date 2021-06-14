import os

print("Inserisci la root dei tuoi progetti (premi invio per saltare): ")
path = input("")

print("Inserisci il nome delle cartelle separate da uno spazio: ")
folders = input("")


for f in folders.split(" "):
    print('----------------------------------------------------------------')
    try:
        command = f"cd {path}{f} && git add * && git commit -m 'automatic update' && git push"
        print(f"{path}{f}")
        print(os.system(command)[1])
        
    except Exception as e:
        print(e)
