import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 1 && column !== 0

    text: visible? Scenario.years[Scenario.currentYearIndex].financial.summary.netIncomeSection.netIncome : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}