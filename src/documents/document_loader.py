from swarmauri.documents.concrete.Document import Document

def load_documents():
    return [
        Document(content="Backend Engineering is the backbone of enterprise solutions"),
        Document(content="Backend Engineering involves developing connections between client and servers"),
        Document(content="Backend Engineering encapsulates core business logic"),
        Document(content="Backend Engineering is built on these 4 pillars; Abstraction,Inheritance, Encapsulationand Polymorphism"),
    ]

def load_additional_documents():
    return [
        Document(content="Frontend Engineering also known as client-side engineering develops solution for user interactivity"),
        Document(content="Frontend Engineering focuses on optimizing user experience and improving UI performance"),
        Document(content="Frontend Engineering involves technologies like HTML, CSS, and JavaScript"),
        Document(content="Frontend Engineers collaborate with Backend Engineers to deliver seamless end-to-end solutions"),
        Document(content="Frontend Engineering includes frameworks such as React, Angular, and Vue.js to build dynamic web applications"),
    ]
