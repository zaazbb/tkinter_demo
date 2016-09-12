
# Using Styles and Themes

# Style Names
>>> b = ttk.Button()
>>> b['style']
''
>>> b.winfo_class()
'TButton'

# Using a Style
b['style'] = 'NuclearReactor.TButton'

# Using Themes
>>> s = ttk.Style()
>>> s.theme_names()
('aqua', 'step', 'clam', 'alt', 'default', 'classic')

>>> s.theme_use()
'aqua'

s.theme_use('themename')

# What's Inside a Style?

# Layout
>>> s.layout('TButton')
[("Button.border", {"children": [("Button.focus", {"children": [("Button.spacing",
{"children": [("Button.label", {"sticky": "nswe"})], "sticky": "nswe"})], 
"sticky": "nswe"})], "sticky": "nswe", "border": "1"})]

# Element Options
>>> s.element_options('Button.label')
('-compound', '-space', '-text', '-font', '-foreground', '-underline', '-width', '-anchor', '-justify',
'-wraplength', '-embossed', '-image', '-stipple', '-background')

# Changing Style Options

# Modifying a Style Option
s.configure('TButton', font='helvetica 24')

>>> s.lookup('TButton', 'font')
'helvetica 24'

# Creating a New, Derived Style
s.configure('Emergency.TButton', font='helvetica 24',
foreground='red', padding=10)

# State Specific Style Options
# to do.
