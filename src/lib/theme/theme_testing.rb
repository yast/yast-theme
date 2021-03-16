require 'yast'

Yast.import "UI"
Yast.import "Label"

module Theme
  class ThemeTesting
    include Yast::I18n
    include Yast::UIShortcuts

    def initialize
      textdomain "theme"
    end

    def combobox
      ComboBox(
        Id(:combobox),
        _("This is the combobox label"),
        [
          Item(Id(:combobox_first_item), "First item"),
          Item(Id(:combobox_second_item), "Second item")
        ]
      )
    end

    def run
      Yast::UI.OpenDialog(
        MarginBox(
          1,
          1,
          VBox(
            Heading(_("This is a Heading")),
            Label(_("This is a label")),
            ComboBox(
              Id(:combobox),
              _("This is the combobox label"),
              [
                Item(Id(:combobox_first_item), "First item"),
                Item(Id(:combobox_second_item), "Second item")
              ]
            ),
            Frame(
              _("A frame"),
              VBox(
                VSpacing(1),
                RadioButtonGroup(
                  Id(:radio_button_group),
                  HBox(
                    RadioButton(Id(:first_option), "First option"),
                    HSpacing(),
                    RadioButton(Id(:second_option), "Second option"),
                  )
                )
              )
            ),
            Frame(
              _("A frame"),
              VBox(
                Label("Which can content whatever content")
              )
            ),
            ButtonBox(
               PushButton(Id(:cancel), Yast::Label.CancelButton),
               PushButton(Id(:ok), Yast::Label.OKButton)
            )
          )
        )
      )

      begin
        case input = Yast::UI.UserInput
        when :cancel, :ok
          Yast::UI.CloseDialog
        end
      end
    end
  end
end
