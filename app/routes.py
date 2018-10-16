from flask import render_template
from app.forms import SubmitForm
from itertools import combinations, chain
from app import app


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(3, len(s) + 1))


def solution(letters, word_list):
    combo_word_list = set()
    for elem in powerset(letters):
        elem = "".join(elem)
        if elem in word_list:
            combo_word_list.add(elem)
    combo_word_list = sorted(list(combo_word_list))
    combo_word_list.sort(key=len)
    return combo_word_list


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = SubmitForm()
    combo_word_list = []
    if form.validate_on_submit():
        letters = form.letters.data
        with open('app/static/words') as f:
            word_list = [word.rstrip("\n").lower() for word in f]
        word_list = {word for word in word_list if 8 >= len(word) >= 3 and not word.endswith("'s")}
        combo_word_list = solution(letters, word_list)
    return render_template('index.html', combo_word_list=combo_word_list, form=form)
