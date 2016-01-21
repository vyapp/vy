from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Token, Punctuation


class VyStyle(Style):
    """
    """

    background_color = "#000000"
    highlight_color = "#222222"
    default_style = "#999999"

    styles = {
        Token:                     "#cccccc",
        # Whitespace:                "",
        Comment:                   "#000080",
        Comment.Hashbang:          "#006680",
        Comment.Multiline:         "#807100",
        Comment.Preproc:           "",
        Comment.Single:            "#f55600",
        Comment.Special:           "#cd0000",

        Keyword:                   "#269900",
        # Keyword.Constant:          "",
        Keyword.Declaration:       "#00cd00",
        Keyword.Namespace:         "#cd00cd",
        Keyword.Pseudo:            "#269900",
        Keyword.Reserved:          "#269900",
        Keyword.Type:              "#00cd00",

        Operator:                  "#269900",
        Operator.Word:             "#269900",

        Punctuation:               "#269900",
        Name:                      "",
        Name.Attribute:            "",
        Name.Builtin:              "#999999",
        Name.Class:                "#00cdcd",
        # Name.Constant:             "",
        Name.Decorator:            "#cd00cd",
        # Name.Entity:               "",
        # Name.Function:             "",
        # Name.Label:                "",
        # Name.Namespace:            "",
        # Name.Other:                "",
        # Name.Tag:                  "",
        Name.Exception:            "#666699",
        Name.Variable:             "#00cdcd",

        String:                    "#805E00",
        String.Backtick:           "#FF470A",
        String.Char:               "#FF470A",
        String.Doc:                "#f0d400",
        String.Regex:              "#82ad00",
        String.Interpol:           "#397472",
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




