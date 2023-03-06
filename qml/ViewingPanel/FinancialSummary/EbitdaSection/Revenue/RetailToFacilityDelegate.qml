import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 2 && column !== 0

    text: visible? Scenario.years[Scenario.currentYearIndex].financial.summary.ebitdaSection.revenue.retailToFacility : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter

}