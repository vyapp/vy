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

        Keyword:                   "#FEE636",
        # Keyword.Constant:          "",
        # Keyword.Declaration:       "#BDBD02",
        # Keyword.Namespace:         "#BDBD02",
        # Keyword.Pseudo:            "#BDBD02",
        # Keyword.Reserved:          "#BDBD02",
        # Keyword.Type:              "#BDBD02",

        Operator:                  "#D5C281",
        Operator.Word:             "#FEE636",
        Punctuation:               "#D5C281",

        Name:                      "#D5C281",
        Name.Attribute:            "#D581CF",
        Name.Builtin:              "#DCCE9F",
        Name.Class:                "#D581CF",
        Name.Function:             "#D581CF",
        Name.Constant:             "",
        Name.Decorator:            "#8B8B6E",
        # Name.Entity:               "",
        # Name.Label:                "",
        # Name.Namespace:            "",
        # Name.Other:                "",
        # Name.Tag:                  "",
        Name.Exception:            "#666699",
        Name.Variable:             "#00cdcd",

        String:                    "#9ED8A4",
        String.Single:             "#9ED8A4",
        String.Double:             "#9ED8A4",
        String.Backtick:           "#9ED8A4",
        String.Char:               "#9ED8A4",
        String.Doc:                "#9ED8A4",
        String.Regex:              "#9ED8A4",
        String.Symbol:             "#9ED8A4",
        Number:                    "#B8AD89",
        
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

