import os
import random
random.seed(20170316)
for typ in ["Type_1", "Type_2", "Type_3"]:
    with open(typ + ".additional.txt", "w") as validF:
        for f in os.listdir(os.path.join("../download/additional/", typ)):
            if f.endswith("jpg") and random.random() >= 0.8:
                validF.write(f + "\n")
