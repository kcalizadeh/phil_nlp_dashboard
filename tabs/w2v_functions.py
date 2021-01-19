import json

def get_dropdown_list_w2v():
    dropdown_list = [
      {'label': 'Plato', 'value': 'plato'},
      {'label': 'Aristotle', 'value': 'aristotle'},
      {'label': 'Empiricism', 'value': 'empiricism'},
      {'label': 'Rationalism', 'value': 'rationalism'},
      {'label': 'Analytic', 'value': 'analytic'},
      {'label': 'Continental', 'value': 'continental'},
      {'label': 'Phenomenology', 'value': 'phenomenology'},
      {'label': 'German Idealism', 'value': 'german_idealism'},
      {'label': 'Communism', 'value': 'communism'},
      {'label': 'Capitalism', 'value': 'capitalism'},
      {'label': 'All Texts', 'value': 'all'},
      {'label': 'Locke', 'value': 'Locke'},
      {'label': 'Hume', 'value': 'Hume'},
      {'label': 'Berkeley', 'value': 'Berkeley'},
      {'label': 'Spinoza', 'value': 'Spinoza'},
      {'label': 'Leibniz', 'value': 'Leibniz'},
      {'label': 'Descartes', 'value': 'Descartes'},
      {'label': 'Malebranche', 'value': 'Malebranche'},
      {'label': 'Russell', 'value': 'Russell'},
      {'label': 'Moore', 'value': 'Moore'},
      {'label': 'Wittgenstein', 'value': 'Wittgenstein'},
      {'label': 'Lewis', 'value': 'Lewis'},
      {'label': 'Quine', 'value': 'Quine'},
      {'label': 'Popper', 'value': 'Popper'},
      {'label': 'Kripke', 'value': 'Kripke'},
      {'label': 'Foucault', 'value': 'Foucault'},
      {'label': 'Derrida', 'value': 'Derrida'},
      {'label': 'Deleuze', 'value': 'Deleuze'},
      {'label': 'Merleau-Ponty', 'value': 'Merleau-Ponty'},
      {'label': 'Husserl', 'value': 'Husserl'},
      {'label': 'Heidegger', 'value': 'Heidegger'},
      {'label': 'Kant', 'value': 'Kant'},
      {'label': 'Fichte', 'value': 'Fichte'},
      {'label': 'Hegel', 'value': 'Hegel'},
      {'label': 'Marx', 'value': 'Marx'},
      {'label': 'Lenin', 'value': 'Lenin'},
      {'label': 'Smith', 'value': 'Smith'},
      {'label': 'Ricardo', 'value': 'Ricardo'},
      {'label': 'Keynes', 'value': 'Keynes'}
      ]
    return dropdown_list


def get_keys(path):
    with open(path) as f:
        return json.load(f)

