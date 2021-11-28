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

        Keyword:                   "#999626",
        # Keyword.Constant:          "",
        # Keyword.Declaration:       "#BDBD02",
        # Keyword.Namespace:         "#BDBD02",
        # Keyword.Pseudo:            "#BDBD02",
        # Keyword.Reserved:          "#BDBD02",
        # Keyword.Type:              "#BDBD02",

        Operator:                  "#999626",
        Operator.Word:             "#999626",

        Punctuation:               "#8C8923",
        Name:                      "#8B8B6E",
        Name.Attribute:            "#957C8B",
        Name.Builtin:              "#999999",
        Name.Class:                "#C24C35",
        Name.Constant:             "",
        Name.Decorator:            "#8B8B6E",
        Name.Entity:               "",
        Name.Function:             "#EB7D7D",
        Name.Label:                "",
        Name.Namespace:            "",
        Name.Other:                "",
        Name.Tag:                  "",
        Name.Exception:            "#666699",
        Name.Variable:             "#00cdcd",

        String:                    "#76778C",
        String.Single:             "#76778C",

        String.Backtick:           "#76778C",
        String.Char:               "#76778C",
        String.Doc:                "#76778C",
        String.Regex:              "#3E4EBF",
        String.Symbol:             "#AAAA5C",
        Number:                    "#8C8923",
        
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

