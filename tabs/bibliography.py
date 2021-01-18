from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


from app import app

FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "20%",
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

analytic_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Analytic Philosophy", href="#analytic")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-1",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Kripke", href="#kripke")),
            dbc.NavLink(html.A("Lewis", href="#lewis")),
            dbc.NavLink(html.A("Moore", href="#moore")),
            dbc.NavLink(html.A("Popper", href="#popper")),
            dbc.NavLink(html.A("Quine", href="#quine")),
            dbc.NavLink(html.A("Russell", href="#russell")),
            dbc.NavLink(html.A("Witgenstein", href="#wittgenstein")),
            
        ],
        id="submenu-1-collapse",
    ),
]

aristotle_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Aristotle", href="#aristotle")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-8",
    ),
]

capitalism_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Capitalism", href="#capitalism")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-2",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Keynes", href="#keynes")),
            dbc.NavLink(html.A("Ricardo", href="#ricardo")),
            dbc.NavLink(html.A("Smith", href="#smith")),            
        ],
        id="submenu-2-collapse",
    ),
]

communism_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Communism", href="#communism")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-3",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Marx", href="#marx")),
            dbc.NavLink(html.A("Lenin", href="#lenin")),           
        ],
        id="submenu-3-collapse",
    ),
]

continental_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Continental Philosophy", href="#continental")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-4",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Deleuze", href="#deleuze")),
            dbc.NavLink(html.A("Derrida", href="#derrida")),
            dbc.NavLink(html.A("Foucault", href="#foucault")),            
        ],
        id="submenu-4-collapse",
    ),
]

empiricism_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Empiricism", href="#empiricism")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-5",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Berekely", href="#berkeley")),
            dbc.NavLink(html.A("Hume", href="#hume")),
            dbc.NavLink(html.A("Locke", href="#locke")),            
        ],
        id="submenu-5-collapse",
    ),
]

german_idealism_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("German Idealism", href="#german_idealism")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-6",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Fichte", href="#fichte")),
            dbc.NavLink(html.A("Hegel", href="#hegel")),
            dbc.NavLink(html.A("Kant", href="#kant")),            
        ],
        id="submenu-6-collapse",
    ),
]

phenomenology_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Phenomenology", href="#phenomenology")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-7",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Heidegger", href="#heidegger")),
            dbc.NavLink(html.A("Husserl", href="#husserl")),
            dbc.NavLink(html.A("Merleau-Ponty", href="#ponty")),            
        ],
        id="submenu-7-collapse",
    ),
]

plato_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Plato", href="#plato")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-9",
    ),
]

rationalism_menu = [
    html.Li(
        dbc.Row(
            [
                dbc.Col(html.A("Rationalism", href="#rationalism")),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-10",
    ),
    dbc.Collapse(
        [
            dbc.NavLink(html.A("Descartes", href="#descartes")),
            dbc.NavLink(html.A("Leibniz", href="#leibniz")),
            dbc.NavLink(html.A("Malebranche", href="#malebranche")),
            dbc.NavLink(html.A("Spinoza", href="#spinoza")),
        ],
        id="submenu-10-collapse",
    ),
]

sidebar = html.Div(
    [
        html.P(
            "Schools of Philosophy", className="lead"
        ),
        dbc.Nav(analytic_menu +
                aristotle_menu + 
                capitalism_menu +
                communism_menu +
                continental_menu + 
                empiricism_menu +
                german_idealism_menu +
                phenomenology_menu +
                plato_menu +
                rationalism_menu, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)

content = html.Div([
                    dcc.Markdown("Texts are ordered alphabetically by school and author's last name."),
                    dcc.Markdown('#### Analytic Philosophy', id='analytic'),
                    dcc.Markdown('##### Saul Kripke', id='kripke'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kripke, Saul A. *Naming and Necessity*. Basil Blackwell Ltd, 1990.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kripke, Saul A. *Philosophical Troubles: Collected Papers*. Oxford University Press, 2011. vol 1.'),
                    dcc.Markdown('##### David Lewis', id='lewis'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; c'),
                    dcc.Markdown('##### G. E. Moore', id='moore'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Moore, G. E. *Philosophical Studies*. 2015. *Project Gutenberg*, [www.gutenberg.org/ebooks/50141](https://www.gutenberg.org/ebooks/50141).'),
                    dcc.Markdown('##### Karl Popper', id='popper'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Popper, Karl. *The Logic of Scientific Discovery*. Translated by Karl Popper, Routledge, 2002.'),
                    dcc.Markdown('##### W. V. O. Quine', id='quine'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quine, W. V. O. *Quintessence: Basic Readings from the Philosophy of W. V. O. Quine*. Edited by Roger F. Gibson, Jr. Harvard University Press, 2004.'),
                    dcc.Markdown('##### Bertrand Russell', id='russell'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Russell, Bertrand. *The Problems of Philosophy*. 2004. *Project Gutenberg*, [www.gutenberg.org/ebooks/5827](https://www.gutenberg.org/ebooks/5827).'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Russell, Bertrand. *The Analysis of Mind*. 2008. *Project Gutenberg*, [www.gutenberg.org/ebooks/2529](https://www.gutenberg.org/ebooks/2529).'),
                    dcc.Markdown('##### Ludwig Wittgenstein', id='wittgenstein'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Wittgenstein, Ludwig. *Tractatus Logico-Philosophicus*. Translated by D. F. Pears and B. F. McGuiness, Routledge, 2001.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Wittgenstein, Ludwig. *Philosophical Investigation*. Translated by G. E. M. Anscombe, Blackwell, 1986.'),
                    dcc.Markdown('#### Aristotle', id='aristotle'),
                    dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Aristotle. *The Complete Works of Aristotle*. Edited by Jonathan Barnes, Princeton University Press, 1991. 2 vols."),
                    dcc.Markdown('#### Capitalism', id='capitalism'),
                    dcc.Markdown('##### John Maynard Keynes', id='keynes'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Keynes, John Maynard. *The General Theory of Employment, Interest, and Money*. 2003. *Project Gutenberg Australia*, [gutenberg.net.au/ebooks03/0300071h.html](http://gutenberg.net.au/ebooks03/0300071h.html).'),
                    dcc.Markdown('##### David Ricardo', id='ricardo'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ricardo, David. *On the Principles of Political Economy and Taxation*. 2010. *Project Gutenberg*, [www.gutenberg.org/ebooks/33310](https://www.gutenberg.org/ebooks/33310).'),
                    dcc.Markdown('##### Adam Smith', id='smith'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Smith, Adam. *An Inquiry into the Nature and Causes of the Wealth of Nations*. 2009. *Project Gutenberg*, [www.gutenberg.org/ebooks/3300](https://www.gutenberg.org/ebooks/3300).'),
                    dcc.Markdown('#### Communism', id='communism'),
                    dcc.Markdown('##### Karl Marx', id='marx'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Marx, Karl. *Capital*. Translated by Samuel Moore and Edward Aveling, Progress Publishers, 1887.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Marx, Karl and Engels, Frederick. *Manifest of the Communist Party*. Translated by Samuel Moore, Foreign Language Press, 1970.'),
                    dcc.Markdown('##### Vladimir Ilyich Lenin', id='lenin'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Lenin, Vladimir Ilyich. *Essential Works of Lenin*. Bantam, 1966.'),
                    dcc.Markdown('#### Continental Philosophy', id='continental'),
                    dcc.Markdown('##### Gilles Deleuze', id='deleuze'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Deleuze, Gilles, and Buattari, Felix. *Anti-Oedipus: Capitalism and Schizophrenia*. Translated by Robert Hurley, Mark Seem, and Helen R. Lane, University of Minnesota Press, 1997.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Deleuze, Gilles. *Difference and Repetition*. Translated by Paul Patton, Continuum, 1994.'),
                    dcc.Markdown('##### Jacques Derrida', id='derrida'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Derrida, Jacques. *Writing and Difference*. Translated by Alan Bass, Routledge, 2001.'),
                    dcc.Markdown('##### Michel Foucault', id='foucault'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Foucault, Michel. *The Order of Things: an Archeology of the Human Sciences*. Routledge, 2002.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Foucault, Michel. *History of Madness*. Translated by Jonathan Murphy and Jean Khalfa, Routledge, 2006.'),
                    dcc.Markdown('#### Empiricism', id='empiricism'),
                    dcc.Markdown('##### George Berkeley', id='berkeley'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Berkeley, George. *A Treatise Concerning the Principles of Human Knowledge*. 2009. *Project Gutenberg*, [www.gutenberg.org/ebooks/4723](https://www.gutenberg.org/ebooks/4723).'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Berkeley, George. *Three Dialogues between Hylas and Philonous in Opposition to Sceptics and Atheists*. 2009. *Project Gutenberg*, [www.gutenberg.org/ebooks/4724](https://www.gutenberg.org/ebooks/4724).'),
                    dcc.Markdown('##### David Hume', id='hume'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hume, David. *A Treatise of Human Nature*. 2003. *Project Gutenberg*, [www.gutenberg.org/ebooks/4705](https://www.gutenberg.org/ebooks/4705).'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hume, David. *Dialogues Concerning Natural Religion*. 2009. *Project Gutenberg*, [www.gutenberg.org/ebooks/4583](https://www.gutenberg.org/ebooks/4583).'),
                    dcc.Markdown('##### John Locke', id='locke'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Locke, John. *An Essay Concerning Human Understanding*. 2004. *Project Gutenberg*, [www.gutenberg.org/ebooks/10615](https://www.gutenberg.org/ebooks/10615). 2 vols.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Locke, John. *Second Treatise of Government*. 2010. *Project Gutenberg*, [www.gutenberg.org/ebooks/7370](https://www.gutenberg.org/ebooks/7370).'),
                    dcc.Markdown('#### German Idealism', id='german_idealism'),
                    dcc.Markdown('##### Johan Gottlieb Fichte', id='fichte'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fichte, Johan Gottlieb. *The System of Ethics According to the Principles of the Wissenschaftslehre*. Translated by Daniel Breazeale and Günter Zöller, Cambridge University Press, 2005.'),
                    dcc.Markdown('##### Georg Wilhelm Friedrich Hegel', id='hegel'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hegel, Georg Wilhelm Friedrich. *The Science of Logic*. Translated by George di Giovanni, Cambridge University Press, 2010.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hegel, Georg Wilhelm Friedrich. *Phenomenology of Spirit*. Translated by A. V. Miller, Oxford University Press, 1977.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hegel, Georg Wilhelm Friedrich. *Elements of the Philosophy of Right*. Translated by H. B. Nisbet, Cambridge University Press, 1991.'),
                    dcc.Markdown('##### Immanuel Kant', id='kant'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kant, Immanuel. *Critique of Practical Reason*. Translated by Werner S. Pluhar, Hackett Publishing Company, 2002.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kant, Immanuel. *Critique of Judgement*. Translated by James Creed Meredith, Oxford University Press, 2007.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kant, Immanuel. *Critique of Pure Reason*. Translated by Paul Guyer and Alan W. Wood, Cambridge  University Press, 1998.'),
                    dcc.Markdown('#### Phenomenology', id='phenomenology'),
                    dcc.Markdown('##### Martin Heidegger', id='heidegger'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Heidegger, Martin. *Being and Time*. Translated by Joan Stambaugh, State University of New York Press, 1996.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Heidegger, Martin. *Off the Beaten Track*. Edited and Translated by Julian Young and Kenneth Haynes, Cambridge University Press, 2001.'),                    
                    dcc.Markdown('##### Edmund Husesrl', id='husserl'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Husserl, Edmund. *The Idea of Phenomenology*. Translated by Lee Hardy, Kluwer Academic Publishers.'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Husserl, Edmund. *The Crisis of European Sciences and Transcendental Phenomenology: an Introduction to Phenomenological Philosophy*. Translated by David Carr, Northwestern University Press, 1970.'),
                    dcc.Markdown('##### Maurice Merleau-Ponty', id='ponty'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Merleau-Ponty, Maurice. *Phenomenology of Perception*. Translated by Colin Smith, Routledge, 2002.'),
                    dcc.Markdown("#### Plato", id='plato'), 
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Plato. *Complete Works*. Edited by John M. Cooper, Hacket Publishing Company, 1997.'),
                    dcc.Markdown('#### Rationalism', id='rationalism'),
                    dcc.Markdown('##### René Descartes', id='descartes'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Descartes, René. *A Discourse on Method*. Translated by John Veitch. 2008. *Project Gutenberg*, [www.gutenberg.org/ebooks/59](https://www.gutenberg.org/ebooks/59).'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Descartes, René. *Meditations on First Philosophy*. Translated by Michael Moriarty, Oxford University Press, 2008.'),
                    dcc.Markdown('##### G. W. Leibniz', id='leibniz'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Leibniz, G.W.. *Theodicy: Essays on the Goodness of God, the Freedom of Man, and the Origin of Evil*. Translated by E.M. Huggard. 2005. *Project Gutenberg*, [www.gutenberg.org/ebooks/17147](https://www.gutenberg.org/ebooks/17147).'),
                    dcc.Markdown('##### Nicolas Malebranche', id='malebranche'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Malebranche, Nicolas. *The Search After Truth*. Edited by Thomas M. Lennon and Paul J. Olscamp, Cambridge University Press, 1997.'),
                    dcc.Markdown('##### Baruch Spinoza', id='spinoza'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Spinoza, Benedict de. *Ethics*. Translated by R.H.M. Elwes. 2003. *Project Gutenberg*, [www.gutenberg.org/ebooks/3800](https://www.gutenberg.org/ebooks/3800).'),
                    dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Spinoza, Benedict de. *On the Improvement of the Understanding*. Translated by R.H.M. Elwes. 1997. *Project Gutenberg*, [www.gutenberg.org/ebooks/1016](https://www.gutenberg.org/ebooks/1016).'),
                    ], style=CONTENT_STYLE)
                    

layout = html.Div([
    dcc.Location(id="url"), 
    sidebar, 
    content
    ])

# this function is used to toggle the is_open property of each Collapse
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# this function applies the "open" class to rotate the chevron
def set_navitem_class(is_open):
    if is_open:
        return "open"
    return ""

for i in range(0,100):
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

    app.callback(
        Output(f"submenu-{i}", "className"),
        [Input(f"submenu-{i}-collapse", "is_open")],
    )(set_navitem_class)
