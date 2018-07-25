from flask import redirect, render_template, url_for
from app.forms import SubmitForm
from itertools import combinations, chain
import json
from app import app


def has_repeated_characters(letters):
    if len(set(letters)) != len(letters):
        return True
    return False


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(3, len(s) + 1))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = SubmitForm()
    if form.validate_on_submit():
        letters = form.letters.data
        with open("app/static/dictionary_words.json") as json_data:
            word_list = json.load(json_data)
            combo_word_list = set()
            if has_repeated_characters(letters):
                for elem in powerset(letters):
                    for word in word_list:
                        if len(word) == len(elem) and sorted(word) == sorted(elem):
                            # Filter the word list for only the required characters
                            if all(x in word for x in elem):
                                combo_word_list.add(word)
            else:
                for elem in powerset(letters):
                    for word in word_list:
                        if len(word) == len(elem):
                            # Filter the word list for only the required characters
                            if all(x in word for x in elem):
                                combo_word_list.add(word)
            combo_word_list = sorted(list(combo_word_list))
            combo_word_list.sort(key=len)
        return render_template('index.html', combo_word_list=combo_word_list, form=form)
    return render_template('index.html',
                           form=form,
                           combo_word_list=[]
                           )
