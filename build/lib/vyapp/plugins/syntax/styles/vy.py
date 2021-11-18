from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Token, Punctuation, Text


class VyStyle(Style):
    """
    """

    background_color = "#000000"
    default_style    = "#957C8B"

    styles = {
        Token:                     "#cccccc",
        # Whitespace:                "#957C8B",
        # Note: The Text tokens are set to default_style. So, when inserting chars.
        # it gets highlighed afterwards.
        Text:                      '#957C8B',
        Comment:                   "#ffbf00",
        Comment.Hashbang:          "#006680",
        Comment.Multiline:         "#807100",
        Comment.Preproc:           "#ff8000",
        Comment.Single:            "#f55600",
        Comment.Special:           "#cd0000",

        Keyword:                   "#3E9D40",
        # Keyword.Constant:          "",
        # Keyword.Declaration:       "#3E9D40",
        # Keyword.Namespace:         "#3E9D40",
        # Keyword.Pseudo:            "#3E9D40",
        # Keyword.Reserved:          "#3E9D40",
        # Keyword.Type:              "#3E9D40",

        Operator:                  "#957C8B",
        Operator.Word:             "#3E9D40",

        Punctuation:               "#957C8B",
        Name:                      "#957C8B",
        Name.Attribute:            "#957C8B",
        Name.Builtin:              "#999999",
        Name.Class:                "#00cdcd",
        # Name.Constant:             "",
        Name.Decorator:            "#cd00cd",
        # Name.Entity:               "",
        Name.Function:             "#D244D2",
        # Name.Label:                "",
        # Name.Namespace:            "",
        # Name.Other:                "",
        # Name.Tag:                  "",
        Name.Exception:            "#666699",
        Name.Variable:             "#00cdcd",

        String:                    "#3E6F9D",
        # String.Single:             "#805E00",

        String.Backtick:           "#FF470A",
        String.Char:               "#FF470A",
        String.Doc:                "#f0d400",
        String.Regex:              "#82ad00",
        String.Symbol:             "#657439",
        Number:                    "#cd00cd",
        
        Generic.Heading:           "#000080",
        Generic.Subheading:        "#800080",
        Generic.Deleted:           "#cd0000",
        Generic.Inserted:          "#00cd00",
        Generic.Error:             "#FF0000",
        # Generic.Emph:              "",
        # Generic.Strong:            "",
        Generic.Prompt:            "#000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "#FF0000"
    }















