import click

# Define a group for the CLI commands
@click.group()
def mycommands():
    pass

# Command to add a contact to the list
@click.command()
@click.argument("lista_contactos", type=click.Path(exists=False), required=False)
@click.option('--nombre', prompt='Ingrese su nombre', help='Nombre', default="n")
@click.option('--apellido', prompt='Ingrese su apellido', help='Apellido', default="a")
@click.option('--telefono', prompt='Ingrese su teléfono', help='Teléfono', default="t")
@click.option('--email', prompt='Ingrese su correo electrónico', help='Correo electrónico', default="m")
def agregar_contacto(nombre, apellido, telefono, email, lista_contactos):
    # Determine the filename based on provided argument or default
    filename = lista_contactos if lista_contactos is not None else "lista_contactos.txt"
    # Open the file in append mode and add contact information
    with open(filename, "a+") as f:
        f.write(f"{nombre}: {apellido}: {telefono}: {email}\n")  # Append contact information

# Command to list contacts
@click.command()
@click.argument("lista_contactos", type=click.Path(exists=True), required=False)
def listar_contactos(lista_contactos):
    # Determine the filename based on provided argument or default
    filename = lista_contactos if lista_contactos is not None else "lista_contactos.txt"
    if lista_contactos is not None:
        # Read the contacts from the file and display them
        with open(filename, "r") as f:
            lista_contactos = f.read().splitlines()
            print(f"Contacts in {filename}:")
            for un_contacto in lista_contactos:
                print(un_contacto)
    else:
        # If no file provided, show a message about using the default file
        print("No file provided. Using default file: lista_contactos.txt")
        # Proceed with using default file 'lista_contactos.txt'
        # or handle the case when no file is provided

# Command to search contacts by a specific key
@click.command()
@click.argument("lista_contactos", type=click.Path(exists=True), required=False)
@click.option('--key', prompt='Enter key to search', help='Key to search by (e.g., name, email)')
def buscar_contacto(lista_contactos, key):
    # Determine the filename based on provided argument or default
    filename = lista_contactos if lista_contactos is not None else "lista_contactos.txt"
    if lista_contactos is not None:
        # Read the contacts from the file
        with open(filename, "r") as f:
            lista_contactos = f.read().splitlines()
            # Search for the key in the contacts
            found_contacts = [contact for contact in lista_contactos if key in contact]
            if found_contacts:
                print(f"Contacts in {filename} with '{key}' present:")
                for contact in found_contacts:
                    print(contact)
            else:
                print(f"No contacts found in {filename} with '{key}' present.")
    else:
        # If no file provided, show a message about using the default file
        print("No file provided. Using default file: lista_contactos.txt")

# Add the commands to the command group
mycommands.add_command(agregar_contacto)
mycommands.add_command(listar_contactos)
mycommands.add_command(buscar_contacto)

# Execute the CLI commands
if __name__ == '__main__':
    mycommands()
