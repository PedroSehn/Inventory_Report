from inventory_report.reports.ReportTools.oldest_fabrication import (
    oldest_fabrication,
)
from inventory_report.reports.ReportTools.sooner_expiration import (
    sooner_expiration,
)
from inventory_report.reports.ReportTools.most_items import most_items


class SimpleReport:
    def generate(list):
        return (
                f"Data de fabricação mais antiga: {oldest_fabrication(list)}\n"
                f"Data de validade mais próxima: {sooner_expiration(list)}\n"
                f"Empresa com mais produtos: {most_items(list)}"
        )


SimpleReport.generate = staticmethod(SimpleReport.generate)
