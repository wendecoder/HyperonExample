from hyperon import MeTTa, E, S, ValueAtom

metta = MeTTa()


def write_to_file(filename, text):
    """Write the given text to a file."""
    with open(filename, "a") as file:
        file.write(text)
    print(f"Text written to {filename}")

def initialize_knowledge_graph(metta: MeTTa):
    """Initialize the MeTTa knowledge graph, and no need to write knowledge to file here since initialize_knowledge_graph will be called every time the server starts."""
    
    # Agent Types → Capabilities
    metta.space().add_atom(E(S("capability"), S("uAgent"), S("microservice")))
    metta.space().add_atom(E(S("capability"), S("uAgent"), S("message_handling")))
    metta.space().add_atom(E(S("capability"), S("uAgent"), S("event_processing")))
    metta.space().add_atom(E(S("capability"), S("uAgent"), S("REST_endpoints")))
    metta.space().add_atom(E(S("capability"), S("ASI:One"), S("LLM_processing")))
    metta.space().add_atom(E(S("capability"), S("ASI:One"), S("agent_querying")))

     # Communication Patterns → Methods
    metta.space().add_atom(E(S("communication"), S("ctx.send"), S("asynchronous")))
    metta.space().add_atom(E(S("communication"), S("ctx.send"), S("fire_and_forget")))
    metta.space().add_atom(E(S("communication"), S("ctx.send_and_receive"), S("synchronous")))
    metta.space().add_atom(E(S("communication"), S("ctx.send_and_receive"), S("request-response")))
    metta.space().add_atom(E(S("communication"), S("chat protocol"), S("structured_messaging")))
    metta.space().add_atom(E(S("communication"), S("chat protocol"), S("acknowledgments")))

    # Examples containing Valueatoms
    metta.space().add_atom(E(S("treatment"), S("antidepressants"), ValueAtom("therapy, medications"))) # here it seems the ValueAtom is used because the target is multi value, but it isn't the correct way of multi-value targets since the target value will be sparsed when retrieving them targets later correctly. The recommended way to store multi-value is using an E(Expression). Just to mention, Expression in MeTTa can be used both for storing triplets(i.e relation-subject-object), and also as a list collaction of values, symbols in MeTTa.
    # Using Expression for multi-value target
    metta.space().add_atom(E(S("treatment"), S("antidepressants"), E(S("therapy"), S("medications")))) # This way when running pattern matching query later, you will get both "therapy" and "medications" as target values correctly.

# My guess this part of the code from repo

#  !(match &self (capability $x $y) ($x $y))

# Matches metta atom, capability uAgent Rest_endpoints
# Metta reads that file and then runs each space().add like below to create the knowledge base?

#  metta.space().add_atom(E(S("capability uAgent Rest_entpoints"), S("uAgent"), S("Rest_endpoints")))

# Is this correct cause in the medical example there is also a line using  ValueAtom():

# metta.space().add_atom(E(S("treatment"), S("antidepressants"), ValueAtom("therapy, medications")))  

# how would that fit in that example?