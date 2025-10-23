from hyperon import MeTTa, E, S, ValueAtom

metta = MeTTa()

query_str = f'''
    !(load-ascii &self mettakb.metta)
    !(match &self (capability $x $y) ($x $y))
'''
def write_to_file(filename, text):
    """Write the given text to a file."""
    with open(filename, "a") as file:
        file.write(text)
    print(f"Text written to {filename}")

### Querying Before adding new capabilities
results = metta.run(query_str)
print("Query Results Before:", results)

### Adding new capabilities to the mettakb.metta file
write_to_file("mettakb.metta", "(capability uAgent Rest_endpoints)")
write_to_file("mettakb.metta", "(capability uAgent LLM_processing)")
write_to_file("mettakb.metta", "(capability uAgent agent_querying)")

### Querying After adding new capabilities
results = metta.run(query_str)
print("Query Results After:", results)