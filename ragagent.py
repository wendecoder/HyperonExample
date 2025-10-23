from hyperon import MeTTa, E, S, ValueAtom
from knowledge import write_to_file, initialize_knowledge_graph

metta = MeTTa()
initialize_knowledge_graph(metta)

def query_capability(capability):
    """Find capabilities linked to a concept."""
    capability = capability.strip('"')
    query_str = f'''
    !(load-ascii &self mettakb.metta) ; load external knowledge base
    !(match &self (capability {capability} $feature) $feature)
    '''
    results = metta.run(query_str)
    print(results, query_str)

def query_communication(communication):
    """Find communication patterns linked to a concept."""
    communication = communication.strip('"')
    query_str = f'''
    !(load-ascii &self mettakb.metta) ; load external knowledge base
    !(match &self (communication {communication} $pattern) $pattern)
    '''
    results = metta.run(query_str)
    print(results, query_str)

def add_knowledge(relation_type, subject, object_value):
    """Add new knowledge dynamically. Here you need to write to file as well to persist the knowledge."""
    if isinstance(object_value, str):
        object_value = ValueAtom(object_value)
    metta.space().add_atom(E(S(relation_type), S(subject), object_value))
    write_to_file("mettakb.metta", str(E(S(relation_type), S(subject), object_value)))
    return f"Added {relation_type}: {subject} → {object_value}"

# Example usage:

# Query existing knowledge of capabilities
# query_capability("uAgent") # Output = [microservice, message_handling, event_processing, REST_endpoints]

# # Now let's add new capability knowledge
# add_knowledge("capability", "uAgent", "new_capability")

# Assume now your server went down and up again, if you haven't written to file, you would lose the new knowledge, but since you wrote to file, just by loading the file again(which is done in the above methods in `query_str`) you will have the new knowledge available.
query_capability("uAgent") # Output = [microservice, message_handling, event_processing, REST_endpoints, new_capability]

# The same can be done for communication patterns
# query_communication("ctx.send") # Output = [asynchronous, fire_and_forget]
# add_knowledge("communication", "ctx.send", "new_pattern")
# query_communication("ctx.send") # Output = [asynchronous, fire_and_forget, new_pattern]