import QtQuick
import QtQuick.Controls.Material

Row {
    id: root

    property string labelText: ""
    property alias text: text.text

    spacing: height/5

    Label {
        id: label

        text: root.labelText + ":"
        verticalAlignment: Text.AlignVCenter
        height: implicitHeight * 2.5
    }

    Label {
        id: text

        text: ""

        verticalAlignment: Text.AlignVCenter
        height: label.height
    }


}