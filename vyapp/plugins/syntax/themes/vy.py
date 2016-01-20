from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Token, Punctuation


class VyStyle(Style):
    """
    """

    background_color = "#000000"
    highlight_color = "#222222"
    default_style = "#cccccc"

    styles = {
        Token:                     "#cccccc",
        Whitespace:                "",
        Comment:                   "#000080",
        Comment.Hashbang:          "#006680",
        Comment.Multiline:         "#807100",
        Comment.Preproc:           "",
        Comment.Single:            "#f55600",
        Comment.Special:           "#cd0000",

        Keyword:                   "#7a7a7a",
        Keyword.Constant:          "",
        Keyword.Declaration:       "#00cd00",
        Keyword.Namespace:         "#cd00cd",
        Keyword.Pseudo:            "#7a7a7a",
        Keyword.Reserved:          "#7a7a7a",
        Keyword.Type:              "#00cd00",

        Operator:                  "#7a7a7a",
        Operator.Word:             "#7a7a7a",

        Punctuation:               "#7a7a7a",
        Name:                      "",
        Name.Attribute:            "",
        Name.Builtin:              "#cccccc",
        Name.Class:                "#00cdcd",
        # Name.Constant:             "",
        # Name.Decorator:            "",
        # Name.Entity:               "",
        # Name.Function:             "",
        # Name.Label:                "",
        # Name.Namespace:            "",
        # Name.Other:                "",
        # Name.Tag:                  "",
        Name.Exception:            "bold #666699",
        Name.Variable:             "#00cdcd",

        String:                    "#0094f0",
        Number:                    "#cd00cd",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#cd0000",
        Generic.Inserted:          "#00cd00",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }


