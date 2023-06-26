# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
from tqdm import tqdm

path = "../birth_dev.tsv"
predictions = ["London" for line in tqdm(open(path, encoding='utf-8'))]

total, correct = utils.evaluate_places(path, predictions)

print('Correct: {} out of {}: {}%'.format(correct, total, correct / total * 100))
