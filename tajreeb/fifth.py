import space, os
import en_core_web_sm
from numpy.doc.constants import lines

nlp = en_core_web_sm.load()

doc = nlp(str(lines))
print("Noun phrases: ", [chunk.text for chunk in doc.noun_chunks])
print("verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
for entity in doc.ents:
    print(entity.text, entity.label_)
