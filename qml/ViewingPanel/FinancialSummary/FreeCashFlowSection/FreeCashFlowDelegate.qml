import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 3 && column !== 0

    text: visible? Scenario.years[Scenario.currentYearIndex].financial.summary.freeCashFlowSection.freeCashFlow.toFixed(2) : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}