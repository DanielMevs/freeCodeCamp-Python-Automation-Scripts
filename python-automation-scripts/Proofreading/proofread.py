# author: Shittu Olumide @ https://www.freecodecamp.org/news/python-automation-scripts/
import lmproof


def proofread(text):
    """Proof-reads text"""
    proof_read = lmproof.load("en")
    correction = proof_read.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))
