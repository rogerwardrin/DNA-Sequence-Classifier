import lightgbm as lgb
import numpy as np
import pickle
from collections import Counter
import re

class DNAClassifier:
    def __init__(self, model_path, kmer_path, species, k_values = [5]):
        self.model = lgb.Booster(model_file = model_path)

        with open("kmer_index.pkl", "rb") as f:
            self.kmer_index = pickle.load(f)

        self.k_values = k_values
    
    def _kmer_vector(self,seq):
        seq = seq.upper()
        seq = re.sub(r'[^ATGC]', 'N', seq)

        vec = np.zeros(len(self.kmer_index), dtype = float)
    
        for k in self.k_values:
            counts = Counter(seq[i:i+k] for i in range(len(seq) - k + 1))
            
            valid_total = {kmer: c for kmer, c in counts.items() if kmer in self.kmer_index}
            total = sum(valid_total.values()) or 1

            for kmer, c in counts.items():
                if kmer in self.kmer_index:
                    vec[self.kmer_index[kmer]] = c/total

        gc_ratio = (seq.count('G') + seq.count('C')) / len(seq)

        n_ratio = seq.count('N') / len(seq)

        vec = np.append(vec, [n_ratio, gc_ratio])

        return vec
    
    def predict(self, seq):
        vec = self._kmer_vector(seq)
        vec = vec.reshape(1,-1)

        prob = self.model.predict(vec)[0]

        

        with open("best_thresh.pkl", "rb") as f:
            THRESHOLD = pickle.load(f)
        
        label = species[0] if prob > THRESHOLD else species[1]

        return label, prob


with open("species.pkl", "rb") as f:
            species = pickle.load(f)

classifier = DNAClassifier("dna_model_human_dog.txt", "kmer_index.pkl", species)

seq = input("Enter DNA Sequence: ")

label, prob = classifier.predict(seq)

print("\nPrediction: ",label)
print(f"\nProbability {species[0]}: {round(prob, 4)}")