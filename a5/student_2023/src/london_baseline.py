# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

EVAL_FILE =  "birth_dev.tsv"

if __name__ == "__main__":
    true_pred = ["London"] * 500
    total, correct = utils.evaluate_places(EVAL_FILE, true_pred)
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))